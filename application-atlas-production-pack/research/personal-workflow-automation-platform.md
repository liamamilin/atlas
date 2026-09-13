# Research Notes — Personal Workflow Automation Platform

## Research Goal

Understand what a **Personal Workflow Automation Platform** is as an Application Type: what the user builds in it, what the automations act on, where they execute, what the connector catalog contributes, how the lifecycle runs (build → test → activate → run → history → maintain), and — critically for this directory node — how the Type is separated from its two §03.16 siblings (No-code Personal Automation Application and Desktop Automation Application, both processed) and from the surrounding automation family (RPA, workflow-management/BPM, data integration, marketing automation, agent platforms, app builders).

Two pre-hung flags must be handled this pass (see STATUS Boundary Issues):

1. The no-code-personal-automation pass recorded the working seam (device-hub vs vendor-cloud connector orchestration) and left the joint review open until this leaf was processed; it also recorded: "if the platform-sibling pass samples IFTTT, revisit the seam."
2. The desktop-automation pass recorded the artifact-level test ("what does the artifact act on, and where does it execute") with the second half of the flag open for this leaf.

This pass samples the cloud/connector pole directly and discharges both flags from this side.

## Initial Boundary Hypotheses (pre-research)

1. The §03.16 family splits by **automation hub**: the person's own device (No-code Personal Automation), the local desktop (Desktop Automation), and **connected external services orchestrated from a hosted runtime (this leaf)**.
2. "Platform" is load-bearing: the product is a hosted service whose value is the **connector catalog** plus always-on execution, not an installed app.
3. "Personal" means the unit of ownership is the individual's own account and own tasks — with team/organizational usage as a common extension in commercial products (the consumer pole must still satisfy the definition).
4. Alias-risk with no-code-personal-automation-application must be honestly evaluated: if the two leaves are the same Type, say so; if they are two poles of one family with distinct markets, record the seam and keep both.

## Research Questions

1. What is the unit the user builds (Zap / Applet / Scenario / Workflow)? What are its parts?
2. What triggers a workflow — external service events, schedules, incoming webhooks, manual runs?
3. What do the actions act on, and how are external services connected (connector catalog, linked accounts/credentials)?
4. Where does execution happen — vendor cloud, self-hosted server, user device? What run machinery exists (history, statuses, replay, metering)?
5. What does the authoring model look like (no-code visual; testing; drafts vs published; escape hatches)?
6. Is there an organizational layer, and is it definitional or an extension?
7. What is the workflow lifecycle end to end?
8. Where are the boundaries: no-code personal automation (device hub), desktop automation, RPA, workflow-management/BPM, data integration/ETL, marketing automation, agent platforms, no-code app builders?
9. Historical check: would older/regional products fit the definition, or is it overfit to the current SaaS/AI packaging?

## Representative Products

| Product | Pole | Access this pass |
|---|---|---|
| IFTTT | consumer connection pole (simple service-to-service applets) | Developer/Platform docs fetched; consumer help center **unreachable** (timeout, also in sibling pass) |
| Zapier | mainstream commercial pole (connector catalog at scale) | Help Center root, Zap-workflows category, "What is a Zap?" article fetched |
| Make (formerly Integromat) | visual depth pole (branching scenarios, operation metering) | Help Center structure + "Learn the basics" fetched; deeper mechanics not fetched |
| n8n | open-source / self-hostable pole (developer-flavored) | Docs root + full docs index (llms.txt) fetched |
| Microsoft Power Automate | organizational pole (boundary sample) | "What is Power Automate?" / flow types fetched |

IFTTT, Zapier, Make, and n8n are the Type-core samples; Power Automate is sampled primarily as boundary evidence (organizational identity; same vendor ships cloud flows and desktop flows as two artifact types, corroborating the sibling seam).

## Sources

Fetched 2026-09-08 unless noted:

- IFTTT — Platform documentation, "Get started" (services, applets, triggers/queries/actions, review process) — https://platform.ifttt.com/docs — fetched. Consumer help center https://help.ifttt.com/hc/en-us — timeout (this pass and sibling pass); https://ifttt.com/explore/what_is_ifttt — 404 (sibling pass). Abandoned per retry rule.
- Zapier — Help Center root — https://help.zapier.com/hc/en-us ; Zap workflows category — https://help.zapier.com/hc/en-us/categories/14013973271565-Zap-workflows ; "What is a Zap?" — https://help.zapier.com/hc/en-us/articles/8496309697421-What-is-a-Zap — all fetched.
- Make — Help Center root — https://help.make.com ; "Learn the basics" — https://help.make.com/learn-the-basics — fetched.
- n8n — Docs root — https://docs.n8n.io/ ; full documentation index — https://docs.n8n.io/llms.txt — fetched.
- Microsoft — "What is Power Automate?" (flow types) — https://learn.microsoft.com/en-us/power-automate/flow-types — fetched.
- Historical sample (Yahoo Pipes / mashup era) — https://en.wikipedia.org/wiki/Yahoo!_Pipes and https://en.wikipedia.org/wiki/Yahoo_Pipes — **timeout ×2, abandoned**; earlier passes also recorded Wikipedia/Wayback timeouts.

Evidence layers: **A** = directly observed on fetched official pages (all per-product observations below); **B** = cross-product commonality; **C** = canonical inference.

## Product A — IFTTT (consumer connection pole)

### Key observations (evidence layer A, developer/platform docs)

- **Services** are "the basic building blocks of IFTTT" — third-party products (examples: Amazon Alexa, Twitter, Dropbox, Fitbit, ecobee) each with a dedicated service page.
- **Applet**: "An Applet is an automation workflow that connects two or more services together and allows users to do something that those services couldn't do on their own."
- "Applets are composed of **triggers, queries, and actions**. Triggers tell an Applet to start, queries provide additional conditions, and actions are the result of an Applet run. Applets can be published by a service admin or users themselves."
- Direction of integration: "Your triggers will be sending data to IFTTT when something happens with your product"; queries are "a way for IFTTT to request additional data"; "Your actions will collect instructions that IFTTT sends you to do something with your product." IFTTT sits **between** the services as the broker of events and instructions.
- Example applets: "Get a daily email with the weather report"; "Get a notification when the ISS passes over your house but only if it is clear skies and after dark" (schedule, location, and condition machinery visible in official examples).
- Platform machinery: services require IFTTT review before publishing; "Works with IFTTT" program; Connect API for embedding; IFTTT MCP listed in navigation; Pro subscription tier exists ("Try IFTTT Pro"); consumer surfaces include Explore/Applets/Services catalog and mobile apps.
- Consumer-side operational details (applet limits, Pro feature set) are NOT in the fetched docs — no claims made.

## Product B — Zapier (mainstream commercial pole)

### Key observations (evidence layer A)

- Definition: "A Zap is a workflow that connects your apps to automate repetitive tasks. It consists of a **trigger**, which starts the Zap, and one or more **actions**, which are the events that the Zap performs after it's triggered."
- Watching machinery: "Zapier watches for this event and runs the Zap each time it occurs." Trigger article taxonomy distinguishes **polling vs instant** triggers.
- Data flow: each step has fields; values may be static or dynamic by "**mapping fields from a previous step**… each Zap run uses the actual data from that event."
- Lifecycle: "**Build** → **Test** → **Publish**": test each step with sample/test records; "publish your Zap to turn it on. Your Zap will only process new data created after it's published."
- Positioning: "automate your repetitive tasks without code"; "any of the **9,000+ apps** on Zapier" (another help page says "over 8,000 apps… from Airtable to Zendesk" — catalog scale numbers differ per page; treat as thousands-scale).
- Surrounding machinery (help-center structure): Zap history (view/manage/export, run statuses, **replay** of runs), Zap **drafts and versions**, notes, **flood protection** limits, custom **error handling**, Zap limits, guided **templates**, share/import/export "in your Team or Enterprise account", **Enterprise** publishing restrictions.
- Connector-plus surfaces: Tables ("no-code data storage"), Forms, Canvas (diagramming), Lead Router; **Zapier AI** (AI-generated Zap workflows, chatbots, agents, MCP); **Custom logic** (code steps, direct API calls, webhooks).
- Org layer: Team/Enterprise accounts documented; individual usage is the base posture ("manage incoming sales leads… notify your sales team" example is small-team scale; consumer-style personal usage is the product's origin posture per its own help framing "your apps").

## Product C — Make (visual depth pole)

### Key observations (evidence layer A, help-center structure + basics page)

- Positioning: "With Make, you can connect your favorite apps and create custom automations that work for you — all **without writing a single line of code**."
- Unit and parts (directly evidenced by documentation structure): **Scenarios** ("Create your first scenario", "Scenarios & connections"), built from **apps & modules**, configured through **data & mapping**, executed and metered via **credits & operations**, with **functions**, **tools**, and **data stores** available.
- **Connections**: a first-class concept — per-app linked accounts ("Scenarios & connections").
- **Error handling** is first-class: "Error handlers", "**Exponential backoff**", "Throw", "Common errors and warnings and their fixes" — retry/resume machinery documented.
- Org layer: "**Organizations & teams**", "**Subscription**", "**Administration**", "**Access management**", "Make Managed Services" — team/enterprise machinery documented.
- AI-era: "Make AI Agent (New)" docs, "Maia by Make" assistant, "Make MCP server", "Make Grid" — AI and extension surfaces documented as part of the current product.
- Catalog: apps.make.com with popular apps (Google Sheets, Gmail, OpenAI, Anthropic Claude, Airtable, Notion, HubSpot CRM, Canva…).
- Deeper scenario mechanics (canvas editing details, iterators/aggregators) not fetched this pass — kept generic; no claims beyond structure.

## Product D — n8n (open-source / self-hostable pole)

### Key observations (evidence layer A, docs root + full docs index)

- Definition: "n8n is a fair-code licensed **workflow automation tool** that combines AI features with business process automation."
- **Hosting split is explicit**: "Choose between **n8n Cloud and self-hosting**" — the runtime can be the vendor's cloud or the user's own server instance (Docker/npm/cloud-provider install guides; self-hosted configuration: executions, scheduler, queue mode, SSO, user management, database, license editions Community→Enterprise). The execution locus is a **hosted server runtime**, not the user's personal device, in both cases.
- Workflow model: **nodes** ("A node is an entry point for retrieving data, a function to process data, or an exit for sending data") joined by **connections** ("A connection establishes a link between nodes to route data through the workflow"); **trigger nodes** (app triggers, Email Trigger (IMAP), Chat Trigger, Activation Trigger, Error Trigger); scheduled runs via a "durable scheduler [that] runs time-based workflows from a database-backed queue"; **webhook** endpoints.
- **Executions**: "An execution is a single run of a workflow"; manual, partial, and automatic execution types; execution history, debugging by copying execution data, filtering; execution-data redaction for compliance.
- Lifecycle: "Save, **publish**, **unpublish**, and name workflow **versions**"; workflow **reviews** ("Submit a workflow version for review before publishing… approve or request changes"); change history; tags/folders; export/import; packages; **templates**; **sharing with others**.
- Authoring depth: **expressions**, **Code node**, AI Transform, HTTP Request node, sub-workflows ("Call workflows from other workflows"), flow logic (If/Switch, Merge, Loop, Wait, error handling), **credentials** ("Creating and editing credentials").
- AI-era: **AI Assistant** ("create, edit, test, and troubleshoot n8n workflows from a chat"), **AI Workflow Builder** ("natural language descriptions"), **agents** ("Build agents in n8n alongside your workflows, publish them, and let people reach them through chat, channels, and schedules"), MCP server integration, LangChain integration, evaluations.
- Org layer: user management, 2FA, SSO (SAML/OIDC), security policies, projects ("Data tables… within project boundaries"), source control, Enterprise features, OEM/embedded deployment ("surfacing n8n's interface inside your own product's UI under an OEM agreement").

## Product E — Microsoft Power Automate (organizational pole — boundary sample)

### Key observations (evidence layer A)

- Positioning: "helps you streamline your business processes and automate repetitive tasks… many **connectors** allow you to create workflows with **little to no knowledge of coding**."
- **Access requires a Microsoft work or school email address** — organizational identity, not personal-consumer.
- Three flow types: **Cloud flows** ("triggered either automatically, instantly, or via a schedule"), **Desktop flows** ("automate tasks on the web or the desktop"), **Generative actions (preview)** ("specify only the *intent*… have the AI choose the right set of actions in the right order").
- Confirms, from a second vendor, that cloud-flow and desktop-flow are **two artifact types in one product family** — the artifact-level seam with Desktop Automation is vendor-articulated, not inferred.

## Cross-product Comparison

| Aspect | IFTTT | Zapier | Make | n8n | Power Automate (cloud) |
|---|---|---|---|---|---|
| Unit of automation | Applet | Zap | Scenario | Workflow | Cloud flow |
| Authoring | trigger + queries + actions over services | trigger + one or more actions, field mapping | scenario canvas of modules, data mapping | nodes on a canvas, connections, expressions | visual editor, drag-and-drop |
| Trigger source | service events ("sending data to IFTTT…"), schedules, location (official examples) | app events (polling or instant) | service/module events, schedules | app/service trigger nodes, schedules (durable scheduler), webhooks, chat | service events, instant, schedule |
| Acts on | connected services (actions = "instructions that IFTTT sends") | connected apps (thousands-scale catalog) | connected apps (apps.make.com catalog) | connected apps/services via nodes + credentials, HTTP, code | connected services via connectors |
| Execution locus | IFTTT's service (broker between services) | Zapier's cloud ("watches for this event") | Make's cloud (operations metered) | n8n Cloud **or self-hosted server instance** | Microsoft cloud |
| Connections/credentials | service-level account linking (OAuth per service API) | per-app accounts (implied by app connection + mapping docs) | "Connections" as first-class concept | "Credentials" as first-class concept | connectors with account sign-in |
| Lifecycle | enable applet (consumer surface; not fetched in detail) | build → test (test records) → publish ("only process new data… after published") → history/replay | create → run → operations metered → error handlers/backoff | build → save/publish/unpublish → versions → executions (manual/partial/automatic) → debug | create → run (automatic/instant/scheduled) |
| Run machinery | — (consumer docs unreachable) | Zap history, statuses, replay, flood protection | history implied by ops metering + error handling docs | execution log, types, debug-by-execution, redaction | — (not fetched this pass) |
| Metering | Pro tier exists (features unverified) | tasks (glossary term) | credits & operations | executions data retention/governance | (licensing not fetched) |
| Org layer | none observed (consumer; Pro tier) | Team/Enterprise accounts, publishing restrictions | Organizations & teams, access management, admin | projects, SSO, reviews, source control, enterprise | work/school identity required |
| AI layer | IFTTT MCP listed | AI-generated Zaps; chatbots/agents/MCP | AI agents, Maia, MCP server | AI Assistant, AI Workflow Builder, agents, MCP | generative actions (preview) |
| Escape hatches | — (maker-side API instead) | code steps, webhooks, API calls | functions, tools | expressions, Code node, HTTP node | (not fetched) |
| Sharing | applets published by users themselves | templates, share/import/export (Team/Enterprise) | templates, community | templates, sharing, packages, OEM embed | templates (not fetched) |

### What is stable across the Type-core sample (evidence layer B)

- **Trigger + steps workflow**: every product composes a persistent, named workflow from (1) a trigger and (2) an ordered set of steps acting on connected services. (Applet: triggers/queries/actions; Zap: trigger/actions; Scenario: modules; Workflow: nodes.)
- **Connector catalog + linked accounts**: the subject matter is external services; the user links accounts (connections/credentials) per service; the platform mediates events in and instructions out.
- **Hosted-runtime execution on the user's behalf**: the platform watches for trigger conditions and executes the workflow unattended, remote from the user's personal device — vendor cloud in four products; a self-hosted server instance in n8n's alternative posture (still a hosted runtime, still not the personal device).
- **Run recording**: every product documents run machinery — history/execution logs, statuses, debugging, replay/recovery (n8n executions; Zapier history/replay; Make operations + error handling; IFTTT run semantics implied by trigger/action contract).
- **No-code authoring with escape hatches**: selecting and configuring prebuilt blocks never requires programming; optional code/webhook/HTTP steps exist for advanced use (Zapier code steps, n8n Code node, Make functions).
- **Lifecycle gates**: draft/test → publish/activate → live runs; testing with sample data before going live (Zapier test records + "only process new data after publish"; n8n save/publish/versions).
- **Templates/gallery sharing**: prebuilt workflows for adoption; community/template ecosystems in all four core products.
- **Metering**: usage-based metering (tasks/operations/executions) appears across the commercial products (Zapier tasks, Make credits & operations; n8n execution-data governance) — consumer pole less evidenced.

### Common but not defining (L1 candidates)

- filters/conditions/branching (Zapier filters/paths glossary; n8n If/Switch; Make routing)
- data stores/tables inside the platform (Zapier Tables, Make data stores, n8n data tables)
- error-handling machinery (retries/backoff, error notifications, error-handler branches) — Make/n8n documented directly, Zapier custom error handling documented
- webhooks/incoming-request triggers and API access to the platform itself
- team/organizational layer (shared workspaces, roles, admin, reviews, SSO) — present in the three commercial products, absent from the consumer pole → extension, not definition
- AI-era authoring aids and companion agent artifacts (all four commercial products) — extensions
- sub-workflows / multi-workflow composition (n8n directly; Zapier multi-step Zaps)
- platform-embedded distribution (IFTTT Connect API; n8n OEM) — variant

### Variant, era, or positioning dependent (L2 candidates)

- vendor-hosted vs self-hosted vs open-core licensing
- consumer-simple (applets) vs visual-deep (scenarios) vs developer-flavored (expressions/code) depth poles
- catalog scale and catalog composition (consumer apps ↔ enterprise SaaS)
- pricing/metering postures (subscription tiers, task/operation quotas) — not deeply evidenced; kept generic
- embedded/OEM distribution of the engine
- AI-companion artifacts (agents, MCP servers, chat surfaces) as parallel artifacts beside deterministic workflows

### Vendor-specific (L3 — kept out of the final document)

- Zapier: Zap/task naming, Next Gen Zaps, Tables/Canvas/Forms/Lead Router, flood-protection limits, Enterprise publishing restrictions, Zapier Learn/Experts programs.
- IFTTT: Applet/service/query vocabulary, service review process, "Works with IFTTT" program, Connect API, Pro tier, IFTTT MCP.
- Make: scenario/module/operation vocabulary, Make Grid, Maia, Managed Services, scenario inputs.
- n8n: nodes/expressions/Code node, durable scheduler, queue mode, environment-variable configuration surface, LangChain integration, community editions, OEM packaging.
- Power Automate: work/school identity requirement, flow-type triad, Power Apps integration, generative actions preview.

## Canonical Model (abstraction)

### L0 — Defining Invariant (minimal)

A Personal Workflow Automation Platform is recognizable by four jointly-held properties:

1. **No-code workflow composition** — the user assembles persistent, named workflows from prebuilt blocks: a trigger plus an ordered sequence of steps, with data mapped between steps; programming is never required to build or change a workflow (code/webhook steps exist only as optional escape hatches).
2. **Connected external services as the automation's subject** — trigger and action steps act on external applications/services through the platform's connector catalog, with the user linking an account to each service; the platform is the hub **between** services (events in from one, instructions out to others).
3. **Hosted-runtime execution on the user's behalf** — the workflow runs unattended on the platform's runtime (vendor cloud, or a self-hosted server instance in the open-source pole), remote from the user's personal device; the platform watches for trigger conditions and records each run.
4. **Personal ownership and scale at the core** — the unit of ownership is the individual user's own account and their own everyday tasks; organizational machinery (teams, roles, admin governance) is a common extension, not part of the definition (the consumer pole satisfies the Type with none).

Jointly-held is load-bearing:
- (1 + 4) with the person's own device as hub and on-device execution = **No-code Personal Automation Application** (sibling).
- (2 + 3) without no-code authoring = raw integration middleware / developer tooling.
- (1 + 2 + 3) with organizational processes as the managed subject = **Workflow Management Platform / BPM** territory.
- Ownership inverted to organization-deployed robots operating application UIs at fleet scale = **Robotic Process Automation Platform**.
- (2) swapped to local desktop apps/windows/input via a local engine = **Desktop Automation Application** (sibling).

Negative-space discriminators (same mechanism family, different Type when removed):
- Remove the external-services hub — triggers/actions centered on the person's own device and life context, execution on-device → **No-code Personal Automation Application**.
- Remove the hosted runtime — automation drives local desktop apps/windows/input through a local engine → **Desktop Automation Application**.
- Remove personal scale — centrally managed bot fleets as organizational assets → **Robotic Process Automation Platform**.
- Remove human-designed determinism — a model chooses actions at runtime from live observations → **Agent Tool / Computer-use Platform** / Agent Orchestration territory.
- Remove the "automate my own tasks" job — building software for others → **No-code Application Builder** territory.
- Remove the task/event framing — bulk structured data movement between data systems as the product → **Data Integration Platform / ETL** territory.

### L1 — Common Mature Structure

- connector catalog spanning services/apps with per-service authentication (linked accounts/credentials)
- trigger families: service/app events, schedules, incoming webhooks/requests; events reaching the workflow by polling or push
- step editor with per-step parameter forms and data mapping from prior steps
- filters, conditions, branching; multi-step chains; sub-workflows in deeper products
- test runs with sample data before activation; draft vs published states; versions
- run history with statuses; debugging from recorded runs; replay/retry
- error machinery: failure notifications, retries/backoff, error-handler branches
- usage metering (per task/operation/execution) in commercial products
- templates/galleries and community sharing
- in-platform data storage (tables/stores) for workflow state
- team/organizational extension (shared workspaces, roles, admin, reviews, SSO)
- AI-era extensions: authoring assistants, workflow generation from natural language, companion agent artifacts, MCP surfaces

### L2 — Variant / Optional Structure

- hosting posture: vendor cloud vs self-hosted/open-source vs open-core editions
- depth poles: consumer-simple applets ↔ visual-deep scenarios ↔ developer-flavored workflows
- catalog composition and scale (consumer apps ↔ enterprise SaaS)
- embedded/OEM distribution of the engine
- org-scale path (teams/enterprise governance)
- AI-companion artifacts as parallel product surfaces
- pricing/metering postures

### L3 — Vendor-specific

See vendor-specific list; stays in Research Notes.

## Vendor-specific Findings

- IFTTT's developer docs articulate the broker role explicitly: services push trigger data to IFTTT; IFTTT sends action instructions to services — the platform-between-services posture in the vendor's own words.
- Zapier's docs articulate the watch-and-run posture ("Zapier watches for this event…") and the publish gate ("only process new data created after it's published").
- n8n's docs articulate the hosting split (Cloud vs self-hosted) as a first-class choice, with the same workflow/executions model in both — evidence that "vendor cloud" specifically is an implementation, while "hosted runtime remote from the personal device" is the invariant.
- Power Automate's own taxonomy (cloud flows vs desktop flows vs generative actions) confirms the artifact-level seams from a second vendor.
- Consumer-vs-commercial split inside the sample: IFTTT carries no organizational layer; Zapier/Make/n8n all document team/enterprise machinery — supporting the decision to hold the org layer as extension, not definition.

## Rejected Findings

- "Personal Workflow Automation Platform = any automation tool for individuals" — rejected: that would merge the device-hub sibling into this Type. The hub (connected external services via a catalog, executed on a hosted runtime) is the discriminator.
- "Cloud execution in the vendor's cloud is definitional" — rejected: n8n's self-hosted pole satisfies the Type with a user-operated server; the invariant is the hosted runtime remote from the personal device, not vendor ownership of it.
- "The Type is defined by thousands-scale catalogs" — rejected: catalog scale varies (IFTTT's services, n8n's nodes); the invariant is the catalog-with-linked-accounts structure, not a number.
- "Team/organizational usage is part of the definition" — rejected: the consumer pole (IFTTT) satisfies the Type without any org machinery; the commercial products' team layers are extensions. (This is the deliberate asymmetry with the device-hub sibling, whose sampled products carry no org layer at all.)
- "AI runtime behavior is part of this Type" — rejected: AI appears as authoring aids (assistant, natural-language workflow generation) and as companion agent artifacts beside the workflows; the workflow itself remains a user-authored deterministic recipe. Model-decides-at-runtime is the neighboring agent Type.
- "This Type equals data integration/ETL" — rejected as an identity claim: data-movement steps exist inside these workflows, but the product's center of gravity is task/event automation across a person's or team's everyday services, not bulk pipeline management between systems of record.

## Boundary Findings

1. **vs No-code Personal Automation Application (§03.16 sibling — the central seam).** The seam recorded from the sibling side is confirmed from this side and sharpened by direct IFTTT evidence: the discriminator is **where the automation lives and what it acts on** — this Type's workflows act on connected external services through a connector catalog and execute on a hosted runtime (IFTTT's own docs: services push events in, IFTTT sends instructions out); the sibling's recipes act through the person's own device and personal-context triggers and execute on-device. Straddle is real and bidirectional (cloud platforms serve individuals; device automations reach internet services) — center-of-gravity, not mutual exclusion. The two leaf names are **not aliases**: each pole has a distinct market with distinct products (Shortcuts/Tasker vs Zapier/IFTTT/Make/n8n) and the sampled products do not migrate between poles. **This discharges the no-code sibling's joint-review flag from this side** (including the IFTTT caveat: IFTTT was sampled, via its developer docs). Recommend keeping both leaves as distinct Types with the recorded seam.
2. **vs Desktop Automation Application (§03.16 sibling).** The artifact-level test ("what does the artifact act on, and where does it execute") is confirmed from this side: this Type's artifact orchestrates external services from a hosted runtime; the desktop sibling's artifact drives local desktop apps/windows/input via a local engine. Power Automate documents cloud flows and desktop flows as two artifact types in one family. **This discharges the desktop-automation flag's open half from this side.**
3. **vs Robotic Process Automation Platform (§10).** Same mechanism family at organizational scale: bots deployed as managed organizational assets operating enterprise application UIs, with central fleet governance. Here: personal-scale self-owned workflows over service APIs/events. Scale + artifact surface keep the Types apart.
4. **vs Workflow Management Platform / BPM / Approval Workflow Platform (§10).** Those center the organization's business processes (forms, routing, approvals, SLAs, governance) with process participants as users; here the center is the individual's cross-service tasks, and org machinery is an optional overlay. The inverted-ownership leg keeps the boundary.
5. **vs Data Integration Platform / ETL (§13).** Mechanism neighbor: both move data between systems. The seam is the job — bulk structured pipeline management between data systems vs task/event-level automation across everyday app events for a person/team. Market straddle exists (these platforms add data tools; integration platforms add triggers); recorded as adjacency, not alias.
6. **vs Marketing Automation Platform (§06).** Similar event→action loops, but the subject is a marketing function's prospect/customer machinery (campaigns, journeys, segments), not the individual's own cross-service tasks. Domain vertical, not the same Type.
7. **vs Agent Tool / Computer-use Platform / Agent Orchestration Platform (§13).** Consistent with prior passes: runtime decisions here are the user-authored deterministic recipe; AI appears as authoring aid or companion artifacts. No merge. (Both Make and n8n now ship agent features *beside* their workflow engines — evidence the market itself separates the artifacts.)
8. **vs No-code Application Builder / Low-code Application Platform (§12).** Different job: those build applications for others; this composes automations over existing services for one's own tasks. Both no-code; boundary is the artifact and the beneficiary.
9. **vs Instant Messaging / notification surfaces, home automation, and single-service automation.** Single-service embedded automation (mail rules, scheduler features inside one product) is capability-level, not this Type — no cross-service catalog, no platform. Household device networks as the subject are home-automation territory (consistent with the sibling's Apple-documented personal-vs-home split).

## Historical / Market-Sample Check (§24 check)

- Dedicated historical sources could not be reached this pass (Wikipedia timeouts ×2; earlier passes recorded Wikipedia/Wayback timeouts), so the check is kept **conceptual** per the evidence rules: no precise historical claims are made.
- Conceptual check: the definition was phrased to avoid overfitting to the current SaaS/AI packaging — the core (no-code trigger→steps composition, connector catalog with linked accounts, hosted-runtime execution with recorded runs, personal ownership) does not depend on AI assistants, visual canvases, usage metering, or any vendor's pricing. A web-era service-to-service composition tool (visual cloud-hosted pipelines connecting web services) satisfies all four legs; a device-era or feature-phone automation does not (it is the device-hub sibling's ancestry, which that pass already documented). Server-side scripts/cron fail the no-code leg by design.
- The founding generation of this market (late-2000s/early-2010s consumer connection services and integration marketplaces) is asserted nowhere in detail this pass; the market's current poles are the evidentiary base.
- Check conclusion: the definition abstracts cleanly above the current implementation packaging; the historical leg is retained at conceptual strength only, flagged in Uncertainties.

## Uncertainties

1. IFTTT's consumer help center was unreachable (timeout, this pass and sibling pass). All IFTTT evidence comes from its own developer/platform documentation — official but maker-perspective; consumer-side operational details (applet limits, Pro features, run mechanics) are not asserted anywhere.
2. Make's deeper scenario mechanics (canvas editing, iterators/aggregators) were not fetched; Make claims are limited to its documented structure (scenarios, modules, connections, operations, error handlers, org layer, AI surfaces).
3. Power Automate was sampled at overview level only; licensing/premium-connector specifics not asserted.
4. Wikipedia/Wayback unreachable — the historical breadth check stays conceptual; no historical product is claimed for the Type.
5. Metering details (exact task/operation definitions, quotas) were not researched; no numeric claims made (catalog-scale numbers on Zapier's own pages differ between pages and are reported only as "thousands-scale").
6. The market boundary toward Data Integration/ETL and toward agent platforms is moving (both sampled commercial platforms now ship agent artifacts and data tools); the recorded seams are center-of-gravity judgments, expected to need re-checking over time.

## Final Synthesis

A Personal Workflow Automation Platform is a hosted service where an individual connects the external apps and services of their digital life and composes no-code workflows between them: an event in one service (or a schedule, or an incoming request) starts a workflow whose steps carry data out to other services — the platform watches, executes, and records each run. Its defining core is small and jointly-held: no-code trigger→steps composition with data mapping; connected external services via a connector catalog and per-service linked accounts as the automation's subject; hosted-runtime execution on the user's behalf (vendor cloud or self-hosted server), remote from the personal device; and personal ownership at the core, with organizational machinery as a common extension rather than definition. Everything that makes modern products feel different — catalog scale, visual canvases, branching and data stores, run replay and error handlers, metering, teams and governance, AI assistants and companion agents — is standard capability or variant. The mechanism family is shared with the device-hub sibling (different hub: the person's own device and life context — seam confirmed and jointly discharged this pass), with desktop automation (different artifact surface, confirmed by same-vendor flow-type taxonomies), with RPA (different ownership scale), with workflow-management/BPM (different subject: org processes vs personal tasks), with data integration (different job: pipelines vs task automation), and with agent platforms (opposite runtime decision-maker). The Type is real and distinct — not an alias of its siblings — and its seams are all center-of-gravity judgments in a market whose edges are converging.
