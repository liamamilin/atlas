# Research Notes — Web Application Builder

## Research Goal

Understand the third target-scoped member of the ratified §12 "application development framework" genus (siblings: desktop-app-development-framework-builder, mobile-app-development-platform): the products by which developers build **applications delivered through the web browser**. Extract the defining core, the common mature structure, the variant space, and the boundaries — with special attention to the two joint-review flags left by the sibling passes and the leaf-name question ("/ Builder" semantics).

## Initial Boundary (working hypothesis before research)

- Hypothesis: this leaf is the web-target member of the genus — products whose output artifact is an application served to a browser (the artifact test's third arm: installed desktop executable vs mobile package vs browser-served page).
- Expected nearest neighbors: Web Development IDE (where code is written vs what code is written against), Visual Website Builder §04.16 (content sites vs applications), Low-code Application Platform / No-code Application Builder (authoring medium), PaaS Management Console (operating deployed apps vs building them), Cloud IDE (hosting axis), Project Scaffolding / Code Generator (entry ramps).
- Known prior context: the desktop pass recorded the leaf-name note — "/ Builder" maps to the visual/RAD-builder authoring posture (a variant), NOT website-builder semantics. The low-code pass recorded a boundary "vs web application builder (content site vs business app)" — suspected mislabel of this leaf, to be corrected from this side.
- Unknowns: whether the web "shell" leg has a clean analog of the desktop/mobile app shell; how deployment (vs packaging) behaves as the artifact path; where the SPA/hybrid rendering split sits (definitional or variant).

## Research Questions

1. What do the products call themselves, and what do they say they build?
2. What does the framework supply vs what does the developer write (the shell question)?
3. What is the output artifact, and how does it reach end users (deploy vs install)?
4. What is the daily construction loop (scaffold → build UI → wire logic/data → run → deploy)?
5. Which structures are universal across the sample, and which are rendering-architecture, scope, or posture variants?
6. Where exactly are the boundaries: desktop/mobile siblings (joint review), website builders, low-code/no-code, IDEs, PaaS, scaffolding, API tooling?
7. Historical check: do mid-90s web application tools (application servers, visual web builders) satisfy the same core without modern machinery?

## Representative Products

| Product | Pole | Why sampled |
|---|---|---|
| Django | server-rendered, batteries-included Python framework | canonical full-stack framework; excellent docs |
| Ruby on Rails | convention-over-configuration MVC framework | the archetype of the modern web framework; excellent guides |
| ASP.NET Core | vendor platform component (Microsoft), multi-model UI (Blazor/Razor/MVC) | vendor-platform pole; C#-without-JS UI substrate |
| Next.js | React full-stack, hybrid rendering (server + client components) | the modern hybrid-rendering pole; strong docs incl. deployment |
| Bubble | visual no-code web application builder | the "builder"-name pole; boundary counterparty to low-code/no-code |
| Angular (corroborating) | client-side SPA framework + CLI | sixth observation; SPA pole + PWA/service-worker boundary nuance |

## Sources

All fetched 2026-09-09 (evidence layer A unless noted):

- Django — FAQ: General: https://docs.djangoproject.com/en/stable/faq/general/
- Django — Overview ("Why Django?"): https://www.djangoproject.com/start/overview/
- Ruby on Rails — Getting Started with Rails: https://guides.rubyonrails.org/getting_started.html
- ASP.NET Core — Overview: https://learn.microsoft.com/en-us/aspnet/core/introduction-to-aspnet-core
- Next.js — Layouts and Pages: https://nextjs.org/docs/app/getting-started/layouts-and-pages
- Next.js — Deploying: https://nextjs.org/docs/app/getting-started/deploying
- Angular — What is Angular?: https://angular.dev/overview
- Angular — Essentials: https://angular.dev/essentials
- Bubble — Building your first app (manual.bubble.io, GitBook markdown): https://manual.bubble.io/help-guides/getting-started/building-your-first-app.md

Sibling counterparty files (read, not fetched): research/desktop-app-development-framework-builder.md, research/mobile-app-development-platform.md, applications/mobile-app-development-platform.md; STATUS.md entries for low-code-application-platform, no-code-application-builder, cloud-ide, desktop and mobile siblings.

## Product Observations

### Product A — Django (evidence layer A)

- Self-label: "The web framework for perfectionists with deadlines"; "a generic web development framework that let them build web applications more and more quickly"; "a web framework; it's a programming tool that lets you build websites".
- Explicit boundary self-statement: "Django is not a CMS, or any sort of 'turnkey product'… It's a web framework… Django is something you use to *create* things like Drupal." (Direct evidence for the website-builder/CMS boundary from inside the sample.)
- **Shell leg, directly stated**: asked why MVC names differ — "a 'view' is the Python callback function for a particular URL… the 'controller' is probably the framework itself: the machinery that sends a request to the appropriate view, according to the Django URL configuration." The framework IS the request-dispatch machinery; developer code plugs in as view callbacks.
- Batteries included: "Django takes care of user authentication, content administration, site maps, RSS feeds, and many more tasks — right out of the box"; automatic admin site ("one module of Django the framework"); cache framework; database layer and application layer cleanly separated.
- Security: "helps developers avoid many common security mistakes, such as SQL injection, cross-site scripting, cross-site request forgery and clickjacking. Its user authentication system provides a secure way to manage user accounts and passwords."
- Scale/deployment: "shared-nothing" architecture — "you can add hardware at any level – database servers, caching servers or web/application servers"; "from concept to public launch" in hours (newsroom origin).
- Versatility: "from content management systems to social networks to scientific computing platforms."

### Product B — Ruby on Rails (evidence layer A)

- Self-label: "Rails is a web application development framework written in the Ruby programming language. It is designed to make programming web applications easier by making assumptions about what every developer needs to get started."
- Philosophy: DRY + "Convention Over Configuration… defaults to this set of conventions, rather than require that you define them yourself through endless configuration files." "Opinionated software."
- Scaffold: `rails new store` generates the whole application foundation (directory structure: app/, config/, db/, test/…); `rails generate model` / `generate controller` generate model + migration + tests + views.
- **Shell leg**: "A Request's Journey Through Rails" — "A route maps a request to a controller action. A controller action performs the necessary work… A view displays data." Routes pair HTTP method + URL path → controller#action; `resources :products` generates the CRUD route set; route parameters capture URL portions. Rack configuration (`config.ru`) for Rack-based servers.
- Dev server: `bin/rails server` starts Puma serving the app at http://localhost:3000; autoloading/auto code reloading in development ("without having to restart your Rails server after every change").
- Data layer: Active Record maps relational databases to Ruby; migrations ("a set of changes we want to make to our database… so they can be deployed to production safely"); validations; console.
- Views: ERB templates, layouts and rendering, form helpers; Hotwire for JS.
- Shared services: Action Mailer (email), Active Storage (file uploads), Active Job + Solid Queue (background jobs), Action Cable (real-time), I18n, caching.
- Auth: "Adding Authentication" chapter in the getting-started guide.
- Testing: "Testing Rails Applications"; fixtures; CI with GitHub Actions chapter.
- **Artifact leg**: "Deploying to Production" chapter — deploy via Kamal; migrations "deployed to production (live, online!)".
- Scope variant documented by the product itself: "Using Rails for API-only Applications" guide exists — the framework can be used without views (boundary nuance, see below).

### Product C — ASP.NET Core (evidence layer A)

- Self-label: "a cross-platform, high-performance, open-source framework for building modern web apps using .NET… built for large-scale app development… a robust choice for enterprise-level apps."
- **Shell leg**: "Lightweight and modular HTTP request pipeline"; Kestrel "high-performance and cross-platform HTTP server"; integrated dependency injection; environment-based configuration; logging/tracing/metrics.
- UI construction: Blazor — "Create rich interactive web UI components using C#—no JavaScript required"; versioned page content also documents "Develop apps and APIs using Razor Pages and Model-View-Controller (MVC) frameworks"; "Integrate seamlessly with popular client-side frameworks… Angular, React, Vue, and Bootstrap."
- API surface: Minimal APIs ("build fast web APIs with minimal code"); SignalR (real-time); gRPC.
- Security: "Built-in security features for authentication, authorization, and data protection."
- Testing: "Easily create unit and integration tests."
- Tooling: Visual Studio and Visual Studio Code.
- **Artifact leg**: "Cloud-ready: Whether you're deploying to your own data centers or to the cloud, ASP.NET Core simplifies deployment, monitoring, and configuration."

### Product D — Next.js (evidence layer A)

- UI construction: file-system based routing — "folders and files to define routes"; a **page** is "UI that is rendered on a specific route" (a React component); **layouts** are UI shared between multiple pages, nested, state-preserving; dynamic segments (`[slug]`) "generate routes from data".
- Rendering architecture: Server Components fetch data directly (`async` page components); Client Components read state via hooks; `searchParams` "opts your page into dynamic rendering"; prerendering vs dynamic rendering vocabulary.
- Navigation: `<Link>` extends the HTML `<a>` tag with prefetching and client-side navigation.
- Tooling: `next dev`, `next build`, `next start`, `next typegen`; typed props generated by the CLI.
- **Artifact leg (richest deployment evidence in sample)**: "Next.js can be deployed as a Node.js server, Docker container, static export, or adapted to run on different platforms" — deployment-option table (Node.js server: all features; Docker: all; static export: limited — "hosted on any web server that can serve HTML/CSS/JS static assets… AWS S3, Nginx, or Apache"; adapters: platform-verified, e.g. Vercel; other platforms: Cloudflare, Netlify, AWS Amplify, Firebase App Hosting…). "Next.js enables starting as a static site or Single-Page Application (SPA), then later optionally upgrading to use features that require a server."

### Product E — Angular (evidence layer A; corroborating observation)

- Self-label: "Angular is a web framework that empowers developers to build fast, reliable applications that users love… a broad suite of tools, APIs, and libraries… a solid platform on which to build fast, reliable applications that scale with both the size of your team and the size of your codebase."
- UI construction: components ("split your code into well-encapsulated parts"), templates, signals ("fine-grained reactivity model"), forms ("standardized system for form participation and validation"), dependency injection.
- **Shell leg**: Angular Routing — "feature-rich navigation toolkit, including support for route guards, data resolution, lazy-loading"; DI as the application-wide wiring system.
- Rendering variants: "supports both server-side rendering (SSR) and static site generation (SSG) along with full DOM hydration."
- Tooling: CLI ("gets your project running in under a minute with the commands you need to grow into a deployed production application"), DevTools (component tree inspector, DI tree view, profiling), Language Service, `ng update` (automated migrations), build pipeline (Vite/esbuild).
- Security/i18n: HTML sanitization, trusted types, XSS/CSRF protection framing; internationalization (ICU).
- Boundary nuance: docs navigation includes "Service Workers & PWAs" — web apps can gain install-to-home-screen behavior while remaining web-delivered.

### Product F — Bubble (evidence layer A; boundary pole)

- Self-framing: "Bubble uses intuitive and self-explanatory terminology like *things*, *workflows*, and *conditions*, to remove the barriers of complex coding languages."
- App model: "Most apps are about collecting information, and then manipulating and presenting it… a useful design on top of a database." To build: "Set up your **database**… Design a **user interface**… Link your design to **workflows**."
- UI construction: elements (buttons, texts, inputs), styles, pages, reusable elements; responsive design referenced via design resources.
- Logic: workflows — "a sequence of automated steps or actions initiated by an **event**" (button click, dropdown change, page load); each step an **action** (change database, navigate, hide/show); **conditions** ("if this, then that") and **dynamic expressions** ("live formulas").
- Data: Things (records), Data Types (tables), Fields (attributes); **privacy rules** ("define who can access or modify what data").
- **Artifact leg**: two environments — Test and Live, each "with its own separate database"; "Once you're satisfied with your changes in your test environment, you can **deploy** them to the live environment, ensuring that your users always experience a polished… version of your app." Version control feature for branching.
- Extension/integration: plugins (built-in + store), Data API / Workflow API (inbound), API Connector (outbound).
- Authoring medium: configuration-first throughout — no code artifact is produced or edited; the app lives on Bubble's runtime. (This is the low-code/no-code passes' defining leg, observed directly.)

## Cross-product Comparison

| Dimension | Django | Rails | ASP.NET Core | Next.js | Angular | Bubble |
|---|---|---|---|---|---|---|
| Self-label | web framework | web application development framework | framework for building modern web apps | (React) framework, pages/layouts on routes | web framework | visual app builder (no-code) |
| UI substrate | templates + views (server-rendered) | ERB views + Hotwire | Blazor components (C#), Razor Pages/MVC, or client frameworks | React server + client components | components + templates + signals | visual elements on pages |
| Routing/URL binding | URL configuration dispatches to views | routes → controller#action; resource routes | request pipeline + endpoints | file-system routing (folders = segments) | router (guards, resolvers, lazy-loading) | pages addressed by URLs (workflow navigation) |
| Request/render lifecycle owner | the framework ("the controller is probably the framework itself") | the framework (request journey: route→controller→view) | the framework (HTTP request pipeline, Kestrel) | the framework (server render + client navigation) | the framework (client runtime + router + DI) | the Bubble runtime |
| Shared services | auth, admin, cache, DB layer | Active Record, mailer, storage, jobs, cable, i18n | DI, config, auth/authz/data protection | data fetching in server components | DI, forms, HTTP client | database, privacy rules, APIs |
| Dev loop | (docs site; dev server implied by "concept to launch") | Puma dev server + autoloading | (tooling: VS/VS Code) | `next dev` | CLI + DevTools | editor preview (Test environment) |
| Scaffolding | (docs site) | `rails new`, generators | (project templates via tooling) | (CLI scripts) | CLI "project running in under a minute" | new app in editor |
| Output artifact path | deploy to web/application servers (shared-nothing scaling) | deploy to production (Kamal) | deploy to own data centers or cloud | Node.js server / Docker / static export / platform adapters | "grow into a deployed production application" | deploy Test → Live on Bubble hosting |
| Testing | (docs site) | testing guide + fixtures + CI | unit + integration tests | (docs index) | testing guides | (preview/Test environment) |
| Security machinery | SQLi/XSS/CSRF/clickjacking protections, auth | security guide, auth chapter | auth, authorization, data protection | (docs index) | sanitization, XSS/CSRF | privacy rules |
| Extension model | pluggable apps/ecosystem | gems/plugins | NuGet/client frameworks | platform adapters, plugins | libraries, Angular Material/CDK | plugins + API connector |
| Authoring medium | code | code | code | code | code | configuration (no code artifact) |

### Evidence-layer roll-up

- **A (directly observed):** every cell above is anchored to a fetched official page of that product.
- **B (cross-product commonality):** browser-delivered UI construction in all six; a framework-owned routing/request/render structure in all six; shared application services (auth/security, data path, forms, i18n) in five to six; scaffolding + dev-server + fast-iteration tooling in five (Django/ASP.NET Core tooling pages not deep-fetched); deployment-to-host as the artifact path in all six (no package, no install, no store anywhere in the sample); testing in four directly observed; extension ecosystems in all six.
- **C (canonical inference):** the three-part defining core below; the genus relationship (third target of the ratified application-development-framework genus); "deployment replaces packaging" as the web artifact path's structural signature.

## Canonical Model

### L0 — Defining Invariant (jointly held; remove any leg and the Type collapses)

1. **Browser-delivered UI construction.** The framework provides the primary means by which the developer composes the application's user interface as experienced in a web browser — pages, templates, components, or visual elements. The substrate is irrelevant to the definition (server-rendered templates, client-side component trees, hybrid rendering, C#-compiled UI, visual elements all satisfy). *Remove → a backend/service framework or a UI-less toolkit.*
2. **Framework-supplied web application shell.** The framework supplies the running application structure — the routing that binds URLs to code, the request/render lifecycle, and commonly shared application services (data access, sessions/auth, templating) — and the developer's code plugs into it as handlers, controllers, components, or workflow steps. Django states this leg explicitly: the framework itself is "the machinery that sends a request to the appropriate view." *Remove → a bare template library or HTTP micro-library the developer wires into their own server; the softest leg, but all six sampled products hold it, and the RAD "builder" posture holds it absolutely (the builder IS the shell).*
3. **The browser-served application as the output artifact.** The deliverable is an application reached by end users through a web browser at a URL, served over the web from a hosting target the developer/team chooses or the vendor operates — never installed as a package. Changes reach users by **redeployment** (build → deploy → URL), not by installers, app identity, signing, or store review. *Remove → desktop framework (installed executable) or Mobile App Development Platform (package on a mobile OS).*

Jointly-held load-bearing: 1+3 without 2 = hand-authored static pages or bare scripts — pages, not an application; 2+3 without 1 = a backend/API framework serving no UI; 1+2 without 3 = a construction harness whose result never reaches users.

Note on the ratified genus artifact test: the desktop pass phrased the web artifact as "browser-served page." This pass refines: the invariant is the **application delivered through the browser over the web** — server-rendered per request, prerendered/static-exported, or client-side hydrated are all realizations; what separates the Type is that nothing is installed on the user's device and updates propagate by redeployment. The separating function of the artifact test (browser-served app vs desktop executable vs mobile package) is unchanged.

### L1 — Common Mature Structure (very common; not definitional)

- **Project scaffolding and generators** — a new-project command that produces a runnable skeleton (Rails `rails new` + generators; Angular CLI "under a minute"; Next.js CLI scripts; Bubble's new-app editor).
- **Dev server and fast iteration** — a local server serving the app during development (Rails/Puma at a local port; `next dev`; Angular CLI; Bubble preview) with automatic reload of changed code (Rails autoloading documented explicitly).
- **Routing** — URL→code binding in every sampled product (the shell's visible face).
- **Templating/component rendering** — the UI vocabulary (templates, components, elements).
- **Data path** — server-side frameworks commonly include an ORM/database layer and migrations (Rails Active Record + migrations; Django database layer; Bubble built-in database); front-end frameworks consume APIs instead (Angular HTTP client; Next.js data fetching in server components). The *presence of a data path* is common; *owning the ORM* is a variant.
- **Forms and validation** — form helpers/controls and validation machinery (Rails form helpers + Active Record validations; Angular forms; Bubble inputs + conditions).
- **Authentication/security machinery** — framework-level auth and protection against common web vulnerabilities (Django: SQLi/XSS/CSRF/clickjacking + auth system; ASP.NET Core: auth/authz/data protection; Rails: security guide + auth chapter; Angular: sanitization; Bubble: privacy rules).
- **Testing tiers** — unit and integration/interface tests, locally and in CI (Rails, ASP.NET Core, Angular directly observed).
- **Internationalization** (Rails I18n, Angular i18n directly observed; common across mature frameworks).
- **Caching** (Django cache framework, Rails caching — directly observed).
- **CLI/build tooling and debugging/profiling** (Angular CLI + DevTools; Next.js CLI; Rails CLI).
- **Extension ecosystem** — plugins/packages/libraries/connectors (all six).
- **Deployment machinery** — product-documented paths from build to a running host (Rails/Kamal; Next.js deployment table; ASP.NET Core cloud-ready; Bubble Test→Live deploy).
- **Multi-user serving** — web applications serve many concurrent users over the network (Django scaling FAQ; ASP.NET Core "any size workload"; Bubble "actual users"); user accounts are prominent framework services. Common, not definitional (a single-user internal web app is still in-type).

### L2 — Variant / Optional Structure

- **Rendering architecture** — server-rendered per request (Django/Rails classic) / client-side SPA (Angular-class) / hybrid (Next.js server+client components; Angular SSR/SSG/hydration) / static export (Next.js static output) / non-JS interactive UI compiled for the browser (Blazor). Major differentiator, not definitional.
- **Scope** — full-stack (server + client: Django, Rails, ASP.NET Core, Next.js, Bubble) vs front-end-focused (Angular-class, consuming APIs). API capability is universal-adjacent (Rails documents API-only applications; ASP.NET Core Minimal APIs) but API-only *usage* sits outside the Type's center (boundary below).
- **Batteries-included vs minimal core** — the sampled frameworks bundle large service sets; micro-frameworks (Flask/Sinatra-class; market anchors, not fetched) hold the minimal pole and still satisfy L0.
- **Authoring posture** — code-first (the dominant population) vs visual/RAD builder (visual design surface generating/editing code — the historical Visual InterDev/Dreamweaver UltraDev lineage; survives as visual designers inside code-first frameworks) vs configuration-first no-code (Bubble-class — assigned to the no-code Type by authoring medium; boundary below).
- **Hosting/deployment target** — own servers, containers, cloud platforms, static hosting/CDNs, platform hosts with adapters, vendor-operated runtime (Bubble). Plural by design; no vendor gatekeeping.
- **Language substrate** — Python, Ruby, C#, TypeScript/JavaScript, visual configuration.
- **Real-time, email, file storage, background jobs** — present in batteries-included products (Rails Action Cable/Mailer/Storage/Job; ASP.NET Core SignalR), absent or external elsewhere. Optional.
- **Business model** — open-source foundation (Django), open-source community (Rails), vendor platform component (ASP.NET Core/Microsoft; Angular/Google), commercial SaaS (Bubble).
- **Installable-web nuance** — service-worker/PWA capability lets a web app present an install-to-home-screen surface while its delivery and updates remain web-served (Angular documents Service Workers & PWAs).

### L3 — Vendor-specific (research notes only; must not enter the canonical document)

- **Django**: MTV naming ("model, template, view"); automatic admin site; shared-nothing scaling doctrine; Django Software Foundation governance.
- **Rails**: Convention-over-Configuration/DRY as branded philosophy; Active Record/migrations/validations specifics; `resources` CRUD route generation; Hotwire; Kamal deployment; Solid Queue; Action Mailer/Storage/Cable; `bin/rails` conventions; Puma as default dev server; localhost:3000 as the documented dev port (product doc fact, not a Type rule).
- **ASP.NET Core**: Kestrel; Blazor; Razor Pages/MVC; Minimal APIs; SignalR; gRPC; data protection; environment-based configuration; Visual Studio/VS Code tooling; moniker-versioned docs.
- **Next.js**: app directory file conventions (page/layout/special files); dynamic segments; Server/Client Component split; searchParams-driven dynamic rendering; `<Link>` prefetching; Adapter API + verified adapters (Vercel); static export feature limits.
- **Angular**: signals; DI; route guards/resolvers/lazy-loading; ng update automated migrations; Language Service; DevTools; Google monorepo testing claim; Vite/esbuild build; Angular Material/CDK; Firebase/Flutter partnership framing.
- **Bubble**: Things/Data Types/Fields vocabulary; workflows/events/actions; conditions/dynamic expressions; privacy rules; Test vs Live environments with separate databases; version control; Reusable Elements; Data API/Workflow API/API Connector; plugin store.

## Historical / Market-Sample Check (§24 reasoning)

Question: would older, regional, or differently-structured web development products still fit the L0?

- **Mid-1990s application servers and visual web builders** (ColdFusion-class tag-based application servers; Microsoft Visual InterDev-class visual builders for server-page web apps; WebObjects-class application-server frameworks): browser-delivered UI construction (server-page templates), framework shell (application-server request lifecycle and routing), browser-served artifact (pages served over HTTP) — satisfy all three legs with no SPA, no hot reload, no cloud deploy, no build pipeline. *(reasoning-based; not fetched)*
- **CGI scripting (early 1990s)**: bare scripts against the web server's protocol — no framework shell; the developer wires everything. The ancestor *below* the Type; confirms leg 2 is load-bearing. *(reasoning-based)*
- **A language alone (PHP-class, 1995)**: not a framework — no shell until frameworks arrive (Laravel-class later). Fails leg 2 as a language; the Type is the framework layer. *(reasoning-based)*
- **FrontPage-class site tools (1996)**: content-site authoring for non-programmers — website-builder semantics, not application construction; excluded consistently with the ratified leaf-name note. *(reasoning-based)*
- **Rails (2004) / Django (2005)** themselves are now two decades old — the Type predates the modern JS/SPA era; SPA/hybrid rendering, TypeScript, hot reload, and cloud-platform deployment are era machinery, not structure.

Conclusion: L0 survives the historical check. Rendering architecture, batteries, tooling polish, and deployment targets all stay in L1/L2.

## Vendor-specific Findings (L3 — excluded from the final document)

See L3 list above. Additional positioning notes:

- Django's FAQ explicitly disclaims being a CMS — used above as boundary evidence, not as structure.
- Rails' "Developer happiness" framing and "opinionated software" stance are product philosophy.
- ASP.NET Core's "industry leading performance" and hyperscale-name-dropping are marketing.
- Angular's Google-monorepo testing narrative is a trust signal, not structure.
- Bubble's "apps are all a useful design on top of a database" is a teaching simplification — useful for the no-code pole's mental model, not adopted as this Type's model.

## Boundary Findings

1. **vs Desktop App Development Framework / Builder** — designated counterparty; **JOINT REVIEW DISCHARGED from this side** (desktop pass's boundary 1 + this pass). The desktop L0 (desktop-window UI construction + framework-owned shell + desktop-executable artifact) and this web L0 (browser-delivered UI construction + framework-supplied web shell + browser-served artifact) are parallel three-leg structures over one ratified genus, target swapped. The artifact test separates cleanly: installed desktop executable vs application served to a browser. Web-technology desktop wrappers (Electron/Tauri-class) adopt web *technology* while their defining output remains the desktop binary — technology overlap does not collapse the boundary (ratified from this side). Multi-target products instantiate per target.
2. **vs Mobile App Development Platform** — designated counterparty; **JOINT REVIEW DISCHARGED from this side** (mobile pass's forward flag + this pass). The mobile L0 (mobile-screen UI construction + platform-supplied mobile shell + package on a mobile OS) parallels this web L0 with the target swapped. The artifact test separates: package installed on a mobile OS vs application served to a browser. PWA nuance recorded: install-to-home-screen web apps remain web-delivered (updates by redeployment, no store package) — the delivery path, not the install gesture, carries the boundary. No directory change; genus stands as three target-scoped leaves.
3. **vs Visual Website Builder (§04.16) / Online Store Builder (§05.01)** — content-site semantics vs application semantics. The ratified leaf-name note holds from this side: "/ Builder" in this leaf's name maps to the RAD/visual-builder authoring posture, not website-builder semantics. Django's own FAQ draws the line from inside the sample ("not a CMS… you use Django to *create* things like Drupal"). Removal test: if the product's center is composing content pages for non-developers without application data structures and logic, it is the website-builder Type.
4. **vs Low-code Application Platform / No-code Application Builder** — **CORRECTION recorded**: the low-code pass's boundary line "vs web application builder (content site vs business app)" mislabels this leaf (it imports website-builder semantics the desktop pass's leaf-name note already rejected). The actual seam is **authoring medium + audience + runtime ownership**: this leaf's center of gravity is code-first construction by developers (the code artifact is the product); the low-code/no-code Types are defined by configuration-first authoring on the platform's own building blocks with the app held on the platform's runtime. Bubble-class products satisfy this leaf's three target legs (browser-delivered UI, shell, artifact) but their authoring medium is configuration metadata, not code — assigned to the no-code Type; they are this pass's boundary pole, not core sample. The visual/RAD builder posture *within* code-first construction (visual surface generating/editable code — historical Visual InterDev lineage, visual designers inside modern frameworks) remains a variant of THIS leaf. Gradient, not wall; keep-both with cross-reference.
5. **vs Web Development IDE** — where code is written vs what the code is written against (desktop pass boundary 5, ratified from this side). Frameworks ship tooling (CLIs, DevTools) as L1 satellites; a framework without an editor exists; an editor without a framework behind it is the other Type.
6. **vs Cloud IDE** — hosting axis (where development happens) vs domain axis (what is being built); the cloud-ide pass already recorded the name-collision-only relationship. A cloud IDE can host development *of* a web application; the framework remains the substrate.
7. **vs PaaS Management Console** — the PaaS pass's L0 (application of record + platform-managed runtime + deploy loop + app-scoped operating surface) is the **operating** surface over deployed apps; this leaf is the **construction** substrate. Framework deployment guides route into foreign runtimes (Next.js's deployment table lists platforms; Rails' Kamal deploys to any host) — the framework builds, the PaaS operates. A framework does not operate the deployed application.
8. **vs Project Scaffolding / Code Generator** — scaffolding commands (`rails new`, CLI create commands) are entry ramps into a framework, not the framework; ratified from the desktop pass.
9. **vs API Development Workbench / API Design Platform** — frameworks can serve APIs (Rails API-only guide; ASP.NET Core Minimal APIs), but this leaf's defining target is the browser-delivered UI; a framework used API-only in a given project is operating outside this Type's center in that project. API tooling products are separate Types.
10. **vs CMS / static-site tooling** — content publication is a *use* of web frameworks, not the Type's center; the application shell (logic, data structures, state) separates an application from a content site. Django's self-disclaimer is the in-sample anchor.

## Uncertainties

1. **Django's tutorial/overview doc pages not fetched** — the component list is held at overview-page strength (auth, admin, sitemaps, RSS, cache framework, database layer); ORM/middleware specifics not directly observed.
2. **ASP.NET Core observed at overview-page depth** — Razor Pages/MVC evidence comes from the page's versioned content blocks; Blazor/Razor internals not fetched.
3. **Angular observed at overview + essentials-index depth** — routing/SSR/forms pages not fetched; claims held at self-description level.
4. **Bubble observed at getting-started depth** — deployment/version-control detail pages not fetched; Test/Live and deploy claims held at that page's statements.
5. **Micro-framework pole (Flask/Sinatra-class) not fetched** — held as market anchor at reasoning level; the minimal-core variant is argued, not observed.
6. **Historical anchors reasoning-based** (ColdFusion/Visual InterDev/WebObjects/CGI/FrontPage not fetched) — no precise historical claims made.
7. **No numeric claims** — dev ports, version floors, performance figures are product-doc facts (e.g., Rails' documented dev port) and are not asserted as Type rules anywhere.

## Final Synthesis

A Web Application Builder is the developer-facing construction substrate for applications delivered through the web browser — the third target-scoped member of the ratified application-development-framework genus. Its defining core is the conjunction of three structures: it provides (1) the means to construct the application's interface as experienced in a browser (templates, components, or visual elements — substrate irrelevant), (2) the web application shell — URL routing, the request/render lifecycle, and shared application services — into which the developer's code plugs, and (3) a delivery path whose output is an application reached at a URL through a browser, deployed to a hosting target of the developer's choosing, updated by redeployment rather than by installing packages. The market realizes the Type across server-rendered, client-side, hybrid, and vendor-platform products, with the visual/RAD builder posture as a named variant and configuration-first no-code platforms assigned to the no-code Type by authoring medium. Rendering architecture, batteries, tooling polish, and hosting targets are common mature structure or variants, not definition.
