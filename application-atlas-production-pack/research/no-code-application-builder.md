# Research Notes — No-code Application Builder

Research date: 2026-09-09. Methodology: atlas-writer v1.1 (WORKFLOW/WRITING_GUIDE in update-v1/). Evidence layers: A = directly observed in fetched official documentation for a named product; B = cross-product commonality across the sample; C = canonical inference. L0/L1/L2/L3 per abstraction hierarchy.

**Carried obligation:** this pass discharges the joint-review flag hung by the low-code-application-platform pass (2026-09-08): "candidate STRUCTURE-IDENTICAL L0 … recommend joint review … either workflow/BPM-precedent keep-both-with-gradient or alias consolidation." Resolution recorded in §Boundary Findings below and in STATUS.md.

---

## Research Goal

Establish what a No-code Application Builder is as an Application Type: what the central artifact is, what the authoring medium is (and whether code is ever required), how the build→publish→run loop works, what the platform provides (data, users, hosting), and — the pass's special duty — whether the no-code population merges with, or stands beside, the Low-code Application Platform population documented on 2026-09-08.

## Initial Boundary (pre-research hypothesis)

- Core hypothesis: a platform on which a non-programmer assembles a working application (data + interface + logic) from platform-provided building blocks and runs it on the platform.
- Nearest neighbors to test: Low-code Application Platform (§12 sibling, processed 2026-09-08 — joint-review flag pending), Visual Website Builder / Web Application Builder / Landing Page Builder (§04.16), Online Form Builder (§03.11), Structured Table / Lightweight Database Application (§03.03, unprocessed), Personal Workflow Automation Platform (§03.16, processed), BPM Platform / Workflow Management Platform (§10, processed), Mobile App Development Platform (§12 sibling), Internal Developer Platform (§12, processed), RPA Platform (§10, processed).
- Known straddles going in: Softr-class portal builders lean website-ish; Airtable-class interfaces lean data-first; Glide's new GlideOS generation is prompt-first AI generation of the same artifact.

## Research Questions

1. What is the central managed artifact — an application? What is it composed of?
2. What is the authoring medium? Is code ever required on the primary build path?
3. Where does the finished application run, and who operates that runtime?
4. What does the build → publish → use → iterate loop look like?
5. What data substrate do builders provide — built-in database, external sources, or both?
6. Who builds (audience), and what happens when a maker hits the platform's limits?
7. What end-user machinery exists (accounts, permissions, distribution surfaces)?
8. What lifecycle machinery exists (preview vs live, versioning, collaboration)?
9. Which capabilities are definitional vs common vs variant vs vendor-specific?
10. JOINT REVIEW: does the no-code population satisfy the low-code L0 triple (application of record + configuration-first medium + platform-operated runtime)? If yes, is the seam center-of-gravity (keep-both) or full merge (alias)?

## Representative Products

Selection rationale: market representativeness + documentation completeness + different product philosophies + different customer tiers. The low-code pass sampled the low-code population (Power Apps, Mendix, Retool, Zoho Creator, Oracle APEX); this pass samples the no-code population across its own philosophical spread.

| Product | Philosophy / pole | Tier reached | Access notes |
|---|---|---|---|
| Bubble | full-stack no-code pole; visual programming depth (database + workflows + expressions); entrepreneur/MVP through enterprise | Tier-1 (manual.bubble.io, multiple pages incl. workflows article) | fully reachable |
| Glide (glideapps.com) | data-first pole; spreadsheet-like data editor + automatic design system; operations teams; now split Glide Classic / GlideOS (AI generation) | Tier-1 (glideapps.com classic platform + data-sources + GlideOS docs pages) | fully reachable (docs root 404 ×2; reached via site pages) |
| Softr | blocks/portal pole; assemble apps from pre-built blocks over external data sources; non-technical portal builders | Tier-1 (docs.softr.io core concepts + building blocks + publishing) | fully reachable |
| Google AppSheet | declarative/ecosystem pole (Google Workspace; app generation from data) | — | support.google.com/appsheet timed out ×2, help.appsheet.com timed out ×2 — abandoned per network rule; **no claims from AppSheet**; market anchor only |

## Sources

- Bubble: https://manual.bubble.io/ ; https://manual.bubble.io/help-guides/getting-started.md ; https://manual.bubble.io/help-guides/logic/workflows.md (fetched 2026-09-09)
- Glide: https://www.glideapps.com/ ; https://www.glideapps.com/classic/platform ; https://www.glideapps.com/classic/data-sources ; https://www.glideapps.com/docs/os/what-is-glide-os (fetched 2026-09-09)
- Softr: https://docs.softr.io/ ; https://docs.softr.io/core-concepts-overview ; https://docs.softr.io/core-concepts-overview/visualize-data-with-building-blocks ; https://docs.softr.io/core-concepts-overview/publish-your-application (fetched 2026-09-09)
- Market anchor (not fetched, no claims): Google AppSheet. Also noted as adjacent anchors: Adalo, FlutterFlow, Airtable (not sampled).

---

## Product Observations (evidence layer A unless noted)

### Bubble

- Self-positioning: "Bubble lets you turn your ideas into fully functional, scalable apps by combining the power of AI and visual development … no coding required." "One platform, limitless possibilities … With a shared database, workflows, and infrastructure, Bubble supports creating seamless experiences across web, iOS, and Android, all from a single, unified editor."
- **AI generation entry**: "Bubble's advanced AI Agent empowers you to create a fully functional app using simple prompts … This initial app will be fully functional with a built-in database and workflows."
- **The editor is the whole product**: "Bubble contains all the tools you need to create awesome web applications, all wrapped into one editor."
- **Data**: "The database manages all the dynamic data … You can create, modify, view, and delete data as needed and run bulk operations … Data in the database is stored securely on Bubble's servers." Database editor: "create, assign fields to and connect data types with no database experience." Also static data (redeploy to update), temporary data (page-scope variables), built-in user accounts ("your users can create and log in to their account purely with built-in tools"), file uploads.
- **Design**: elements dragged onto pages; styles, color/font variables; responsive engine (grid-based); component library of pre-built UI components; Figma import.
- **Logic**: "A *workflow* is the combination of an *event* that triggers one or more *actions*." Events: button click, input change, condition true, login/logout, database changes; page-side or server-side. Actions: create/update/delete database things, show/hide/animate elements, account operations, send emails, navigate, load data, plugin actions (payments). Dynamic expressions: "like 'live' formulas that update in real-time based on user input, database updates and other changes." Conditions: element-level if/then behavior. Workflow canvas: event at top, sequential actions beneath; folders/colors; workflow-level conditions.
- **Error behavior (precise, product-specific)**: "If a workflow runs into an error, it will stop running on the action where the error happened. Any previous actions will not be reverted." Error-catching events (element-level, page-level unhandled). Timeouts documented with workload guidance (bulk list operations efficient "up to 1,000 records", backend operations recommended near 10,000).
- **Maintenance/lifecycle**: collaborators (up to 40 per project); **version control with branches** ("independent iterations of your app (called *branches*) … from development to testing to deployment"); commenting; database maintenance (backups, bulk operations); testing/debugging "isolated from the live version"; API workflow scheduler (view/pause/cancel scheduled workflows).
- **Integrations**: API Connector (outgoing calls), plugin store ("thousands of plugins that extend the platform's core feature set"), SQL Database Connector (Postgres/MySQL/MSSQL), Bubble App Connector.
- **Infrastructure**: "Bubble is not only a no-code platform, but a complete hosting solution that automatically scales as needed." Custom domain (bubbleapps.io subdomain → own domain). Sub-apps (main app pushes changes to sub-apps, each with own database — SaaS pattern). Release tiers. Compliance (SOC 2 Type II, DDoS protection).
- **Enterprise**: "centralized management for both users and apps, a dedicated support team, and the flexibility to choose their hosting location"; invoicing/ACH payment options.

### Glide (glideapps.com)

- Self-positioning (Classic): "The no code platform for intelligent apps. Glide empowers operations teams to create modern, AI-powered apps that increase efficiency—without coding." FAQ: "No code app development allows non-technical users to create custom apps without writing code. Glide makes this possible through its intuitive platform that combines a powerful data editor and layout designer."
- **Data-first development**: "Build powerful apps with a familiar spreadsheet-like interface. Connect data wherever it lives—from spreadsheets to databases—or start from scratch." Data Editor "organizes your data using advanced logic and an intuitive spreadsheet interface to empower anyone to easily edit and customize apps without writing a single line of code or formula."
- **Data sources**: external-first menu — Google Sheets ("sheet tabs become tabs in your app. Changes sync in minutes"), Excel (Office 365 sync), Airtable, BigQuery, SQL Server, MySQL, PostgreSQL, Google Cloud SQL; "Bring your own data. Keep it that way … No migration, no lock-in – just connect & sync." Built-in options: Glide Tables ("Create a Table from scratch or import existing data from a CSV or XLSX"), Glide Big Tables ("enterprise scale database hosted directly in Glide … millions of rows"). "Whenever your data changes in Glide, it instantly syncs directly back to your data source."
- **Data-level power without code**: "Create relationships, perform calculations, look up values across other tables, create messages, generate QR codes, call APIs, and more – without writing code or formulas." Computed columns, custom actions, data security named as the three advanced layers.
- **Design**: "Automatic Design System. Your apps automatically have a polished look and feel for mobile and desktop, thanks to professionally designed themes, layouts, and components." Mobile-adaptive by default.
- **Workflows**: "Build complex automations without code … with triggers, conditions, loops, and AI steps … monitoring performance in real time."
- **Glide AI**: managed models for text/extraction/transcription; AI custom components via chat.
- **GlideOS (new generation, separate product line)**: "an operating system for your business, with an AI agent that works alongside you. Describe a process … and GlideOS builds what that work needs: apps for your team and the data behind them, together in one place." Structure: Home / **Projects** ("Every app lives inside a project: one or more apps plus the chats, data, files, and secrets they share") / **Apps** / **Data** ("Data tables that a project's apps read and write. Connect Google Sheets, upload Microsoft Excel or CSV files, or let GlideOS create tables from what you describe") / **Workflows** ("Routines GlideOS runs for you on a schedule, from a webhook, or on demand, using the same data as your apps") / Integrations (1,000+ directory).
- **Enterprise posture**: SSO, advanced permissions and roles, SOC 2 Type 2, FedRAMP/ISO 27001/PCI/GDPR claims on the security page; 400+ templates; Glide University; certified Experts marketplace.

### Softr

- Self-positioning: "build secure, production-ready business software with Softr—the first AI-native platform where you can generate complete, connected apps from a single prompt."
- **Core concepts (the documented object set)**: Pages and Navigation; Create a Database (Softr Databases = built-in substrate); Connect your data source (14 data-source articles — Airtable, HubSpot, SQL, Google Sheets class); Visualize data with building blocks; Actions ("Adding and editing data … Let your users modify your data"); User Authentication; User groups & permissions ("Define what users can see and edit on the application"); Style your app; Publish your application.
- **Blocks**: "pre-built components that enable you to visualize and interact with data … the foundation for designing and customizing your app." Three families: **dynamic blocks** (list, table, calendar — pull from data sources, real-time), **static blocks** (hero, FAQ, CTA — same content for all users), **container blocks** (tabs, columns). Per-block configuration: data source (+ conditional filters, sort), content mapping, actions, style, **visibility** (user groups + device type).
- **AI Co-Builder**: "Open the AI Co-Builder chat in the editor and describe what you need … The AI will instantly generate and configure the appropriate block on your page."
- **Publishing**: "Until you publish your Softr application, it remains private and inaccessible to others." Preview tools: live preview, **user-role simulation**, device testing, shareable preview link. Default randomized subdomain → customizable subdomain → custom domain. "After publishing, any subsequent changes to your app … will require re-publishing to update the live version." PWA publishing (plan-gated). SEO tooling for public-facing apps.
- **Extension**: Custom Code section (JS/CSS; 3 articles — escape-hatch scale, not a tier); Softr API; 28 integration articles.
- **Users**: user authentication as a core concept; user groups & permissions with conditional filters per block.

### Google AppSheet (anchor only — no claims)

Unreachable this pass (support.google.com/appsheet timeout ×2; help.appsheet.com timeout ×2). Held as a market anchor for the declarative/data-generated pole inside a productivity-ecosystem vendor. No operational claims made.

---

## Cross-product Comparison

| Dimension | Bubble | Glide (Classic) | Softr |
|---|---|---|---|
| Central artifact | app (pages + database + workflows) inside a Bubble account | app (data + layouts + workflows) inside a Glide project/team | app (pages + blocks + data + users) inside a Softr workspace |
| Data substrate | built-in database (data types + fields) primary; SQL connector + API Connector for external | external-first (Sheets/Excel/Airtable/SQL/BigQuery) + built-in Glide Tables/Big Tables | external sources (Airtable/SQL/HubSpot/Sheets class) + built-in Softr Databases |
| Interface authoring | drag-drop elements on pages; styles/variables; responsive engine; component library; Figma import | layout designer over professionally designed themes; automatic design system; mobile-adaptive | pre-built blocks (dynamic/static/container) arranged on pages; per-block config |
| Logic authoring | workflows (event → action sequence), dynamic expressions, conditions; server-side workflows | workflows with triggers/conditions/loops/AI steps; computed columns/rollups in data layer | per-block actions (add/edit data); workflows section (automate tasks) |
| Code's role | none on primary path; plugins + API Connector as extension; no general code tier documented | none documented ("without writing a single line of code or formula") | Custom Code (JS/CSS) as escape hatch; Softr API |
| Who runs the app | Bubble hosting ("complete hosting solution"); custom domain; sub-apps | Glide-hosted apps; mobile-adaptive web | Softr publishing (subdomain → custom domain); PWA |
| Publish loop | preview/test isolated from live version; version control with branches | real-time preview; publish/share with access control | private until published; re-publish on change; role-simulation preview |
| End-user machinery | built-in user accounts (signup/login) | roles, row-level security posture, SSO (enterprise) | user authentication + user groups & permissions + conditional visibility |
| AI-era generation | AI Agent generates app structure (database + workflows) | GlideOS: prompt/spreadsheet → apps + data + workflows in projects | AI Co-Builder generates blocks from chat |
| Ecosystem | plugin store, templates, enterprise plan | templates (400+), University, certified Experts | integrations directory, affiliate program |
| Audience center | entrepreneurs → enterprise ("any type of app … MVPs to enterprise-grade") | operations teams, non-technical builders | non-technical portal/business-software builders |

### Cross-product commonalities (layer B)

1. **The composed application is the named, persistent central artifact in all three** — bundling data substrate + user-facing interfaces + executable logic, managed as one unit (created, edited, published, shared).
2. **Assembly from the platform's own building blocks is the primary medium in all three** — and all three explicitly advertise that the primary path requires no programming ("no coding required" / "without writing a single line of code or formula" / "generate complete, connected apps from a single prompt").
3. **The platform runs the finished app in all three** — publish → live on the vendor's operated runtime (Bubble hosting, Glide-hosted apps, Softr publishing); end-user access granted at platform level (accounts/groups/roles).
4. **Both data-substrate poles are mature**: built-in database (Bubble primary; Glide Tables; Softr Databases) AND external-source connection (Glide external-first; Softr 14 source articles; Bubble SQL/API connectors).
5. **End-user accounts + permission groups are first-class core concepts in all three** — more prominent in no-code documentation than in the low-code sample's docs (where maker-side governance dominated).
6. **Preview → publish → re-publish loop in all three**, with draft/live separation (Bubble preview-vs-live + branches; Softr re-publish rule; Glide publish/share).
7. **AI-assisted generation is the era-current entry path in all three** (Bubble AI Agent, GlideOS agent, Softr AI Co-Builder) — accelerant, not a separate Type.
8. **Templates/marketplace/expert ecosystems in all three.**

### Population-level differences vs the low-code sample (layer B, cross-pass)

1. **Pro-code extension tier**: documented as first-class in 5/5 low-code sample (Power Apps developers, Mendix Java/JS actions, Retool React/JS, Zoho Deluge, APEX PL/SQL). In the no-code sample: absent (Glide), plugin-mediated (Bubble — makers configure pre-built plugins; no general code tier documented), escape-hatch (Softr custom code, 3 doc articles). **Not a universal no-code structure.**
2. **Deployment-target breadth**: no-code sample runs on the vendor's operated cloud (3/3; caveat: Bubble Enterprise documents "flexibility to choose their hosting location" — detail not fetched). Low-code sample documents multi-target (Mendix Cloud/K8s/Azure/SAP BTP/on-prem; Zoho on-premises edition; Retool self-hosted; APEX database-embedded).
3. **Audience posture**: no-code products design and market for non-programmers as the primary maker; low-code products document mixed maker populations with explicit developer roles.
4. **CORRECTION to the low-code pass's proposed gradient**: "shallower SDLC depth" is NOT a reliable discriminator — Bubble (no-code) documents version control with branches, collaborators, preview-vs-live testing, database backups, sub-apps, and an enterprise tier with centralized management. Lifecycle machinery exists on both sides of the seam; its depth is a product-maturity variable, not a population boundary.

---

## Canonical Model (L0 → L3)

### L0 — Defining Invariant (minimal)

A **No-code Application Builder** is a platform whose:

1. **Central artifact is the composed application** — a persistent, individually identified application bundling a data substrate (tables with typed fields), user-facing interface(s), and executable logic, managed as one unit. (Remove → website builder [content site], form builder [single instrument], automation platform [recipes over existing services], structured-table tool [data-first], component library.)
2. **Primary authoring medium is assembly from the platform's own building blocks, usable without programming** — the maker composes from platform primitives (data tables, interface components, logic steps); code is absent, an optional escape hatch, or packaged inside pre-built extensions — never the required primary path. (Remove → code-first frameworks/IDEs/development platforms; also separates from low-code's tolerance of a first-class code tier.)
3. **The platform itself runs the finished application** — publish/deploy through the platform's own machinery; end users run the app on the platform-operated runtime with access granted at platform level. (Remove → authoring-only modelers/generators; frameworks handing artifacts to foreign runtimes.)

Jointly held: 1 without 2 = a code IDE with a run button / custom-code hosting; 2 without 1 = a component/block toolkit or form builder; 3 without 1+2 = generic hosting; 1+2 without 3 = an app modeler (BPM-studio-class); 1+3 without 2 = PaaS/IDP territory.

**Structure-compatibility note (joint review):** these three legs are the same triple the low-code pass documented. The populations are structure-compatible; the discrimination is center-of-gravity, recorded below.

### L1 — Common Mature Structure

- Visual page/layout editor with component/block libraries and styling systems
- Built-in data substrate (tables with typed fields, relationships) — where present alongside external-data support
- External-data connections (spreadsheets, SQL databases, SaaS sources; sync-back behavior documented in one sample)
- Event→action logic layer with expressions/formulas and conditions
- End-user accounts + permission groups/roles for the app's users (visibility and edit control per page/block/record class)
- Preview/test vs live publish loop; custom domains; re-publish discipline
- Templates, plugin/integration ecosystems, expert/marketplace programs
- AI-assisted generation (2026 era-current: app-level, block-level, or project-level)
- Mobile delivery: responsive web standard; PWA and native mobile as variant surfaces

### L2 — Variant / Optional Structure

- Data-substrate posture: built-in-DB-first vs external-data-first (both poles first-class in-sample)
- App surface: web app / PWA / mobile-adaptive / native mobile (one sample documents native iOS/Android)
- Audience center: entrepreneurs/MVP builders, operations teams, portal builders, enterprise IT
- Generation posture: manual visual assembly vs prompt-first AI generation vs hybrid (one vendor now runs both generations as separate product lines)
- Logic depth: full visual programming (workflows + expressions + server-side) vs lighter per-block configuration
- Lifecycle depth: single-stream publish vs branches/version control (product-maturity variable, NOT a population boundary — see correction above)
- External-facing surfaces: public pages/SEO tooling, client portals, sub-app/multi-tenant patterns

### L3 — Vendor-specific Structure (kept here, not in final doc)

- Bubble: workflow canvas mechanics (event top, sequential actions, folders/colors); dynamic expressions; static vs temporary data; error semantics (stop-at-failing-action, no auto-revert); timeout/workload guidance with numeric thresholds; 40-collaborator limit; sub-apps; release tiers; SQL connector database list; Figma import; enterprise hosting-location choice.
- Glide: Glide Classic vs GlideOS product split; spreadsheet-like Data Editor; sync-back to source; Glide Tables vs Big Tables; computed columns/custom actions; automatic design system; Glide AI managed models; Projects container (apps + chats + data + files + secrets); 1,000+ integrations directory; certified Experts.
- Softr: block taxonomy (dynamic/static/container); per-block visibility (user groups × device); AI Co-Builder; role-simulation preview; re-publish rule; PWA plan gating; Custom Code escape hatch; Softr API.

## Rejected Findings (considered, then excluded from the core)

- **"Drag-and-drop" as definitional** — rejected: assembly happens through multiple interaction styles (block libraries, chat-driven AI generation, form/config panels); the invariant is configuration-first assembly, not a specific gesture.
- **"No code anywhere" as definitional** — rejected: Softr documents custom code; Bubble's plugins encapsulate code; the invariant is that code is never required on the primary build path.
- **Built-in database as definitional** — rejected: Glide's documented center is external sources ("no migration, no lock-in"); Softr leads with external sources beside its built-in DB; substrate choice is a variant axis.
- **Spreadsheet-as-source as definitional** — rejected: it is one implementation of the external-data pole (and one vendor's marketing signature), not the Type's structure.
- **AI generation as definitional** — rejected: era machinery (2026); all three products' pre-AI generations satisfy the L0.
- **Mobile-first as definitional** — rejected: web-first, mobile-adaptive, PWA, and native-mobile surfaces all in-sample.
- **"Shallow depth / simple apps only" as definitional** — rejected: one sampled product documents enterprise-grade claims, version control, sub-apps, and compliance posture; depth is a maturity variable.
- **Website-builder scope** — rejected: the sampled products' centers are data+logic+users applications; static content blocks exist (Softr) as furniture, not the center.

## Historical / Market-Sample Check (§24)

Ask: would older, regional, platform-native products still fit the L0?

- **HyperCard (1987, conceptual — no primary source fetched this pass)**: stacks of cards with fields/buttons, optional HyperTalk scripting, running inside the HyperCard runtime; non-programmers built functional applications. Satisfies the triple conceptually (composed stack-as-application, assembly from primitives, platform runtime). Kept conceptual per source limits.
- **FileMaker / Microsoft Access / Lotus Notes (conceptual)**: the low-code pass already claimed this forms-over-data generation as its ancestry; the same packages served non-programmers building data+form+script applications on a bundled runtime. The shared ancestry is itself evidence that the no-code and low-code populations are two market segments of one structural family — supporting keep-both-with-gradient over two unrelated Types.
- **The "no-code" label is 2010s market vocabulary.** The definition deliberately names no label-era machinery: no drag-and-drop, no AI, no cloud, no templates, no subscription pricing, no mobile-first posture.
- Conclusion: L0 holds across eras when phrased as composed-application + no-programming-required assembly + platform-operated runtime.

## Boundary Findings

| Neighbor | Seam (what to remove / what remains) | Evidence |
|---|---|---|
| **Low-code Application Platform** (§12 sibling, processed 2026-09-08) — **JOINT REVIEW RESOLVED** | Populations are STRUCTURE-COMPATIBLE: the no-code sample satisfies all three low-code L0 legs. **Resolution: keep-both with center-of-gravity seam (workflow/BPM precedent), NOT alias consolidation.** The seam rests on three observable population-level differences: (i) audience posture — no-code designs for non-programmers as the primary maker; low-code documents mixed citizen+pro maker populations; (ii) pro-code extension tier — first-class in 5/5 low-code sample; absent/plugin-mediated/escape-hatch in the no-code sample; (iii) deployment-target breadth — vendor-cloud runtime in 3/3 no-code sample; multi-target (customer infra/self-host/database-embedded) documented in the low-code sample. **Correction recorded:** the low-code pass's proposed "shallower SDLC depth" discriminator is NOT supported — Bubble documents branches/version control/collaborators/enterprise governance; lifecycle depth is a maturity variable on both sides. Label drift confirmed from this side (Glide's own FAQ defines no-code by "non-technical users … without writing code" while shipping API access; Softr ships custom code) — labels cannot isolate the populations; the structural gradient can. | A (3 no-code products fetched) + cross-pass comparison with the low-code pass's A-evidence |
| **Visual Website Builder / Web Application Builder** (§04.16) | Website builders center a published content/presentation site for web audiences; no-code builders center a data+logic application with user accounts and record-level permissions. Softr straddles mildly (static blocks, SEO tooling) but its core-concept set is data blocks + authentication + permissions — app-shaped. Remove data+logic+users → website builder. | A (Softr static blocks + SEO docs) + prior-pass definitions |
| **Online Form Builder** (§03.11) | Form builders center the question instrument + collected responses; no-code builders include form/input components but center the multi-page application over a data model with logic and users. | A (input elements/actions as components, not the center) |
| **Structured Table / Lightweight Database Application** (§03.03, unprocessed) | Data-first tools center the table with views; no-code builders center the composed app; spreadsheet-like data editors are common furniture (Glide's Data Editor). Airtable-class unexamined — reasoned seam, flagged for that leaf's pass. | reasoning + A (Glide data editor as furniture) |
| **Personal Workflow Automation Platform** (§03.16, processed) | Automation platforms connect existing services with trigger→step recipes; no-code workflows are logic inside a composed new application with its own data. | prior-pass definitions + A |
| **BPM Platform / Workflow Management Platform** (§10, processed) | Process model vs composed application — prior pass's seam confirmed from this side; workflow engines appear inside no-code apps as logic components. | prior-pass cross-reference |
| **Mobile App Development Platform** (§12 sibling) | Code/frameworks producing store-distributed binaries vs platform-hosted applications; native mobile inside a no-code builder (Bubble documents iOS/Android from the same editor) is a variant surface. | A (Bubble mobile docs) |
| **Internal Developer Platform / Portal** (§12, processed) | IDP provisions runtime for code-first apps authored in external IDEs; no in-platform composition of the app itself. | prior-pass definitions |
| **RPA Platform** (§10, processed) | RPA operates existing applications' surfaces; no-code builders compose new applications. | prior-pass cross-reference |

**Taxonomy issue resolution:** the low-code/no-code joint-review flag is DISCHARGED — keep-both ratified with the center-of-gravity seam documented in both directions; the "shallower depth" gradient component is corrected in STATUS.md.

## Uncertainties

- Google AppSheet unreachable (timeouts ×2 on both support domains) — the declarative/ecosystem pole is market-anchor only; no operational claims.
- Bubble Enterprise "flexibility to choose their hosting location" noted but not detailed — the deployment-breadth claim is kept moderate (vendor-cloud runtime is the documented norm in-sample).
- Airtable-class structured-table tools unexamined — the §03.03 seam is reasoned, not evidenced.
- Mobile-first no-code products (Adalo-class) and code-generating visual builders (FlutterFlow-class) not sampled — the native-mobile and code-export variant axes are anchored by single-product evidence only.
- Numeric limits (collaborator counts, row thresholds, plan gates) observed in vendor docs are recorded here and deliberately excluded from the final document.
- Glide's docs root 404'd twice; evidence came from site pages and the GlideOS docs entry page — Classic deep mechanics (workflow editor internals) not fetched.

## Final Synthesis (layer C)

A No-code Application Builder is best modeled as **a non-programmer's application factory-and-runtime in one product**: the composed application (data + interfaces + logic) is the unit of record; assembly from the platform's own building blocks is the primary medium and is guaranteed to require no programming; and the platform itself runs the published application for end users whose access is managed at platform level. The Type shares its structural skeleton with the Low-code Application Platform — they are two market segments of one application-factory family — and is discriminated by center of gravity: who the maker is assumed to be, whether a pro-code tier is first-class, and how many deployment targets the runtime spans. Everything else — canvases, blocks, spreadsheets-as-database, templates, AI generation, PWAs, marketplaces — is mature furniture arranged differently by each vendor.
