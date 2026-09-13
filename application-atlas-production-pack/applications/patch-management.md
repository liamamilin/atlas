# Patch Management

## Overview

A **Patch Management application** is the IT operations system for keeping the software on a managed population of machines current. It maintains a catalog of available software updates, assesses each machine against that catalog to determine what is missing, installs approved updates under operator-defined controls, and records the outcome per machine.

Its purpose is to close — continuously and verifiably — the gap between the software a vendor has released and the software each machine is actually running. Unpatched machines are the standing exposure behind most software-exploit incidents, so the work is recurring by nature: vendors release updates, the population is re-assessed, approved updates are deployed within controlled windows, and compliance is re-measured.

The boundary of the Type: patch management is not general software distribution (installing new software), not device configuration and policy administration, not vulnerability analysis, and not change governance. Modern products frequently bundle adjacent pieces of all four, but the update-currency loop is the defining center.

## Users & Context

The primary user is an **IT operations administrator** — endpoint administrator, systems administrator, or the IT team member who owns the organization's update posture. Their recurring work: watch for new updates, decide what gets approved, keep deployment policies aligned with business hours, chase machines that fall out of compliance, and produce evidence that the estate is current.

Secondary participants:

- **security teams** — set the urgency rules (which severities must be deployed within which timeframes) and consume compliance reporting
- **service desk / end users** — experience the visible edge of patching: notifications, postponed reboots, forced restarts
- **change managers** — treat patch deployments as a governed, typically pre-approved change class
- **managed service providers** — run patching across many client fleets from one console

The working context is a **recurring operational rhythm**: monthly cycles aligned to the major vendors' release schedules, maintenance windows that avoid business hours, and audit regimes that require demonstrable patch compliance rather than good intentions.

## Core Model

### The Defining Core

Four structures exist together; remove any one and the product stops being a patch management system:

```text
Update catalog
(synchronized from vendor / update sources)
        ↕ assessed against
Managed machine population
(joined via agent, native update channel, or agentless discovery)
        ↕ produces
Per-machine currency state
(missing / installed / not applicable / unknown)
        ↕ drives
Controlled update deployment
(approved updates × targeted machines × policy) → recorded outcomes
```

- **Managed machine population** — the computers under management (workstations, laptops, servers), each an individually addressable record. Machines join the population through a installed agent, through the operating system's native update channel pointed at the system, or through agentless network discovery. Machines are organized into groups (by site, role, platform, criticality) that deployment targets.

- **Update catalog** — the system's maintained knowledge of what updates exist: operating-system updates and, in most modern products, third-party application updates. The catalog is refreshed by synchronization from upstream sources — the OS vendor's update service, individual software vendors, or the tool vendor's own aggregation feed — and each entry carries metadata: what it updates, its severity, whether a restart is required, which platforms it applies to.

- **Currency assessment** — the scan. Each machine's installed software state is compared against the catalog, producing per-machine, per-update state. Conceptually the states are: **missing** (applicable and not installed), **installed**, **not applicable**, and **unknown / not yet reported** (the machine has not successfully reported). This state is the system's central record — the answer to "what is out of date, where".

- **Controlled update deployment** — approved updates are installed on targeted machines under operator-defined policy: when (schedules, deployment windows, deadlines), how (download staging, installation, restart handling), and with what user experience (notification, postponement, forced restart). Outcomes are recorded back per machine, updating the currency state.

The four legs are mutually dependent. A catalog with no population is an update mirror. A population with no catalog is a remote-execution fleet. Assessment without deployment is a scanner that fixes nothing. Deployment without assessment is blind software distribution. The joint holding is what makes the Type.

### Standard Capabilities

Mature products commonly add the following. They make patching practical; they do not change what the Type is.

- **Approval workflow** — updates found by the catalog do not deploy until approved; products commonly support test groups or pilot rings that receive updates before broad deployment, and declining updates that would break legacy software.
- **Deployment policies** — named, reusable policies binding update selection to target groups, schedules, deployment windows, and restart rules. Recurring automation ("deploy matching updates as they arrive") is the normal steady state; manual selection is used for baselines and emergencies.
- **Restart orchestration** — pending-restart tracking, user notification with postponement options, forced restarts after deadlines, and skip-restart-when-not-required behavior.
- **Compliance reporting** — per-machine and rolled-up views of patch state, historical trends, and audit-ready evidence.
- **Content staging** — updates downloaded once from the upstream source and distributed internally (distribution servers/points, relays), so machines pull from the local network rather than the internet.
- **Severity and CVE context** — vulnerability identifiers and severity ratings attached to updates, so deployment urgency can be risk-driven.
- **Rollback and decline** — removing a faulty update or excluding an update from deployment permanently.
- **Offline operation** — importing catalogs and content into closed networks (air-gapped or DMZ environments).
- **Role-based access** — restricting who can modify approvals, policies, and deployment configuration.

### One Structure, Many Implementations

The core model is conceptual; products realize each piece differently:

```text
Concept:            Machine acquisition
Implementations:    installed agent, OS-native update channel, agentless scan

Concept:            Catalog source
Implementations:    OS vendor update service, per-vendor feeds, tool vendor's aggregation feed, subscription content service

Concept:            Deployment control
Implementations:    manual selection, criteria-driven automatic rules, policy templates

Concept:            Currency state
Implementations:    agent-reported state messages, scan results, package-manager queries
```

A reader who has only seen one implementation — say, a cloud agent console — should still be able to recognize an on-premises server-based or subscription-content product from the core model alone.

## How It Works

The operational loop has six steps that repeat for the life of the deployment:

### 1. Bring machines under management

```text
Install the agent (or point the native update channel at the system, or discover machines agentlessly)
→ machine appears as a managed record
→ assign it to groups
→ it begins reporting its installed software state
```

### 2. Synchronize the update catalog

```text
Connect to upstream update sources (on a schedule or on demand)
→ new update metadata enters the catalog
→ content is staged internally for later distribution
```

Without fresh synchronization the catalog goes stale and the system stops seeing new updates — catalog currency is a maintenance obligation, not a one-time setup.

### 3. Assess the population

```text
Each machine scans its installed state against the catalog
→ per-machine, per-update state recorded (missing / installed / not applicable / unknown)
→ dashboards and reports show the compliance picture
```

Assessment and deployment are separate steps: knowing an update is missing does not deploy it. A machine can be fully assessed and still receive nothing until a deployment targets it.

### 4. Select and approve

```text
Choose updates (manually, or by criteria such as severity and release date)
→ optionally test on a pilot group
→ approve for deployment (or decline)
```

### 5. Deploy under policy

```text
Deployment policy fires (schedule / window / new-update trigger)
→ machines in the target group download the staged content
→ missing updates install
→ restarts handled per policy (immediate, deferred to a reboot window, or offered to the user with postponement and a forced deadline)
→ outcome recorded per machine
```

Deployment windows are the main instrument for reconciling security urgency with business continuity: installation and restarts happen inside defined time frames; incomplete deployments continue in the next window.

### 6. Record, report, repeat

```text
Outcomes update the currency state
→ compliance reports roll up per machine, per group, per update
→ new updates arrive from vendors → the loop begins again
```

### The exception paths that shape real operations

- **The machine that misses its window** — powered off, asleep, or off-network; it stays non-compliant until it next checks in, which is why products differ on whether patching requires corporate-network connectivity.
- **The update that requires a restart the business cannot afford now** — the pending-restart state exists precisely because an installed-but-unrestarted update is not yet a fixed machine.
- **The update that breaks something** — hence test groups, decline, and rollback.
- **The zero-day with no patch** — severity context flags the exposure; remediation may require configuration changes beyond the update catalog.
- **The end user who postpones forever** — hence forced deadlines after configurable postponement.

## Interfaces

The surfaces below are described conceptually; exact layouts and names vary by product.

### Machine inventory with patch state

The operator's ground truth.

- lists every managed machine with its group, platform, and patch compliance state
- typical information: missing-update count, last scan/check-in time, pending restarts
- primary actions: drill into a machine's missing updates, run a scan on demand, add to a target group

### Update catalog view

The system's knowledge of what exists.

- lists available updates with platform, severity, release date, restart requirement, and how many machines need each
- primary actions: inspect an update's details, approve/decline, add to an update group

### Approval workbench

Where update decisions are made.

- pending updates awaiting decision, test-group assignments, approval history
- primary actions: approve, decline, assign to test group, promote from test to production

### Deployment policy editor

The control surface for how and when updates install.

- schedule (weekly/monthly patterns, often aligned to vendor release days), deployment windows, target groups, update selection criteria
- pre- and post-deployment actions (wake machines, run scripts, notifications) in products with deeper policy machinery
- restart rules: immediate, deferred to a reboot window, or user-postponable with a forced deadline
- primary actions: create/edit/enable/disable policies

### Compliance dashboard and reports

The evidence surface.

- rolled-up compliance percentages, per-machine and per-update breakdowns, trends over time, exportable audit reports
- primary actions: filter, export, schedule report delivery

### End-user notification surface

The visible edge on the managed machine.

- patch-in-progress notices, reboot prompts with postponement options, countdown before forced restart

### Settings

Update-source configuration (which upstream sources, proxies, credentials), content-staging topology, notification channels, role assignments.

## Important Rules / Behaviors

- **Assessment drives deployment.** Only updates found missing on a machine are installed on it; already-installed updates are not re-installed. Periodic re-evaluation re-checks previously deployed updates and repairs drift (for example, if an update was rolled back locally).
- **Approval gates deployment.** An update present in the catalog and missing on a machine still installs nothing until it is approved and a deployment targets that machine. Scanning refreshes knowledge; deployment policy causes action.
- **An update completes at restart.** Many operating-system updates leave the machine in a pending-restart state until then; compliance accounting treats the machine as not fully current until the restart happens. This makes restart orchestration a first-class concern rather than a cosmetic option.
- **Windows constrain when, not whether.** Deployment and reboot windows defer work; they do not cancel it — incomplete deployments resume in the next window, and forced deadlines eventually override user postponement.
- **Catalog currency decays.** Synchronization is a standing obligation; a stale catalog silently hides new updates.
- **Reachability matters.** A machine that is off, asleep, or unreachable during its window stays non-compliant until it next communicates; products differ on whether that requires the corporate network or any internet connection.
- **Compliance is measured, not assumed.** The per-machine state record — and the reports built on it — is the audit artifact. Regulated organizations run patch management as much for this evidence as for the remediation itself.
- **Content must reach the machine.** Staging and distribution machinery exists because downloading every update from the internet on every machine, at patch time, does not scale; closed networks require explicit catalog/content import.

## Variants

Common shapes the Type takes in the market:

- **Platform-native enterprise console** — update management built on the operating system vendor's own update infrastructure, typically inside a broader systems-management platform; deep Windows-estate machinery (staged content, maintenance windows, criteria-driven automatic deployment).
- **Cloud-native dedicated product** — a lightweight agent plus a cloud console; patching works wherever the machine has internet access, with third-party application catalogs as a headline capability.
- **Standalone dedicated product (on-premises or cloud)** — a purpose-built patch product sold on its own, and commonly also packaged as the patching component of a broader endpoint-management suite.
- **Suite module** — patch management embedded in endpoint-management (UEM), remote-monitoring (RMM), or security suites; the module shares the suite's agent and console.
- **Linux subscription-content manager** — the OS vendor's own content-distribution and update system for its enterprise Linux estate, with repository curation across development/test/production stages and signature-verified content.
- **Security-suite patch management** — patching bundled with vulnerability scanning and application control, often for data-center servers, sometimes agentless.
- **MSP multi-tenant** — patch management operated across many client organizations from one console.

Content scope is a variant axis, not an identity marker: OS-only products, OS-plus-third-party products, and products extending to drivers, BIOS, and firmware all occur. The same holds for acquisition mode (agent, native channel, agentless) and control plane (cloud, on-premises, hybrid).

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Application Deployment Management | sibling, shared machinery | installs/uninstalls operator-chosen software on endpoints (any package content); patch management keeps already-installed software current against a continuously refreshed vendor catalog — the catalog, currency assessment, and recurring update stream are the patch-specific additions |
| Endpoint Management / UEM | broader device administration | owns device configuration, security policy, and the device lifecycle; update/patch machinery appears as a module inside it; remove patching and it is still UEM, remove configuration/policy/lifecycle and it is a patch tool |
| Remote Monitoring & Management (RMM) | adjacent, MSP-oriented | monitoring/maintenance-first tooling over client fleets; patching is one maintenance action among monitoring, alerting, and remote access; dedicated patch products add catalog depth, approval machinery, and compliance evidence |
| Vulnerability Management | complementary, security-side | owns the risk picture — finding, prioritizing, and tracking vulnerabilities; patch management owns remediation execution; modern products converge (CVE metadata on updates, scanner integrations, patch modules in VM tools) but the centers differ |
| IT Change Management | governance counterpart | governs modifications per change (assess → authorize → schedule → review); patch deployments are a recurring, typically pre-approved change class that patch tooling executes at fleet scale |
| Configuration Management | different content source | enforces authored desired-state declarations on nodes; patch management distributes vendor-produced updates to maintain currency — conformance vs currency |
| Infrastructure Automation Platform | generic vs domain | runs arbitrary governed automation against infrastructure; patch policies carry update-specific semantics (catalog currency, applicability, approval, restart) that generic automation lacks |
| Endpoint Protection Platform | adjacent module | EPP updates its own protection intelligence internally; security suites that patch operating systems and third-party applications carry a patch-management-shaped module |
| Server Management Platform | broader umbrella | server operations including provisioning, monitoring, and configuration; patching is one slice; products covering both are suite drift, not identity |
| IT Service Management | integration seam | patch deployments and compliance feed change and service records; ITSM owns the service/request machinery itself |

The two most consequential seams: with **Application Deployment Management** (same population/target/outcome machinery, different content semantics — chosen packages vs catalog-driven currency) and with **UEM** (the update slice of device administration vs the whole). Both are keep-both boundaries; the market sells the pieces separately and bundled.

## Representative Products

- **Microsoft Configuration Manager (software updates)** — platform-native enterprise pole; update management built on the OS vendor's update infrastructure
- **Automox** — cloud-native dedicated pole; agent + cloud console, third-party catalog breadth
- **ManageEngine Patch Manager Plus** — standalone dedicated pole (also packaged inside the Endpoint Central suite); on-premises and cloud editions
- **Red Hat Satellite** — Linux subscription-content pole; repository curation and signature-verified update distribution for enterprise Linux estates
- **Ivanti Security Controls** — security-suite pole; data-center patch management with agentless assessment and CVE-to-patch mapping

## Sources

Research date: **2026-09-09**

- Microsoft Learn — "Introduction to software updates - Configuration Manager" — https://learn.microsoft.com/en-us/mem/configmgr/sum/understand/software-updates-introduction
- Automox — platform overview — https://www.automox.com/platform ; how it works — https://www.automox.com/how-it-works
- Automox Help Center — index — https://help.automox.com/hc/en-us ; "Policy Catalog Overview and Usage" — https://help.automox.com/hc/en-us/articles/46712227910420-Policy-Catalog-Overview-and-Usage ; "How Automox Sources and Updates Third-Party Applications" — https://help.automox.com/hc/en-us/articles/51637368237076-How-Automox-Sources-and-Updates-Third-Party-Applications
- ManageEngine — Patch Manager Plus — https://www.manageengine.com/patch-management/ ; help documents — https://www.manageengine.com/patch-management/help/ ; "Patch Management Workflow & Setup" — https://www.manageengine.com/patch-management/help/patch-management-workflow.html ; "Deployment Policies" — https://www.manageengine.com/patch-management/help/deployment-policies.html
- Red Hat — Satellite product page — https://www.redhat.com/en/technologies/management/satellite
- Ivanti — Security Controls patch management — https://www.ivanti.com/products/patch-management

> Sourcing limitations: Red Hat's operational documentation was not reachable from the research environment (access denied); Satellite observations rest on the vendor's product page and no Satellite-specific operational parameters are asserted. NinjaOne (the MSP-tier pole) was unreachable after repeated attempts and was dropped from the sample; the MSP variant is described from market structure, not from direct product evidence. Precise numeric limits, default schedules, and state-name vocabularies are deliberately not standardized in this document; where a concrete mechanism is described, it is attributed to the product whose documentation demonstrates it.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample check are recorded in the paired Research Notes.
