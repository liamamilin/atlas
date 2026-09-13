# Research Notes — Mobile Threat Defense

## Research Goal

Understand what "Mobile Threat Defense" (MTD) is as an Application Type: what objects exist inside such a product (protected devices, threat findings, risk states, policies, remediation actions), who operates it, how protection flows from deployment through detection to response, and where its boundaries lie against neighboring Types — especially Endpoint Protection Platform / EDR (same job class, different estate), Endpoint Management / UEM (consumes MTD risk signals), Email/Browser Security (phishing overlap), Malware Analysis Sandbox (app analysis overlap), and consumer mobile-security apps (detection core without organizational context).

## Initial Boundary

Working hypothesis before research:

- MTD = security products that continuously assess mobile devices (smartphones/tablets, iOS/Android) for mobile-specific threats: malicious/risky apps, device compromise (rooting/jailbreaking, OS vulnerabilities), network attacks (man-in-the-middle, rogue networks), and mobile-targeted phishing ("mishing").
- Detection happens on-device (agent/SDK) and/or in a backend analysis service; output is a per-device risk state.
- The organizational consumption loop — risk level → compliance/conditional access → blocked resource access until remediation — is the dominant deployment pattern, but may be common-mature rather than definitional.
- Closest neighbors: EPP/EDR (estate difference), UEM (job difference: manage vs assess), consumer mobile AV (audience difference).

## Research Questions

1. What threat categories do MTD products cover (apps / device-integrity / network / phishing)? Are all four definitional or market-common?
2. How does detection work: on-device engine vs cloud analysis vs gateway? What telemetry is captured?
3. What is the core object model: device, threat finding, risk level/score, policy, remediation?
4. How is the result consumed by the organization: admin console, UEM compliance, conditional access, SIEM/SOAR? Is this integration model definitional or common?
5. What does the end user see and do (app, alerts, remediation guidance)?
6. What are the deployment variants (BYOD vs corporate-owned, enrolled vs unenrolled, agent vs SDK/agentless)?
7. What distinguishes MTD from EPP/EDR, UEM, per-channel phishing tools, and consumer mobile AV — with "remove what → becomes another Type" judgments?

## Representative Products

Selected for market representation, documentation quality, product-philosophy spread, and customer-level spread:

| Product | Pole | Evidence actually obtained |
|---|---|---|
| Zimperium Mobile Threat Defense | independent specialist, on-device detection engine, public sector | vendor product page (Tier 2) + Intune connector doc (Tier 1) |
| Jamf Protect | UEM-company endpoint security, Apple-first, ZTNA enforcement | vendor product page (Tier 2) |
| Check Point Harmony Mobile (Mobile Security) | large security-suite vendor, workspace bundling | vendor product page (Tier 2) |
| Lookout Mobile Endpoint ("Lookout for Work") | independent specialist, cloud-intelligence heritage | Intune connector doc (Tier 1) |
| Pradeo Security | independent specialist, on-device analysis heritage | Intune connector doc (Tier 1) |

Plus one integration-platform source (Microsoft Intune MTD overview) that documents the standard consumption model and enumerates the MTD partner market.

## Sources

### Successfully fetched (2026-09-08)

- Zimperium — "Mobile Threat Defense" product page — https://zimperium.com/mtd/mobile-threat-defense (Tier 2)
- Jamf — "Jamf Protect" product page — https://www.jamf.com/products/jamf-protect/ (Tier 2)
- Check Point — "Mobile Security Services" (Harmony Mobile) product page — https://www.checkpoint.com/harmony/mobile-security/ (Tier 2)
- Microsoft — "Mobile Threat Defense with Microsoft Intune" — https://learn.microsoft.com/en-us/intune/device-security/mobile-threat-defense/overview (Tier 1)
- Microsoft — "Zimperium MTD connector with Microsoft Intune" — https://learn.microsoft.com/en-us/intune/device-security/mobile-threat-defense/zimperium (Tier 1)
- Microsoft — "Lookout Mobile Endpoint with Microsoft Intune" — https://learn.microsoft.com/en-us/intune/device-security/mobile-threat-defense/lookout (Tier 1)
- Microsoft — "Pradeo Mobile Threat Defense connector and Microsoft Intune" — https://learn.microsoft.com/en-us/intune/device-security/mobile-threat-defense/pradeo (Tier 1)

### Source-access limitations

- https://www.lookout.com (product pages), https://support.lookout.com and https://docs.lookout.com — unreachable from research environment (403 / transport errors, 2 attempts each). Lookout observations rely on the Intune connector documentation instead; assertions about Lookout-specific detection technology, console details, and product tiers are NOT verifiable from primary sources and are kept correspondingly weak.
- https://www.pradeo.net / pradeo.com — unreachable (transport errors, 2 attempts). Same degradation: Pradeo observations rely on the Intune connector doc; Pradeo's own engine architecture (its known on-device analysis heritage) is NOT asserted from primary evidence.
- https://docs.zimperium.com — unreachable (transport error). Zimperium detail comes from its product page + Intune connector doc only.
- https://learn.microsoft.com/en-us/defender-endpoint/android — 404 (path changed); Microsoft Defender for Endpoint mobile product docs not fetched. Defender's existence as an MTD provider is evidenced via the Intune partner list only.
- Model memory was NOT used to fill precise product details (engine names, limits, version minimums) for unreachable sources.

## Product Observations

### Zimperium Mobile Threat Defense (vendor product page, Tier 2; + Intune connector doc, Tier 1)

Evidence layer A unless noted.

- Positioning: "robust mobile security for enterprises, safeguarding both corporate and personal devices … while ensuring privacy"; protection "even when the device is not connected to your network" (offline on-device protection).
- Four threat surfaces named: Device ("visibility into risk and vulnerabilities"), Network ("detect unsafe and rogue networks"), Apps ("assesses security, permissions, compliance, and malware risks for enterprise and personal apps"), Mishing ("detect and mitigates mobile-targeting phishing attacks").
- Named capabilities: Advanced App Vetting (risky/unauthorized behaviors vs enterprise policy), Device Integrity Checks ("detects jailbreaks, rooting, and other compromises before granting access to corporate resources"), Forensic Scanning (user-triggered checks "after connecting to unknown networks or traveling to high-risk areas"), AI-driven detection including zero-day malware.
- Differentiators claimed: On-Device Dynamic Detection Engine (behavioral + AI, works offline); configurable end-user alerts ("alerts the end-user for selective threats to take action"); zero-touch deployment; cloud/on-premises/air-gapped/FedRAMP deployment; integration "with leading MDM, EMM, UEM, SIEM, SOAR, and XDR platforms, delivering scalable mobile threat visibility and risk insights"; Android, iOS, ChromeOS coverage; BYOD privacy-first design ("sensitive data remains on the device" per quoted user review — vendor-quoted, weaker).
- Intune doc (Tier 1): "The Zimperium app … captures file system, network stack, device, and application telemetry where available, then sends the telemetry data to the Zimperium cloud service to assess the device's risk for mobile threats." Supports enrolled devices (compliance rule → block Exchange Online/SharePoint Online; "Users also receive guidance from the Zimperium app … to resolve the issue and regain access") and unenrolled devices (app protection policy → block or selective wipe). Scenarios: malicious apps → block email/OneDrive/company apps; man-in-the-middle → block Wi-Fi/SharePoint; access granted on remediation. Note: Zimperium supports Intune Certificate Sync.

### Jamf Protect (vendor product page, Tier 2)

- Positioning: "Mac and mobile endpoint protection" — macOS, iOS, visionOS; Apple-native frameworks.
- Dedicated "Mobile threat defense" section: "Keep devices healthy. Block access if they aren't. Mobile threat defense automates responses to risky apps or behavior."
- Mobile capabilities named: Application controls ("block applications that are too risky or don't meet regulatory requirements"), Jailbreak detection ("identifies at-risk devices and enforces ZTNA policies to prevent them from accessing sensitive work resources"), App risk monitoring ("apps with dangerous permissions, malicious code patterns, risky behaviors or suspicious developer profiles").
- Web protections (shared mobile/Mac surface): content control/filtering, privacy on public Wi-Fi ("prevents attackers from intercepting internet traffic"), threat protection against "phishing, ransomware, cryptojacking, malware domains and Command and Control server traffic".
- Organizational loop: "Risk signaling — alerts for out of compliance Macs, with a risk score based on security data to inform zero trust access decisions"; on-device behavioral analysis ("detects and notifies faster than cloud-based analysis"), threat blocking/quarantine; SIEM integrations (Splunk, Microsoft Sentinel, Google SecOps, Sumo Logic) and SOAR; backed by Jamf Threat Labs research.
- Note: Jamf Protect spans Mac + mobile; the MTD-relevant slice is mobile (iOS). The product's MTD section is embedded in a broader endpoint-security product of a UEM vendor — bundling-pole evidence.

### Check Point Harmony Mobile / Mobile Security (vendor product page, Tier 2)

- Positioning: "A market-leading mobile threat defense solution"; "securing employees' mobile devices across all attack vectors: apps, files, network and OS"; "protects devices without impacting user experience or privacy"; "seamlessly fits into existing mobile environments".
- Threat responses named: "blocks malicious app and file downloads" (malware and phishing), "Prevents Man-in-the-Middle attacks", "Blocks infected devices from accessing corporate assets and resources", "Recognizes and blocks advanced jailbreaking and rooting techniques", "Detects OS vulnerabilities (CVE) and misinformation".
- Three protection areas: App and File Protection (real-time detection/blocking of malicious downloads), Network Protection ("On-device Network Protection — extends industry-leading network security technologies to mobile devices"), OS and Device Protection ("real-time risk assessments detecting attacks, vulnerabilities (CVE) management, configuration changes or weak security settings, and advanced rooting and jailbreaking").
- Management claims: "Scalable and easy-to-manage security for any type of mobile workforce"; part of Harmony workspace suite (beside Email & Collaboration, Endpoint, Browse, SaaS).

### Lookout Mobile Endpoint / Lookout for Work (Intune connector doc, Tier 1 only)

- "Lookout's mobile app, Lookout for Work, is installed and run on mobile devices. This app captures file system, network stack, and device and application telemetry where available, then sends it to the Lookout cloud service to assess the device's risk for mobile threats."
- Risk inputs named: "Operating system vulnerabilities, Malicious apps installed, Malicious network profiles."
- "You can change risk level classifications for threats in the Lookout console to suit your requirements." — direct Tier-1 evidence of an admin console with adjustable threat→risk-level classification.
- Same enrolled/unenrolled consumption model and the same four sample scenarios (malicious apps → block email/OneDrive/company apps; MITM → block Wi-Fi/SharePoint; access granted on remediation) as Zimperium/Pradeo.
- Limitation: everything beyond this (cloud intelligence engine detail, consumer heritage, product tiers) is NOT verified from primary sources in this pass.

### Pradeo Security (Intune connector doc, Tier 1 only)

- "Pradeo app for Android and iOS/iPadOS captures file system, network stack, device, and application telemetry where available, and then sends the telemetry data to the Pradeo cloud service to assess the device's risk for mobile threats."
- Compliance rule → "users are blocked access to corporate resources like Exchange Online and SharePoint Online. Users also receive guidance from the Pradeo app … to resolve the issue and regain access."
- **Variant evidence**: "This Mobile Threat Defense vendor is not supported for unenrolled devices." — unenrolled-device (MAM) support is NOT universal across MTD partners.
- Same sample scenarios (malicious apps, MITM/Wi-Fi, SharePoint, remediation restores access).
- Limitation: Pradeo's own detection architecture not verified from primary sources in this pass.

### Microsoft Intune as MTD consumption platform (overview page, Tier 1) — evidence layer B for the market pattern

- "Intune can integrate data from a Mobile Threat Defense (MTD) vendor as an information source for device compliance policies and device Conditional Access rules … by blocking access from compromised mobile devices."
- The canonical loop, stated plainly: "a connected MTD app reports … that a phone on your network is currently connected to a network that is vulnerable to man-in-the-middle attacks. This information is categorized to an appropriate risk level of low, medium, or high. This risk level is then compared with the risk level allowances you set in Intune. Based on this comparison, you can revoke access to certain resources while the device is compromised."
- Works for enrolled devices (compliance) AND unenrolled devices (app protection policies → block or selective wipe of corporate data).
- Connector machinery: connector states (Unavailable / Not Set Up / Available / Enabled / Unresponsive / Error) with message-blocking consequences; opt-in App Sync (app inventory metadata: App ID, version, name, store source, managed status…) and Certificate Sync (supported partners listed); Android "MTD role" granting the MTD app "exemptions from app suspension, hibernation, power restrictions, and user controls" to "maintain continuous threat protection"; one-vendor-per-platform-per-tenant recommendation (multiple vendors per platform force all devices to run every configured app).
- Partner list (16 MTD connectors): Better Mobile, BlackBerry Protect Mobile, Check Point Harmony Mobile, CrowdStrike Falcon for Mobile, iVerify Enterprise, Jamf Mobile Threat Defense, Lookout for Work, Microsoft Defender for Endpoint, Pradeo, SentinelOne, Sophos Mobile, Symantec Endpoint Protection Mobile, Trellix Mobile Security, Trend Micro Mobile Security as a Service, Trustd Mobile, Zimperium — Android/iOS for all; Defender also Windows. This is Tier-1 confirmation of the market's shape: independent specialists + EDR/endpoint vendors + UEM vendors all sell into one integration-standard category.

## Cross-product Comparison

| Dimension | Zimperium | Jamf Protect | Check Point Harmony Mobile | Lookout | Pradeo |
|---|---|---|---|---|---|
| Mobile threat assessment (apps) | yes — app vetting incl. personal apps | yes — app risk monitoring, block risky apps | yes — malicious app download blocking | yes — "malicious apps installed" | yes — telemetry incl. application |
| Device integrity / OS | yes — jailbreak/root detection | yes — jailbreak detection → ZTNA enforcement | yes — "advanced jailbreaking and rooting", CVE detection | yes — "operating system vulnerabilities" | yes — device telemetry |
| Network threats | yes — unsafe/rogue networks | yes — traffic interception prevention, C2 | yes — MITM prevention, on-device network protection | yes — "malicious network profiles" | yes — network stack telemetry, MITM scenarios |
| Phishing / web | yes — "mishing" | yes — phishing/web threat protection | yes — phishing blocking | not stated in fetched source | not stated in fetched source |
| Telemetry → backend risk assessment | file system, network stack, device, app telemetry → cloud service | on-device behavioral analysis + cloud/telemetry | real-time risk assessments, on-device network protection | same telemetry list → cloud service | same telemetry list → cloud service |
| Per-device risk output | risk insights; levels via connector | risk score; risk signaling | real-time risk assessments | risk level classifications (admin-adjustable) | risk assessment |
| User-visible response | configurable end-user alerts; forensic scan app | app blocking; ZTNA enforcement | blocks downloads/devices; UX preserved | in-app remediation guidance | in-app remediation guidance |
| Organizational access enforcement | via MDM/EMM/UEM integration | native (own UEM + ZTNA) | "blocks infected devices from accessing corporate assets" | via Intune compliance/conditional access | via Intune compliance |
| Admin console | yes (integration emphasis) | yes (part of Jamf platform) | yes (suite management) | yes (classification adjustment documented) | yes (implied; connector doc) |
| Unenrolled-device (MAM) support | yes | not stated | not stated | yes | **no (explicit)** |
| Offline protection claim | yes ("even offline") | yes ("faster than cloud-based") | yes (on-device network protection) | not stated in fetched source | not stated in fetched source |
| Suite/bundling posture | independent (MAPS app-security sibling) | UEM vendor's endpoint-security product | workspace-security suite module | independent (not verified) | independent (not verified) |
| Platform breadth | Android, iOS, ChromeOS | macOS, iOS, visionOS | mobile workforce (Android/iOS implied; not explicit in fetched text) | Android, iOS | Android, iOS |

Convergent findings (evidence layer B — cross-product):

1. Every sampled product continuously assesses mobile devices across the same three base vectors — installed apps, device/OS integrity, network context — plus web/phishing in the products whose sources state it.
2. Every sampled product reduces findings to a per-device risk state (level or score) that others (admins, access systems) consume.
3. Every sampled product has a protective response story: user alerts/remediation guidance, on-device blocking/cleanup, and/or blocking of corporate access from infected devices.
4. The organizational integration pattern (MTD app + connector + compliance/conditional access + block-until-remediated) is documented identically for Zimperium, Lookout, and Pradeo in the same Tier-1 source and claimed by Jamf and Check Point on their own pages.
5. The end-user side is always an app on the device that receives alerts and remediation guidance ("Users also receive guidance from the … app … to resolve the issue and regain access").
6. Privacy posture is a stated design concern in every fetched source ("without impacting user experience or privacy" — Check Point; "ensuring privacy" — Zimperium; BYOD emphasis — Zimperium/Intune app-protection model).
7. Deployment is zero-touch/UEM-distributed where stated (Zimperium zero-touch; Intune "Add MTD apps to devices").

## Abstraction Hierarchy

### L0 — Defining Invariant

The Type holds when all three structures are jointly present:

1. **Continuous mobile-platform-scoped threat assessment of identified devices.** The system evaluates protected mobile devices — their installed app population, device/OS integrity state, and network context — against mobile-specific threats and compromise, continuously rather than on-demand only. The subject is the mobile device in its users' hands, identified per user/device. Remove the mobile-platform scoping → full-estate endpoint security (EPP/EDR); remove the threat assessment → device management (UEM).
2. **Per-device risk state as the unit of record.** Findings are reduced to an assessable device-level risk posture (level, score, or finding set) that persists, updates as conditions change, and can be compared against policy thresholds. Remove → raw telemetry feed or per-file verdicts with no assessable device posture (mobile threat detection/research telemetry, not Defense).
3. **Protective response loop.** Assessment drives action: alerts with remediation guidance to the user, on-device blocking/cleanup, and/or enforcement that bars the risky device from corporate resources until remediation restores its state. Remove → passive monitoring or a scanning utility; the "defense" is gone.

Jointly-held load-bearing analysis:

- 1 without 2 = mobile telemetry capture (sensor, not defense product)
- 1 without 3 = detection/reporting only ("Mobile Threat Detection", a marketing-real partial product)
- 2 without 1 = compliance checklist with nothing detected
- 3 without 1+2 = generic access policy with no threat basis
- 1+2 without 3 = research/visibility feed (SIEM-source posture)
- 2+3 without 1 = enforcement keyed to nothing mobile-specific

### L1 — Common Mature Structure

Very common in current products, not required to recognize the Type:

- Admin web console: device inventory with risk states, threat/event lists, policy configuration, investigation views; vendor consoles may allow admin adjustment of threat→risk-level classifications (Lookout — Tier 1).
- UEM/MDM integration as the standard distribution and consumption channel: app pushed via UEM; risk level mapped to a compliance rule; compliance feeds conditional access; block → remediate → restore pattern (Intune Tier 1 across three vendors; Jamf/Check Point claims).
- Phishing / mobile-web threat coverage ("mishing") as a fourth vector alongside apps/device/network (Zimperium, Jamf, Check Point; not stated in fetched Lookout/Pradeo sources — treat as common, not definitional).
- SIEM/SOAR/XDR telemetry export and integrations (Zimperium, Jamf).
- End-user app with security status, alerts, remediation guidance, and on-demand scanning/forensic checks (Zimperium forensic scanning; guidance wording is Tier-1 standard).
- BYOD privacy engineering: minimal personal-data collection claims, configurable privacy settings, corporate/personal app distinction (Zimperium, Check Point, Intune opt-in App Sync).
- Zero-touch deployment and continuous-protection platform accommodations (Android MTD role exemptions — Intune Tier 1).
- On-demand/offline protection claims (on-device engines work without connectivity).

### L2 — Variant / Optional Structure

- Detection substrate: on-device dynamic/behavioral engine (Zimperium, Jamf claims) vs cloud intelligence analysis (Lookout, Pradeo, Zimperium all also send telemetry to cloud) vs network-gateway heritage — most products are hybrids; the substrate is not definitional.
- Scope of the vendor's product: standalone MTD specialist vs MTD inside EDR (CrowdStrike, SentinelOne, Defender, Trellix per Intune partner list) vs MTD inside UEM bundle (Sophos Mobile, Jamf) vs workspace-security suite module (Check Point Harmony) — bundling is market structure, not Type structure.
- Protection scope: enrolled-device compliance only (Pradeo's connector doc) vs enrolled + unenrolled app-protection protection (Zimperium, Lookout, Defender).
- Agent app vs SDK/agentless embedding into protected apps (market-known; only partially evidenced here — treat as variant).
- Deployment shape: SaaS cloud vs on-premises vs air-gapped (Zimperium claims all three).
- Platform breadth: iOS/Android base; ChromeOS extension (Zimperium); macOS coexistence in endpoint products (Jamf).
- Audience lineage: independent specialists with consumer-security heritage vs enterprise-native entrants; consumer/individual mobile-security apps share the detection core but lack organizational operation (see Boundary Findings).
- Sector packaging: government/FedRAMP-class environments, education (Zimperium, Jamf industry pages).

### L3 — Vendor-specific (Research Notes only)

- Zimperium: "On-Device Dynamic Detection Engine" branding; zIPS/z3r0day engine naming (not verified this pass); ChromeOS MTD positioning; FedRAMP/air-gapped deployment claims; MAPS sibling product line for app shielding.
- Jamf: Threat Labs research backing; "risk score … to inform zero trust access decisions" phrasing; Apple endpoint-security API usage; SOAR integration claims; Computing Security Awards marketing.
- Check Point: "On-device Network Protection" branding; ThreatCloud AI lineage; Harmony workspace packaging; "detects … misinformation" claim (single-source).
- Lookout: "Lookout for Work" app name; "Mobile Endpoint Security/Mobile Endpoint" product naming; admin-adjustable threat classification (Tier 1); legacy consumer heritage (NOT verified this pass).
- Pradeo: agentless/SDK positioning (NOT verified this pass); no unenrolled-device support in Intune connector (Tier 1).
- Microsoft: connector state machine, App Sync/Certificate Sync inventories, Android MTD role toggles, one-vendor-per-platform rule — platform-side machinery, not part of the MTD Type itself.
- Intune risk levels "low, medium, or high" — the three-level scheme is the connector standard; numeric scoring (e.g., Jamf "risk score") is vendor-specific; do not generalize a single scale.

## Rejected Findings

- "On-device AI/ML detection" as definitional — rejected: several sampled products route assessment through cloud services (Lookout, Pradeo per Tier-1 wording); hybrid is normal. The invariant is the assessment loop, not where the engine sits.
- "The four-vector model (apps/device/network/phishing)" as definitional — rejected: phishing coverage is not evidenced in the fetched Lookout/Pradeo sources; three vectors are universal in evidence, the fourth is current-market common. Keep phishing as common-mature.
- "UEM integration / conditional-access enforcement" as definitional — rejected with care: it is the dominant consumption pattern, but it is an integration posture (connector to an external manager) rather than the Type's internal structure; Jamf enforces natively via its own stack; consumer-pole products lack it entirely. Held as common-mature standard consumption.
- "Numeric risk score" as definitional — rejected: connector standard uses levels; scores are vendor-specific.
- "Agent app on every device" as definitional — partially rejected: agent is the standard realization; SDK/agentless embedding is a claimed variant (weakly evidenced this pass) and Intune's app-protection model protects unenrolled devices through the app anyway. Agent is common-mature realization of the assessment leg, not the leg itself.
- "MTD = mobile antivirus" — rejected: file/AV verdicts alone do not produce a device-level risk posture or network/device/phishing coverage; the mobile AV utility is a historical partial form (see Historical Check).
- "Protection of corporate resources via the vendor's own ZTNA/VPN" as definitional — rejected: Jamf-specific enforcement posture; conditional-access pattern is the general shape.

## Boundary Findings

| Neighbor | Relationship | Distinction | Remove-what judgment |
|---|---|---|---|
| Endpoint Protection Platform / EDR | sibling (same job class) | EPP/EDR estates are desktops/laptops/servers; MTD is the mobile-platform-specialized pole (apps outside store control, roaming networks, jailbreak/root states). Vendors now span both; the directory keeps the mobile pole separate. | Extend the estate to full endpoint management and desktop-first surfaces → EPP/EDR. |
| Endpoint Management / UEM | adjacent consumer of output | UEM configures/manages devices and holds compliance policy; MTD assesses threats and supplies risk states that UEM compliance rules consume (Intune Tier 1). Already cross-referenced in UEM research. | Remove threat assessment, keep configuration/inventory/compliance → UEM. |
| Email Security Gateway / Browser Security Platform | overlapping control, different scope | Those protect one channel (mail flow, browser session); MTD phishing protection is device-scoped across SMS/web/QR/other apps. | Scope the product to a single content channel → email/browser security. |
| Malware Analysis Sandbox | overlapping analysis | Sandbox detonates single submitted samples in isolation; MTD vetting judges the installed app population in situ for policy risk. | Make deep single-sample detonation the unit of work → Malware Analysis Sandbox. |
| Threat Intelligence Platform | upstream/adjacent | TIP's unit of record is intelligence data; MTD's unit of record is the device risk state. MTD vendors operate intel engines internally. | Sell findings/indicators instead of device protection → TIP. |
| SIEM / SOAR | downstream consumer | MTD emits device risk and events; SIEM/SOAR correlate and orchestrate across sources. | Become the correlation/orchestration layer → SIEM/SOAR. |
| Zero Trust Network Access / identity enforcement | enforcement counterpart | ZTNA/conditional access enforce access decisions; MTD supplies the device-risk input those decisions can weigh. | Own the access decision machinery → ZTNA/identity side. |
| Consumer mobile-security app | audience-lineage neighbor | Shares the detection core (app/device/network scanning, alerts) but is operated by an individual, with no admin console, policy engine, or corporate access enforcement. Market names this category separately; several MTD vendors began there. | Remove organizational operation → personal mobile security utility (adjacent lineage, not this Type's market realization). |
| Mobile Forensics (e.g., Jamf Mobile Forensics) | adjacent | Forensics investigates devices post-incident as evidence work; MTD is continuous protective assessment. | Make per-device deep evidence extraction the product → forensics. |

## Historical / Market-Sample Check

- The Type has no pre-smartphone form: the category co-emerged with enterprise mobility (consumer mobile-security apps of the early 2010s are the recognizable lineage ancestors: on-device app scanning, web filtering, anti-theft, user alerts).
- Test the L0 against the ancestor form: early consumer mobile-security apps satisfy leg 1 (mobile threat assessment) and partially leg 3 (scan/alert/clean) but had no persistent, policy-comparable per-device risk state consumed by an organization (leg 2 weak). They are therefore treated as the **audience-lineage ancestor**, not a full realization — the organizational consumption loop is what the market added when it named the category "Mobile Threat Defense". This keeps the L0 honest: it names the loop structure, not the modern integration machinery (no UEM, no conditional access, no cloud console in the definition).
- Test against region/platform variation: the definition does not require any app-store regime, any MDM protocol, any specific OS version, any cloud-only backend (on-prem/air-gapped variants documented), or any specific risk-scale format. It passes.
- Test against bundling drift: EDR vendors (Defender, CrowdStrike, SentinelOne) and UEM vendors (Sophos, Jamf) ship MTD capabilities inside larger products; the leaf remains valid because the market and the integration standard (Intune connector list, Tier 1) treat "MTD provider" as a product category boundary regardless of bundling.

## Uncertainties

1. Lookout and Pradeo primary documentation unreachable; their detection architecture, console depth, and phishing coverage are unverified this pass. Cross-product claims relying on them are therefore evidence-weak and held at layer B only where the Intune source states them.
2. Whether phishing/web coverage is now universal across MTD products could not be confirmed for Lookout/Pradeo from fetched sources; held as common-not-definitional.
3. Agentless/SDK deployment variants are market-known but only weakly evidenced; not promoted.
4. The exact composition of "files" as a separate vector (Check Point's "apps, files, network and OS") vs the three-vector model varies by vendor phrasing; treated as phrasing variance over the same underlying vectors.
5. Check Point platform list not explicit in fetched text (Android/iOS implied by Harmony Mobile docs elsewhere); not asserted precisely.

## Final Synthesis

Mobile Threat Defense is the mobile-platform-specialized member of the device-security family. Its defining core is a three-legged loop: continuous assessment of identified mobile devices against mobile-specific threats (installed apps, device/OS integrity, network context — with phishing now commonly covered), reduction of those findings to a persistent per-device risk state, and a protective response loop that alerts users with remediation guidance, takes on-device blocking/cleanup action, and/or enables the organization to bar the risky device from corporate resources until remediation. The canonical consumption pattern is the MTD-to-UEM/identity chain — risk level → compliance rule → access decision → block-until-remediated — which is standard mature structure rather than the Type's definition. Detection substrate (on-device vs cloud vs hybrid), bundling (specialist vs EDR vs UEM vs workspace suite), and protection scope (enrolled vs unenrolled devices) are variant axes. The Type is bounded from EPP/EDR by its mobile estate, from UEM by its assess-not-manage job, from per-channel anti-phishing tools by its device scope, and from consumer mobile-security apps by its organizational operation.
