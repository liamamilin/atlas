# Research Notes — Web Development IDE

Leaf: `Web Development IDE` (Section 12 — Software Development & Product Engineering)
Slug: `web-development-ide`
Research date: 2026-09-09
Methodology: WORKFLOW_v1.1 (Understand → Plan → Sample → Research → Model → Compare → Synthesize → Write → Review → Cite)

---

## Research Goal

Understand what a Web Development IDE is as an Application Type: what objects exist in its world, what the edit→run→see loop looks like when the software being built executes in a web browser, which capabilities are definitional vs common vs optional, and — the designated joint-review question left by the IDE pass (2026-09-08) — whether this leaf's defining structures are anything more than the general IDE core with a web target, i.e. whether it earns independent Type status or resolves as a domain variant.

## Initial Boundary (hypothesis before research)

- Working hypothesis: a development environment specialized for the web stack (HTML/CSS/JS/TS, frameworks, Node.js), where the run surface is a browser rather than a host process the IDE owns.
- Prior context from processed siblings:
  - IDE pass (2026-09-08) flagged this leaf as "likely a domain/platform variant of the IDE Type rather than an independent one (browser/frontend-targeted tooling over the same project → edit → build/run → debug model; the embedded-firmware sibling earned independence only via the host↔target bridge, which web targets lack)" — this pass must check its defining structures against the IDE core before claiming independence.
  - Web Application Builder pass (2026-09-09) boundary 5: "where code is written vs what the code is written against" — ratified from that side; this pass ratifies back.
  - Cloud IDE pass: the name collision with this leaf is orthogonal axes (target domain vs hosting locus), not overlap.
- Likely users: front-end and full-stack web developers, web designers who code, agencies/freelancers maintaining sites.
- Nearest neighbors: Integrated Development Environment / IDE (parent candidate), Code Editor (the dominant actual web-dev surface today), Web Application Builder (the framework being coded against), Visual Website Builder §04.16 (non-developer content-site authoring), Cloud IDE (hosting axis), Web Browser / browser devtools (the run surface).
- Open questions going in: (1) is the browser-terminated preview loop definitional or merely common? (2) is integrated debugging definitional for this leaf, given that the historical authoring pole (Dreamweaver-class) lacks it? (3) does the visual/authoring pole belong in this Type at all, or in Visual Website Builder territory?

## Research Questions

1. What do the products call themselves, and what is their declared subject matter?
2. What is the unit of work (project/site), and what attaches to it?
3. What is the edit→run→see loop? Where does the app actually execute, and how does the environment relate to the browser?
4. Is debugging integrated, and against which runtimes (browser, Node.js)?
5. What web-specific machinery exists (HTML structure tools, CSS rule/style inspection, cross-language awareness, live preview/reload, framework integration)?
6. Does the visual/authoring pole (visual page editing, master pages, publish-to-host) constitute a different core or a variant of the same Type?
7. Where exactly are the boundaries: general IDE, code editor, web application builder (framework), visual website builder, cloud IDE?
8. Historical check: does the 1990s–2000s generation of professional web tools (Dreamweaver/FrontPage-class authoring tools, early code-first web IDEs) satisfy the same core without modern machinery?

## Representative Products

| Product | Pole | Why sampled | Evidence quality |
|---|---|---|---|
| WebStorm (JetBrains) | dedicated code-first web IDE, commercial | the canonical surviving "web IDE" label; rich product/features docs | Tier 2 (product + features pages; help center unreachable) |
| Pinegrow Web Editor | independent visual+code web editor, active indie | the professional visual-authoring pole on standard files; rich official docs | Tier 1 (docs) + Tier 2 (product page) |
| Apache NetBeans | open-source general IDE carrying web tooling | the "general IDE doing web" pole — tests the domain-variant thesis | Tier 2 (product page; tutorial pages 404) |
| VS Code (Microsoft) | boundary witness | the dominant actual web-dev surface; classified by Microsoft as a code editor | A (from code-editor + IDE passes, 2026-09-07/08) |
| Adobe Dreamweaver (class) | historical authoring-pole heavyweight | the lineage anchor of the category | Tier 3 only (Adobe unreachable; Pinegrow comparison + founder lineage quote) |

Coverage check: commercial vs indie vs open source; code-first vs visual-authoring vs general-IDE poles; dedicated vs general tooling; one deliberate out-of-Type witness. Stop condition satisfied: further fetches repeated existing patterns or failed (Adobe, JetBrains help, NetBeans tutorials — recorded below).

## Sources

Fetched 2026-09-09:

- WebStorm — product page: https://www.jetbrains.com/webstorm/ — Tier 2
- WebStorm — Features page: https://www.jetbrains.com/webstorm/features/ — Tier 2
- Pinegrow — product page: https://pinegrow.com/ — Tier 2
- Pinegrow — "Interactive Introduction to Pinegrow" (official docs): https://pinegrow.com/docs/getting-started/quick-introduction-to-pinegrow/ — Tier 1
- Pinegrow — "Pinegrow for Dreamweaver Users – User Review" (republished user review): https://pinegrow.com/pinegrow-for-dreamweaver-users/ — Tier 3
- Apache NetBeans — homepage: https://netbeans.apache.org/ — Tier 2

Cross-referenced (read, not fetched): research/integrated-development-environment-ide.md (IDE core + VS Code witness evidence), research/code-editor.md (via the IDE pass's summary), research/cloud-ide.md (via STATUS.md note), research/web-application-builder.md (boundary 5), research/embedded-firmware-development-ide.md (host↔target bridge precedent).

Source-access limitations (recorded per the evidence rules):

- **Adobe Dreamweaver**: helpx.adobe.com returned 403 and adobe.com timed out (2 attempts, abandoned). Dreamweaver-class evidence rests on Tier 3 sources (Pinegrow's Dreamweaver-comparison page; Pinegrow founder's lineage quote naming Dreamweaver/FrontPage/Expression as the professional visual web tools). No Dreamweaver-specific operational claims are made anywhere in this research.
- **JetBrains help center**: three help-topic URLs 404'd (abandoned per retry rule). WebStorm evidence is held at product/features-page strength; no help-topic-level mechanics (exact debug configuration semantics, run-configuration details) are asserted.
- **NetBeans tutorial pages**: two tutorial URLs 404'd (abandoned). NetBeans web-tooling evidence is held at product-page strength.
- Wikipedia (Dreamweaver) fetch timed out; abandoned. Historical check kept reasoning-based with the Tier 3 lineage quote as the only external corroboration.

---

## Product Observations

### WebStorm (JetBrains) — evidence layer A at product/features-page strength

From jetbrains.com/webstorm/ and /webstorm/features/:

- Self-label: "The JavaScript and TypeScript IDE"; "the JetBrains IDE for JavaScript and TypeScript".
- **Batteries-included web stack**: "Get straight to coding without having to install and configure lots of plugins. WebStorm includes everything you need for JavaScript and TypeScript development right from the start" — JavaScript, TypeScript, HTML, CSS, React, Angular, Vue, Node.js, SQL.
- **Project-scope analysis (key evidence)**: "WebStorm analyzes your entire project when you first open it. This enables fast navigation, advanced coding assistance, and safe refactoring – even in large projects."
- **Cross-language web-stack awareness (key evidence)**: code completion "context and type-aware" and "work across different languages – i.e. class names from CSS will be completed in your *.js* files"; Emmet, live templates, postfix completion.
- Code quality: "hundreds of inspections for all supported languages"; ESLint/Stylelint integration; errors/warnings "reported in the editor as you type, with plenty of quick-fix options".
- Safe refactorings: "refactoring code safely across the entire codebase… rename files, folders, and symbols as well as extract components, methods, or variables".
- **Built-in HTML preview (key evidence for the browser-terminated loop)**: "You can preview static HTML files right in WebStorm. The changes you make to an HTML file or the linked CSS and JavaScript files will be saved, with the **preview reloaded automatically** so you can see the changes."
- **JavaScript debugging (key evidence)**: "Run and debug **client-side and Node.js applications** right where you edit the code. Add breakpoints, step through the program, set watches, and more – all with a unified experience across different kinds of applications."
- Integrated tools: unit testing (Jest, Mocha, Protractor, Vitest + coverage), Prettier, Docker (run/debug apps in containers), built-in terminal, built-in HTTP Client ("test your web services… create, edit, and run HTTP requests"), package managers (npm, Yarn, pnpm — "install, locate, update, and remove packages from inside the IDE"), database tools + SQL bundled.
- VCS: Git/GitHub integration (compare branches, diff, resolve merge conflicts, manage GitHub projects); Local History ("tracks all changes made to your project files… even if you are not using version control").
- Navigation/search: Search Everywhere, go-to declaration/usages, project navigation, find/replace with project scopes.
- Remote development: "local lightweight client… and a remote server to handle all the heavy processing" (hosting-locus axis, not the target axis).
- AI assistant (chat, test/doc generation, commit messages, project-aware actions); plugins/marketplace; keymaps; accessibility.

### Pinegrow Web Editor — evidence layer A (Tier 1 docs + Tier 2 product page)

From pinegrow.com and official docs:

- Self-label: "visual web editor for professionals"; "HTML and CSS editor"; "Pinegrow lets you work faster with HTML, CSS, SASS, Bootstrap, Tailwind CSS, GSAP Interactions, WordPress and WooCommerce."
- **Standard-files posture (key boundary evidence)**: "Pinegrow works with standard web files and fits into your existing workflow and AI agents"; FAQ: "How is Pinegrow different from other website builders? Pinegrow is a desktop app that works with regular HTML and CSS files… **Pinegrow doesn't add any abstraction on top of your HTML and CSS.** It simply helps you to work with pages and stylesheets more efficiently, either visually or through code. Pinegrow is tailored to professional web developers and designers."
- **Visual editing on the rendered page (key evidence)**: the page view is the primary surface — hover-highlighted elements, click-to-select, element menus (duplicate/delete), drag & drop from a Library panel of HTML elements and components, Tree panel showing "the nested HTML structure of the selected page", Element properties panel (attributes, classes, framework controls e.g. Bootstrap).
- **CSS as rules, not paint (key evidence)**: Style panel — "Visual styling of page elements is done with CSS rules. Each rule has a selector… and properties"; Active tab "displays all CSS rules that affect the selected element"; visual editor controls; style attribute editable then "Save as a CSS rule" (transfers properties into a real rule and removes the attribute); "Dev tools-like editor or code - all working together as one. Edit SASS and LESS, live, without any external tools."
- **Code editing alongside visual**: Element code panel ("edit the code of individual elements… The change is immediately seen on the page"), Page code editor (whole page; "also used for editing CSS code and Javascript files"; selecting in code highlights the element in the page view and vice versa).
- **Responsive multi-view (key evidence for the browser-terminated loop)**: "Each page can have multiple page views showing the page at different sizes and in different devices"; "Edit & test your page on all device sizes at once"; media-query helper detects breakpoints "by analyzing stylesheets"; style changes "reflected on all pages in real time".
- **Project scope**: "Pinegrow projects are plain-old file folders. Just open a folder as a project"; Project panel lists files/subfolders; master pages, smart components with editable areas, partials, static CMS mode (PRO).
- **Publish**: "Publish your websites on Netlify" (docs); live sync with Atom & VS Code ("any edit you make in either app is instantly reflected in both"); Browsersync live preview on any device/browser.
- WordPress theme builder: convert HTML projects into PHP-based standard WordPress themes; WooCommerce shop builder; Pinegrow Interactions (GSAP timeline).
- Sibling products by the same vendor: Piny ("Visual React, Next & Tailwind editor for VS Code, Cursor…"), Vue Designer ("A powerful IDE for Vue applications… works with every Vite project").
- No debugger anywhere in the product/docs — the visual pole's "inspection" is the DevTools-like CSS/style editor, not a JS debugger.

### Apache NetBeans — evidence layer A at product-page strength

From netbeans.apache.org:

- Self-label: "Development Environment, Tooling Platform and Application Framework."
- "Apache NetBeans is much more than a text editor. It highlights source code syntactically and semantically, lets you easily refactor code, with a range of handy and powerful tools."
- **Web stack among supported subjects (key evidence for the general-IDE pole)**: "Java, JavaScript, PHP, HTML5, CSS, and More — Apache NetBeans provides editors, wizards, and templates to help you create applications in Java, PHP and many other languages."
- Cross-platform; plugin ecosystem; tutorials under review (not fetched — see limitations).

### VS Code (boundary witness — not a sample member)

Evidence layer A, from the code-editor pass (2026-09-07) and IDE pass (2026-09-08):

- Microsoft's own classification: "a lightweight, cross-platform **code editor**" (on the Visual Studio IDE page).
- Built-in debugging for JavaScript, TypeScript, Node.js; other runtimes via debugger extensions; `launch.json`/`tasks.json` machinery; folder-centric working set ("lightweight human-readable wrapper over folders").
- Interpretation for this leaf: the dominant actual web-development surface today is a code editor whose web loop is assembled from extensions (including live-preview servers); the working set remains file/folder-centric and the build/run/debug plumbing is delegated. This is the code-editor Type's IDE-adjacent variant, not this leaf's center.

### Adobe Dreamweaver (class) — evidence layer C/Tier 3 only (Adobe unreachable)

From Pinegrow's comparison page and founder statement (Tier 3):

- Pinegrow founder: "visual website building tools aimed at professionals (such as Dreamweaver, FrontPage, Expressions) seem to be a thing of the past. Dealing with code directly is considered to be the best approach." — names the professional visual web tools lineage this leaf's authoring pole descends from.
- Republished Dreamweaver-forum user review (Tier 3): Pinegrow compared as "what Dreamweaver would have been in a parallel universe"; "Master pages, custom reusable components with editable areas are quite handy for quick static sites (like DW)"; visual editing "similar to DW"; "It's like having a super-charged Inspect Element view on your side."
- No Dreamweaver-specific operational claims are made; the class-level picture (visual+code hybrid page/site authoring, live preview, site management, publish-to-server) is held at Tier 3 strength and used only for lineage/variant reasoning.

---

## Cross-product Comparison

| Aspect | WebStorm | Pinegrow | NetBeans | VS Code (witness) | Dreamweaver-class (Tier 3) |
|---|---|---|---|---|---|
| Self-label | "JavaScript and TypeScript IDE" | "visual web editor for professionals" | "Development Environment, Tooling Platform and Application Framework" | "code editor" (per Microsoft) | professional visual web tool (named lineage) |
| Subject | JS/TS/HTML/CSS + frameworks + Node.js | HTML/CSS/SASS + Bootstrap/Tailwind/WordPress | Java, JavaScript, PHP, HTML5, CSS "and more" | everything via extensions | HTML/CSS pages/sites |
| Unit of work | project ("analyzes your entire project") | project = plain folder; master pages/components | project (platform model; page-strength) | folder/workspace (lightweight) | site (class-level) |
| Web-stack editing | cross-language completion (CSS classes in .js), inspections, refactorings, quick fixes | tree/DOM structure, active CSS rules on selection, style-attribute→rule, element/page code editors | syntactic+semantic highlighting, refactoring (page-strength) | IntelliSense + web extensions | visual+code hybrid (class-level) |
| Run surface | **built-in HTML preview, auto-reloaded on save** | **page views at device sizes, live multi-page editing, Browsersync live preview** | (not observed this pass) | via live-preview extensions | live preview (class-level) |
| Debugging | **client-side + Node.js debugging in-IDE** (breakpoints, stepping, watches) | none in docs — DevTools-like CSS inspection instead | (not observed this pass) | built-in JS/TS/Node; extensions otherwise | none (browser's job; class-level) |
| Build/bundle | package managers, build tools, linters, Prettier in-IDE | none needed (static files; SASS/LESS live-compiled in-tool) | (not observed) | tasks.json delegating to external tools | (class-level) |
| Publish/deploy | (not on features page; framework/CLI territory) | publish to Netlify; WordPress theme export | (not observed) | extensions | site publishing to server (class-level) |
| Extra integrated | testing, HTTP client, Docker, DB tools+SQL, terminal, VCS, remote dev, AI | WordPress/WooCommerce builders, interactions/timeline, static CMS | wizards/templates, plugin platform | terminal, VCS, extensions marketplace | (class-level) |

### Evidence-layer roll-up

- **A (directly observed)**: every WebStorm and Pinegrow cell above is anchored to a fetched official page; NetBeans cells to its product page; VS Code cells to prior-pass official docs.
- **B (cross-product commonality)**: web-stack-aware editing in all in-type samples; a project/site/folder working scope in all; the browser-terminated preview loop in every dedicated web tool (WebStorm built-in preview; Pinegrow page views + Browsersync; Dreamweaver-class live preview at Tier 3); debugging integrated in the code-first pole (WebStorm; VS Code witness) and absent in the visual pole (Pinegrow; Dreamweaver-class).
- **C (canonical inference)**: the three-part defining core below; the variant resolution vs the general IDE; the two-pole structure of the category.

---

## Canonical Model

### L0 — Defining Invariant (deliberately small)

A Web Development IDE is a development environment whose subject is **software delivered through a web browser**. Three jointly-held structures:

1. **Web-target working scope** — a first-class working context (project, site, or opened web folder) whose subject is a web application/site; the unit to which tooling, preview, and settings attach. Realized as projects (WebStorm), plain folders opened as projects (Pinegrow), sites (Dreamweaver-class), or the platform project model of general IDEs carrying web tooling (NetBeans).
   *Remove → a file/folder editor with no web working scope.*
2. **Web-stack-integrated editing** — editing assistance computed against web semantics: HTML structure (element trees, DOM relationships), CSS as rules/selectors with active-rule inspection, JS/TS symbols; cross-language awareness across the stack (e.g. CSS class names completed inside JS); framework awareness era-common.
   *Remove → a generic text editor.*
3. **The browser-terminated loop** — the environment operates the app's development cycle from within: build/bundle where needed (integrated tooling or delegated to framework CLIs), serve the app locally, present the **rendered result in a browser surface** (built-in preview or launched browser), and refresh on change — the edit→see loop closes inside the environment, with the browser as the app's execution surface.
   *Remove → an editor with separately operated tooling and no in-environment run surface (the code-editor Type's IDE-adjacent variant).*

Jointly-held is load-bearing:

- 1 alone = a folder of web files.
- 2 alone = a web-aware text editor.
- 3 without 1+2 = a live-reload server utility.
- 1+2 without 3 = a code editor with web language support (the VS Code witness pattern).
- 1+3 without 2 = a preview harness.
- 2+3 without 1 = a single-file playground.

### L1 — Common Mature Structure

- **Integrated debugging against web runtimes** — breakpoints, stepping, watches against client-side (browser) and Node.js runtimes, with runtime state mapped back to source. Universal in the code-first pole (WebStorm explicit; VS Code built-in for JS/TS/Node); **absent in the visual/authoring pole** (Pinegrow ships no debugger; Dreamweaver-class historically left execution inspection to browser devtools). Held as common-in-pole, NOT definitional for this leaf — the pole-dependence is the leaf's key difference from the general IDE, where debugging sits inside the core.
- Testing integration (Jest/Mocha/Protractor/Vitest-class runners with coverage — WebStorm).
- VCS integration, integrated terminal, package-manager integration (npm/Yarn/pnpm), HTTP/API clients, linters/formatters (ESLint/Stylelint/Prettier).
- Framework tooling integration (React/Angular/Vue-class; Bootstrap/Tailwind visual controls at the authoring pole).
- Navigation/search across the project; inspections with quick fixes; safe refactorings.
- Publish/deploy paths (authoring pole: publish static output to a host — Netlify in Pinegrow's docs, server publishing in the Dreamweaver class; code-first pole: delegates to framework/CLI deploy).
- Extension/plugin ecosystems; AI assistance (era-current).

### L2 — Variant / Optional Structure

- **Authoring posture** — the category's two poles:
  - *code-first* (WebStorm-class): the code is the substrate; visual surfaces are auxiliary (built-in preview).
  - *visual/authoring-first* (Dreamweaver/Pinegrow-class): the rendered page is the primary surface; code is edited alongside it (element code panels, page code editors); distinctive machinery: master pages, smart components with editable areas, static CMS mode, WordPress/WooCommerce theme export, publish-to-host. The substrate remains standard web files — this is what keeps the pole inside this Type and out of Visual Website Builder territory.
- **Dedicated web tool vs general IDE carrying web tooling** (WebStorm/Pinegrow vs NetBeans-class) — the same subject served from different packaging.
- **Debugging depth** — full in-IDE debugger (code-first pole) vs none/external (authoring pole).
- **Deployment posture** — static publish to a host (authoring pole) vs framework/CLI-mediated deployment (code-first pole).
- **Hosting locus** — local desktop tool vs online edition (Pinegrow Online) vs remote-development front ends (WebStorm) — the Cloud IDE axis, orthogonal to this leaf's target axis.
- **AI posture** — embedded assistants/agents (era-current capability overlays).
- Business model: commercial subscription (WebStorm), one-time/subscription indie (Pinegrow), free open source (NetBeans).

### L3 — Vendor-specific Detail (research notes only)

- WebStorm: "superset" positioning within the JetBrains family; bundled database tools + SQL at no extra cost; Local History; Search Everywhere; IdeaVim; Settings Sync across JetBrains IDEs; remote-development client/server split; AI credits/bring-your-own-key posture.
- Pinegrow: page-view model (multiple simultaneous device views of one page); style-attribute→CSS-rule workflow; Repeater; simplified code syntax for element editing; PRO edition split (projects/master pages/CMS); WordPress smart actions mapped to page elements; GSAP-based Interactions add-on; Piny/Vue Designer sibling products; Browsersync integration; Netlify publish.
- NetBeans: "Fits the Pieces Together" platform framing; tooling platform + application framework roles.
- VS Code (witness): launch.json/tasks.json machinery; debug-adapter extension model; Live Server-class preview extensions (extension-supplied, not built-in).
- Dreamweaver-class: site management + server publishing model (Tier 3, class-level only).

---

## Vendor-specific Findings

See L3. None promoted to the canonical model. Notably: the built-in-preview *mechanism* (WebStorm's auto-reloading static preview vs Pinegrow's multi-device page views vs Browsersync) is implementation; the invariant is the browser-terminated loop itself. WordPress/WooCommerce builders are Pinegrow-specific packaging of the authoring pole. Database tools in WebStorm are suite packaging, not web-IDE structure.

## Rejected Findings

- "A Web Development IDE is defined by visual/WYSIWYG editing" — rejected; the code-first pole (WebStorm) has no visual page editor and is the category's center of gravity today. Visual authoring is a pole/variant.
- "A Web Development IDE is defined by integrated debugging" — rejected *for this leaf*: the authoring pole (Pinegrow observed; Dreamweaver-class at Tier 3) satisfies the Type without any debugger. Debugging is common-in-pole (code-first), not definitional. (Contrast: the general IDE holds debugging inside its core — this pole-dependence is precisely why this leaf is documented as a specialized sibling rather than a pure subset.)
- "A Web Development IDE must bundle framework tooling" — rejected; Pinegrow works on plain static files with no build step; WebStorm's tooling integrates external package managers/build tools rather than owning them.
- "The category is defined by live reload" — rejected as mechanism; the invariant is the browser-terminated loop (preview + refresh-on-change), of which live reload is the current-era implementation.
- "Dreamweaver-class tools belong to Visual Website Builder" — rejected from this side: the authoring pole works on standard web files with code as the substrate and is aimed at professionals who code (Pinegrow's own FAQ draws this line); website builders replace the code substrate for non-developers.

---

## Boundary Findings

1. **vs Integrated Development Environment / IDE** (processed 2026-09-08) — the designated joint-review seam; **DISCHARGED from this side**. The code-first pole satisfies the general IDE's four legs with the web stack as subject: project scope ✓ (WebStorm "analyzes your entire project"), scope-bound editing ✓ (cross-language, project-wide refactorings), integrated build/run ✓ (realized as serve + browser preview — the run surface is the browser rendering the app), integrated debugging ✓ (client-side + Node.js). The web leaf therefore **resolves as the web-targeted variant of the IDE Type, keep-both documented** — not an independent Type. What this leaf adds beyond a domain label: (a) the **browser-terminated loop** as the run surface — the app executes in a browser, not in a host process the IDE owns, and the edit→see loop closes inside the environment; (b) the **authoring-first pole** (visual page editing + publish-to-host), a substantial population the general IDE definition never claimed and which fails the general IDE's debugging leg. The embedded-firmware sibling earned independence via the host↔target hardware bridge (cross-build → flash → probe-debug); web has no such bridge — dev server and browser are host-adjacent, so the web leaf does not earn full independence. Both leaves stay in the directory; each documents its own lens.
2. **vs Code Editor** (processed 2026-09-07; witness VS Code) — the same seam as the IDE/editor boundary, sharpened for web: the dominant actual web-dev surface is a code editor whose web loop is assembled from extensions (debug adapters, live-preview servers, framework extensions). The seam is the working set (file/folder vs web project scope) and who owns the loop (delegated plumbing vs in-environment loop with a built-in run surface). Convergence pressure noted by the IDE pass applies here with full force.
3. **vs Web Application Builder** (processed 2026-09-09) — where code is written vs what the code is written against; **ratified from this side** (that pass's boundary 5). Frameworks ship CLIs/DevTools as satellites; the IDE is the environment in which the framework's code is edited, run and debugged. A framework without an editor exists; an editor without a framework behind it is this leaf.
4. **vs Visual Website Builder (§04.16)** — content-site authoring for non-developers vs professional web development on standard files. Pinegrow's own FAQ is the in-sample boundary statement: it "works with regular HTML and CSS files", "doesn't add any abstraction on top of your HTML and CSS", and is "tailored to professional web developers and designers" — the code substrate and the professional audience separate the authoring pole from website builders even when the surfaces look similar.
5. **vs Cloud IDE** (processed) — hosting locus (where development happens) vs target domain (what is built); orthogonal axes (cloud-ide pass note ratified). A cloud IDE can host development of a web app; Pinegrow Online and WebStorm remote development are hosting-locus variants of this leaf's tools, not Type membership changes.
6. **vs Web Browser / browser developer tools** — the browser is this Type's run surface and (at the authoring pole) the external inspector; the IDE integrates browser-attached debugging and DevTools-like inspection rather than being a browser. No Type collision; recorded because the run surface's identity is the leaf's distinctive structure.
7. **vs Mobile App Development Platform / Desktop App Development Framework** (processed 2026-09-09) — the ratified genus artifact test separates: application served to a browser (this leaf's subject) vs package on a mobile OS vs installed desktop executable.
8. **vs Debugger / Build Automation System** — component Types the code-first pole integrates (browser/Node debuggers, bundlers); standalone engines remain separate Types (consistent with the IDE pass's resolution).

---

## Historical / Market-Sample Check

Question: would older, regional, or differently-positioned web development tools still fit the L0?

- **1990s–2000s professional visual web tools (Dreamweaver/FrontPage/Expression lineage)**: site scope + web-aware editing (visual + code) + browser preview — satisfies all three legs with no modern machinery. Evidence: Tier 3 only (Pinegrow founder's lineage quote naming the class; the republished Dreamweaver-forum review describing the class's master-pages/visual-editing model). Held at class level, no version-level claims. ✓-at-Tier-3
- **Early code-first web IDEs (Aptana-class, 2000s)**: project scope + web-stack editing + browser run/debug loop — satisfies the legs; reasoning-based, not fetched. ✓-reasoning
- **General IDEs with web tooling (NetBeans-class, 2000s→present)**: the same environment carrying HTML5/CSS/JS tooling among other languages — the packaging variant predates the dedicated-web-tool framing. ✓ (product-page strength)
- **Static-file era**: the authoring pole's core needs no bundler, no framework, no Node — plain HTML/CSS/JS files, a folder, a preview. The L0 deliberately does not require any modern machinery. ✓

Conclusion: the L0 survives the historical check. Live reload, framework integration, TypeScript, AI assistance, and cloud/remote postures are era machinery, not structure.

---

## Uncertainties

1. **Adobe Dreamweaver official documentation unreachable** (helpx 403, adobe.com timeout) — the authoring pole's lineage evidence rests on Tier 3 sources; all Dreamweaver-class claims are held at class level and no Dreamweaver-specific operational detail is asserted anywhere.
2. **JetBrains help center unreachable** (404 ×3) — WebStorm's debug/run mechanics are known only at features-page strength ("run and debug client-side and Node.js applications… breakpoints, stepping, watches"); configuration-level semantics not asserted.
3. **NetBeans tutorial pages unreachable** (404 ×2) — NetBeans web-tooling evidence is product-page strength; its HTML5/JS project model and browser-debug integration are NOT asserted this pass.
4. The exact market share/population of dedicated web IDEs today (vs code editors with extensions) is market context, not asserted numerically.
5. Whether the authoring pole's publish-to-host machinery (FTP-class site publishing) should be weighted as common structure or pole-specific variant is held as variant — only Pinegrow's Netlify publish is directly observed; the Dreamweaver-class publishing model is Tier 3.

---

## Final Synthesis

A Web Development IDE is the development environment whose subject is browser-delivered software. Its defining core is the conjunction of three structures: a **web-target working scope** (project/site/folder whose subject is a web application), **web-stack-integrated editing** (assistance computed against HTML structure, CSS rules, and JS/TS symbols, with cross-language awareness), and the **browser-terminated loop** — the environment itself builds/serves the app and presents its rendered result in a browser surface, refreshed on change, with the browser as the app's execution surface. Around that core, the code-first pole (WebStorm-class) adds the full IDE machinery — integrated debugging against browser and Node runtimes, testing, VCS, package managers, HTTP clients — and thereby satisfies the general IDE's core with the web stack as subject; the visual/authoring pole (Dreamweaver/Pinegrow-class) makes the rendered page the primary editing surface, adds site-authoring machinery (master pages, components, static CMS, publish-to-host), and historically ships without a debugger. The leaf therefore resolves as the **web-targeted variant of the Integrated Development Environment Type, keep-both documented**: the general IDE pass's flag is discharged, the browser-terminated loop and the authoring heritage are recorded as this leaf's own structure, and the seams to Code Editor, Web Application Builder, Visual Website Builder, and Cloud IDE are ratified from this side.
