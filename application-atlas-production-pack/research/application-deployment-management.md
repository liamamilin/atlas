# Research Notes — Application Deployment Management

## Research Goal

Understand what "Application Deployment Management" is as an Application Type: what objects it manages, who operates it, how a deployment flows from package to tracked installation, and where it ends relative to neighboring types (Patch Management, Endpoint Management / UEM, Desktop & Application Delivery, Configuration Management, Continuous Delivery / Release Management).

## Initial Boundary

Position in DIRECTORY.md: section 14 "IT, Cloud & Infrastructure", between Patch Management and Desktop & Application Delivery — i.e., the **endpoint / IT-operations** flavor of deployment.

Initial hypothesis: IT-admin-controlled distribution and installation of software packages onto a managed population of endpoint devices, with per-device execution tracking. The name is ambiguous: "application deployment" is also used by server-side release tooling (Continuous Delivery). Directory neighborhood supports the endpoint reading; this is checked below under Boundary Findings.

## Research Questions

1. What is a "deployable unit"? (installer file? app record? store app? script?)
2. How are targets expressed? (static groups? dynamic collections? users? OUs?)
3. What is a "deployment" as an object? What parameters does it carry?
4. Required vs optional installs — how do products model admin-driven vs user-initiated installs?
5. How does the system know software is already installed (detection) and what happens on failure?
6. What tracking/reporting does "management" imply? Is there a maintenance loop (redeploy, remediate, uninstall)?
7. What user-facing surfaces exist (self-service portals)?
8. Where does this type end and Patch Management / UEM / CD begin?

## Representative Products

| Product | Segment / philosophy | Rationale |
|---|---|---|
| Microsoft Configuration Manager (SCCM/MECM) | enterprise Windows; suite ancestor (SMS) with the fullest application model | richest Tier-1 documentation; defines much of the category vocabulary |
| PDQ Deploy | SMB/mid-market Windows; admin-centric, lightweight, on-prem | package-library-driven philosophy; different customer tier |
| ManageEngine Endpoint Central | mid-market/enterprise unified endpoint suite | deployment as a module of UEM; cross-OS incl. mobile apps |
| Jamf Pro | Apple-only enterprise MDM | different platform and management substrate (MDM), user Self Service emphasis |

## Sources

Research date: 2026-09-06.

- Microsoft Learn (Configuration Manager docs) — fetched:
  - "Introduction to app management" — https://learn.microsoft.com/en-us/mem/configmgr/apps/understand/introduction-to-application-management
  - "Deploy applications" — https://learn.microsoft.com/en-us/mem/configmgr/apps/deploy-use/deploy-applications
- PDQ — fetched: PDQ Deploy product page + FAQ — https://www.pdq.com/pdq-deploy/
- ManageEngine — fetched: Endpoint Central "Automated software deployment" feature page — https://www.manageengine.com/products/desktop-central/software-deployment.html
- Jamf — fetched: Jamf Pro product page — https://www.jamf.com/products/jamf-pro/ . **Access limitation:** learn.jamf.com (operational documentation) is a JavaScript-only web application; two fetch attempts returned no content. Kandji support 404; docs.ninjaone.com transport error. Jamf evidence is therefore limited to its product page (Tier 2); assertions from Jamf are marked B-limited and no precise Jamf workflow details are claimed.
- No access was attempted to the ConfigMgr admin console itself; all ConfigMgr observations come from official docs.

## Product Observations

### Product A — Microsoft Configuration Manager (SCCM/MECM) [Evidence: A]

From official docs:

- **Application** = a container ("box") holding one or more **deployment types** (sets of installation files + instructions how to deploy), e.g. MSI, MSIX, store app, script installer, App-V, macOS, task sequence. Legacy simpler model: "packages and programs".
- **Requirements** (e.g. OS version) and a library of **global conditions** decide whether/which deployment type installs on a device. Client re-evaluates requirement rules on a schedule; if a device later meets requirements, the app installs.
- **Detection method** — the system checks whether the application is already installed; if detected, it does not install again.
- **Deployment** = instructions to the client on how and when to install or uninstall. Deployment parameters observed:
  - **Action**: Install or Uninstall (Install takes priority over Uninstall on the same device; uninstall deployments are forced to Required purpose).
  - **Purpose**: **Required** (client automatically installs per schedule; user can install early via Software Center) or **Available** (appears in Software Center; user installs on demand).
  - **Target**: a user or device **collection**.
  - **Content**: distribution of installation files to **distribution points**.
  - **Scheduling**: availability time; **installation deadline** for required deployments; **grace period** (defined in client settings, hours) delaying enforcement until a non-business window.
  - **User experience**: user notifications (toast vs dialog), software installation and system restart behavior outside **maintenance windows**.
  - **Approval**: user requests for available apps can require administrator approval (per-device approval variant exists).
  - Extras: send wake-up packets (Wake On LAN); allow metered-connection downloads; "uninstall if device falls out of the collection" (implicit uninstall); pre-deploy to user's primary device (user-device affinity); auto-upgrade superseded versions.
- **Dependencies** (must install other apps first), **supersedence** (new version replaces old; optionally auto-upgrade), **revisions** (versioned app definitions with history/restore), **application groups** (several apps as one deployment, ordered install).
- **Simulated deployment** — evaluates requirements/detection/dependencies without installing; **phased deployments** — sequenced rollout (pilot collection → automatic continuation based on success criteria).
- **State-based monitoring**: per-device compliance state per deployment, monitored in the console; state messages.
- **Re-evaluation / remediation loop**: if a user uninstalls a required deployed app, the client detects it at the next evaluation cycle and automatically reinstalls.
- **Software Center** (end-user application): browse/request apps deployed to user or device, install and schedule installations, view installation status, repair (if repair command defined).

### Product B — PDQ Deploy [Evidence: A]

From official product page/FAQ:

- Deployment tool for on-prem Windows devices (domain/VPN-connected); companion cloud product (PDQ Connect) for remote fleets.
- **Package Library**: 200+ prebuilt packages for common apps, kept updated and tested to ensure **silent installations**; auto-update posture.
- **Custom packages**: multi-step packages (install an MSI, run PowerShell scripts); steps notion.
- **Targeting**: specific computers, device groups, or **dynamic collections** from companion product PDQ Inventory (identify machines missing a specific app/update).
- **Schedules**: run at specific times, recurring intervals, or **heartbeat triggers** (when the machine becomes available) so offline devices get deployments when they come online; recurring patch-style schedules.
- **Deployment history**: current and completed deployments with status, package deployed, target details; post-deployment status emails.
- **Central server**: centrally maintained packages, deployment histories, schedules across multiple administrators.
- Overlaps patch management (deploys Windows cumulative updates, hotfixes).
- Per-admin licensing; MSP/education/nonprofit presence.

### Product C — ManageEngine Endpoint Central [Evidence: A]

From official feature page:

- Software deployment is one module of a **unified endpoint management and security suite** (with Patch Management, OS Deployment, Asset Management, MDM, etc.); deployment spans Windows, Mac, Linux, iOS, Android, tvOS, chromeOS.
- **Software packages** created from **pre-defined application templates** (10,000+ with install/uninstall switches) or manually; stored in a central **Software Repository** (network share for LAN agents, HTTP repository for WAN agents).
- **Mobile app distribution**: bulk deploy to users or devices, custom-built or store apps (IPA, APK, XAP, MSIX, APPX, APPXBUNDLE, MSI); store integration; install/update/delete and license management.
- **Self Service Portal**: admin publishes apps and patches; users install on their own (explicitly framed as reducing help-desk tickets). **Enterprise app catalogue**: approved-app discovery surface.
- **Pre-deployment activities**: condition checks and configuration before installation (targets must meet prerequisites); **post-deployment activities**: custom scripts, registry changes, shortcuts, path changes after install; uninstall of previous versions.
- Same package used for **install and uninstall** (MSI, EXE, MSU, APPX, MSP).
- **Deployment policy scheduling**: day/date/time, preset time window, off-hours; optionally copy installables to clients before installing; install **as a specific user** vs default System User.
- **Software metering** (usage tracking for license optimization) and patch/asset modules "work in tandem" with software deployment.
- Framing quote: "Software Deployment is the process of remotely installing software on multiple or all the computers within a network simultaneously, from a central location… in the context of a large network (more than 20 computers)."

### Product D — Jamf Pro [Evidence: B, limited — product page only]

- Apple device management (Mac/iPhone/iPad/Apple TV); **app lifecycle management** described as "automated and secure app management"; **Self Service+** lets users install apps, update software, maintain their own devices.
- Management model: configuration profiles plus **policies and scripts**; **Smart Groups** (dynamic device and user groups); **Blueprints** (declarative device management including app installations); zero-touch deployment; **inventory management**; patch Apple devices "without user interaction".
- No operational-doc details accessible (JS-only doc site); per limitation rule, treat as confirming that the same structures exist on a macOS/MDM substrate (groups, app install actions, self service, inventory, patching) without precise workflow claims.

## Cross-product Comparison

| Structure | ConfigMgr | PDQ Deploy | Endpoint Central | Jamf Pro |
|---|---|---|---|---|
| Managed endpoint population with an agent/management substrate | ✓ (client) | ✓ (agent/remoting; Inventory companion) | ✓ (agents per OS) | ✓ (MDM enrollment) |
| Deployable unit = installer content + install instruction(s) | ✓ (application/deployment type; packages) | ✓ (package with steps; silent tested) | ✓ (package from template; store/custom apps) | ✓ (apps/packages/policies — page-level) |
| Binding of package × target set = deployment object | ✓ (deployment to collection w/ purpose, action) | ✓ (deployment: package × targets × schedule) | ✓ (package + deployment policy/labels) | ✓ (policy/blueprint scoped to groups — page-level) |
| Target sets are groups, incl. dynamic/criteria-based | ✓ (collections) | ✓ (dynamic collections via Inventory) | ✓ (users/devices; inventory-driven per suite) | ✓ (Smart Groups) |
| Executed install vs user-requested install distinction | ✓ (Required vs Available) | admin-scheduled primarily (no user portal in Deploy) | ✓ (scheduled vs Self Service Portal) | ✓ (automated vs Self Service+ — page-level) |
| Per-target execution status tracked and surfaced | ✓ (state-based monitoring, per-device compliance) | ✓ (deployment history w/ status, emails) | ✓ (deployment reporting; suite reports) | ✓ (dashboard of policy/patch statuses — page-level) |
| Detection / already-installed logic | ✓ explicit (detection methods) | ✓ (silent-tested packages; re-deploy scheduling; exact detection mechanics not confirmed from fetched pages) | ✓ (templates carry switches; install/uninstall same package) | not confirmed from accessible evidence |
| Failure handling / retry / remediation | ✓ (re-evaluation auto-reinstall; phased rollouts) | status + re-scheduling | ✓ (pre/post activities; failure framing "target computers don't meet prerequisites") | not confirmed |
| Maintenance-window / scheduling controls | ✓ (deadline, grace period, maintenance windows, user notifications) | ✓ (schedules, heartbeat triggers) | ✓ (deployment policy windows, off-hours) | not confirmed |
| Pre-built catalog of ready packages | partial (store apps; supersedence) | ✓ (Package Library) | ✓ (10,000+ templates) | not confirmed |
| Self-service end-user portal | ✓ (Software Center) | ✗ (admin-only product) | ✓ (Self Service Portal, app catalogue) | ✓ (Self Service+ — page-level) |
| Approval gates for user requests | ✓ (admin approval of requests) | ✗ observed | not confirmed on fetched page | not confirmed |
| Uninstall as first-class action | ✓ (deployment action; implicit uninstall) | uninstall packages via steps | ✓ (same package installs/uninstalls; delete apps) | not confirmed |
| Content-distribution infrastructure (distribution points/repository) | ✓ (distribution points) | local/central server | ✓ (software repository: share/HTTP) | n/a (MDM substrate) |
| Bundled as module of wider suite | ✓ (full systems-management suite) | paired product (Inventory); suite siblings | ✓ (UEM suite) | ✓ (Apple management suite) |

Reading: every sampled product maintains (1) a managed device population, (2) a deployable software unit, (3) a binding of unit to target set, (4) tracked per-target outcomes. These recur across four very different substrates (Windows on-prem suites, lightweight admin tooling, cross-OS UEM, Apple MDM) — strong cross-product commonality. Historical sanity checks (Group Policy software installation: MSI package + OU-linked policy + per-machine install state; SMS "packages → collections → advertisements → status"; iOS VPP store-app deployment via MDM) also fit this structure, so it is not an artifact of the current market.

## Canonical Model

### L0 — Defining Invariant (minimal)

```text
Managed endpoint population (devices under the system's control)
└── Deployable package (software content + installation instruction)
    └── Deployment assignment (package × target set, with an execution policy:
        when it runs, whether it is mandatory or user-initiated, how it behaves)
        └── Tracked per-target execution outcome
            (pending / succeeded / failed per device, surfaced to the operator)
```

Four invariants. Remove any one and the type collapses:
- no endpoint population → it is not endpoint deployment (becomes server-side release tooling or a download site);
- no package/instruction → nothing to deploy (becomes inventory);
- no binding/execution policy → software exists but is never distributed (becomes a file store);
- no tracked outcome → there is no "management" (becomes a remote launcher).

### L1 — Common Mature Structure

- **Targeting machinery**: device/user groups, dynamic/criteria-based collections, user-device affinity.
- **Silent/unattended installation** as the default execution mode; install commands/switches.
- **Detection logic**: skip if already installed; version awareness.
- **Required vs available deployments**: mandatory auto-install with deadline vs optional user-requested install; approval gates for user requests.
- **Scheduling controls**: availability times, deadlines, recurring schedules, maintenance windows, offline-device handling (triggers when devices come online), wake-up.
- **User experience controls**: notifications, restart behavior, user-visible progress.
- **Per-deployment status reporting** (per-device success/failure) and deployment history; alerts.
- **Uninstall and re-assertion**: uninstall deployments; re-evaluation that reinstalls mandated software users removed.
- **Pre/post deployment activities**: condition checks before install; scripts/registry/shortcuts after install.
- **Content distribution infrastructure**: repository/distribution points/staging.
- **Self-service portal** exposing selected deployments to end users.
- **Prebuilt application catalogs / package libraries / templates** with maintained silent-install definitions.
- **Packaging support**: multi-step packages, dependencies, supersedence/version upgrades, app grouping, deployment simulation/testing, phased/pilot rollouts.
- **Inventory linkage**: what is installed where, feeding targeting and reporting.

### L2 — Variant / Optional Structure

- **Platform substrate**: Windows agent-based (dominant historical form), macOS/Linux, mobile (MDM-based store and custom app deployment), cross-OS suites.
- **Deployment topology**: on-prem console + infrastructure vs cloud-hosted console + internet-connected agents.
- **Suite position**: standalone deployment tool vs module inside UEM/endpoint suite; paired inventory product vs integrated inventory.
- **Content scope**: arbitrary custom software vs OS updates vs store apps vs scripts (overlaps into Patch Management / OS deployment without being defined by them).
- **Deployment style**: policy-driven reassertion (state-based) vs run-once deployments.
- **Per-user vs per-device targeting**; primary-device concepts.
- **Governance**: approval workflows, phased rollouts, pilot rings, metered-connection rules.
- **Adjacent bundling**: patch management, OS imaging/provisioning, software metering, license compliance, remote control.

### L3 — Vendor-specific (kept out of final document)

- ConfigMgr: "application vs package and programs" duality, deployment types per technology, global conditions library, task sequences, distribution point groups, enforcement grace period mechanics, Windows Embedded write filters, Software Center branding.
- PDQ: Package Library testing regime, "heartbeat" trigger name, central server, per-admin pricing, pairing with PDQ Inventory.
- Endpoint Central: template count, network-share vs HTTP repository distinction, LAN/WAN agent split, "install as specific user", software metering framing.
- Jamf: Blueprints/Declarative Device Management naming, Smart Groups, Self Service+.

## Vendor-specific Findings

- PDQ Deploy is admin-only in its on-prem form (no user portal observed) — user self-service is not universal across the type.
- Endpoint Central explicitly ties deployment to license-compliance outcomes (metering) — a suite-level motivation, not a definitional one.
- ConfigMgr's simulated deployment and phased rollout are the most developed "test/rollout" machinery observed; treat as advanced/common-mature rather than defining.

## Rejected Findings

- **"Deployment = CI/CD release of server applications"** — rejected as the L0 for this leaf. That workflow targets servers/build artifacts with dev/ops actors; it belongs to Continuous Delivery / Release Management types in section 12. Directory placement (section 14, next to Patch Management and UEM) and the entire sampled market describe endpoint software distribution. Flagged as a naming-ambiguity boundary issue for STATUS.md.
- **"Package library / templates are part of the definition"** — rejected: valuable (PDQ, Endpoint Central) but ConfigMgr and historical GPO-style deployment work without them; a market convenience, not an invariant.
- **"Self-service portal is required"** — rejected: absent in at least one major product (PDQ Deploy on-prem).
- **"Distribution-point infrastructure is defining"** — rejected: an implementation of content delivery on on-prem topologies; cloud/MDM products distribute differently.
- **"Windows-only"** — rejected: macOS/Linux/mobile substrates carry the same model.

## Boundary Findings

| Neighboring type | Shared surface | Discriminator ("remove what → becomes the other type") |
|---|---|---|
| **Patch Management** | same execution machinery (packages → endpoints → status) | restrict content to vendor-published updates with vulnerability/compliance metadata → Patch Management. ADM's content is any software the organization chooses. Many products bundle both. |
| **Endpoint Management / UEM** | device population, groups, app install | add configuration profiles, compliance, security policy, restriction enforcement as primary objects → UEM. ADM is the software-distribution slice. |
| **Desktop & Application Delivery** | "getting applications to users" | remove installation-on-the-endpoint (deliver via virtualization/streaming/packaged layers, app runs elsewhere) → Desktop & Application Delivery. |
| **Continuous Delivery Platform / Release Management** (section 12) | the word "deployment" | targets become servers/environments and content becomes build artifacts with release pipelines, actors become dev/ops → CD. Endpoint-vs-server is the hard split; naming overlap flagged. |
| **Software Inventory / IT Asset Management** | installed-software data | ADM changes installed software; inventory/asset types only observe and account for it. Inventory data feeds ADM targeting. |
| **Configuration Management / IaC** | "state enforcement" | ADM enforces installed-software presence via installer execution on managed endpoints; IaC/CfM declares machine configuration broadly. Overlap exists (re-assertion loops) but objects differ (apps vs full config). |
| **Mobile Application Management (MAM)** | app distribution to phones | MAM focuses on app-level protection/config without device management; ADM's app delivery rides on device management. Distinct type; partial overlap on store-app delivery. |

## Uncertainties

- Exact per-device status vocabularies (state names, retry counts, default re-evaluation intervals) were not normalized across products; ConfigMgr specifics are documented, others not — final document keeps status descriptions conceptual.
- Jamf Pro's operational workflow (package→policy→scope mechanics) is unverified from primary sources due to JS-only documentation; its inclusion is limited to confirming structural commonality at product-page level.
- PDQ's already-installed detection mechanics were not confirmed from the fetched pages (only silent-install testing and scheduling are confirmed).
- Endpoint Central approval workflows for self-service installs were not confirmed on the fetched page.
- Degree to which mobile store-app deployment belongs here vs MAM was resolved pragmatically (device-managed deployment is in scope; app-protection-focused MAM is not) — could merit a dedicated research pass if the taxonomy later splits mobile app management.

## Final Synthesis

Application Deployment Management is the IT-operations type whose world consists of four stable things: a managed population of endpoint devices, deployable software packages (content plus install instruction), deployment assignments binding packages to target device sets under an execution policy (mandatory vs user-initiated, scheduled, conditioned), and tracked per-target execution outcomes feeding a remediation loop. Everything else commonly seen — silent-install catalogs, self-service portals, distribution infrastructure, phased rollouts, approvals, suite bundling with patching or UEM — is mature but non-defining. The type is bounded on one side by Patch Management (content = vendor updates), on another by UEM (adds configuration/compliance objects), by Desktop & Application Delivery (no endpoint installation), and across the taxonomy by Continuous Delivery (server-side homonym).
