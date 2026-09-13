# Research Notes — Endpoint Management / UEM

## Research Goal

Understand what "Endpoint Management / UEM" is as an Application Type: what objects exist inside such a product (devices, profiles, policies, compliance state, apps, actions), who operates it, how a device moves through management from enrollment to retirement, and where the boundaries lie against the neighboring Types in §14 (Patch Management, RMM, Application Deployment Management, Desktop & Application Delivery, DEX, IT Asset Management, Configuration Management, SaaS Management) and §15 (EDR, Mobile Threat Defense, browser security), plus already-processed counterparties (IAM, CMDB, classroom management, cyber asset management, device testing, backup management, remote customer support).

## Initial Boundary

Preliminary hypothesis (pre-research): an organization-side administration application whose primary object is the endpoint device; IT administrators enroll devices, define and apply configuration/security policy, keep software current, evaluate compliance, and retire devices. Nearest confusions: RMM (MSP monitoring), Patch Management (updates slice), Application Deployment Management (software distribution slice), IT Asset Management (asset records), EDR (threat detection on the same devices), DEX (experience telemetry on the same devices).

Naming note: the directory leaf joins two lineage names — "Endpoint Management" (PC/desktop lifecycle management lineage: SCCM, Landesk, ZENworks) and "UEM" (mobile MDM/EMM lineage that expanded to all endpoints: AirWatch/Workspace ONE, MobileIron). Research should confirm whether these are one Type or two.

## Research Questions

1. What are the core objects: device records, users, groups, profiles/policies, compliance rules, apps, actions?
2. How does a device enter management (enrollment flows: user-initiated, automated/zero-touch, staging)? What is installed/established at enrollment?
3. How is configuration administered (profiles, baselines, settings catalogs)? How are policies targeted (device groups, user groups, smart/dynamic groups)?
4. What is compliance evaluation, and what happens on noncompliance (remediation, quarantine, conditional access, remote lock/retire)?
5. How does software/app delivery and update/patch management work inside UEM vs the standalone Application Deployment Management Type?
6. What remote actions exist (lock, wipe, retire, restart, query), and what are the exact semantics of corporate vs personal ownership (BYOD)?
7. What inventory/monitoring does UEM hold, and where does it stop (vs ITAM, vs DEX, vs RMM)?
8. What interfaces exist (admin console, user-facing portal, on-device agent, API)?
9. What is the management substrate (OS-native management frameworks vs vendor agents)?
10. Where do the boundaries run vs each neighbor, including counterparty flags from prior passes (DEX, browser security, application deployment management, configuration management, device testing, classroom management)?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Philosophy / tier | Evidence tier |
|---|---|---|
| Microsoft Intune | cloud-native endpoint management from the platform/identity giant; enterprise; deep Windows + mobile | Tier-1 (Microsoft Learn, 4 pages fetched) |
| Omnissa Workspace ONE UEM | classic cross-platform UEM suite (AirWatch heritage); large enterprise; SaaS + on-prem | Tier-1 (Omnissa docs, 3 pages fetched) |
| Jamf Pro | Apple-only specialist; business + education | Tier-2 (jamf.com product page); Tier-1 docs JS-gated |
| ManageEngine Endpoint Central | value-tier unified endpoint management & security; SMB/mid-market; on-prem + cloud | Tier-1 (ManageEngine help, 2 pages fetched) |

## Sources

- Microsoft Learn — What is Microsoft Intune: https://learn.microsoft.com/en-us/mem/intune/fundamentals/what-is-intune (fetched 2026-09-08)
- Microsoft Learn — Device compliance policies in Intune: https://learn.microsoft.com/en-us/mem/intune/protect/device-compliance-get-started (fetched 2026-09-08)
- Microsoft Learn — Device features and settings (configuration profiles): https://learn.microsoft.com/en-us/mem/intune/configuration/device-profiles (fetched 2026-09-08)
- Microsoft Learn — Enroll devices in Intune: https://learn.microsoft.com/en-us/mem/intune/fundamentals/deployment-guide-enrollment (fetched 2026-09-08)
- Microsoft Learn — Wipe devices with Intune: https://learn.microsoft.com/en-us/mem/intune/remote-actions/devices-wipe (fetched 2026-09-08)
- Omnissa Docs — Workspace ONE UEM category: https://docs.omnissa.com/category/WorkspaceONEUEM (fetched 2026-09-08)
- Omnissa Docs — Managing Devices with Workspace ONE UEM: https://docs.omnissa.com/WorkspaceONE-UEM-Managing-Devices-VSaaS/AWT-MANAGINGDEVICESOVERVIEW (fetched 2026-09-08)
- Omnissa Docs — Device Actions: https://docs.omnissa.com/WorkspaceONE-UEM-Managing-Devices-VSaaS/DeviceActionDescriptions (fetched 2026-09-08)
- Jamf — Jamf Pro product page: https://www.jamf.com/products/jamf-pro/ (fetched 2026-09-08)
- ManageEngine — Endpoint Central help index: https://www.manageengine.com/products/desktop-central/help/ (fetched 2026-09-08)
- ManageEngine — What is Endpoint Central: https://www.manageengine.com/products/desktop-central/help/introduction/what-is-desktop-central.html (fetched 2026-09-08)

Source-access limitations:
- learn.jamf.com (Jamf Tier-1 documentation hub) is a JavaScript application; two fetch attempts (root + deep link) returned only the app splash. docs.jamf.com legacy path 404'd once. Jamf evidence is therefore product-page level (Tier-2); Jamf-specific operational details are NOT asserted in the final document beyond what the product page states.
- Historical products (SCCM/ConfigMgr, ZENworks, Landesk, classic MDM) were not fetched this pass; the historical check uses the fetched products' own references to that lineage (Intune co-management with Configuration Manager; ManageEngine's "Endpoint Central vs SCCM" positioning) plus general lineage knowledge, kept at low precision.

## Product A — Microsoft Intune

### Key observations (evidence layer A unless noted)

- Self-description: "a cloud-based endpoint management service that secures and manages your organization's devices and apps. Use Intune to enroll, configure, secure, and update devices, deploy and protect apps, and control which users and devices can access organization resources." Platforms: Android, iOS/iPadOS, Linux, macOS, tvOS, visionOS, Windows. Cloud-only service; web-based admin center; every console action backed by a Graph API call.
- Three pillars: identities (Entra ID), devices, apps. "Intune doesn't store user identities or perform authentication" — identity lives in the IdP; Entra security groups are "the foundation for assigning policies, profiles, and apps"; compliance state flows to Entra Conditional Access which gates access based on device posture.
- Two management modes: MDM (whole device enrolled — via Company Portal, Windows Autopilot, Apple Automated Device Enrollment, Android Enterprise) and MAM (only work apps and their data managed — typical for BYOD personal devices; selective wipe of org data without touching personal content). Modes can combine.
- Lifecycle framing: "Intune covers the full lifecycle of a managed device and the apps that run on it: enrolling devices, configuring settings, securing endpoints, deploying and protecting apps, and keeping everything up to date."
- Enrollment: enrollment installs an MDM certificate enabling policy enforcement; device must first establish identity in Entra (registration or join). Pre-enrollment configuration: enrollment restrictions (platform restrictions — OS version/manufacturer/ownership; device limit restrictions), device enrollment managers (bulk enrollment accounts), terms-and-conditions policy, MFA requirement, device categories auto-grouping. Per-platform method families: Android Enterprise (personally owned work profile / corporate-owned work profile COPE / fully managed COBO / dedicated COSU / zero-touch), Apple (automated device enrollment via Apple Business/School Manager; Apple Configurator; User Enrollment; BYOD via Company Portal), Windows (Entra join + automatic enrollment; Autopilot user-driven/self-deploying; Group Policy-triggered; bulk provisioning packages; Company Portal), Linux BYOD. Factory-reset-before-enrollment requirements vary by platform/ownership. Co-management with Configuration Manager: split workloads between ConfigMgr and Intune (e.g., compliance + configuration in Intune, app deployment + security policies in ConfigMgr).
- Configuration profiles: settings/features packaged as profiles, assigned ("apply or 'assign' the profile to user groups or device groups"). Two authoring forms: Templates (logical grouping: email, kiosk, VPN, Wi-Fi, certificates, device restrictions, endpoint protection, eSIM, OEMConfig, preference files, shell scripts, update policies, delivery optimization, BIOS/DFCI, education, shared multi-user devices...) and Settings Catalog ("lists all the settings you can configure... similar to configuring on-premises Group Policy Objects, but cloud native"). Custom profiles (OMA-URI, Apple Configurator imports). Profile conflict management and monitoring ("check the status of devices, and the profiles assigned... resolve conflicts by seeing the settings that cause a conflict").
- Compliance policies: "sets of rules and conditions that you use to evaluate the configuration of your managed devices." Two areas: tenant-wide compliance policy settings (mark devices with no policy assigned as compliant/noncompliant; compliance status validity period — devices failing to report within the period are treated as noncompliant) and per-platform device compliance policies (min/max OS version, jailbroken/rooted, encryption, PIN, threat level from integrated threat management). Actions for noncompliance: mark noncompliant (default), send email, remotely lock, retire after a period (retire = remove from management + remove company data; admin must explicitly execute from a marked-for-retirement list). Evaluation depends on device check-in; Windows supports client-driven compliance evaluation. Remediated vs quarantined semantics: some settings are OS-enforced (user forced to set PIN), others are access-gated (device blocked via Conditional Access; Company Portal notifies the user).
- Conditional Access integration: compliance status reported to Entra; Conditional Access can require "device marked as compliant" to grant access to email and other resources.
- Remote actions (wipe page): Wipe = factory reset removing all personal and organizational data, apps, configurations — for retirement, repurposing, troubleshooting, secure erase of lost/stolen devices. Platform-specific options: Windows (wipe keeping enrollment state + user account; wipe-protected continuing despite power loss; plain wipe), macOS (6-digit recovery PIN; obliteration behavior options), ChromeOS (remove user profiles only vs factory reset/powerwash — deprovision first or the device auto-re-enrolls), eSIM/data-plan preservation choices. Governance: RBAC roles (Help Desk Operator; custom role with Remote tasks/Wipe permission), tenant daily action limits, possible Multiple Administrative Approval (second admin must approve). Post-wipe follow-ups: deregister from Autopilot, remove device record from Entra.
- Advanced capabilities (suite drift zone): endpoint security, app management, certificates, remote support, analytics, device updates, secure remote access, specialty-device management; Copilot AI assistant (policy summarization, conflict flagging, triage agents).

## Product B — Omnissa Workspace ONE UEM

### Key observations

- Product family context (docs nav): Workspace ONE UEM is one product beside Intelligent Hub (the agent/app), Assist (remote access/troubleshooting "while respecting end-user privacy"), Mobile Threat Defense, Tunnel, Access, Intelligence, Freestyle Orchestrator for UEM. UEM is the device-management core of a digital-workspace suite.
- Supported endpoints: Android 8+ (Android Enterprise Work Profile BYOD / Fully Managed / COPE; two management methods — Custom DPC using the Intelligent Hub agent, or AMAPI using native Android OS functionality via Google Cloud), iOS/iPadOS, macOS, Windows 10/11 desktop + Windows Server, Chrome OS (via Google Admin console account + Chrome Enterprise/Education upgrade), Linux, plus printers/IoT (Zebra, MQTT-based or connector-based). On-prem (Windows Server + SQL Server) and cloud-hosted deployments.
- Managing Devices guide structure (the UEM console's device-management surface): Device Enrollment (How Do You Enroll; Basic vs Directory Services enrollment; BYOD enrollment; Privacy for BYOD deployments; Self-Enrollment vs Device Staging; enrollment options/restrictions; denylist/allowlist device registrations; device registration; enrollment status), Device Dashboard, Device List View (filtering; add device manually), Device Details, Device Assignments, Device Actions (+ expanded), Device Updates, Device Profiles (profile processing; add/edit; compliance profiles; geofence areas; installation schedules; time windows), Compliance Policies (list view; rules and actions; add; view devices; compromised-device detection with health attestation), Conditional Access (Microsoft Entra ID; Google BeyondCorp), Certificate Management, Wipe Protection, Custom Attributes, Device Tags, Lookup Values.
- End-user surface: Self-Service Portal (SSP) "to enable end users to manage their own devices and reduce the strain on Help Desk personnel."
- Device actions vocabulary (platform-agnostic list, run from console on one or many devices): queries (Apps, Baselines, Books, Certificates, Device Information, Profiles, Security, Query All), Change Device Passcode, Clear Passcode, Delete Device (unenroll + enterprise wipe on next check-in), Device Wipe (iOS data-plan preservation options; Windows Wipe / Wipe Protected ("end user cannot circumvent... keeps trying to reset until successful") / Wipe and Persist Provisioning Data), Cancel Wipe (before the device receives the command), Freeze Mode (temporarily pause resource delivery during troubleshooting), Lost Mode (lock + message on lock screen; request device location; Apple MDM protocol overrides device-side location controls during Lost Mode), Enroll (message unenrolled device users), Enterprise Reset (factory reset keeping enrollment; Windows variant restores "Ready to Work" state reinstalling OS while preserving user data), Enterprise Wipe (unenroll + remove all managed enterprise resources — apps and profiles; re-enrollment required to manage again), Find Device (audible sound), Force BIOS Password Reset / View BIOS Password, Lock Device, Lock SSO, Managed Settings (roaming/hotspot toggles), Provision Now ("ordered installation of files, actions, profiles, and applications into a single product"), Reboot/Warm Boot, Remote Assist/Remote Management/Remote View, Request Device Log (System or Hub logs), Request Device Check-In, Send Message (email/push/SMS), File Manager / Registry Manager / Task Manager (remote inspection surfaces), Start AirPlay, Sync Device, Add/Manage Tags, Change Ownership (Corporate-Dedicated, Corporate-Shared, Employee Owned, Undefined), Change Organization Group, Edit Device (friendly name, asset number, ownership, device group, category).
- Organizational structure: Organization Groups (device home OG; static or dynamic), device tags, custom attributes — the targeting/organization layer.

## Product C — Jamf Pro

### Key observations (Tier-2 product page only — see sourcing limitation)

- Self-description: "Complete Apple device management. Manage and secure Apple devices from anywhere." Apple-only (Mac, iPhone, iPad, Apple TV).
- Management features: zero-touch deployment ("Provision Mac, iPhone, iPad or Apple TV with hands-free zero-touch deployment... including BYOD"); Smart Groups ("dynamic device and user groups"); Blueprints ("manage device settings, commands, app installations, and restrictions across all your Apple devices with Declarative Device Management"); inventory management ("automatically collect hardware, software and security configuration details from your Apple devices").
- Security features: app lifecycle management ("automated and secure app management"); Self Service+ ("users can install apps, update software and maintain their own devices"); compliance benchmarks ("automated configurations that use comprehensive device security baselines based on industry benchmarks"); remote security commands ("manage device settings and configurations, restrict malicious software, and patch all your Apple devices without needing user interaction").
- Integrations: Microsoft (Entra, Power BI, Security Copilot, Sentinel), Google (Workspace, Cloud Identity, Chrome Enterprise), Okta; marketplace.
- Product family split by audience: Jamf Pro (business/higher-ed), Jamf Now (SMB), Jamf School (K-12), Jamf Protect (endpoint security), Jamf Connect (identity), Jamf Safe Internet (content filtering), ZTNA — the suite drift zone.

## Product D — ManageEngine Endpoint Central

### Key observations

- Self-description (help): "Unified Endpoint Management & Security is a tool that helps IT to manage, audit, monitor, and secure your endpoints... The management operations include distributing software and OS, installing patches, collecting asset details, device provisioning, and enforcing security policies." Platforms: Windows, Mac, Linux, Android, iOS, iPadOS, tvOS, ChromeOS. "More than 15 years" in the domain (Desktop Central heritage).
- Module map (help nav): Device Onboarding (per-OS: Windows, Apple, Android, Knox, Chrome, Linux); Management — Asset Management, Remote Troubleshoot, Configurations & Profiles, OS Imaging and Deployment, DEX Manager, Reports, Conditional Access, Certificate Management, Content Management, Integrations, Application Management; Security — Patch Management, Vulnerability Management, Geo-fencing, EDR, BitLocker Management, Browser Security, Application Control, Endpoint Privilege Management, Device Control (USB/peripheral), Endpoint DLP, Network Access Control, Private Access.
- Feature list page: Device Onboarding, Device Provisioning, Risk-based Vulnerability Assessment & Remediation, Real-time Asset Management, Software Provisioning & Application Management, Remote Troubleshooting, OS Imaging & Deployment, Reports, Integrations, BitLocker, USB & Peripheral Device Control, Browser Security, Malware Protection, Application Control, Privilege Management, Endpoint DLP.
- Mobile-side surfaces: MDM for iOS/Android/Windows, MAM, BYOD management, self-service portal, software repository + software installation, patch deployment (Microsoft + third-party), remote desktop sharing, system tools (shutdown/Wake-on-LAN, chat, disk tools, custom scripts), power management.
- Positioning pages: "Endpoint Central vs SCCM", "vs Tanium", "vs Jamf", "vs Ivanti", "vs Intune", "vs Omnissa Workspace ONE", "vs NinjaOne", "vs BigFix" — evidence that the competitive set of this Type spans both the PC-lifecycle lineage (SCCM, BigFix, Ivanti, Tanium) and the UEM lineage (Intune, Workspace ONE, Jamf), plus the MSP RMM lineage (NinjaOne, Atera, Kaseya).
- Suite drift zone: bundles EDR, DLP, privilege management, browser security, vulnerability management — "Unified Endpoint Management & Security" (UEMS) positioning.

## Cross-product Comparison

| Structure | Intune | Workspace ONE UEM | Jamf Pro | Endpoint Central | Evidence |
|---|---|---|---|---|---|
| Managed device population as primary object | yes (Devices; All devices) | yes (Device List View / Dashboard / Details) | yes (Apple device inventory) | yes (computers + mobile devices) | B |
| Enrollment as the entry gate | yes (MDM certificate; Entra identity first; per-platform methods) | yes (enrollment guide section; registration; staging) | yes (zero-touch deployment incl. BYOD) | yes (Device Onboarding per OS) | B |
| Ownership models (corporate vs personal) | yes (corporate-owned vs personal; BYOD; MAM for personal) | yes (Corporate-Dedicated/Shared/Employee Owned; BYOD privacy) | yes (zero-touch incl. BYOD) | yes (BYOD module) | B |
| Configuration profiles/policies targeted via groups | yes (profiles assigned to user/device groups; Entra groups) | yes (profiles; organization groups; tags; custom attributes) | yes (Smart Groups; Blueprints) | yes (Configurations & Profiles; custom groups) | B |
| Compliance evaluation with actions | yes (compliance policies; actions for noncompliance; Conditional Access) | yes (compliance policies; rules and actions; health attestation; Conditional Access Entra/BeyondCorp) | yes (compliance benchmarks — baselines framing) | yes (Conditional Access module; security configs) | B (Jamf weaker: benchmarks framing) |
| Software/app deployment + updates | yes (app deployment; update policies; delivery optimization) | yes (app management; Device Updates; Product Provisioning) | yes (app lifecycle; patching via remote commands) | yes (Software Provisioning; Patch Management) | B |
| Remote actions on devices | yes (wipe/retire/lock/restart/sync/queries; RBAC; MAA) | yes (very broad action vocabulary incl. Lost Mode, Freeze Mode, remote view) | yes (remote security commands) | yes (remote desktop sharing, shutdown/WOL, tools) | B |
| Inventory collection | yes (device records; Endpoint Analytics as advanced) | yes (device details; queries) | yes (hardware/software/security details) | yes (Asset Management module) | B |
| User-facing self-service surface | yes (Company Portal) | yes (Self-Service Portal; Intelligent Hub) | yes (Self Service+) | yes (Self Service Portal) | B |
| Identity delegated to IdP | yes (explicit: Entra; Intune stores no identities) | yes (directory services enrollment; Entra/BeyondCorp conditional access) | yes (Entra/Okta/Google integrations) | yes (AD integration; conditional access) | B |
| OS-native management substrate | yes (MDM certificate; Apple ADE/User Enrollment; Android Enterprise AMAPI/DPC; Windows CSPs referenced) | yes (Custom DPC vs AMAPI; Chrome OS via Google Admin; Apple MDM) | yes (Declarative Device Management; native Apple features) | yes (Knox; per-OS onboarding) | B |
| Platform breadth | 7+ platforms, cloud-only | broadest incl. ChromeOS, Linux, printers/IoT, servers | Apple-only | 8 OS families, on-prem + cloud | B |
| Deployment form | SaaS only | SaaS + on-prem | SaaS (Jamf Cloud) | on-prem + cloud | B |
| Suite position | Microsoft ecosystem (Entra, Defender, Copilot) | digital-workspace suite (Hub, Assist, Tunnel, Access, Intelligence) | Apple security suite (Protect, Connect, Safe Internet) | UEMS security bundle (EDR, DLP, EPM, browser security) | B (variant) |

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant (deliberately small)

An organization-side administration application over endpoint devices, holding three jointly-held structures:

1. **The managed endpoint device population** — the organization's endpoint devices (laptops, desktops, phones, tablets, and in mature products specialized devices) held as identified, individually manageable records that have been brought under management (enrolled/registered). Remove → device inventory / asset registry, not management.
2. **Centrally-defined device configuration and security policy** — settings, restrictions, and security posture defined once by the organization and applied to devices through targeting (groups of devices/users), so the organization — not each device user — governs how devices are configured. Remove → inventory with no policy model (ITAM) or a policy engine with no devices (server-side configuration management / IAM).
3. **The device lifecycle loop executed through a management channel** — onboarding devices into management (enrollment), applying and maintaining their configuration and software over time (profiles, apps, updates, remote actions), and retiring them (unenroll, wipe, repurpose). Remove → policy documents or one-shot installers; the standing administration is gone.

Jointly-held is load-bearing: 1 alone = asset inventory; 2 without 1 = server config management/IAM policy; 3 without 2 = remote-support tooling; 1+2 without 3 = unenforced policy; 1+3 without 2 = bare remote administration (RMM-shaped).

### L1 — Common Mature Structure (not definitional)

- Enrollment machinery variety: user-initiated (portal/app), automated/zero-touch (vendor purchase-program integration), staging/bulk accounts; enrollment restrictions (platform, ownership, device limits); terms-of-use acceptance.
- Ownership model: corporate-owned vs employee-owned (BYOD), with control depth and privacy boundaries varying by ownership; container/work-profile separation on personal devices.
- Targeting layer: device/user groups, dynamic/smart groups, tags, org-group hierarchies.
- Compliance machinery: per-platform rule sets (OS version, encryption, PIN, jailbreak/root, threat level), evaluated on check-in; actions for noncompliance (mark, notify, lock, retire); tenant-wide defaults for unassigned devices.
- Conditional-access integration: compliance state exported to an identity provider / access broker to gate resource access (Entra Conditional Access, Google BeyondCorp).
- Software and update management: app deployment, OS update policies, patching (the Application Deployment Management / Patch Management slices as modules).
- Inventory: hardware/software/security-configuration details collected from devices.
- Remote action vocabulary: lock, wipe (with platform-specific variants), enterprise wipe vs full reset, restart, lost mode, passcode reset, queries (apps/profiles/certs/security), log collection, check-in request, messaging.
- Certificates and resource-access profiles: Wi-Fi, VPN, email, wired networks, SCEP/PKCS certificates.
- Encryption management: FileVault/BitLocker-class disk-encryption administration.
- User-facing surfaces: company portal / self-service portal (enroll, install apps, check compliance, remote-lock a lost device).
- Admin governance: RBAC/delegated admin roles (help-desk operator), approval gates for destructive actions, audit, APIs (every console action mirrored by API in one sampled product).
- Reporting/dashboards over fleet state.

### L2 — Variant / Optional Structure

- Platform specialization: Apple-only specialist vs cross-platform generalist vs platform-native (OS vendor's own console).
- Deployment substrate: cloud-only SaaS vs on-prem servers vs hybrid.
- Suite position: standalone vs module of a security suite (UEMS), digital-workspace suite, or ITSM suite; bundled security modules (EDR, DLP, privilege management, browser security, vulnerability management) are suite drift, not the Type.
- PC-lifecycle pole vs mobile-MDM pole: OS imaging/deployment, heavy patching, remote control (PC lineage) vs profile/restriction/wipe-centric mobile lineage — both inside the Type.
- MAM-only mode: managing work apps/data without device enrollment (BYOD-light); drifts toward app management when it is the only mode.
- Specialized device classes: kiosk/dedicated devices, shared devices, rugged/Zebra devices, printers/IoT, servers (in some products), education shared carts.
- MSP multi-tenancy (provider-managed fleets).
- Geofencing, content/document distribution, per-app VPN/tunneling (suite modules).
- DEX/remote-support add-ons (experience telemetry, remote assist) — adjacent Types bundled.

### L3 — Vendor-specific (research notes only)

- Intune: settings catalog vs templates; Entra co-management workload split with Configuration Manager; Windows Autopilot; device enrollment manager accounts (1,000-device vs 15-device standard limit); 500 wipe actions/day tenant limit; Multiple Administrative Approval; Company Portal; client-driven compliance evaluation; remediated-vs-quarantined per-setting table; Copilot in Intune.
- Workspace ONE UEM: Organization Groups (static/dynamic); Intelligent Hub as agent (Custom DPC) vs AMAPI; Product Provisioning (ordered installs); Freeze Mode; Wipe Protection; Enterprise Reset "Ready to Work"; AirWatch Cloud Messaging; Freestyle Orchestrator; Zebra MQTT printer management.
- Jamf Pro: Blueprints on Declarative Device Management; Self Service+; compliance benchmarks; Smart Groups; Jamf Now/School audience split.
- ManageEngine Endpoint Central: unified-agent argument; OS Imaging & Deployment; DEX Manager; Desktop Central MSP edition; "vs SCCM/Intune/Workspace ONE/Jamf/NinjaOne" battle-card set.

## Historical / Market-Sample Check

Would older, regional, platform-native, or differently positioned products still fit the L0?

- Classic PC lifecycle management (SCCM/ConfigMgr lineage, Landesk/Ivanti, Novell ZENworks, HCL BigFix): agent-enrolled managed PC population + centrally-defined configuration/software policy + lifecycle (deploy, patch, inventory, retire). Fits all three legs; compliance machinery and conditional access are absent in older generations — correctly held at L1, not L0. Intune's own co-management documentation treats ConfigMgr as a peer management authority for the same devices, confirming one Type.
- Classic MDM/EMM (AirWatch-era, MobileIron-era): enrollment + profiles/restrictions + app deployment + wipe. Fits; the "Unified" expansion to desktops is the lineage merge that produced the leaf's joint name.
- Platform-native management (Apple Business/School Manager + MDM; Google Admin console ChromeOS management; Windows MDM): fits — devices enrolled, settings/policies applied, lifecycle administered, using OS-native frameworks as the channel.
- Regional/education variants (Jamf School, K-12 device programs): fit — same core with education-specific enrollment (shared carts, staged devices).
- Conclusion: L0 survives the historical check. The modern additions (compliance engines, conditional access, zero-touch programs, AI assistants) are era-current L1/L2, not definitional.

## Vendor-specific Findings

See L3 above. Also: ManageEngine's "Unified Endpoint Management & Security" naming and ManageEngine's competitive set confirm the market treats PC-lifecycle, UEM, and (partially) RMM products as one competitive arena — supporting one Type with variant poles rather than separate Types.

## Boundary Findings

1. **vs Application Deployment Management (§14, processed — counterparty confirmed from both sides).** ADM is the software-distribution slice: package → assignment → tracked per-device install. UEM adds configuration profiles, compliance, security policy, and the device lifecycle as primary objects; software deployment is one module inside UEM. Remove config/compliance/lifecycle → ADM. Confirmed against application-deployment-management pass's own boundary note.
2. **vs Patch Management (§14, unprocessed — flag for that pass).** Patch management is the vendor-published-update slice. UEM products include update/patch machinery as one module (Intune update policies; Jamf "patch all your Apple devices"; Endpoint Central Patch Management). Remove patching → still UEM; remove configuration/compliance/lifecycle → patch tool.
3. **vs Remote Monitoring & Management / RMM (§14, unprocessed — flag).** Shared endpoint-agent machinery and overlapping action sets (patching, remote control). Proposed seam: RMM is monitoring/maintenance-first and MSP-oriented (client companies' fleets, alerting, scripting); UEM is configuration/policy/lifecycle-first for one organization's endpoints. Endpoint Central's own battle cards (vs NinjaOne/Atera/Kaseya) show the market adjacency. To be confirmed by the RMM pass.
4. **vs Digital Employee Experience Management (§14, processed — counterparty duty DISCHARGED).** DEX pass flagged: "UEM owns device configuration/policy/security state; DEX observes experience and fixes issues but owns no policy — UEM is typically the DEX collector's delivery vehicle; drift zone: compliance/patch machinery inside DEX platforms." This pass CONFIRMS the seam from the UEM side: policy ownership is the UEM discriminator; DEX's compliance/patch machinery is variant capability; UEM consoles themselves now bundle DEX modules (Endpoint Central DEX Manager; Intune Endpoint analytics) — the drift runs both directions but the cores remain distinct.
5. **vs Endpoint Detection & Response (§15, processed).** UEM configures/complies/manages devices; EDR detects/responds to threats on them. Shared agents possible; suites bundle both (Endpoint Central EDR module; Jamf Protect; Intune + Defender). Remove threat detection/response → UEM.
6. **vs Mobile Threat Defense / Endpoint Protection (§15, unprocessed).** Threat-level signals from MTD feed UEM compliance rules (Intune compliance references "threat level as specified by threat management software that integrates with Intune") — integration seam, distinct Types.
7. **vs IT Asset Management (§14, unprocessed — flag).** UEM device records carry asset-like fields (asset number, ownership, purchasing data in one sampled product's device details) and inventory, but the financial/contract/procurement lifecycle is ITAM. Remove financial/contract administration → still UEM; remove operational administration → ITAM.
8. **vs Configuration Management (§14, processed — counterparty confirmed).** Seam is the object model: UEM centers the enrolled device fleet and its lifecycle; configuration management centers declared desired-state on managed nodes regardless of device class. Chef Desktop shows a CfM product can target desktops; UEM's enrollment/ownership/compliance machinery has no CfM analog.
9. **vs Desktop & Application Delivery (§14, processed).** Delivery hosts execution centrally (nothing installed on the endpoint); UEM administers the endpoint itself. Vendors sell both side by side (Workspace ONE UEM + Horizon; Intune + AVD).
10. **vs Identity & Access Management (§14, processed).** Devices are UEM's primary object; identity lives in the IdP (Intune explicitly stores no identities). Device posture flows INTO IAM conditional access as an input signal. Integration seam, distinct Types.
11. **vs CMDB (§14, processed).** CMDB is the maintained record of what exists; UEM enforces what devices should be. UEM inventory can feed CMDB/ITSM.
12. **vs browser-security-platform (§15, processed — counterparty note).** Browser configuration management (settings, updates, extension allowlists) appears inside UEM consoles (Endpoint Central Browser Security module; ChromeOS policy management) and is configuration-level, consistent with the browser-security pass's proposed split (configuration vs session-level protective enforcement). The joint-review flag for a dedicated browser-management leaf remains open; this pass adds the UEM-side observation only.
13. **vs classroom-management (§14, processed — counterparty confirmed).** Teacher-facing live control of students' devices during class vs IT-admin standing policy management of device fleets; vendors ship separate products/consoles for the two jobs.
14. **vs cyber-asset-management (§14, processed).** Action vs knowledge: UEM acts on devices; CAM inventories the estate and checks management/protection coverage (UEM appears in CAM's multi-source ingestion list).
15. **vs device-testing-platform (§12, processed — counterparty confirmed).** Workforce endpoints administered for IT operations vs test-substrate device catalogs for app QA.
16. **vs remote-customer-support-platform (§14, processed).** Per-session consent-gated support connections vs standing administration of an enrolled fleet.
17. **vs backup-management (§14, processed — counterparty confirmed).** Device administration vs recovery-point custody; some endpoint suites bundle laptop backup, which does not make backup definitional to UEM.
18. **vs SaaS Management (§14, unprocessed).** SaaS application subscriptions/usage vs devices. Distinct objects.
19. **Naming/lineage:** "Endpoint Management" (PC lineage) and "UEM" (mobile lineage) are one Type with two lineage names; the market's own competitive sets and self-descriptions (ManageEngine "Unified Endpoint Management & Security"; Intune "endpoint management"; Workspace ONE "UEM") treat them as one arena. No directory change needed.

## Uncertainties

- Jamf operational details (enrollment flows, compliance-rule structure, action semantics) are unverified — Tier-1 docs unreachable (JS-gated). Jamf-specific claims in the final document are limited to product-page statements.
- Whether a settings-only UEM product with NO software/app deployment exists at all: not found in the sample; software/update management is treated as part of the lifecycle leg's maintenance, not as a separately definitional leg, to keep L0 minimal.
- Exact per-platform capability boundaries (what each OS-native framework permits) are broad-stroked from the fetched docs; precise per-OS setting lists not asserted.
- RMM seam is proposed, not confirmed — RMM leaf unprocessed.
- Historical products (SCCM, ZENworks, Landesk) not directly fetched this pass; the historical check relies on the sampled products' own references to that lineage plus low-precision lineage knowledge.

## Final Synthesis

Endpoint Management / UEM is the organization-side administration application for endpoint devices. Its defining core is the jointly-held triad: an enrolled, identified device population as the primary record; centrally-defined configuration and security policy applied to devices through group targeting; and a lifecycle loop (enroll → configure → maintain → retire) executed through the system's management channel to each device. Everything else the market associates with the category — compliance engines, conditional-access integration, zero-touch enrollment programs, app stores/self-service portals, patching, encryption management, remote-control surfaces, bundled security modules, AI assistants — is common mature structure or variant packaging, not the definition. The Type has two lineage poles (PC lifecycle management; mobile MDM/EMM) that the market has already merged, and it sits in a dense integration web: identity (IdP), access (conditional access), threat (EDR/MTD), experience (DEX), assets (ITAM/CMDB), software distribution (ADM), and hosted delivery (Desktop & Application Delivery) are all neighbors, not parts of the definition.
