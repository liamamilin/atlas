# Research Notes — PaaS Management Console

## Research Goal

Understand the operator-facing management application of a Platform-as-a-Service (PaaS): what the console holds as objects of record, what the user deploys and operates, what the platform operates on the user's behalf, how the deploy→release→operate loop works, and where this Type ends and Container Management, Kubernetes Management, Cloud Management, and Serverless Management begin.

The directory leaf is the **console** — the management surface. The PaaS platform itself is the substrate beneath it, described only as needed to explain the console's work. This follows the family pattern already established by two processed siblings: API Gateway Management Console (gateway-operations control surface over a gateway runtime) and CPaaS Management (operator-facing management surface for a communications API platform).

## Initial Boundary

Working hypothesis at start:

- This is the web dashboard (+ CLI/API) through which developers and app-owning operators manage applications deployed to a managed runtime platform: create apps, deploy code, scale, configure, attach backing services, watch logs/metrics, manage domains and access.
- Nearest neighbors: Container Management (exposes container substrate), Kubernetes Management Platform (exposes cluster estate), Cloud Management Platform (account/resource/cost governance), Serverless Management Platform (function/invocation unit, sibling leaf, unprocessed), Internal Developer Platform (org-defined abstraction layer above).
- Two processed sibling passes already recorded the seam from the other side: Container Management's Related-Types table says "a platform-as-a-service abstracts the runtime away (deploy code, receive an endpoint); container management exposes the container substrate as the object of work", and Kubernetes Management Platform says the same ("substrate exposed vs abstracted"). This pass must test and ratify that seam from the PaaS side.

## Research Questions

1. What is the unit of record in the console? (app? service? site?)
2. What exactly does the user supply, and what does the platform build/run? (source vs image vs spec)
3. What does a "deploy" produce, and how is version history / rollback modeled?
4. What does the user operate at app grain (scale, config, routing, logs, metrics)?
5. How are backing services (databases etc.) attached and consumed?
6. How are environments (dev/staging/prod) modeled — separate apps, slots, spaces, projects?
7. Is the console the only surface, or are CLI/API peers? (console-as-client-of-management-API)
8. Who uses it (developer vs platform operator), and how is access organized?
9. Where does the substrate abstraction leak (sizing, SSH, instance types) — and does the leak change the Type?
10. Where is the exact seam vs container/K8s/cloud/serverless management?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, different customer tiers, and different packaging:

| Product | Pole | Why |
|---|---|---|
| **Heroku** | Classic commercial developer PaaS; standalone dashboard; the category archetype | Richest concept documentation; deploy via Git/GitHub/API |
| **Cloud Foundry** | Open-source, self-hosted enterprise PaaS (deployable on own infra); CLI-centric, cf push | Platform-model anchor; orgs/spaces; buildpack→droplet staging |
| **Azure App Service** | Hyperscaler PaaS embedded in a general cloud portal | App-as-cloud-resource; deployment slots; code and custom-container poles |
| **Render** | Modern self-serve next-generation PaaS | Git-native auto-deploy; service types; preview environments; Blueprints |

Market-context anchors (not fetched, no claims made from them): Google App Engine (historical hyperscaler PaaS; cloud.google.com unreachable in sibling passes on 2026-09-06/07), AWS Elastic Beanstalk (impure pole — PaaS built over IaaS primitives), Railway/Fly.io (modern peers).

## Sources

All fetched 2026-09-09. Evidence layer A (direct official documentation) unless noted.

- Heroku Dev Center — "How Heroku Works" — https://devcenter.heroku.com/articles/how-heroku-works
- Heroku Dev Center — "The Heroku Dashboard" — https://devcenter.heroku.com/articles/heroku-dashboard
- Heroku Dev Center — "Pipelines" — https://devcenter.heroku.com/articles/pipelines
- Cloud Foundry Docs — "Cloud Foundry overview" — https://docs.cloudfoundry.org/concepts/overview.html
- Cloud Foundry Docs — "Pushing your app with Cloud Foundry CLI (cf push)" — https://docs.cloudfoundry.org/devguide/deploy-apps/deploy-app.html
- Microsoft Learn — "Overview of Azure App Service" — https://learn.microsoft.com/en-us/azure/app-service/overview
- Microsoft Learn — "Set Up Staging Environments" (deployment slots) — https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots
- Render Docs — documentation index — https://render.com/docs
- Render Docs — "The Render Dashboard" — https://render.com/docs/render-dashboard.md
- Render Docs — "Deploying on Render" — https://render.com/docs/deploys.md

Failed fetches (abandoned per network rule):

- CF console surface: docs.cloudfoundry.org/console/apps-manager.html (404), stratos-ui.readthedocs.io (404) — the web-console layer of Cloud Foundry was NOT verified; CF is used only as platform/CLI-model evidence.
- Google App Engine: not attempted (cloud.google.com unreachable ×2 in sibling passes on 2026-09-06/07).

## Product A — Heroku (Tier-1, 4 pages)

Console-as-surface (Dashboard article):

- Dashboard is "the primary web interface for interacting with the Heroku platform": create/rename/delete apps; create and manage datastores; view app metrics; configure add-ons; manage Teams; create pipelines; configure deployment integrations; view usage, invoice, billing.
- Default view = **app list** (name, technology, stack, region); context switcher between personal account and Teams; **app overview** = "at-a-glance information about an app's resources (dynos and add-ons), metrics, collaborator activity, and deployment activity"; More menu → view recent logs, open web console (attach to a one-off dyno, `heroku run`).
- Parity: "Most of these tasks can also be performed with the Heroku CLI or the Platform API." (console = one peer surface over the platform's management API)

Platform model (How Heroku Works):

- **App** = source code + dependency description (+ Procfile declaring **process types** — named commands). App is the persistent record.
- Deploy: Git (`git push heroku main`), GitHub integration, or API. Build: **buildpacks** produce a **build artifact** (slug; or OCI image for the newer generation).
- **Dynos**: "isolated, virtualized Unix containers" preloaded with the release; **dyno formation** = counts per process type; scale = `heroku ps:scale web=3 queue=2`. **Dyno manager** keeps dynos running (cycles, replaces on fault).
- **Config vars**: configuration stored outside code, exposed as environment variables; "you can change it independently."
- **Release** = build artifact + config vars + add-ons, held in an **append-only ledger**; every deploy/config/add-on change creates a new release; `releases:rollback` to any prior release.
- **Add-ons**: third-party/marketplace backing services (datastores, queues, email) provisioned and **attached** to the app; credentials delivered via config var (e.g. `REDIS_URL`).
- **Logging**: platform collates dyno + router logs into a single stream (Logplex); `logs --tail`; drains for persistence.
- **HTTP routing**: platform routers distribute requests across web dynos; scaling web traffic = scaling web process count.
- No OS management: "Because Heroku manages and runs applications, there's no need to manage operating systems or other internal system configuration."
- Ephemeral filesystem per dyno; one-off dynos for admin tasks; some dyno types **sleep/scale to zero** when idle.
- **Pipelines**: "a group of Heroku apps that share the same codebase", each app at a stage (development/review/staging/production); **promotion** copies the *same build artifact* downstream ("production contains the exact same code that you tested in staging"); **review apps** = ephemeral apps per pull request; CI integration; pipeline-level access permissions on ephemeral apps.

## Product B — Cloud Foundry (Tier-1, 2 pages)

Platform model (overview):

- Explicit PaaS stack diagram: in a PaaS the provider manages everything except applications and data ("PaaS Stack: The provider manages all layers except for applications and data").
- "Deployment automation: Developers can deploy their apps to Cloud Foundry using their existing tools and with zero modification to their code."
- Deployment postures: open-source platform installed by an operator on own infra/IaaS (BOSH layer), or a commercial CF provider. Operators (installing CF) and developers (deploying apps) are documented as distinct audiences with distinct doc trees.
- **Cloud Controller** "runs the apps and other processes on the cloud's VMs, balancing demand and managing app lifecycles"; **Diego** distributes app instances over host VMs; **Gorouter** routes incoming traffic.
- **Staging**: Cloud Controller combines **stack** (OS) + **buildpack** + source into a **droplet** that VMs run.
- **Orgs/spaces/roles** (UAA, OAuth2, LDAP/SAML): workspaces and roles (admin/developer/auditor) scoped per org and space.
- **Services**: Service Broker API advertises a catalog; user **provisions a service instance**, then **binds** it to the app; credentials delivered to the app (VCAP_SERVICES env).
- **Loggregator**: aggregates app logs + container metrics into a stream (Firehose; nozzles/drain targets).

Deploy flow (cf push):

- `cf push APP-NAME`: creates app in org/space → creates and binds route (host+domain, e.g. `example-app.apps.example.com`) → uploads source (`.cfignore` to exclude) → stages with buildpack → uploads droplet → instances running; status table shows requested state, instance counts, per-instance cpu/memory/disk, URLs.
- Custom settings: instances, **memory limit**, disk limit, log rate limit, start command; or a **manifest.yml**; `.profile` init script; services block binds service instances.
- Updates: default push stops existing instances (downtime); **rolling deployments** or **blue-green** route swapping avoid it; schema-migration case documented (stop-then-push).
- `cf scale`, health checks, app SSH (configurable), CF API (CAPI V2/V3) and app revisions documented in the doc tree.
- CLI-first: the console's canonical surface is the cf CLI targeting the Cloud Controller API endpoint; a web console (Apps Manager / Stratos) exists in the ecosystem but was not verifiable this pass.

## Product C — Azure App Service (Tier-1, 2 pages)

Platform model (overview):

- "A platform that lets you run web applications, mobile back ends, and RESTful APIs **without worrying about managing the underlying infrastructure**."
- Managed web stacks (.NET, Java, Node.js, Python, PHP) on Windows/Linux **or deploy as a custom container** ("if your app is containerized, you can just deploy it as a custom container").
- Scale **up** (plan tier) or **out** (instances, autoscale); automatic OS/runtime management and patching; staging environments (deployment slots); continuous deployment from GitHub Actions/Azure Pipelines; custom domains + managed certificates; built-in authentication; VNet integration / dedicated **App Service Environment** for isolation; App Service **plans** (pricing/capacity tiers; apps run in a plan).
- Audience spread documented: students, small business/startups, enterprises.
- Packaging note: the console is the Azure portal's app management page (and CLI/PowerShell/ARM); the app is an Azure resource ("go to your app's management page"; resource groups; App Service (Slot) resource type).

Environments (deployment slots):

- **Deployment slots** = "live apps with their own host names" attached to the app; deploy to a nonproduction slot, validate, then **swap** into production.
- Swap mechanics: settings applied and instances warmed up on the source slot, then routing rules switched — "eliminates downtime"; swap can run with preview (two-phase), be automated (auto swap), or be **rolled back by swapping back** ("restore the slots to their pre-swap states by swapping the same two slots immediately").
- Slot-specific vs swapped settings are explicit and configurable ("deployment slot setting" checkbox); **traffic % routing** to slots for canary-style release; per-tier slot-count limits documented.

## Product D — Render (Tier-1, 3 pages)

Console (Dashboard + index):

- "The Render Dashboard is the web interface for managing everything in your Render workspace — services, team members, billing, and more."
- Main page lists **services** plus **projects**; service detail = logs + settings; left panel jumps to **Blueprints** (IaC) and **environment groups**; workspace switcher; ⌘K search; billing page (plan, payment, usage charges, included amounts).
- Parity: "You can also manage Render resources from your terminal with the Render CLI or programmatically with the Render API" (plus MCP server for agents).

Deploy model (Deploys):

- **Service** = the unit (types: web service, private service, background worker, cron job, static site). Create service by linking a repo branch → **auto-deploy on commit** (optionally gated on CI checks passing), or manual deploys (latest commit / specific commit / clear cache & deploy / **restart** = redeploy same commit), deploy-hook URL, API.
- Deploy steps: **build command → pre-deploy command (optional) → start command → live**. "If any command fails or times out, the entire deploy fails... Your service continues running its most recent successful deploy."
- **Zero-downtime deploys**: build fail keeps old instance; new instance spins up, health-checked, traffic switches, old instance gets graceful-shutdown signals; multi-instance rolls one at a time, reverting on failure. Overlapping-deploy policy (wait vs override) configurable.
- **Deploy history** and current live deploy per service (Deploys page); rollbacks documented separately; ephemeral filesystem by default; persistent disks as opt-in.
- Packaging: native runtimes (build commands) **or** Dockerfile builds **or** prebuilt images from registries — the container is a packaging option, not an operated substrate.

## Cross-product Comparison

| Structure | Heroku | Cloud Foundry | Azure App Service | Render | Layer |
|---|---|---|---|---|---|
| Application as persistent named record | app | app (in org/space) | web app (Azure resource) | service (in workspace/project) | universal |
| Platform manages runtime/OS | dyno manager; "no need to manage operating systems" | provider manages all layers but apps+data; Diego/Cell infra | "without worrying about managing the underlying infrastructure"; automatic OS patching | platform-managed infra; compute plans abstract CPU/RAM | universal |
| User supplies code/spec; platform builds | Git/GitHub/API → buildpacks → slug/OCI | cf push source/manifest → buildpack → droplet | code deploy (IDE/CLI/CI) or custom container | git branch → build command; or Dockerfile/image | universal (packaging varies) |
| Versioned release + history + rollback | release ledger + releases:rollback | rolling deploys; revisions (CAPI) | slots + swap + swap-back | Deploys page + rollbacks | universal |
| Scale at app grain (instances) | ps:scale per process type | cf scale instances/memory | scale up (plan) / out (autoscale) | instance count per service | universal |
| Config outside code | config vars → env | env vars / manifest; VCAP_SERVICES | app settings / connection strings; slot-sticky | environment variables & secrets; environment groups | universal |
| Routing/endpoints managed in-console | HTTP routing to web dynos; domains | routes + domains (host/domain) | custom domains, managed TLS | custom domains, managed TLS, private services | universal |
| App logs + metrics in surface | Logplex stream; dashboard metrics | Loggregator streaming + container metrics | diagnostics/monitoring | logs + service metrics pages | universal |
| Backing services attached to app | add-ons marketplace; creds via config var | service instances via broker; bind; creds via env | databases/connection strings; Service Connector | Postgres/Key Value datastores; connect | universal |
| Console+CLI+API peers | Dashboard + CLI + Platform API | cf CLI + CAPI (+ ecosystem web console) | portal + CLI/PowerShell + ARM | Dashboard + CLI + API + MCP | universal |
| Team/access model | Teams, collaborators, pipeline access | orgs/spaces/roles (UAA) | Azure RBAC/Entra | workspaces/members/roles; audit logs | universal |
| Environment separation + promotion | pipelines (stages; promote artifact); review apps | spaces as environments; blue-green | deployment slots + swap + traffic % | projects/environments; preview environments | common (mechanisms differ) |
| Health checks | (not verified in-sample) | cf health checks | swap warm-up/health gate | health checks gate traffic switch | common |
| One-off/admin tasks | one-off dynos (`heroku run`), scheduler | cf tasks | (not verified in-sample) | one-off jobs; SSH/shell | common |
| Autoscaling | (not verified in-sample) | via separate autoscaler (not core) | autoscale documented | (not verified in-sample) | optional |
| Declarative app spec | app.json/Heroku.yml (adjacent docs) | manifest.yml | ARM templates | render.yaml Blueprints | common |
| Scale-to-zero / free tier | eco dynos sleep | — | free tier documented | free tier documented | variant |
| Isolation postures | Private Spaces | isolation segments | VNet/ASE | private services/private network | variant |
| Deployed as SaaS vs self-hosted | SaaS | self-hosted open-source or commercial provider | SaaS (within cloud) | SaaS | variant |
| Console packaging | standalone dashboard | CLI-first; web console in ecosystem | embedded in general cloud portal | standalone dashboard | variant |

## Canonical Abstraction

### L0 — Defining Invariant (four jointly-held structures)

1. **The application as the unit of record.** A persistent, named application/service held by the console — created and deleted through it, surviving deploys, restarts, and sessions, carrying its releases, configuration, bindings, and routing. Remove → an inventory/dashboard with nothing to operate (or a bare build service).
2. **The platform-managed runtime substrate.** The execution environment — OS images, patching, capacity, process supervision, traffic routing — is owned and operated by the platform. The user deploys *code* (or a declared spec/image) and receives a running endpoint; the user is never required to operate servers, nodes, or clusters. Remove → an IaaS/hosting console (VM dashboard) or, if the substrate becomes the object of work, Container Management.
3. **The code→build→release deploy loop.** Supplying source or a declarative spec triggers a platform build producing a versioned **release** that becomes the running state of the app; release history is retained and rollback to a prior release is available; failed deploys leave the prior release running. Remove → CI/CD delivery machinery (deploy with no operated runtime) or static hosting (no release lifecycle).
4. **The app-scoped operating surface.** Scale (instance counts / compute), configuration (env vars/connection strings), routing/endpoints/domains, and observable state (logs, metrics, events) are operated at the *application* grain through the console — with CLI and API as peer clients of the same platform management API. Remove → the runtime substrate becomes the object of work (Container Management), or the surface degrades to a deploy button with no operations.

Jointly-held load-bearing checks (all four legs are A-layer, 4/4 products):

- 1 alone = app registry / IDP catalog shelf
- 2 alone = hosting / VM dashboard
- 3 without 1+4 = CI/CD build-and-deploy service
- 4 without 2 = container management (substrate exposed)
- 1+3 without 4 = deployment service with no operating surface
- 1+2 without 3 = plain web hosting with no release lifecycle
- 2+4 without 1 = ephemeral file-drop hosting (no app-of-record)
- 1+4 without 2 = impossible-in-practice; the console cannot operate what it does not have a runtime for

### L1 — Common Mature Structure

- **Backing services attached to the app** — marketplace/catalog of managed datastores and services; provisioning binds the service to the app and delivers credentials (config var / env var / connection string). Universal in-sample.
- **Console + CLI + API parity** — the console is one peer client of the platform's management API; all three surfaces perform the same operations. Universal in-sample (echoes the CPaaS/API-gateway console family pattern).
- **Team / access model** — accounts, teams/workspaces/orgs/spaces/projects, roles scoped to the app hierarchy; audit/activity records.
- **Environment separation and promotion** — staging/production (and review/preview) as separate operable instances of one app; promotion moves an artifact/release between them (pipelines, slots+swap, environments, blue-green). Mechanisms vary widely; the structure is common.
- **Logs and metrics in the surface** — app log streams (tail/search/drain) and basic performance metrics as first-class app pages.
- **Custom domains and managed TLS** for the app's endpoints.
- **One-off / administrative tasks** — run a command against the app's latest release (one-off dynos, cf tasks, one-off jobs); shell/SSH access offered with varying posture.
- **Declarative app specification** — a manifest/template describing the app (manifest.yml, render.yaml, ARM templates) as an alternative or complement to console forms.
- **Usage and billing visibility** in the console (usage meters, invoices, included amounts).

### L2 — Variant / Optional Structure

- **Packaging substrate**: buildpack/source builds vs Dockerfile builds vs prebuilt registry images (all three poles in-sample; several products support multiple).
- **Console packaging**: standalone developer dashboard vs embedded in a general cloud portal vs CLI-first platform with an ecosystem web console.
- **Deployment posture**: hosted SaaS PaaS vs self-hosted open-source platform (operator installs the platform itself — platform-operator role is a different audience with different tooling).
- **Service-type breadth**: web-only vs typed surfaces (background workers, cron jobs, private services, static sites).
- **Scale-to-zero / free tiers / sleep behavior**.
- **Isolation posture**: shared multi-tenant runtime vs private/dedicated spaces/networks.
- **Traffic shaping**: percentage traffic splitting, canary, auto-swap (product-dependent).
- **Autoscaling** (present in some products, absent or add-on in others).
- **IaC machinery around the app** (Blueprints/Terraform providers) — optional, and distinct from the IaC Type.
- **AI-era surfaces** (managed model access, agent/MCP integration) — era-typical optional.

### L3 — Vendor-specific (research notes only)

- Heroku: dynos, dyno formation, Procfile/process types, slugs, Logplex, one-off dynos, eco sleep, Private Spaces, pipeline stage names, Fir/Cedar generations, session-length rules.
- Cloud Foundry: droplets, stacks, Diego auctions, Gorouter, VCAP_SERVICES, CAPI V2/V3, orgs/spaces/UAA, Service Broker API, .profile scripts, log rate limits.
- Azure App Service: App Service plans, deployment slot semantics (swap steps, sticky settings, slot-count-per-tier), App Service Environment, Managed Instance pole, WEBSITE_* settings.
- Render: service types naming, deploy-hook URLs, pipeline minutes, overlapping-deploy policies, shutdown-delay mechanics, environment groups, MCP server.

## Rejected Findings (anti-overfit)

- **"git push deployment" is NOT definitional.** Heroku pushes via Git, but CF pushes a directory, Azure deploys via IDE/ZIP/CLI/CI, Render triggers via dashboard/hook/API. Canonical concept: *transport of source/artifact/spec to the platform*, with git as a common implementation.
- **Buildpacks are NOT definitional.** Container-image and arbitrary-build-command poles exist in the same sample (Azure custom containers, Render Docker/image deploys). The invariant is "the platform builds/assembles what runs", not the buildpack mechanism.
- **Process-model specifics are NOT definitional.** Procfiles/dynos are Heroku's realization; CF processes, Render service types, Azure plan+settings are sibling realizations. The common structure is "the user declares how the app runs and how much of it".
- **SaaS-only delivery is false.** CF is a self-hosted open-source platform; the console pattern survives (CLI + web console over the platform's own API).
- **Scale-to-zero is NOT definitional.** It is a specific dyno-tier behavior on Heroku; most paid tiers are always-on.
- **"Zero infrastructure visibility" is NOT absolute.** The abstraction is *operational*: the user is not required to operate the substrate (Heroku forbids managing OS; Azure sizes plans but patches OS; Render sizes compute but runs infra). Some products expose sizing tiers (App Service plans) or even IaaS primitives beneath (Elastic Beanstalk, unverified). The invariant is "no substrate operations are required to deploy and run", not "no substrate information is shown".

## Boundary Findings

- **vs Container Management** (ratifies the seam recorded by the container-management and kubernetes-management passes from their side): the object of work differs. A container manager operates images, hosts, clusters, and running containers; a PaaS console operates *applications* on a runtime the platform owns. Even when a PaaS accepts **container images as packaging** (Azure custom containers, Render Docker deploys, CF Docker support), no nodes, clusters, or orchestrator objects are exposed to operate — packaging ≠ substrate. Remove the abstraction (expose hosts/clusters/images as the operating surface) → Container Management. Expose Kubernetes objects specifically → Kubernetes Management Platform.
- **vs Cloud Management Platform**: CMP governs cloud *accounts, resource estates, and cost* across providers (onboarding existing resources, provisioning, governance). A PaaS console governs the *application lifecycle* on one platform's own managed runtime; it never onboards foreign cloud accounts as its estate. Azure App Service's console is in-type here, not a CMP.
- **vs Serverless Management Platform** (sibling leaf, unprocessed): proposed seam = unit of record and execution model. PaaS console manages long-running applications with declared processes/process types routed via HTTP (plus workers/cron); serverless management centers functions invoked by events/triggers with per-invocation scale. Convergence is real and documented in-sample: scale-to-zero exists on PaaS (Heroku eco), and PaaS consoles carry function-adjacent primitives (cron jobs, one-off jobs). Scale-to-zero is therefore NOT the seam; the unit-of-record test is. Flag for joint review when serverless-management-platform is processed.
- **vs Internal Developer Platform**: an IDP is an organization-defined self-service abstraction layer (catalogs, scaffolding, golden paths) that may itself be built on a PaaS; the PaaS console is the platform vendor's own operating surface for apps already on the platform. No scaffolding/catalog-of-templates center observed in any sampled console.
- **vs CI/CD platforms**: delivery machinery (pipelines, runners, promotion logic) vs the operating surface for what is delivered. Sampled consoles integrate CI (Render CI-gated auto-deploys, Heroku CI, Azure Pipelines) but deployment delivery is not the console's center; the app's running state is.
- **vs Infrastructure-as-Code Platform**: IaC declares infrastructure and runs to completion; the PaaS console is a long-lived operating surface. IaC machinery inside consoles (Blueprints, ARM templates) is optional tooling, not the center.
- **vs the console-family siblings (API Gateway Management Console, CPaaS Management)**: same family pattern — operator-facing control surface over a managed platform, console as client of the platform's management API, CLI/API parity. Managed-substrate test separates: gateway routes/policies/consumers; communications sender resources/credentials; here, applications and their releases on a managed runtime.
- **vs Application Deployment Management**: endpoint/device software distribution vs platform-hosted application lifecycle. No end-user device estate exists in any sampled console.
- **Component-view Type note**: like API Gateway Management Console, the console never ships as a standalone SKU — it is always the management surface of a PaaS product (standalone dashboard, cloud-portal section, or CLI-first platform with web console). Packaging variance, not a Type split.

## Historical / Market-Sample Check

- Pre-Docker PaaS generation (Heroku's Bamboo era, Google App Engine 2008, Engine Yard): app record + managed runtime + source upload → running app + logs/scale. All four L0 legs satisfied with no containers, no git-push, no buildpacks, no slots/pipelines. ✓
- Self-hosted/regional generation (Cloud Foundry distributions, regional CF-derived clouds): same legs; console may be CLI-first; platform-operator role distinct. ✓
- Modern self-serve generation (Render/Railway-class): same legs; git-native auto-deploy, preview environments, IaC files. ✓
- Embedded-console pole (App Service inside the Azure portal; App Engine inside the GCP console): same legs; console is a section of a general cloud portal. ✓ (GAE itself unreachable — held as market anchor only, no claims.)
- Impure pole (Elastic Beanstalk over EC2, unverified this pass): recorded as market context; the operational-abstraction reading of L0 leg 2 accommodates substrate leakage without changing the Type.

## Uncertainties

- Cloud Foundry's web console (Apps Manager/Stratos) surface details were not verified (2 fetch failures); CF evidence is platform/CLI-model only. The final document makes no console-surface claims specific to CF.
- Autoscaling presence on Heroku/Render was not verified in fetched pages; autoscaling is written as product-dependent/optional.
- Heroku/CF health-check mechanics were only partially in evidence (CF health checks and Render health checks documented; Heroku's verified pages did not cover them); health checks are written as "common", not universal.
- Google App Engine and AWS Elastic Beanstalk were not fetched; no claims made from them.
- Precise numeric limits (slot counts per tier, timeouts, shutdown delays, session lengths) were observed in evidence but are deliberately kept in these notes, not in the final document.

## Final Synthesis

The PaaS Management Console is the platform's operator-facing application-management surface. Its defining core is four jointly-held structures: (1) the **application as unit of record** — a persistent named app carrying its releases, configuration, bindings, and routing; (2) the **platform-managed runtime substrate** — the user deploys code and receives an endpoint, never required to operate servers/OS/clusters; (3) the **code→build→release deploy loop** — platform builds of supplied source/spec produce versioned releases with retained history and rollback, failed deploys leaving the prior release live; (4) the **app-scoped operating surface** — scale, configuration, routing/domains, logs/metrics operated at application grain, with the console, CLI, and API as peer clients of one platform management API.

Around this core, mature products standardly add: attached backing services (marketplace/catalog, bound with credential delivery), environment separation and artifact promotion, team/access models with audit, custom domains/TLS, one-off administrative tasks, declarative app manifests, and usage/billing visibility. The market varies along packaging (buildpacks ↔ containers), console packaging (standalone ↔ portal-embedded ↔ CLI-first), deployment posture (SaaS ↔ self-hosted), service-type breadth, and isolation posture.

The Type is a component-view member of the platform-console family (alongside API Gateway Management Console and CPaaS Management): the console is always the management surface of a PaaS product, never a standalone SKU. Its sharpest boundary is with Container Management / Kubernetes Management (substrate abstracted vs exposed) and its nearest unprocessed sibling seam is with Serverless Management Platform (long-running app-of-record vs function/invocation unit) — flagged for joint review.
