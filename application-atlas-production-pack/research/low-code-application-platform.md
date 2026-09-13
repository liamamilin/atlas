# Research Notes — Low-code Application Platform

Research date: 2026-09-08. Methodology: atlas-writer v1.1 (WORKFLOW/WRITING_GUIDE in update-v1/). Evidence layers: A = directly observed in fetched official documentation for a named product; B = cross-product commonality across the sample; C = canonical inference. L0/L1/L2/L3 per abstraction hierarchy.

---

## Research Goal

Establish what a Low-code Application Platform (LCAP) is as an Application Type: what the central artifact is, what the authoring medium is, how the build→run loop works, what lifecycle and governance machinery mature products carry, and where the Type's boundaries lie against its dense neighborhood (no-code builders, website builders, BPM/workflow platforms, IDP, RPA, code-first development platforms).

## Initial Boundary (pre-research hypothesis)

- Core hypothesis: a platform whose central artifact is a **business application** (data model + user-facing interface + logic), authored primarily by configuring/modeling platform-provided building blocks, and which **runs the application itself** (build and run in one product).
- Nearest neighbors to test: No-code Application Builder (sibling leaf), Web Application Builder (§04.16), Internal Developer Platform / Portal (§12, both already processed), Business Process Management Platform (§10, processed — recorded boundary "process model vs application as central artifact"), Workflow Management Platform (§10, processed — same seam), Robotic Process Automation Platform (§10, processed — "operate existing apps vs build new"), Mobile/Web/Desktop development platforms (§12 siblings), Structured Table / Lightweight Database Application (§03.03).
- Known straddles from prior passes: Appian self-labels in the low-code space while being process-centric (recorded in the BPM pass as "straddles observed"); Retool is code-heavy but markets as low-code.

## Research Questions

1. What is the central managed artifact — an application? a process? a website? What is it made of?
2. What is the authoring medium — visual configuration, model definition, scripting, code? What role does code play?
3. Where does the finished application run, and who operates that runtime?
4. What does the typical build → publish/deploy → run → iterate loop look like?
5. What data substrate do platforms provide — built-in data platform, external sources, or both?
6. Who builds (audience gradient) and who governs (admin surface)?
7. What lifecycle machinery exists (versions, environments, deployment)?
8. What does the platform give end users of the finished app (clients, access control, distribution)?
9. Which capabilities are definitional vs common vs variant vs vendor-specific?
10. Historical check: would older/regional/platform-native members (4GL/RAD generation, forms-over-data packages) satisfy the definition, or is it over-fit to the cloud visual-canvas era?

## Representative Products

Selection rationale: market representativeness + documentation completeness + different product philosophies + different customer tiers.

| Product | Philosophy / pole | Tier reached | Access notes |
|---|---|---|---|
| Microsoft Power Apps | platform-suite pole; citizen+pro mix; built-in data platform (Dataverse) | Tier-1 (Microsoft Learn, multiple pages fetched) | fully reachable |
| Mendix (Siemens) | model-driven enterprise pole; desktop studio; full SDLC + version control | Tier-1 (docs.mendix.com, multiple pages) | fully reachable |
| Retool | developer-first pole; code-friendly low-code for internal tools; external-data-centric | Tier-1 (docs.retool.com, multiple pages) | fully reachable |
| Zoho Creator | SMB/midmarket pole; forms-over-data; scripting extension; low cost | Tier-2 (resource center + detailed quickstart guide) | fully reachable |
| Oracle APEX | database-embedded pole; declarative; lives inside Oracle Database | Tier-1 (docs.oracle.com) | fully reachable |
| Appian | process-first low-code pole (market anchor) | — | docs.appian.com 403 ×2, appian.com 406 — abandoned per network rule; **no claims from Appian** |
| OutSystems | enterprise developer-centric pole (market anchor) | — | success.outsystems.com empty ×2, www.outsystems.com/product empty — abandoned; **no claims from OutSystems** |
| Bubble | no-code pole (market anchor for the boundary seam) | — | not fetched this pass; boundary handled via low-code side evidence + joint-review flag |

## Sources

- Power Apps: https://learn.microsoft.com/en-us/power-apps/powerapps-overview ; https://learn.microsoft.com/en-us/power-apps/maker/ (fetched 2026-09-08)
- Mendix: https://docs.mendix.com/ ; https://docs.mendix.com/refguide/studio-pro-overview/ (fetched 2026-09-08)
- Retool: https://docs.retool.com/ ; https://docs.retool.com/build/apps/quickstart ; https://docs.retool.com/apps/quickstart (fetched 2026-09-08)
- Zoho Creator: https://www.zoho.com/creator/help/ ; https://www.zoho.com/creator/help/new-quickstart-guide.html (fetched 2026-09-08)
- Oracle APEX: https://docs.oracle.com/en/database/oracle/application-express/24.2/htmdb/understanding-oracle-apex.html (fetched 2026-09-08)
- Market anchors (not fetched, no claims): Appian (docs 403, site 406), OutSystems (docs/site empty), Bubble, ServiceNow App Engine, Salesforce Platform.

---

## Product Observations (evidence layer A unless noted)

### Microsoft Power Apps

- Self-positioning: "a suite of apps, services, and connectors, as well as a data platform, that provides a rapid development environment to build custom apps for your business needs"; "build custom business apps that connect to your data stored either in the underlying data platform (Microsoft Dataverse) or in many online and on-premises data sources"; "Power Apps democratizes the business-app-building experience by enabling users to create feature-rich, custom business apps without writing code."
- Two documented authoring styles for the same artifact class ("two types of apps: canvas and model-driven"):
  - **Canvas apps**: "start with your user experience… craft a highly tailored interface with the power of a blank canvas and connect it to your choice of more than 200 data sources"; built in **Power Apps Studio** ("makes creating apps feel more like building a slide deck in Microsoft PowerPoint"); buildable from Dataverse, SharePoint list, Excel data, or blank.
  - **Model-driven apps**: "start with your data model. You build up from the shape of your core business data and processes in the Dataverse to model forms, views, and other components. Model-driven apps automatically generate a great UI that's responsive across devices." Configured via forms, views, business rules, process flows, security roles, dashboards.
- **Dataverse** = the built-in data platform ("securely store and manage data within a set of standard and custom tables… add columns"); Dynamics 365 apps run on the same Dataverse, so platform apps can sit directly against core business data "without the need for integration."
- **Pro-developer extension explicitly documented**: "Developers are app makers who write code to extend… apply server-side logic with Azure functions, plug-ins, and workflow extensions, apply client-side logic with JavaScript, integrate with external data by using virtual tables and webhooks, build custom connectors."
- **Roles split across the platform**: makers (make.powerapps.com + Studio), app users ("Run apps that you created, or that someone else created and shared with you, in a browser or on mobile devices"), admins (Power Platform admin center: "create and manage environments, view Dataverse analytics"), developers (code extension).
- **Run model**: apps "run seamlessly in browser and on mobile devices"; "You need a license to play the apps you make with Power Apps" — end-user execution is licensed per user.
- **AI-era generation**: Copilot ("describe the app you want and AI designs it") and Plans ("describe your business use case in natural language… generates a complete Power Platform solution… including Microsoft Dataverse tables, canvas apps, model-driven apps, Power Pages sites, Power Automate flows, and Copilot Studio agents").
- Platform-suite embedding: apps can be created inside Microsoft Teams; US Government cloud plans (GCC/FedRAMP-class posture documented).

### Mendix

- **Studio Pro** is "a tool for creating, viewing, and editing your Mendix applications" — a desktop modeling IDE. "An app consists of individual files (also known as documents) and settings that are grouped in folders and modules."
- **Model surface (from the refguide structure)**: Domain model editor — entities, attributes, associations, access rules, validation rules, event handlers, indexes, OQL; Page editor — data widgets (data view, data grid, list view), input elements, layouts/snippets/building blocks/page templates, on-click events; Application logic — **microflows** (server-side visual flows) and **nanoflows** (client-side), with activities (create/commit/retrieve objects, call REST/web service, send email, call Java/JavaScript actions), decisions, loops; **workflows** (BPMN-adjacent user-task orchestration documented as a Mendix concept).
- **Consistency checking**: "Consistency Errors" documentation — the model is checked (page editor and navigation consistency errors), i.e. the model must be coherent before running.
- **Code extension documented**: Call Java Action, Call JavaScript Action; extensibility via C# API and Web API release notes; Model SDK / Platform SDK / Metamodel.
- **Version control inside the studio**: Commit, History, Branch Line Manager (create branch line), Merge dialog; download/upload from version control server; "Versioning an App Deployed to the Cloud."
- **Run/deploy loop**: "Deploy your app by clicking the Publish or Run Locally buttons. To view your deployed app, click View App."; Create Deployment Package; Deploy to the Cloud dialog; deployment targets documented: Mendix Cloud, Mendix on Kubernetes (private cloud), Mendix on Azure, SAP BTP, other on-premises options. Mendix Pipelines for deployment automation.
- **Ecosystem**: Mendix Portal (project/deployment collaboration), Marketplace ("Consuming Add-on Modules and Solutions", importing/exporting modules and widgets), Control Center (platform governance).
- **Integration into external data**: External Entities, View Entities, "Query External Database" activity, call REST/web service actions.
- **AI-era generation**: Maia ("Mendix AI Assistance") — chat, generate for domain model/pages/microflows/workflows, MCP client/server, best-practice recommender.
- Multi-language app translation built into the modeler (batch translate, translatable texts).

### Retool

- Self-positioning: "Create production-ready apps using Retool, your favorite coding agent, or imported React code. Whether you're improving an app or starting from scratch, everything you build is secure by default." Docs sections: Build (Apps new AI builder + Classic drag-and-drop IDE), Automate (Agents, Workflows), Code (Queries, Data Sources, Source Control), Manage (Administration, Permissions, SSO), Host (Retool-hosted, Self-hosted).
- **Classic app anatomy (documented)**: components (drag-and-drop library, "over 100 UI components"), pages (each with own URL/deep-linking), frames (header/sidebar/drawer/modal/split pane); properties configured with static values or `{{ }}` embedded JavaScript expressions; a maintained **dependency graph** ("similar to how spreadsheet formulas work") that re-evaluates downstream references; event handlers trigger queries/actions.
- **Data model: external-first.** "A resource is a saved set of user-configured properties that determines how Retool connects to a data source, such as a PostgreSQL database or REST API… When a resource query is run, Retool proxies the request to the data source, server-side." Queries ("a piece of code you write to interact with a resource and perform CRUD operations") in SQL/JS/GraphQL or GUI mode; transformers (reusable JS blocks). A built-in Retool Database exists as an optional substrate (product listing), but the documented center is connecting external resources.
- **Code is first-class**: JavaScript expressions almost anywhere; JS queries; custom components built with React and TypeScript ("Custom Component Libraries… deploy into any classic app"); HTML/IFrame components.
- **Publish/run loop**: publish checklist ("All functions are approved… changes do not conflict with the published version"), app URL (`<org>--<appName>.retool.app` or custom domain / self-hosted URL), folder-based access ("All users with use access to the folder you select will be able to use your app"), release tagging, branches (threads/branches concept; publishing archives the branch).
- **Governance**: org/users/spaces, permissions, SSO, Retool API; hosting choice Retool-hosted or self-hosted.
- **Audience vocabulary**: quickstart personas are "data and analytics experts", "developer experience advocates", "operations leads" — building support consoles, deploy dashboards, approval apps, refund tools (internal-tool-shaped). Platform pages: Data teams / Engineering / Operations / Enterprise.
- Sibling products inside the same platform: Workflows ("Automate jobs, alerts, and ETL tasks"), Agents, Mobile apps, Retool Database.

### Zoho Creator

- Self-positioning: "low-code platform"; quickstart "covers a small set of Creator's no-code features… for users of all (or no) prior programming experience."
- **Solution structure**: solutions = Applications (+ Analytics + Flows as solution types). Application builder contains: **Forms** (field types; **look-up fields** = "used in Creator to build relationships between form entities"; import from spreadsheet creates "an online form automatically (based on the source file structure and data types)… and an associated report"), **Reports** (list, **Kanban** — "drag and drop the cards… to update the status", calendar, etc.), **Pages** ("custom screens… drag and drop"; embed forms, reports, charts, panels), **Workflows** (approval workflows with approvers + data-access actions; form workflows triggered on form events/load/field input; **Blueprints** = "map business processes" with stages, transitions, criteria, transition owners).
- **Scripting extension: Deluge** — "Deluge, Zoho's proprietary programming language" for validation logic and record updates (documented with inline code examples in the quickstart). Also JS widget API, microservices, REST API, SDK.
- **Run/publish model**: edit mode vs "**published version**" of the application ("Access the application… in the published version of the application"); **Environments** documented for SDLC ("Adhere to the SDLC process by utilizing this restricted area to thoroughly test your applications before publishing").
- **Manage/govern**: Users (Admins/Users/Developers roles; "Users are largely end-users"), roles and permissions per solution and per environment, Organizations, Governance ("Establish governing principles and protocols"), Metrics (usage dashboard), Operations, Billing.
- **Distribution surfaces**: web app; branded mobile apps ("Rebrand your Creator application as a mobile app and distribute it on iOS and Android"); **portals for external users** ("Create self-service portals for external users with dedicated login credentials"); embed.
- **Host**: Zoho cloud; **On-premises** edition ("Host custom applications on your infrastructure").
- **Ecosystem**: Developer Console → publish apps/extensions to Zoho Marketplace (public, with compliance review, pricing) or privately to clients; .ds export/import.

### Oracle APEX

- Self-positioning: "Oracle APEX is an enterprise low-code application platform that enables you to build scalable, secure enterprise apps"; "a hosted declarative development environment for developing and deploying database-centric web applications. Thanks to built-in features such as user interface themes, navigational controls, form handlers, and flexible reports, APEX accelerates the application development process."
- **Metadata-driven engine (documented)**: "When you create or extend an application, APEX creates or modifies metadata stored in database tables. When the application is run, the APEX engine then reads the metadata and displays the application."
- **Runtime = the database**: "provides all the tools you need to build apps in a single, extensible platform, which runs as a part of Oracle Database"; "All processing, data manipulation and business logic is executed in the database."
- **Engine-provided services**: "Session state management, Authentication services, Authorization services, Page flow control, Validation processing."
- **Dev/runtime split**: "Runtime environment. In a runtime environment users can run applications but cannot modify them. Select this option for production implementations. / Full development environment… develop, modify, run, and delete APEX applications." Workspace + App Builder as the development surfaces.

---

## Cross-product Comparison

| Dimension | Power Apps | Mendix | Retool | Zoho Creator | Oracle APEX |
|---|---|---|---|---|---|
| Central artifact | app (canvas or model-driven) inside environments/solutions | app = modules of modeled documents (domain model + pages + logic) | app = components + queries + resources, in org spaces/folders | application (forms + reports + pages + workflows) inside solutions | application = metadata rows in DB tables, inside workspace |
| Data substrate | built-in (Dataverse tables) + 200+ external sources | built-in (entities → relational storage) + external entities | external resources (DB/API) + optional built-in DB | built-in (forms-as-tables with lookups) + Flow integrations | the host Oracle Database itself |
| Interface authoring | canvas drag-drop (UI-first) or generated from data model (model-first) | page editor: widgets, layouts, snippets, building blocks | drag-drop canvas: components/frames/pages + inspector | form builder + page builder + report builder | declarative page/region/item builder + themes |
| Logic authoring | formulas + business rules + flows; server/client code extension | microflows/nanoflows (visual) + Java/JS actions + workflows | queries (SQL/JS/GraphQL/GUI) + event handlers + transformers + JS | approval/form workflows + Blueprints + Deluge scripts | declarative validations/processes + PL/SQL |
| Code's role | explicit extension tier ("developers are app makers who write code") | explicit extension tier (Java/JS actions, SDKs) | first-class glue (expressions/queries/custom React components) | extension tier (Deluge, JS widgets) | extension tier (SQL/PLSQL) |
| Who runs the app | platform-hosted; browser + mobile clients | Mendix Cloud / private K8s / Azure / BTP / on-prem via platform deployment machinery; Run Locally in dev | Retool-hosted or self-hosted instance | Zoho cloud or on-premises edition | the Oracle database (any edition/wherever it runs) |
| Lifecycle machinery | environments + admin center; solutions; publish | version control + branch lines + deployment packages + pipelines | branches + publish checklist + release tags + folders | environments (SDLC) + publish | runtime-only install for production; app export/import |
| Governance surface | Power Platform admin center (environments, analytics) | Portal + Control Center | org/users/spaces + permissions + SSO | Manage section: users/roles/permissions + governance + metrics | workspace/instance admin; authorization schemes |
| End-user access | license to run apps; share to users | access rules per entity + app-level security; users via portal | folder use-access + permissions | user roles per solution/app | authorization schemes; workspace users |
| Ecosystem | templates/Marketplace; Teams embedding | Marketplace modules | templates, custom component gallery | Marketplace publishing/monetization | packaged apps; export/import |
| AI-era generation | Copilot + Plans (solution-level generation) | Maia (model-level generation) | AI app builder + Ask AI | AI features (marketing surface) | (not observed this pass) |
| Audience center | citizen makers + pro developers | professional/enterprise dev teams incl. business engineers | developers/data teams (code-comfortable) | business developers + scripters | database-centric dev teams |

### Cross-product commonalities (layer B)

1. **The application is the named, persistent central artifact in every sample** — always composed of at least a data substrate, user-facing interface(s), and logic, and always held as an individually manageable object (created, edited, published, shared, versioned, deleted).
2. **Authoring is configuration/model-driven on platform-provided building blocks** — every product's primary medium is assembling from the platform's own primitives (tables/forms, widgets, pages, flows, rules); every product also has a code tier, but in none of them is code the *primary* medium for a standard business app (Retool is the closest to code-first, yet still assembles on components/queries/resources).
3. **The platform runs what is built** — build tooling and runtime are the same product in all five; the loop is edit → publish/deploy → end users run it (browser and/or mobile), and the maker returns to edit in the same environment. Production can run on vendor cloud, customer infrastructure, or (APEX) inside a customer database — but always through the platform's own runtime/deployment machinery.
4. **Data layering: built-in OR external, both poles mature** — Dataverse/entities/forms are built-in substrates; Retool and Power Apps (200+ sources) document external-data-first operation; APEX fuses data and runtime in one DB.
5. **A distinct governance surface exists above the app** — environments, users/roles/permissions, admin consoles in all five.
6. **Publishing/versioning discipline** — draft vs published/live states, environments or branches, and deployment packages/checklists appear in every product (form varies: environments, branch lines, publish checklist, runtime-only install).
7. **End-user access is governed at platform level** — sharing, roles, licenses, or folder permissions decide who can run an app (power: Power Apps licenses; Retool folders; Zoho roles; APEX authorization schemes; Mendix access rules + portal).
8. **AI-assisted generation is the era-current authoring accelerant** (Power Apps Copilot/Plans, Mendix Maia, Retool AI builders) — common in 2026, treated as implementation detail of the authoring leg.
9. **Marketplace/template/component ecosystems** in all five.

---

## Canonical Model (L0 → L3)

### L0 — Defining Invariant (minimal)

A **Low-code Application Platform** is a platform whose:

1. **Central artifact is the application of record** — a persistent, individually identified business application composed of a data model, user-facing interface(s), and executable logic. (Remove → the product is a component library, a modeling tool, an automation platform, or a website builder.)
2. **Primary authoring medium is configuration of the platform's own building blocks** — the maker assembles the application from platform-provided primitives (data structures/forms, interface components, logic flows/rules) rather than primarily by writing source code; code exists, if at all, as an extension tier. (Remove → code-first frameworks/IDEs and development platforms.)
3. **The platform itself runs the finished application** — build tooling and runtime are one product; the maker publishes/deploys through the platform and end users execute the app on the platform's runtime (vendor cloud, platform-managed deployment into customer infrastructure, or a database-embedded engine), with end-user access granted through platform-level mechanisms. (Remove → modeling tools, generators, and frameworks that hand artifacts to foreign runtimes; authoring-only IDEs.)

Jointly held: 1 without 2 = a code IDE with a run button; 2 without 1 = a component/workflow toolkit; 3 without 1+2 = generic hosting; 1+2 without 3 = an app *modeler* (BPM-studio-class), not an application platform; 1+3 without 2 = a custom-code app hosting platform (IDP/PaaS territory).

### L1 — Common Mature Structure (common in mature products, not definitional)

- Visual interface builders (canvas/form/page/report designers with widget/component libraries)
- A built-in data substrate (tables/entities/forms with relationships and per-field validation) — where present alongside external-data support
- External-data integration (connectors/resources; documented at scale: 200+ sources in one sample)
- Visual logic layer (flows, business rules, approval workflows, process stages) alongside declarative validation
- End-user clients: browser + mobile (responsive or wrapped/native), navigation, dashboards/reports
- Environments + publish (dev/test/prod separation; draft vs live app state)
- Roles/permissions both for makers and for end users; sharing/distribution machinery
- Admin console / governance surface (usage metrics, org management)
- Marketplace/template ecosystems; reusable modules/components
- AI-assisted app generation (2026 era-current)
- Multi-language/translation support (one sample; treat as common-not-universal)

### L2 — Variant / Optional Structure

- Authoring posture: UI-first canvas vs data-model-first generation (both poles are first-class authoring styles in the same product in one sample) — a philosophy axis, not two Types
- Studio form factor: desktop modeling client vs browser-only builder
- Deployment target: vendor cloud / customer cloud (K8s) / on-premises / database-embedded; runtime-only production installs
- Extension depth: none → scripting language → full pro-code (Java/JS/React/PLSQL)
- Audience center: citizen-dominant vs developer-dominant (market spans; products mix)
- External-facing surfaces: customer portals, public sites, embedded widgets, branded mobile apps
- Bundled platform siblings: workflow/automation products, AI agents, BI/analytics, integrations (iPaaS-class), RPA — cross-sell bundles, not the Type
- Licensing shape: per-user seats, per-app, capacity-based, self-hosted licensing (observed variety; details are L3)
- Monetization: publishing apps to vendor marketplaces

### L3 — Vendor-specific Structure (kept here, not in final doc)

- Power Apps: canvas vs model-driven duality; Dataverse; make.powerapps.com; Power Platform admin center; Plans; GCC government plans; Teams embedding; Dynamics 365 sharing Dataverse.
- Mendix: Studio Pro desktop client; microflows/nanoflows; domain-model access rules; branch lines/Team Server; deployment packages; Mendix Cloud/K8s/Azure/SAP BTP targets; Marketplace modules; Maia; Atlas UI; OQL; consistency-error checking; Model SDK/Metamodel.
- Retool: `{{ }}` embedded JS expressions; dependency graph; resources vs queries split; classic IDE vs new AI app builder; frames taxonomy; publish checklist with function approval; org spaces; self-hosted vs Retool-hosted; Workflows/Agents siblings; Retool Database.
- Zoho Creator: Deluge; Blueprints (stages/transitions/owners); approval centers auto-created for approvers; .ds export; solutions taxonomy (Application/Analytics/Flows); on-premises edition; branded mobile distribution with code-signing; Zoho Marketplace review process.
- Oracle APEX: metadata-in-database engine; workspace model; runtime vs full-dev install; SQL/PLSQL extension; engine services list (session state, authn/authz, page flow, validation).

## Rejected Findings (considered, then excluded from the core)

- **"Visual drag-and-drop" as definitional** — rejected: APEX is declarative without a drag-drop canvas as its center; model-driven generation exists; the invariant is configuration-first authoring, not any specific canvas interaction.
- **Built-in data platform as definitional** — rejected: Retool's documented center is external resources; Power Apps documents 200+ external sources beside Dataverse; the substrate choice is a variant axis.
- **"No writing code at all" as definitional** — rejected: every sampled product carries a documented code tier; Power Apps explicitly documents developers as app makers; the invariant is that code is *optional extension*, not the primary medium.
- **Cloud/SaaS delivery as definitional** — rejected: on-premises editions documented (Zoho, Mendix, APEX-class database-embedded, Retool self-hosted).
- **Internal-tools-only scope** — rejected: external portals/public-site surfaces documented (Power Pages in solution generation output; Zoho portals; APEX "database-centric web applications" unqualified).
- **AI app generation as definitional** — rejected: era machinery (2026); the Type predates it and all pre-AI generations satisfy L0.
- **Workflow/process engine as definitional** — rejected: process orchestration appears inside several products as an app component (Mendix workflows, Zoho Blueprints, Power Automate pairing), but the central artifact remains the application; process-first products (Appian-class) sit on the seam and are not sampled here.

## Historical / Market-Sample Check (§24)

Ask: would older, regional, platform-native products still fit the L0?

- **Oracle APEX** (in-sample, originates late-1990s as HTML DB): satisfies all three legs with a metadata-in-database engine, no cloud, no drag-drop canvas, no AI. Confirms the definition is not cloud-era-bound.
- **Lotus Notes/Domino, Microsoft Access, FileMaker** (conceptual, no direct source fetched this pass — assertion kept conceptual): forms-over-data packages of the 1990s held a data model + composed forms/views + rule/script logic + a platform-hosted runtime (Notes client/Domino, Access/Access-runtime, FileMaker engine), with code (formula/VBA/ScriptMaker) as extension. All three legs satisfied → the 4GL/RAD "forms-over-data" generation is the same Type's ancestry.
- **PowerBuilder-class 4GL RAD IDEs** (conceptual): code-medium-dominant (4GL language first, visual painters secondary) and compiled-executable delivery outside a platform runtime — fails leg 2 (and arguably 3). Recorded as pre-history/adjacent, not a member. This negative case sharpens leg 2: the medium, not the presence of visual tooling, is the invariant.
- Conclusion: L0 holds across eras if phrased as application-of-record + configuration-first medium + platform-operated runtime. Nothing in L0 names cloud, drag-drop, subscriptions, AI, browsers, or a built-in database.

## Boundary Findings

| Neighbor | Seam (what to remove / what remains) | Evidence |
|---|---|---|
| **No-code Application Builder** (§12 sibling leaf) | Candidate STRUCTURE-IDENTICAL L0: a no-code builder that composes data+UI+logic and runs the app satisfies all three legs. Working seam = center-of-gravity/audience posture: low-code centers full application lifecycle with an explicit pro-code extension tier and enterprise SDLC machinery; no-code centers non-programmer-only assembly with simpler depth. Gradient, not wall — market labels drift (Zoho: "low-code platform… no-code features"; Power Apps: "without writing code" while documenting a developer tier). | A-evidence on the low-code side; no-code side not fetched this pass → JOINT REVIEW FLAG |
| **BPM Platform** (§10, processed) | Prior pass's own seam confirmed from this side: BPM's central artifact is a governed versioned process model; LCAP's is the application. Process machinery appears *inside* LCAPs as app components (Mendix workflows; Zoho Blueprints; Power Automate pairing) — presence of workflow ≠ process-model-center. Appian-class process-first "low-code" products straddle the seam (recorded in BPM pass; not sampled here). | B + prior-pass cross-reference |
| **Workflow Management Platform** (§10, processed) | Same seam at lighter weight: routing recipes for recurring work vs composed applications with data model + UI. | prior-pass cross-reference |
| **Internal Developer Platform / Portal** (§12, processed) | IDP provisions runtime for code-first apps authored in external IDEs (no in-platform app composition; operator = platform team). LCAP composes and runs the app itself. IDP L0 legs 1–2 fail against LCAP. | prior-pass definitions |
| **Robotic Process Automation Platform** (§10, processed) | RPA operates existing applications' surfaces; LCAP builds new applications. Bundle overlap real (RPA embedded in LCAP suites). | prior-pass cross-reference |
| **Web Application Builder** (§04.16) | Website builders center a published content/presentation site for web audiences; LCAP centers a data+logic business application with governed user access. External web surfaces inside LCAPs (portals/sites) are variants. | A (limited — website-builder side not sampled this pass) |
| **Code-first development platforms** (§12: mobile/web/desktop frameworks, IDEs, MBaaS-class) | Frameworks: artifact = source code compiled/bundled for a foreign runtime; medium = code. LCAP: artifact = configured application model run by the platform. Same §12 family, opposite medium. | A (Retool "imported React code" shows the bridge but the platform remains the runtime) |
| **Structured Table / Lightweight Database Application** (§03.03, unprocessed sibling) | Data-table-first tools with views/forms; LCAP centers the full application (custom logic depth + dedicated UX + platform governance + lifecycle). Gradient acknowledged; data-first pole not sampled this pass → noted as uncertainty for that leaf's pass. | reasoning only |
| **Business Management Suite** (§07, processed) | Suite ships pre-built business apps on one data core; LCAP is the factory for composing applications. Embedded low-code builders inside suites are variant surfaces of this Type. | prior-pass cross-reference |
| **Personal workflow automation** (§03.16, processed) | Personal automation connects existing services with trigger→step recipes (no composed application, no app-of-record with its own data model/UI). | prior-pass definitions |

**Taxonomy issue recorded:** the low-code/no-code seam needs joint review when `no-code-application-builder` is processed; recommend structure-compatible L0 + center-of-gravity discrimination (workflow/BPM precedent), or alias consolidation if that pass's evidence shows the populations fully merge.

## Uncertainties

- Appian and OutSystems unreachable (403/406/empty ×2 each) — the process-first and enterprise-developer poles are anchored by market position only; no operational claims from them. The L0 was checked against their *known positioning* only conceptually.
- No no-code product fetched; the no-code seam recommendation is one-sided.
- Data-first tools (Airtable-class) unexamined — the §03.03 seam is reasoned, not evidenced.
- Numeric limits (source counts beyond documented ones, data capacities, user minima) deliberately not asserted.
- Power Apps deep mechanics (DLP policies, connector depth) not fetched beyond overview pages; governance claims kept generic.
- Historical samples (Notes/Access/FileMaker) kept conceptual — no primary source fetched; Zoho/Mendix "start from spreadsheet" flows (A-evidence) are the observed living trace of that ancestry.

## Final Synthesis (layer C)

A Low-code Application Platform is best modeled as **a factory and a runtime in one product for composed business applications**: the application of record (data model + interfaces + logic) is authored primarily by configuring the platform's own building blocks, the platform itself runs the published application for governed end users, and the maker iterates inside the same environment through versioned, environment-separated publication. The Type's identity lives in the triple (application-of-record, configuration-first medium, platform-operated runtime); everything else — canvases, connectors, marketplaces, AI generation, process engines, portals — is mature furniture arranged differently by each vendor. The defining triple is era-proof: it covers a 1990s forms-over-data package, a database-embedded declarative engine, a citizen-developer cloud suite, and a developer-first internal-tool shop alike.
