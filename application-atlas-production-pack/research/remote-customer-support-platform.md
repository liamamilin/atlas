# Research Notes — Remote Customer Support Platform

Research date: 2026-09-07
Slug: remote-customer-support-platform
Directory leaf: Remote Customer Support Platform (§07 Sales, Customer & Revenue)

## Research Goal

Understand what a "Remote Customer Support Platform" actually is as an Application Type: what objects exist inside it, who uses it, how a support interaction is established and carried out, what rules govern it, and where its boundary lies against neighboring Types (remote access tools, RMM, customer support chat, help desk/ticketing, video conferencing, telehealth, privileged remote access).

## Initial Boundary

Working hypothesis before research:

- The leaf most plausibly refers to the market category usually called **remote support software** (also "remote desktop support", "remote assistance"): software that lets a support agent remotely view and control a customer's device over a live connection to diagnose and resolve problems. Canonical market products: TeamViewer, Zoho Assist, GoTo Assist/Rescue, BeyondTrust Remote Support, Splashtop SOS, AnyDesk.
- The alternative reading — "customer support delivered remotely" (remote-agent contact center) — is already covered by neighboring leaves (Contact Center Platform, Cloud Contact Center / CCaaS, Omnichannel Customer Service Platform, Customer Support Chat). Treating the leaf as the contact-center reading would make it a duplicate of those leaves.
- Nearest neighbors to police:
  - Remote Access software (user accesses their own device) — same machinery, different relationship.
  - Remote Monitoring & Management / RMM (§14) — proactive fleet management, no customer participant.
  - Customer Support Chat / Omnichannel Customer Service Platform — conversation-first, no device control.
  - Help Desk / Ticketing System — case management core; remote support plugs in at the session seam.
  - Video Conferencing / screen sharing — meeting-shaped, no unattended access, no support records.
  - Telehealth Platform — remote sessions but clinical objects.
  - Privileged Remote Access / PAM — remote access to internal privileged assets, not external support.

## Research Questions

1. What is the central object — the "session"? How is it established (attended vs unattended)?
2. What can the agent do during a session (view, control, file transfer, chat, voice/video, diagnostics, reboot)?
3. How is consent/authorization handled (customer grant, session codes, unattended credentials, privilege elevation)?
4. What does the agent console contain (active sessions, queues, device inventory, history, reports)?
5. How do sessions become records (logs, recordings, transcripts, ticket integration)?
6. What organizational layer exists (technicians, groups, roles, departments, branding)?
7. How do customers reach the agent (service queues, widgets, invite links, scheduling)?
8. What rules matter (consent, security posture, session termination, access scoping)?
9. Where is the boundary vs remote access, RMM, chat, conferencing, help desk?

## Representative Products

| Product | Pole | Why selected |
|---|---|---|
| Zoho Assist | Cloud remote support + unattended access, SMB/mid, suite member | Deep official product docs; strong attended/unattended split documentation |
| Splashtop (Remote Support SOS / Enterprise) | MSP/IT-team lightweight pole, concurrent licensing | Deep official product page; explicit feature matrix |
| TeamViewer (Remote / Tensor) | Market-defining generalist, consumer→enterprise span | Official use-case page; broadest market recognition |
| BeyondTrust Remote Support | Enterprise security/compliance pole (Bomgar heritage) | Official docs; security-first positioning |

GoTo (Assist/Rescue) was sampled for the support-heritage pole but its web properties returned 403/empty on repeated fetches; abandoned per source-access rules and recorded as a limitation. Four products with usable official evidence were retained.

## Sources

All fetched 2026-09-07.

- Zoho Assist — product page: https://www.zoho.com/assist/ ; instant remote support: https://www.zoho.com/assist/instant-remote-support.html ; unattended access: https://www.zoho.com/assist/unattended-remote-access.html
- Splashtop — Remote Support product page: https://www.splashtop.com/sos (covers SOS and Enterprise plans, feature matrix)
- TeamViewer — root: https://www.teamviewer.com/en-us/ ; Remote support use case: https://www.teamviewer.com/en-us/products/remote/use-cases/remote-support/
- BeyondTrust — docs root: https://docs.beyondtrust.com/bomgar/ ; Remote Support welcome: https://docs.beyondtrust.com/rs/ (and /rs/docs, same content)
- GoTo — https://www.goto.com/assist (403), https://support.goto.com/assist (empty) — abandoned after 2 attempts

Source-access limitation: GoTo's official surfaces were unreachable from the research environment; no GoTo-specific claims are made. BeyondTrust evidence is limited to its docs welcome pages (positioning-level, not operational detail); BeyondTrust-specific operational claims are kept weak. TeamViewer evidence is product/use-case pages (Tier 2), not deep help-center articles; TeamViewer operational details are kept at the level the pages state.

## Product Observations

### Zoho Assist (evidence layer A — direct, official product pages)

- Self-description: "cloud-based remote desktop software" for "remote support and access capabilities"; "secure, web-based, on-demand connections with remote PCs, laptops, mobile devices, and servers".
- Two modes, explicitly named and contrasted in official FAQ:
  - **Remote support (attended/instant)**: on-demand sessions; customer joins by running a lightweight file or via browser (cobrowse); "no prior downloads required" framing for technician side; invite participants via email, SMS, or join links; "Every session requires explicit consent from the customer before the technician connects."
  - **Unattended remote access**: "prior installation of a lightweight agent on the remote computers"; connect "at any time" without user present; bulk deployment (Distributor / start-up script); revoke unattended access permissions; group computers and define which technicians may access which groups.
- In-session capabilities: file transfer (both directions), instant chat, voice and video chat, multi-monitor navigation, reverse screen sharing (technician shares own screen), reboot & reconnect (incl. Windows safe mode), one-click Ctrl+Alt+Del, annotation on remote screen, clipboard sharing with configurable permissions, invite technician (multiple technicians collaborate; control transfer).
- Diagnostic tools (unattended context): Task Manager, Command Prompt, Device Manager, Registry editor, and status views for groups/hardware/printers/services/software/users.
- Consent machinery: attended sessions require explicit customer consent; unattended access offers optional "session confirmation" (customer consents to unattended sessions; customizable timeout and message) framed as a HIPAA-compliance feature.
- Power management: Wake-on-LAN; shutdown/restart/log off/lock/hibernate/standby without opening a desktop session.
- Intake machinery: **service queue** — customers initiate requests through a custom URL or web form, automatically routed to available technicians; schedule sessions with automated reminders; rebranding (logos, portal URLs) and an embeddable customer support widget on the organization's website.
- Records: session recording stored in cloud (training/QA/compliance/audit); reports filterable by date/technician/department, exportable.
- Organization: departments, user management, roles and permissions controlling who can initiate sessions and access unattended devices.
- Adjacent surfaces inside the same product: cobrowse (browser-tab session, no install, field highlighting, sensitive-data masking), remote camera sharing / AR (Zoho Lens — smartphone camera or smart glasses), unified endpoint management (vulnerability detection, patch deployment, compliance), mobile device support (Android/iOS screen share; "full control may vary based on platform restrictions"), Raspberry Pi/IoT support.
- Platforms: Windows, macOS, Linux, iOS, Android, Chrome OS, Raspberry Pi; technician can work from browser or mobile app.
- Security claims: SSL/256-bit AES, MFA, inactive session timeouts.

### Splashtop Remote Support — SOS / Enterprise (evidence layer A — direct, official product page)

- Self-description: "remote support solution that delivers multi-platform support… for IT pros to remotely support any device"; plans: SOS (per concurrent user) and Enterprise.
- **Attended access with session code**: "quick, ad-hoc support to end-users on computers and mobile devices via a session code, without a pre-installed agent."
- **Managed/unattended endpoints**: "remotely control and support managed endpoints with or without an end-user present"; per-license managed-computer counts (10 or 300 per license, scaling to 1,200) — licensing detail, vendor-specific.
- In-session: chat (in-session or outside session), in-session voice call, file transfer (copy-paste and drag-and-drop), session recording, multi-to-multi monitor, share screen via web link, session reboot and reconnect, **elevate to admin** ("elevate the session privilege to admin when accessing a Windows standard user session to interact with UAC, perform admin level operations, and support reboot and reconnect").
- **Background Actions**: "access system tools such as task manager, registry editor, device manager, service manager and remote command without interrupting the end-user."
- Multiple technicians (up to 3) in one support session.
- Organization: user role and access management; user and computer grouping; custom branding of the SOS app.
- Intake (Enterprise): "advanced service desk workflow — technician grouping, service channel management and invite links, support requests via SOS Call and webform widgets, session routing."
- Integrations: PSA ticketing and ITSM — Freshservice, Freshdesk, Zendesk, Spiceworks Help Desk, Jira, Microsoft Teams.
- Enterprise security: SSO, granular access controls, IP whitelisting, 2FA, endpoint MFA, session audit logging, SIEM logging, E2E encryption, cloud session recording.
- Adjacent surfaces: unattended Android access; Augmented Reality add-on (camera sharing + AR annotations for off-site locations); Splashtop Connector add-on (bridge RDP/VNC/SSH without VPN or agent); Autonomous Endpoint Management add-on (real-time patching, monitoring, remediation, inventory); on-prem deployment option; free Vulnerability Insights (CVE/KEV visibility).
- Attended support for iOS and Android devices.

### TeamViewer — Remote / Tensor (evidence layer A for product pages; positioning-level)

- Product family: TeamViewer Remote (personal/SMB: "fast and secure remote access and IT support"), Tensor (enterprise), DEX (endpoint experience), Frontline (industrial AR), ONE (platform bundling). The remote-support use case is a first-class use case of TeamViewer Remote.
- Help and service desk framing: "support users immediately and fully remotely — even without the need for software installation"; monitor devices with alerts; gather real-time device information (IP addresses, OS); detect and patch vulnerabilities.
- Support suite for IT service providers: "central dashboard to monitor, manage, and access all your devices, systems, and services"; custom branding on the client; "automate, distribute, and manage support tickets"; "clear connection logs you can use for invoicing."
- **Remote sessions**: "connect more easily and more securely with remote sessions, without the need of sharing ID and password" — a session-invitation model replacing the classic ID+password exchange.
- Unattended devices: "access and maintain remote point-of-sale (POS) devices, kiosks, digital signage, servers, and all kinds of other unattended devices securely and discretely"; mobile-to-mobile connections; file transfer; alerts from unattended devices.
- Feature highlights: remote device control ("become the primary user"); secure unattended access ("no approval needed — with the right permissions"); device monitoring; scripting in and out of session (Batch/CMD/PowerShell, executable without a session); patch management with policies; **service desk** ("automate inbound support requests, balance workloads, and instantly start remote support sessions").
- Security: connection origin detection (see where incoming connections come from before accepting); end-to-end encryption of all connections; headless device support.
- AI: AI-generated session summaries ("case documentation… full transparency of case-solving steps"), analytics on recurring issues.
- Adjacent: Assist AR add-on; Mobile Device Support add-on (Android control, iOS screen sharing); Remote Management add-on (monitoring, asset & patch management); integrations with ServiceNow, Freshworks, Jira, Salesforce, Zendesk, Intune, Slack, Teams.

### BeyondTrust Remote Support (evidence layer A but shallow — docs welcome pages only)

- Self-description: "a secure, enterprise-grade remote support solution that allows IT professionals to connect to and control remote systems and devices to provide technical support. It is used by IT service desks, help desks, and support teams to troubleshoot and resolve technical issues efficiently."
- Value framing: first-call resolution, reduced downtime, "enhances security by limiting unnecessary access and protecting sensitive data", centralized tools, "effective, secure, and compliant technical support, regardless of location."
- Platform context: Remote Support is one product in BeyondTrust's identity-security platform (alongside Password Safe, Privileged Remote Access, Endpoint Privilege Management); docs emphasize session recording/monitoring/audit ("record, monitor, and audit every privileged session") at platform level, and just-in-time / zero-standing-access principles.
- No operational session mechanics were directly observed from official docs in this pass; all BeyondTrust-specific operational claims are withheld.

## Cross-product Comparison

| Dimension | Zoho Assist | Splashtop SOS | TeamViewer | BeyondTrust RS |
|---|---|---|---|---|
| Agent-side console | Web/browser + mobile app | Desktop/console + web | Desktop client + web client + management console | Enterprise appliance/cloud console (not directly observed) |
| Attended connection | Lightweight run file / browser link; email/SMS/join-link invite | Session code, no pre-installed agent | "Remote sessions" without ID/password exchange | (not directly observed) |
| Unattended connection | Pre-installed agent; bulk deployment; group permissions | Managed endpoints per license; with/without user present | Unattended POS/kiosks/signage/servers; alerts | (not directly observed) |
| Remote view + control | Yes | Yes | Yes | Yes ("connect to and control") |
| Chat / voice / video | Chat + voice + video | Chat + voice call | (chat implied by support suite; not itemized on fetched page) | (not observed) |
| File transfer | Yes | Yes (copy-paste, drag-drop) | Yes | (not observed) |
| Privilege elevation | (implied via diagnostic tools) | Elevate to admin / UAC | (not itemized) | (not observed) |
| Diagnostic tools | Task Manager, CMD, Device Manager, Registry, services/users/printers | Background Actions: task manager, registry, device manager, service manager, remote command | Device info (IP, OS); scripting | (not observed) |
| Reboot & reconnect | Yes (incl. safe mode) | Yes | (not itemized) | (not observed) |
| Consent machinery | Explicit customer consent; optional unattended session confirmation | Session-code acceptance by end user | Connection origin detection; session invitation | "limiting unnecessary access" framing |
| Session records | Recording (cloud), reports by date/technician/department | Session recording; audit logging (Enterprise) | Connection logs (invoicing); AI session summaries | Platform-level session record/audit emphasis |
| Organization layer | Departments, roles/permissions | Roles, user/computer grouping | Teams, branding, ticket automation | Enterprise service desks |
| Intake machinery | Service queue (URL/web form → routing), scheduling, website widget | Service channels, invite links, SOS Call, webform widgets, routing | Service desk (automate inbound requests, balance workloads) | (not observed) |
| Ticketing/ITSM integration | Zoho ecosystem + third-party | Freshservice/Freshdesk/Zendesk/Spiceworks/Jira/Teams | ServiceNow, Freshworks, Jira, Salesforce, Zendesk, Intune | Platform integrations (ServiceNow, Splunk, etc. at docs-root level) |
| Adjacent extensions | Cobrowse, AR (Lens), UEM, mobile support, Raspberry Pi | AR add-on, Connector (RDP/VNC/SSH), AEM add-on, on-prem | Assist AR, MDM, Remote Management, DEX, AI summaries | PAM/identity platform adjacency |
| Customer tier | SMB→enterprise, free tier | IT teams/MSP, concurrent licensing | Consumer→enterprise | Enterprise/security-focused |

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

A Remote Customer Support Platform is recognizable only if all of the following hold:

1. **Support-side operator** — a support agent/technician works from their own console, distinct from the device being helped. Without a support operator role, the product is a personal remote-access tool, not support.
2. **Customer device as remote endpoint** — the object of work is a device owned/operated by the supported party (external customer or internal end user). Without a remote endpoint, it is a chat or help desk.
3. **Live remote connection into that device** — a real-time connection that gives the agent at minimum **visibility of the device's screen**, and as the standard capability **interactive control**. Without live device visibility/control, it is conversation-first support (chat), not remote support.
4. **Support purpose** — the connection exists to diagnose and resolve a problem on that device (per-incident or standing access for support/maintenance). Without the support purpose, the same machinery is generic remote access.

Historical check: pre-cloud and platform-native tools (VNC-based support, Windows Remote Assistance-style invitation files, early appliance-based enterprise support) satisfy this core without vendor cloud relays, session codes, browser join, or unattended fleets — so none of those belong in L0. The minimal core is: support operator + live connection into a customer device + screen visibility/control + support purpose.

### L1 — Common Mature Structure

Present across the researched sample (multiple products each):

- **Two connection modes**: attended (on-demand, customer present, joins via code/link/lightweight run file) and unattended (pre-installed agent on the device, no user required). All four sampled products implement both (BeyondTrust's unattended mechanics not directly observed, but its platform context implies managed access; treat unattended-at-BeyondTrust as unverified).
- **In-session collaboration**: chat; file transfer; voice (and in some products video) call inside the session.
- **Remote control affordances**: multi-monitor navigation, clipboard sharing, annotation on the remote screen, reverse screen sharing (agent shares own screen for guidance).
- **Privilege handling**: elevation to admin / interaction with OS privilege prompts (UAC) during a session.
- **Diagnostic tooling without full desktop takeover**: task manager, command prompt, registry editor, device/service managers, system information.
- **Session continuity mechanics**: reboot & reconnect; remote power actions; Wake-on-LAN.
- **Session records**: connection logs, session recording, reports (filterable by technician/date), used for QA, compliance, billing/invoicing.
- **Organization layer**: technicians as managed users; grouping (of technicians and of devices); roles/permissions scoping who can access what; departments/teams.
- **Intake machinery**: service queues / channels routing customer requests to available technicians; invite links; scheduling; embeddable website widgets.
- **Ticketing/ITSM/PSA integration**: sessions launched from or attached to tickets (Freshdesk/Zendesk/ServiceNow/Jira/Teams family).
- **Custom branding** of the customer-facing join experience.
- **Multi-technician collaboration** in one session (invite/transfer).
- **Mobile device support** (screen share on iOS/Android; control where the platform allows).

### L2 — Variant / Optional Structure

- **AR camera assistance** ("see what I see" for field service/industrial equipment) — Zoho Lens, Splashtop AR add-on, TeamViewer Assist AR/Frontline.
- **Cobrowse** (browser-tab-scoped session, no install, field masking) — Zoho; adjacent to customer-engagement tooling.
- **Endpoint monitoring / patch management** (RMM-adjacent add-ons) — Splashtop AEM, TeamViewer Remote Management/DEX, Zoho UEM.
- **Scripting/automation** in and out of session — TeamViewer (Batch/CMD/PowerShell), Splashtop Background Actions overlap.
- **Connector bridging** (RDP/VNC/SSH without VPN) — Splashtop Connector.
- **Deployment posture**: cloud SaaS vs on-prem (Splashtop on-prem; BeyondTrust appliance heritage) vs self-hosted gateway.
- **Compliance posture**: HIPAA-oriented session confirmation (Zoho), SIEM logging/IP whitelisting/SSO/MFA (Splashtop Enterprise), FedRAMP context (BeyondTrust platform).
- **Device-class breadth**: headless servers, POS, kiosks, digital signage, IoT/Raspberry Pi, Android unattended control.
- **AI assistance**: session summaries, support-pattern analytics (TeamViewer; era-common elsewhere).
- **Connection-security extras**: connection origin detection (TeamViewer), session invitation without credential exchange.

### L3 — Vendor-specific (kept out of the final document)

- Zoho: service-queue custom URL mechanics; session-confirmation timeout customization; Raspberry Pi/ARM support; free-plan device counts; Zoho Lens branding.
- Splashtop: SOS naming; 10/300/1,200 managed-computer license tiers; up-to-3-technicians limit; SOS Call; Splashtop Connector; Autonomous Endpoint Management naming; concurrent-user licensing.
- TeamViewer: Tensor/DEX/Frontline/ONE product family; connection logs for invoicing; "Tia" AI agent; Azure Marketplace distribution.
- BeyondTrust: Pathfinder platform framing; Password Safe/PRA/EPM sibling products; zero-standing-access/Entitle cross-sell.

## Vendor-specific Findings

See L3. Additionally:

- Licensing models differ sharply (concurrent user vs named technician vs device counts) — commercial, not structural.
- The "remote sessions without ID/password" model (TeamViewer) vs "session code" (Splashtop) vs "email/SMS/join link" (Zoho) are three implementations of the same concept: a per-session connection invitation that does not require exchanging standing credentials.

## Boundary Findings

- **vs Remote Access Application** (user accessing their own device): identical connection machinery; the difference is the relationship. If the operator and the device owner are the same person and there is no support interaction, it is remote access, not remote support. Several vendors sell both from the same platform (TeamViewer Remote "remote access" vs "remote support"; Splashtop Remote Access vs Remote Support licenses) — evidence that the market itself treats them as distinct products on shared machinery.
- **vs RMM (§14)**: RMM is proactive monitoring/management of a fleet of managed endpoints with no customer participant in the loop; remote support is reactive, per-incident, with a supported party. Convergence is real (Splashtop AEM, TeamViewer DEX/Remote Management, Zoho UEM are add-ons to remote support products), but the session-with-a-customer remains the remote-support core. Remove the live support session and keep fleet monitoring → RMM.
- **vs Customer Support Chat / Omnichannel Customer Service Platform**: conversation-first; no device visibility or control. Remote support products embed chat as an in-session tool; chat platforms do not embed device control. Remove device control → chat.
- **vs Help Desk / Ticketing System**: case management is the core there; remote support contributes the session capability and integrates at the ticket seam. Remove the live device session → help desk.
- **vs Video Conferencing / screen sharing**: meeting-shaped, scheduled, no unattended access, no support records/consent machinery, no endpoint control. Remove support semantics and unattended access → conferencing.
- **vs Co-browsing**: browser-tab-scoped, no device control; appears as a variant surface inside remote support products (Zoho) and as a separate customer-engagement category elsewhere.
- **vs Telehealth Platform**: remote live sessions, but the object is clinical care with its own regulatory frame, not device troubleshooting.
- **vs Privileged Remote Access / PAM**: remote access into internal privileged assets by vendors/admins; the "customer" is an internal asset, access is policy/vault-governed. BeyondTrust sells both (RS and PRA) as separate products — market evidence the boundary is real.
- **"去掉什么就变成另一个 Type" 判据**: remove the support relationship → remote access tool; remove the live device connection → help desk/chat; remove the customer participant (proactive fleet) → RMM; remove device control, keep conversation → support chat.

## Uncertainties

- GoTo (Assist/Rescue) could not be fetched; the support-heritage pole (PIN codes, session queues, agent desktop) is represented only by inference from market knowledge, which is **not** used for any claim in the final document.
- BeyondTrust operational session mechanics (customer client presentation, session keys, unattended Jump-style access) were not directly observed; all BeyondTrust-specific mechanics are withheld from the final document.
- TeamViewer evidence is use-case/product pages rather than deep help-center articles; in-session tool lists for TeamViewer are not itemized at the same depth as Zoho/Splashtop.
- Whether "view-only without control" exists as a first-class mode in all products was not verified per-product; the final document states visibility as the minimum and control as the standard capability, which is consistent with all observed material.
- Exact consent UX per product (what the customer sees/accepts) varies and was only partially documented (Zoho explicit; Splashtop session-code acceptance implied; TeamViewer origin detection + invitation).

## Final Synthesis

The Type is a **support-delivery platform organized around live remote sessions into customer devices**. Its world model:

```text
Support organization (technicians, groups, roles)
        │  operates
        ▼
Agent console ── establishes ──► Support session (live)
        │                              │ into
        │                              ▼
Intake machinery                 Customer device (endpoint)
(service queue / widget /               │
 invite link / schedule)          view + control + in-session tools
        │                              │
        └────── ties to ──────── Ticket / case (external)
                                       │ produces
                                       ▼
                          Session record (log / recording / report)
```

Two connection modes (attended with a present user; unattended via pre-installed agent) are the standard mature shape. Consent and privilege handling are the defining behavioral rules. Everything else — AR, cobrowse, monitoring/patching, AI summaries — is extension surface that must not leak into the definition.
