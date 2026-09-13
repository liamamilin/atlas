# Research Notes — Patch Management

Slug: patch-management
Section: §14 IT, Cloud & Infrastructure
Research date: 2026-09-09
Methodology: update-v1 (WORKFLOW_v1.1 + WRITING_GUIDE_v1.1)

## Research Goal

Understand what a Patch Management application actually is as an Application Type: what the unit of record is, how update knowledge enters the system, how machines are assessed against it, how updates are deployed under operator control, and how the Type separates from its extremely dense §14 neighborhood (Endpoint Management/UEM, Application Deployment Management, RMM, Vulnerability Management, Configuration Management, Infrastructure Automation, IT Change Management, Server Management).

## Initial Boundary (pre-research hypothesis)

- Core hypothesis: patch management = keep installed software current on a managed machine population, against a continuously refreshed catalog of vendor updates, with controlled deployment and compliance evidence.
- Nearest neighbors suspected: UEM (patch as update slice), Application Deployment Management (same package×target machinery), RMM (patch as one maintenance action), Vulnerability Management (risk picture vs remediation execution), IT Change Management (governance vs execution of a recurring change class), Configuration Management (declared state vs vendor currency), Infrastructure Automation (generic automation vs update-domain machinery).
- Known counterparty flags to discharge or ratify:
  - endpoint-management-uem (processed 2026-09-08): "update/patch machinery is a module inside UEM; remove patching → still UEM, remove config/compliance/lifecycle → patch tool" — flag for this pass.
  - it-change-management (processed 2026-09-08): "patch tooling executes a recurring change class at fleet scale, expected to ride the pre-approved/standard change path (governance-vs-execution seam)" — flag for this pass.
  - endpoint-protection-platform (processed): "suites that patch operating systems and third-party applications carry a patch-management-shaped module" — ratify from this side.
  - remote-monitoring-management-rmm (UNPROCESSED): UEM pass proposed seam = RMM monitoring/maintenance-first + MSP-oriented vs UEM policy/lifecycle-first; patch sits inside both — counterparty duty for the RMM pass.
  - vulnerability-management (§15, UNPROCESSED): remediation-execution seam expected — flag for that pass.
  - server-management-platform (UNPROCESSED): patching as one slice of server ops — flag.

## Research Questions

1. What are the core objects? (machine population, update catalog, assessment state, deployment/policy, outcomes)
2. Where does update knowledge come from, and how is it kept current?
3. How does the system know what is missing on each machine? What states exist?
4. How is deployment controlled? (approval, schedules, windows, restarts, user notification)
5. What recurs? What is the operational rhythm?
6. What content scopes exist? (OS only / OS + third-party apps / drivers / BIOS / firmware)
7. How do machines join the population? (agent / native update channel / agentless)
8. What compliance/reporting machinery exists and why?
9. Where does patch management end and UEM / deployment management / RMM / vulnerability management begin?
10. Would older, platform-native, and non-Windows products still fit the definition?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Philosophy / position | Customer tier | Evidence tier reached |
|---|---|---|---|
| Microsoft Configuration Manager (software updates) | platform-native enterprise; update management built on the OS's own update agent (WSUS/WUA lineage) | large enterprise | Tier-1 (Learn conceptual doc, deep) |
| Automox | cloud-native dedicated patch/endpoint automation; vendor-installer sourcing; no on-prem infrastructure | mid-market/upper-SMB | Tier-2 (platform + how-it-works pages) + Tier-1 help-center articles |
| ManageEngine Patch Manager Plus | standalone dedicated patch product (also a component of Endpoint Central suite); on-prem + cloud | SMB/mid-market | Tier-2 product page + Tier-1 help docs (workflow, deployment policies) |
| Red Hat Satellite | Linux subscription-content management; provisioning + patching + config for RHEL estates | enterprise Linux | Tier-2 product page (docs.redhat.com 403) |
| Ivanti Security Controls | security-suite patch management for data centers; agentless option; CVE-to-patch mapping | enterprise | Tier-2 product page |

Rejected/considered: NinjaOne (MSP-tier RMM with patch module — marketing site 404 ×2, docs host transport error; dropped per network rule; MSP pole noted as variant from UEM-pass context), WSUS (legacy platform-native; covered conceptually via ConfigMgr doc's WSUS integration), Qualys PM (vulnerability-rooted pole — left for the vulnerability-management pass), Kandji/Action1 (not fetched; market context only).

## Sources

Fetched 2026-09-09:

- Microsoft Learn — "Introduction to software updates - Configuration Manager" — https://learn.microsoft.com/en-us/mem/configmgr/sum/understand/software-updates-introduction (Tier-1, full text)
- Automox — platform page — https://www.automox.com/platform (Tier-2)
- Automox — how-it-works page — https://www.automox.com/how-it-works (Tier-2)
- Automox Help Center — index — https://help.automox.com/hc/en-us (Tier-1 index)
- Automox Help Center — "Policy Catalog Overview and Usage" — https://help.automox.com/hc/en-us/articles/46712227910420 (Tier-1)
- Automox Help Center — "How Automox Sources and Updates Third-Party Applications" — https://help.automox.com/hc/en-us/articles/51637368237076 (Tier-1)
- ManageEngine — Patch Manager Plus product page — https://www.manageengine.com/patch-management/ (Tier-2)
- ManageEngine — Help documents index — https://www.manageengine.com/patch-management/help/ (Tier-1 index)
- ManageEngine — "Patch Management Workflow & Setup" — https://www.manageengine.com/patch-management/help/patch-management-workflow.html (Tier-1)
- ManageEngine — "Deployment Policies" — https://www.manageengine.com/patch-management/help/deployment-policies.html (Tier-1, deep)
- Red Hat — Satellite product page — https://www.redhat.com/en/technologies/management/satellite (Tier-2)
- Ivanti — Security Controls patch management page — https://www.ivanti.com/products/patch-management (Tier-2)

Access limitations:
- docs.redhat.com 403 (Satellite operational docs unreachable) — Satellite claims held at product-page tier only; no Satellite-specific operational parameters asserted.
- NinjaOne: www.ninjaone.com paths 404 ×2; docs.ninjaone.com transport error — dropped; MSP-tier pole carried as variant context from the UEM pass's counterparty notes, not as sampled evidence.
- docs.automox.com returned empty body once (help.automox.com used instead — reachable).
- help.automox.com article-level 404 on one guessed URL (index + section pages used instead).

## Product Observations

### Microsoft Configuration Manager — software updates (evidence layer A)

From the Learn conceptual document (full text):

- **Synchronization**: the site's software update point connects to Microsoft Update (or an upstream WSUS server) to retrieve software updates *metadata* on a schedule or manually; metadata is stored in the site database as configuration items; multiple software update points replicate downstream. The update *files* are a separate concern (deployment packages).
- **Compliance assessment (scan)**: clients scan for software updates compliance against the synchronized catalog; per-update state messages flow back to the site database. Compliance states: **Required** (applicable and not yet installed / pending restart / deployed-not-installed), **Not Required** (not applicable), **Installed**, **Unknown** (no state received — scan failed/backlog/corrupt).
- **Scan mechanics**: a scan evaluates the client against the *whole synchronized catalog*, not per deployment; cached scan results have a TTL; scans are triggered by schedule, manually, before download, before install, after install, after restart.
- **Assessment ≠ deployment**: "Running a Software Updates Scan Cycle refreshes compliance for all updates... However, the client can only install a newly added update after it also receives the deployment (machine) policy for that update. Refreshing compliance and acting on a deployment are separate steps."
- **Deployment packages**: the vehicle that downloads update source files to a network share and copies them to distribution points; content versioning; clients install from any distribution point that has the content.
- **Two deployment workflows**: **manual** (filter updates → create software update group → download content → deploy; used to establish a baseline) and **automatic deployment rules (ADR)** (criteria e.g. "all security updates released in the last week", evaluation schedule, download, deploy to target collection; used for ongoing monthly "Patch Tuesday" management and definition updates). ADRs support multiple deployments per rule (test collection → broader collections, with per-deployment activation time, deadline, user experience).
- **Deployment process**: assignment policy → client evaluates → downloads to cache at "software available time" → installs at deadline (re-verifying the update is still required just before install) → state message "installed"; optional deployments wait for user initiation.
- **Restart handling**: required restarts start by default after deadline; can be suppressed; maintenance windows constrain when changes apply (write-filter devices require maintenance windows).
- **Reevaluation cycle**: default every 7 days — re-scans previously deployed updates and reinstalls if missing.
- **Extending the catalog**: System Center Updates Publisher manages/publishes updates *not available from Microsoft Update* (custom/third-party) into the update server for deployment.
- Vocabulary: software update point, deployment package, software update group, automatic deployment rule, maintenance window, compliance states.

### Automox (evidence layers A + B)

From platform/how-it-works pages and help-center articles:

- **Agent + cloud console**: one lightweight agent per endpoint (Windows/macOS/Linux); "no VPNs, no gateways, and no on-prem patching infrastructure"; patches "automatically every time a device is connected to the internet".
- **Live inventory**: on agent connect, builds "hardware, installed software, configuration, and missing patches"; endpoints organized into **groups**; "scan automatically or on demand".
- **Policies as the work unit**: "Policies are how work is defined... Policies patch operating systems and third-party apps, deploy required software, or run Worklets... They run on schedules you set, targeted to the groups you choose. Every run reports back, so you know what changed and what didn't."
- **Policy Catalog**: vendor-maintained best-practice policy templates (e.g. "Windows Patch Best Practice – Servers"); filterable by OS / type (Patch Only, Advanced) / category (Third Party Software, OS Software); create editable policy from template; policies editable/disabled/cloned (dev/test/prod variations).
- **Third-party sourcing (Tier-1 article)**: updates obtained "from the software vendor's official source and applied using the vendor's own installer"; some titles via the app's own updater (Office Click-to-Run on Windows, Microsoft AutoUpdate on macOS); **on Linux, third-party software updates through the device's own package manager/repositories** rather than Automox-delivered packages; always targets the latest supported version; device Details → Software shows **Installed Version vs Available Version**; titles can be set to **Ignored**; catalog entries reviewed via support when a public version is missing.
- **Operational behaviors documented in help titles**: patch-age filters (monthly policy skipping a cumulative update), communication apps and active calls (patch deferral while apps in use), required-restart handling, alerting/notifications for patch results, Windows Update service resets as troubleshooting.
- **Beyond patching**: Worklets (PowerShell/Bash) for configuration/mitigation where no patch exists; remote control (Splashtop); unified reporting ("patch coverage, policy results, endpoint status, audit logs... what's patched, what's compliant, what still needs attention").
- Positioning vs WSUS: "WSUS and other legacy tools do not provide... updating anything but Windows software"; "WSUS and other on-prem tools can only patch those remote endpoints when they connect to the corporate network via VPN".

### ManageEngine Patch Manager Plus (evidence layers A + B)

From product page + help docs:

- **Position**: "Automate patching for servers, laptops, and workstations — all from a single console"; "the automated patching component of Endpoint Central" (suite position); on-prem and cloud editions; Windows/macOS/multiple Linux distros + "1100+ third-party applications"; drivers and BIOS updates in Enterprise edition.
- **Stated loop**: "The managed systems are scanned periodically to identify the missing patches and updates. Once detected, they are automatically tested and deployed via lightweight agents."
- **Help-doc structure ("5 simple stages")**: architecture/workflow → installation & setup (agents for Win/Mac/Linux; distribution servers; cloud hosting) → settings (server/proxy/mail/AD) → **patch settings** (patch approval & test group; system health policy; patch DB settings — types of patches per OS + scheduled vulnerability-database update) → **deployment** (patch scan; automate deployment; manual deployment; closed-network/DMZ patching; decline patch; BIOS/driver updates; patch reports).
- **Server needs internet connectivity to access vendor sites and download patches** (proxy configuration documented) — the catalog/content flows from vendor sites through the server.
- **Deployment policies (Tier-1, deep)**: four-step policy creation —
  1. *Deployment schedule*: weekly/day selection with **Regular split** vs **Patch Tuesday split** (weeks numbered relative to Patch Tuesday for Microsoft-aligned cycles); **deployment window** (start/end; incomplete deployments continue in subsequent windows; multiple windows per policy); **patch download timing** ("any time agent contacts the server" vs "only at deployment window"); initiate at startup/refresh cycle.
  2. *Pre-deployment activities*: Wake-on-LAN (same/remote subnet mechanics), pre-deployment reboot (with skip-if-not-required), custom scripts (stop processes, snapshots, cluster/sequential server patching, backup-readiness checks), dependency files.
  3. *Pre-deployment user notification*: notify users; allow skip; force deployment after x days if user skipped.
  4. *Post-deployment activities*: custom scripts; reboot/shutdown policy — force immediately (with notification timeout), force at specified reboot window, or delay with end-user postpone intervals (configurable; macOS defaults fixed); "restart and shutdown" option so patch status reflects before shutdown; execute-activities-even-on-failure option.
- **Role-based access**: Administrators / Policy owners / Patch Management Write access can modify deployment policies.
- **Other capabilities**: patch testing and approval before deployment; decline patches (legacy apps); roll back faulty patches; self-service portal for patches; LAN/WAN/DMZ + remote workers without VPN; mobile admin app; integrations (Tenable, Rapid7, ServiceDesk Plus, CrowdStrike); compliance analytics/audits.

### Red Hat Satellite (evidence layer A, product-page tier only)

- Position: "simplifies the provisioning, patching, and management of your Red Hat Enterprise Linux environments"; manages "entire hybrid RHEL footprint — on-premise to cloud — from a single console"; scale framing "thousands of distributed systems".
- **Patch management and content distribution** feature block: **supply chain verification** ("verify digital signatures on all synced content"); **lifecycle curation** ("curate specific repositories and patches for Dev, QA, and Production environments"); **precision patching** ("deploy specific, critical patches... without forced system-wide upgrades or dependency shifts").
- **Security management** block: centralized security hub ("issue updates at scale on custom schedules from a local, centralized point"; "eliminates reliance on external networks for critical updates"); compliance enforcement; configuration assessment; data sovereignty.
- **Vulnerability prioritization**: "scan and rank named threats and CVEs based on the risk to your specific environment".
- Also does provisioning (bare-metal discovery, compute profiles) — broader than patch management; patch/content management is one pillar.
- Sourcing limitation: operational docs unreachable (403); all Satellite observations are product-page tier; no operational parameters asserted.

### Ivanti Security Controls (evidence layer A, product-page tier only)

- Position: patch management for "physical and virtual servers in the data center" within a security-controls suite (patch + application allowlisting + privilege management).
- Capabilities listed: "Scan physical and virtual systems for missing patches"; **agentless patching** ("assess and deploy patches to workstations and servers connected to your network"); remote task scheduling ("schedule patching when it won't impact your users"); **CVE to patch list creation** ("take a vulnerability assessment from any vendor, find all patches that relate to that list, and build a patch group of updates to quickly deploy"); REST APIs; advanced reporting dashboards.
- OS scope: Windows, Red Hat Linux, CentOS; VMs/templates "regardless of power state or if they are on or offline".
- Customer review (schema.org markup on page): "primary patching solution for over 5000 servers/machines... monthly patch deployment as well as zero day patches".

## Cross-product Comparison

| Structure | ConfigMgr | Automox | Patch Manager Plus | Satellite | Ivanti SC |
|---|---|---|---|---|---|
| Managed machine population (agents/groups) | ✓ collections, client agents | ✓ agent + groups | ✓ agents + distribution servers | ✓ registered RHEL systems | ✓ (agentless or agent) |
| Update catalog synchronized from upstream | ✓ Microsoft Update / WSUS | ✓ vendor-official sources, Automox-maintained | ✓ vendor sites → patch DB (scheduled sync) | ✓ Red Hat content (subscription), signature-verified | ✓ Ivanti patch feed |
| Missing-update assessment (scan) | ✓ compliance scan, 4 states | ✓ automatic/on-demand scan; Installed vs Available | ✓ periodic scan for missing patches | ✓ (implied: vulnerability scan/rank) | ✓ scan physical/virtual systems |
| Controlled deployment under policy | ✓ manual + ADR, deadlines, maintenance windows | ✓ policies on schedules, targeted to groups | ✓ deployment policies: schedule/window/pre-post activities | ✓ custom schedules, precision patching | ✓ scheduled tasks |
| Per-machine outcome / compliance record | ✓ state messages → site DB, console display | ✓ "every run reports back" | ✓ patch reports, compliance analytics | ✓ compliance enforcement/monitoring | ✓ reporting dashboards |
| Restart/reboot orchestration | ✓ restart at deadline, suppressible | ✓ restart handling documented | ✓ force/delay/postpone reboot policies | (not observed at this tier) | (not observed at this tier) |
| Approval / decline / test-before-deploy | ✓ manual selection + ADR criteria; Updates Publisher | ✓ Ignored state; policy templates | ✓ test & approve, decline, rollback | ✓ lifecycle curation (Dev/QA/Prod) | ✓ CVE-to-patch group building |
| Third-party application updates | via Updates Publisher (custom) | ✓ core (vendor installers / app updaters) | ✓ core (1100+ apps) | (RHEL content focus) | ✓ OS + third-party |
| Drivers/BIOS/firmware | (not in fetched doc) | (not observed) | ✓ Enterprise edition | (not observed) | (not observed) |
| Agentless mode | ✗ (agent-based) | ✗ (agent-based) | ✗ (agent-based) | ✗ | ✓ |
| Native OS update channel used | ✓ WUA/WSUS | ✓ (Windows via WU metadata; Linux via package managers) | (agent-centric) | ✓ (subscription content) | (not observed) |
| CVE/severity metadata on updates | (security updates category) | ✓ CVE analysis imagery; zero-day guidance | ✓ vulnerability DB sync; Tenable/Rapid7 integration | ✓ CVE scan/rank | ✓ CVE-to-patch mapping |
| Cloud control plane | on-prem (Intune = cloud sibling) | ✓ cloud-native | ✓ both editions | on-prem (containers in 6.20) | on-prem |
| MSP multi-tenancy | ✗ | (not observed) | ✗ | ✗ | ✗ |
| Suite position | platform suite (ConfigMgr) | dedicated (+ endpoint automation) | dedicated + Endpoint Central suite | infrastructure-management suite | security suite |

Stable commonalities (all five): managed machine population; upstream-synchronized update catalog; missing-update assessment producing per-machine state; policy-controlled deployment; outcome/compliance recording. These are the Type's spine.

Near-universal (4/5 or strong 3/5): approval/decline/test machinery; restart orchestration; recurring automation (ADR / scheduled policies / deployment policies); third-party app updates (absent only where the product is platform- or subscription-scoped); severity/CVE context; compliance reporting.

Variable (variant axes): agent vs agentless vs native channel; content scope (OS-only ↔ OS+apps+drivers+BIOS); packaging (standalone ↔ suite module ↔ platform-native); cloud vs on-prem; server vs workstation emphasis; MSP tenancy; vulnerability-driven prioritization depth.

## Abstraction Hierarchy

### L0 — Defining Invariant

Four jointly-held structures. Remove any one and the product stops being recognizable as patch management:

1. **The managed machine population** — computers (workstations and/or servers) held as individually addressable managed records, brought under management via an agent, a native update channel, or agentless discovery. Remove → an update catalog with no targets, or generic inventory.
2. **The update catalog** — the system's maintained knowledge of available software updates (OS updates, commonly third-party application updates) for the software running on the population, refreshed by synchronization from upstream update sources (OS vendor update services, software vendors, or the tool vendor's aggregation feed). Remove → generic remote execution / software distribution with no update semantics.
3. **Currency assessment** — comparing each machine's installed state against the catalog to determine which updates are missing or applicable, producing per-machine, per-update state (missing/installed/not-applicable/unknown-class states). Remove → blind distribution; the "what is out of date" picture — the reason the Type exists — collapses.
4. **Controlled update deployment** — selecting/approving updates and installing them on targeted machines under operator-defined policy (schedules/windows, restart handling), with per-machine outcomes recorded back. Remove → a scanner/reporter only; the remediation — the "management" — is gone.

Jointly-held is load-bearing:
- 1 alone = device inventory / remote-execution fleet
- 2 alone = update mirror/feed
- 3 alone = missing-patch scanner (vulnerability-assessment-shaped)
- 4 without 1+2+3 = blind software distribution (Application Deployment Management territory)
- 1+2 without 3+4 = mirror with no client picture
- 1+3 without 4 = assessment without remediation
- 1+4 without 2+3 = scripted remote installs (infrastructure-automation territory)
- 2+3 without 1 = catalog + scan with nothing managed

### L1 — Common Mature Structure

Present in most mature products; not required for the definition:

- update approval workflow (approve/decline; test groups / pilot rings before broad deployment)
- deployment policies: recurring schedules, deployment/maintenance windows, deadline semantics, Patch-Tuesday-aligned cycle options
- restart/reboot orchestration: pending-restart state, force/delay/postpone options, user notification, skip-if-not-required
- automatic deployment rules / recurring policy automation (deploy what matches criteria as it arrives)
- per-machine + rolled-up patch compliance reporting (the audit surface)
- content distribution machinery (download once from upstream, stage internally, deliver to machines; distribution points / relays / distribution servers)
- third-party application update support
- severity/CVE metadata attached to updates; zero-day urgency handling
- staged rollout (test collection → production collections)
- decline/rollback of problematic updates
- offline/air-gapped catalog import (closed networks/DMZ)
- end-user notification/postpone surfaces
- role-based access over patch configuration

### L2 — Variant / Optional Structure

- content scope: OS-only ↔ OS + third-party apps ↔ + drivers/BIOS/firmware
- platform scope: Windows-centric ↔ cross-OS ↔ Linux-subscription ↔ Apple-centric
- packaging: standalone dedicated ↔ module of UEM/RMM/security suite ↔ platform-native console
- acquisition mode: agent ↔ agentless ↔ native OS update channel (WSUS/WUA, package managers, app updaters)
- control plane: cloud SaaS ↔ on-prem ↔ hybrid
- customer seat: enterprise IT ↔ MSP multi-tenant (managing many client fleets)
- vulnerability-driven prioritization depth (CVE mapping, risk-based ranking, third-party assessment ingestion)
- server vs workstation emphasis; cluster/sequential server patching practices
- self-service portal for end users
- integrations: ITSM/change records, vulnerability scanners, SIEM
- adjacent bundled capabilities (software deployment, configuration enforcement, remote control) — suite drift zone

### L3 — Vendor-specific (research notes only)

- ConfigMgr: software update point; WSUS as sync source; deployment packages + content library; software update groups; automatic deployment rules; compliance states (Required/Not Required/Installed/Unknown); scan TTL cache; maintenance windows; write-filter handling; System Center Updates Publisher for custom catalogs; 7-day reevaluation default.
- Automox: Worklets; Policy Catalog templates; Turnkey Results; Patch AI; Splashtop remote control; vendor-installer sourcing model with per-title updater delegation (Office Click-to-Run / Microsoft AutoUpdate); communication-app active-call deferral; patch-age filters; Ignored state.
- ManageEngine: Patch Tuesday split scheduling; pre/post deployment activity sequences (WoL, custom scripts, dependency files); reboot policy options (force/delay/postpone with configurable intervals; macOS fixed defaults); rbthist.json reboot attribution; test-and-approve; Endpoint Central suite position; DMZ/closed-network mode.
- Red Hat Satellite: subscription-content distribution; signature verification of synced content; lifecycle curation across Dev/QA/Prod (content views); precision patching without system-wide upgrades; containerized packaging (6.20 LA program); MCP/AI automation preview.
- Ivanti: agentless assessment/deployment; CVE-to-patch list creation from any vendor's assessment; application allowlisting + privilege management bundling; offline VM/template patching.

## Historical / Market-Sample Check (§24)

- **WSUS/SUS generation (2003–2010s)**: synchronize update metadata from Microsoft Update → approve updates → target computer groups → clients scan/report via the native Windows Update Agent → compliance reports. Satisfies all four L0 legs with no cloud, no third-party app patching, no agents beyond the OS-native one, no CVE prioritization. The Type predates every modern convenience in the sample.
- **Early-2000s third-party patch scanners** (Shavlik/PatchLink lineage — Ivanti's own patch lineage): scan for missing OS + application patches against a vendor-maintained catalog, deploy, report. Satisfies the legs; establishes that third-party scope is a variant, not the definition.
- **Manual predecessor**: administrator reads vendor bulletins (the catalog), checks machines against them (assessment), distributes hotfixes via shared folders/login scripts after testing (controlled deployment), tracks state in a spreadsheet (compliance record). The loop is the Type; software is the amplifier.
- **Platform-native / regional**: WSUS (Windows-native), Red Hat Satellite / SUSE Manager / Landscape (subscription-content Linux), Apple-native update mechanisms — all fit the four legs without Windows-specific or cloud-specific machinery.
- Conclusion: L0 holds across eras and platforms. No era machinery (cloud, agents, third-party catalogs, CVE scoring, AI) enters the definition.

## Vendor-specific Findings

See L3. None promoted to the canonical model.

## Rejected Findings

- **"Patch management = software deployment"** — rejected. Deployment machinery is shared with Application Deployment Management, but the catalog + currency assessment + recurring update stream are the patch-specific addition; and deployment management's arbitrary-package generality (install new software) exceeds patch scope. Both Types stand.
- **"Third-party application patching is definitional"** — rejected. WSUS-era and platform/subscription-scoped products (Satellite) satisfy the Type with OS-only content. Scope is the variant axis.
- **"Agents are definitional"** — rejected. Ivanti documents agentless assessment/deployment; WSUS uses the OS-native channel.
- **"CVE/risk-based prioritization is definitional"** — rejected. Absent in the WSUS generation; present as variant depth in modern products.
- **"Patch management includes vulnerability scanning"** — rejected as identity. Missing-update assessment is against the *update catalog*, not an exposure/risk model; CVE context is metadata layered on updates. The vulnerability picture belongs to Vulnerability Management (flag for that pass).
- **"Reboot orchestration is definitional"** — rejected as a separate leg; it is the dominant realization of "restart handling" inside controlled deployment, but Linux-subscription content often needs no restart, and the WSUS generation handled restarts more simply. Held inside L0 leg 4 as "restart handling", not as its own invariant.
- **"Compliance dashboards are definitional"** — rejected; the per-machine/per-update state record is definitional (leg 3/4), the reporting rollup is L1.

## Boundary Findings

1. **vs Application Deployment Management** (processed 2026-09-06) — RATIFIED keep-both from this side. Shared machinery: managed endpoint population, content, targeting, execution policy, per-device outcomes. Seam: ADM installs/uninstalls *operator-chosen software* (any package content, one-shot or managed distribution); patch management keeps *already-installed software current* against a continuously refreshed vendor catalog, with currency assessment and a recurring update stream as the defining additions. Drift zone documented: patch tools also deploy software (Automox "deploy required software"; Endpoint Central suite) and deployment tools also patch (SCCM software updates is literally inside a deployment platform). The test: remove catalog+assessment → ADM-shaped distributor; remove arbitrary-package generality → pure patch tool.
2. **vs Endpoint Management / UEM** (processed 2026-09-08) — RATIFIED from this side, exactly as that pass flagged: update/patch machinery is a module inside UEM (Intune Windows updates; Endpoint Central suite relationship). Remove patching → still UEM (config/policy/lifecycle); remove config/compliance/lifecycle → patch tool. UEM's management channel can be the patch tool's delivery channel; the objects differ (device configuration & security posture vs update currency).
3. **vs Remote Monitoring & Management** (UNPROCESSED) — counterparty duty discharged from this side: RMM is monitoring/maintenance-first, MSP-oriented over client fleets; patching is one maintenance action inside RMM (alongside monitoring, alerting, remote access, scripting). Dedicated patch tools add catalog depth, approval/test machinery, and compliance evidence; RMM adds the monitoring/operations layer. Proposed seam for the RMM pass: monitoring+maintenance-first vs update-currency-first. Patch module inside RMM = the same module pattern as UEM.
4. **vs Vulnerability Management** (§15, UNPROCESSED) — flag recorded: VM owns the risk picture (find, prioritize, track vulnerabilities/exposures); patch management owns remediation execution (update mechanics against a catalog). Modern convergence: patch tools attach CVE metadata and ingest scanner findings (Ivanti CVE-to-patch from "any vendor"; ManageEngine integrates Tenable/Rapid7; Satellite ranks CVEs); VM tools increasingly embed patching. Keep-both expected; the seam is risk-picture vs update-execution.
5. **vs IT Change Management** (processed 2026-09-08) — RATIFIED from this side: patch tooling *executes* a recurring, pre-approved change class at fleet scale; change management *governs* modifications (assess→authorize→schedule→review per change). Patch rides the standard/pre-approved change path; integration = patch deployments recorded as changes (ManageEngine ↔ ServiceDesk Plus integration observed). Governance-vs-execution seam holds.
6. **vs Configuration Management** (processed 2026-09-07) — consistent with that pass's framing: configuration management enforces *authored desired state* (declarations converge nodes to a declared end-state); patch management distributes *vendor-produced updates* to maintain currency. Content source differs (authored declarations vs upstream vendor catalogs); goal differs (conformance vs currency). Drift zone: Satellite does both (configuration assessment + patching); some patch tools express "baselines".
7. **vs Infrastructure Automation Platform** (processed 2026-09-08) — consistent: generic governed automation content vs patch-domain machinery. A patch policy resembles automation content, but carries update-specific semantics (catalog currency, applicability, approval, restart) that generic automation lacks.
8. **vs Endpoint Protection Platform** (processed) — RATIFIED from this side: EPP's own intelligence/signature updates are internal to that Type; security suites that patch OS/third-party apps carry a patch-management-shaped module (Ivanti Security Controls is exactly this pattern).
9. **vs Server Management Platform** (UNPROCESSED) — flag: server management = broader server operations (provisioning, monitoring, configuration, patching as slices). Satellite straddles (provisioning + patching + config) — suite drift zone, same pattern as UEM/Endpoint Central.
10. **vs ITSM** — patch compliance and deployments feed service/change records; ITSM owns the service/request machinery. Integration seam only.
11. **vs Backup Management** — no recovery-point custody in patch management; pre-patch snapshots appear as operator practices (custom scripts), not as the Type's object.
12. **Pure update mirror** (downstream replica of an update source with no management layer) = catalog leg alone → not the Type.

## Uncertainties

- **Satellite operational depth**: docs 403; lifecycle-curation mechanics (content views), errata applicability semantics, and restart behavior for RHEL updates are unverified at operational tier. Satellite claims held at product-page tier.
- **MSP-tier patch machinery** (NinjaOne/Atera/Kaseya class): unverified this pass (fetch failures). The MSP multi-tenant variant is carried from the UEM pass's counterparty context, not from direct evidence. The RMM pass should verify.
- **Apple-native patch management** (Kandji/Jamf patch definitions): not fetched; the Apple pole is inferred from market structure, not sampled.
- **Firmware/BIOS patching depth**: observed as a capability claim (ManageEngine Enterprise edition); operational mechanics unverified.
- **Exact compliance-state vocabularies** vary by product (ConfigMgr's four states are documented; others observed only as "missing/installed" language) — canonical states written conceptually, not as a standard.
- **Windows Update for Business / Intune update-ring machinery**: not fetched this pass (ConfigMgr doc used as the platform-native anchor); the cloud-native Microsoft pole remains unverified in detail. Low risk to L0 (WSUS-generation already anchors the platform-native pattern).

## Final Synthesis

Patch Management is the IT operations application whose defining core is four jointly-held structures: a managed machine population; an update catalog synchronized from upstream vendor/update sources; currency assessment of each machine against that catalog (what is missing, installed, not applicable); and controlled update deployment under operator policy with recorded per-machine outcomes. The recurring operational rhythm — new updates arrive, the population is re-assessed, approved updates are deployed within windows, compliance is re-measured — is the Type's reason to exist: keeping installed software current and provably so.

Everything else is layered on top: approval/test machinery, restart orchestration, content distribution, third-party scope, CVE context, compliance reporting, cloud or MSP delivery. The Type is packaged today as standalone dedicated products, as modules inside UEM/RMM/security suites, as platform-native consoles, and as Linux subscription-content managers — the packaging varies, the four-leg core does not.
