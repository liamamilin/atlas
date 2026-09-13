# Research Notes — Endpoint Protection Platform

Research date: 2026-09-08
Directory leaf: "Endpoint Protection Platform" (§15 Cybersecurity, Identity & Trust)
Slug: endpoint-protection-platform

## Research Goal

Understand what an Endpoint Protection Platform (EPP) actually is as an Application Type: what it protects and how, what its detection machinery produces, how prevention is enforced on the endpoint, how protection is configured and administered across an organization's fleet, how protection is kept current, and how the Type is bounded against EDR, UEM, email/network gateways, mobile threat defense, cloud workload protection, patch management, and browser security.

## Initial Boundary

Working hypothesis at start:

- EPP = prevention-first endpoint security software: protection resident on the endpoint, evaluating what the endpoint runs or encounters against maintained threat intelligence, and blocking/cleaning/quarantining malicious or unwanted software before it does damage — administered for an organization's endpoint fleet from a management console.
- Users: IT/security administrators configure and operate; endpoint users are protected parties, not operators.
- Nearest neighbors: EDR (closest sibling — same devices, usually same agent), UEM (§14 — same devices, different job), Email Security Gateway (perimeter vs endpoint), Network Security Platform (perimeter vs endpoint), Mobile Threat Defense (object-domain slice), CWPP (server-workload estate), Patch Management (adjacent module), Browser Security Platform (session-bound enforcement), XDR (umbrella above).

Pre-existing boundary obligations from earlier passes:

- endpoint-detection-response-edr (processed): "EPP centers on preventing execution (blocking known/unwanted software); EDR centers on detecting what got through, investigating it, and responding. Most products bundle both; the Types are distinguished by center of gravity, and both pure poles have existed. Flag for joint review when EPP is processed." Also: "Classic signature antivirus fails structures 2–4 [of EDR] and is correctly excluded (EPP/AV, not EDR)."
- endpoint-management-uem (processed): different job on the same devices (configure/comply/manage vs detect/respond).
- email-security-gateway (processed): "remove → ... mailbox junk filter or endpoint AV, none a gateway" — endpoint AV explicitly placed outside the gateway Type.
- browser-security-platform (processed): "remove session binding → EDR" — enforcement binding is the seam.
- cloud-workload-protection-cwpp (processed): boundary rests on object domain + operational workflow, not agent technology.
- application-deployment-management (processed): distributes software to endpoints under IT rules — different job from protecting them.

## Research Questions

1. What does the protection software install as, and where does it execute (endpoint-resident vs perimeter)?
2. What is evaluated (files, processes, scripts, downloads, behavior), when (on-access/on-execute/on-demand), and by what detection machinery (signatures, heuristics, behavioral, ML, cloud reputation)?
3. What verdicts are produced (malicious, unwanted/PUA, clean) and what happens on a verdict (block, disinfect, quarantine, delete, allow, report-only)?
4. How is protection configured for an organization (policies, groups, defaults, exclusions, allow/block lists)?
5. How is protection kept current (intelligence/definition updates, product updates, cloud lookups) and kept on (anti-tampering)?
6. What does the admin console show and do (fleet status, events, quarantine, reports)?
7. How do EPP products coexist with each other and with EDR (one primary AV? passive/report-only modes?)?
8. What policy modules are bundled beyond antimalware (web control, device control, firewall, patching, DLP, encryption)?
9. Where are the boundaries vs the neighbor Types listed above?
10. Does the minimal machinery survive older / open-source / differently positioned shapes (historical check)?

## Representative Products

| Product | Pole | Evidence obtained |
|---|---|---|
| Microsoft Defender Antivirus (next-generation protection in Defender for Endpoint) | platform-native prevention bundled with the OS, managed through the OS's management stack | A — three Microsoft Learn pages fetched in full |
| Sophos Endpoint Protection (Sophos Central) | converged mid-market suite; policy-set-driven prevention | A — three Sophos Central help pages fetched in full |
| Bitdefender GravityZone (Endpoint Security Tools + Control Center) | layered-detection suite with modular policy engine, cloud and on-prem consoles | A — support-site structure + Antimalware policy page fetched in full |
| ClamAV | open-source anti-virus toolkit/engine — minimal machinery probe without a management platform | A — documentation introduction fetched in full |

Selection rationale: platform-native vs converged suite vs layered suite vs open-source engine; enterprise vs mid-market; OS-bundled vs third-party; cloud console vs on-prem console (Bitdefender documents both). ESET was attempted three times (help.eset.com root, /epoc/, /ees_win/18.0/ — all 404) and abandoned per the network-limitation rule; the classic European prevention-first suite pole is therefore represented structurally, not observationally. CrowdStrike and SentinelOne prevention layers were not sampled (docs unreachable, per the EDR pass record).

## Sources

Tier 1 (fetched in full, 2026-09-08):

- Microsoft Learn — Microsoft Defender Antivirus in Windows Overview: https://learn.microsoft.com/en-us/defender-endpoint/microsoft-defender-antivirus-windows
- Microsoft Learn — Overview of next-generation protection: https://learn.microsoft.com/en-us/defender-endpoint/next-generation-protection
- Sophos Central Admin help — Endpoint: https://docs.sophos.com/central/customer/help/en-us/ManageYourProducts/EndpointProtection/index.html
- Sophos Central Admin help — Threat Protection Policy: https://docs.sophos.com/central/customer/help/en-us/ManageYourProducts/EndpointProtection/ThreatProtectionPolicy/index.html
- Sophos Central Admin help — Computers: https://docs.sophos.com/central/customer/help/en-us/ManageYourProducts/EndpointProtection/Computers/index.html
- Bitdefender GravityZone support — Features by product / documentation structure: https://www.bitdefender.com/business/support/en/77209-376322-features-by-product.html
- Bitdefender GravityZone support — Antimalware (policy module): https://www.bitdefender.com/business/support/en/77209-342929-antimalware.html
- ClamAV documentation — Introduction: https://docs.clamav.net/

Source-access limitations:

- ESET help portal unreachable (three distinct URL patterns 404). Not sampled. The prevention-first European suite pole is evidenced only through the sampled set's shared structures.
- Microsoft PUA documentation page 404; PUA handling is evidenced through Sophos's documented PUA exclusion machinery instead.
- Bitdefender policy sub-pages (On-access/On-execute/On-demand detail pages) were not individually fetched; the Antimalware overview page and the documented site structure were used. Claims about Bitdefender stay at the level the fetched pages support.
- CrowdStrike / SentinelOne prevention layers: docs unreachable (recorded in the EDR pass); no operational claims made from them.
- Consequence: the prevention machinery, policy model, and enforcement vocabulary are evidenced by 3 commercial products + 1 open-source toolkit at documentation depth; market-leader pure-play operational detail is under-evidenced and is NOT filled from model memory.

## Product Observations

### Microsoft Defender Antivirus / next-generation protection (evidence layer A)

Positioning (overview page):

- "Microsoft Defender Antivirus is a major component of your next-generation protection in Microsoft Defender for Endpoint. This protection brings together machine learning, big-data analysis, in-depth threat resistance research, and the Microsoft cloud infrastructure to protect devices (or endpoints) in your organization. Microsoft Defender Antivirus is built into Windows."
- Anomaly detection: "monitors for process creation events or files that are downloaded from the internet"; on by default.
- "Microsoft Defender Antivirus can also stop threats based on their behaviors and process trees even when the threat has started execution" (fileless malware example).
- Offline posture: "the latest dynamic intelligence from the Intelligence Security Graph is provisioned to the endpoint regularly throughout the day. When connected to the cloud, real-time intelligence gets fed."

Modes (the coexistence model, documented in a mode table):

- Active mode: "used as the primary antivirus app on the device. Files are scanned, threats are remediated, and detected threats are listed in your organization's security reports and in your Windows Security app."
- Passive mode: "isn't used as the primary antivirus app... Files are scanned, and detected threats are reported, but threats aren't remediated" — only available on endpoints onboarded to Defender for Endpoint.
- Disabled/uninstalled: no scanning, no remediation.
- Tamper protection governs mode switches (documented interaction with group policy).

Updates: "Microsoft releases regular updates to help ensure that your devices have the latest technology to protect against new malware and attack techniques" — dedicated protection and product updates named as a next-gen protection component.

Next-generation protection page:

- "blocks malware using local and cloud-based machine learning models, behavior analysis, and heuristics."
- Components: behavior-based, heuristic, and real-time antivirus protection ("always-on scanning using file and process behavior monitoring"; "detecting and blocking apps that are deemed unsafe, but might not be detected as malware" — the unwanted-app class); cloud-delivered protection ("near-instant detection and blocking of new and emerging threats"); dedicated protection and product updates.
- Performance analyzer tool for tuning scan performance (paths/files/processes/extensions impacting scan time).

### Sophos Endpoint Protection / Sophos Central (evidence layer A)

Positioning (Endpoint product page):

- "Endpoint Protection lets you protect your users and devices against malware, risky file types and websites, and malicious network traffic. It also offers peripheral control, web control and more. You use policies to apply protection to users and devices."
- Policy set: Threat Protection, Peripheral Control, Application Control, Data Loss Prevention, Web Control, Update Management, Windows Firewall, Data Collection and Investigation, Endpoint DNS Protection.
- Fleet surfaces: Computers ("manage your protected computers"), Computer Groups; Events list; Global Settings → Protection and Remediation (Allow and Block: global exclusions, allowed applications, block compromised IPs).

Threat Protection policy (the core prevention policy, documented in detail):

- Recommended settings bundle: "Detection of known malware. In-the-cloud checks to allow detection of the latest malware known to Sophos. Proactive detection of malware that has not been seen before. Automatic cleanup of malware." Non-recommended settings produce warnings.
- Live Protection: "checks suspicious files against the SophosLabs threat database... during real-time scanning."
- Deep Learning: "can automatically detect threats, particularly new and unknown threats that have not been seen before. It uses machine learning and does not depend on signatures."
- Real-time scanning (local files, network shares, removable media): "checks files for known malware when they're accessed and updated. It prevents known malicious programs from being run, and infected files from being opened by legitimate applications."
- Real-time scanning (Internet): scan downloads in progress before they reach the browser; block access to malicious websites (reputation check); detect low-reputation downloads with action "Prompt User" (user can trust or delete) or automatic block by reputation level.
- Remediation: "Automatically clean up malware... When Sophos Central cleans up a file, it removes the file from its current location and quarantines it in SafeStore. Files remain in SafeStore until they're allowed or removed... You can restore files quarantined in SafeStore by adding them to Allowed applications." (SafeStore size/count limits are product-specific numbers — recorded here, not generalized. Windows always cleans up detected items regardless of the setting; Mac restore behavior differs.)
- Runtime protection: ransomware protection (CryptoGuard; protect document files from ransomware; remotely run ransomware; MBR ransomware), exploit mitigation for vulnerable applications, process protection (hollowing, DLL loading, credential theft, privilege escalation), malicious beacon/C2 blocking, malicious network traffic (IPS), AMSI protection for scripts, driver detection.
- Adaptive attack protection: "a more aggressive set of protections when an attack is detected" (safe-mode abuse blocking, vulnerable/security-tool driver blocking, compromised-IP blocking).
- Device isolation: "we isolate devices from the network if they report their health as red" (health = threats detected, out-of-date software, non-compliance, not properly protected); "You can't remove these devices from isolation. You need to fix a device's issues and return it to 'green' health."
- Scheduled scanning: "performs a scan at a time or times that you specify"; "Scheduled scanning may not be needed when real-time scanning is turned on... We recommend using real-time scanning, which scans files as they're accessed or modified, rather than relying only on scheduled scan intervals." Missed scans (computer offline) reported on the Events tab.
- Scanning exclusions: files/folders, websites, Potentially Unwanted Applications, detected exploits, ransomware-protection exclusions, driver detection; policy-scoped and global exclusions; "Adding exclusions can reduce your protection. Use them carefully."
- PUA definition (vendor's own): "programs that aren't malicious by design but are potentially unsuitable for business environments... Customers can allow PUAs in their environment based on their business needs."
- Desktop messaging: end-user notifications about threat protection events, customizable.

### Bitdefender GravityZone / Endpoint Security Tools (evidence layer A)

Architecture (documented structure):

- GravityZone Control Center (web console; cloud and on-premises variants documented as separate solution lines); Security agents ("Bitdefender Endpoint Security Tools" — BEST — for Windows/Linux/macOS); Security Server (offload/central scanning component); Relay; policy inheritance rules.
- Inventory management: Network inventory — endpoint types, endpoint status, endpoint details, organizing endpoints into groups, tags, assigning policies, tasks/actions on endpoints, remote shell, reports.
- Security management: Creating policies → Configuring policies with modules: Agent (notifications, settings, communication, update, security telemetry), Antimalware, Sandbox Analyzer, Firewall, Network Protection (Content Control, Web Protection, Network Attacks), Patch Management, Device Control, Integrity Monitoring, Exchange Protection, Encryption (Full Disk Encryption), Incidents Sensor (EDR), Storage Protection, Risk Management, Blocklist.
- Security monitoring: Dashboard, Executive Summary, Health dashboard, Reports (types, scheduled, report-based actions), Notifications (types, settings).
- Quarantine: "Managing the quarantine" — explore the Quarantine page, manage quarantined files (restore/remove/empty as tasks; also API tasks: list, remove, restore, add file to quarantine).

Antimalware module (policy page, fetched in full):

- "The Antimalware module protects the system against all kinds of malware threats such as viruses, Trojans, spyware, rootkits, and adware."
- Protection categories: "On-access scanning: prevents new malware threats from entering the system. On-execute scanning: proactively protects against threats, and can automatically discover and block fileless attacks at pre-execution... On-demand scanning: allows detecting and removing malware already residing in the system."
- Operation modes: "Detection and prevention mode: ...detect and block threats. When it detects a virus or other malware, the Bitdefender security agent will automatically attempt to remove the malware code from the infected file and reconstruct the original file. This operation is referred to as disinfection. Files that cannot be disinfected are moved to quarantine in order to isolate the infection. When a virus is in quarantine, it cannot do any harm because it cannot be executed or read."
- "EDR (Report only) mode: This operation mode exclusively enables On-execute scanning, set to only report threats, and not block them. This mode of operation is available for users that want to install a lightweight EDR solution in their environments, that can run alongside other prevention solutions. For blocking capabilities, you are required to add a full product license."
- Anti-tampering, HyperDetect, Advanced Anti-Exploit, Settings, Security Servers, Exclusions as antimalware policy subsections.
- License note: "Availability and functioning of this feature may differ depending on the license included in your current plan."

### ClamAV (evidence layer A — minimal machinery probe)

- "ClamAV is an open source (GPLv2) anti-virus toolkit, designed especially for e-mail scanning on mail gateways. It provides... a flexible and scalable multi-threaded daemon, a command line scanner and advanced tool for automatic database updates. The core of the package is an anti-virus engine available in a form of shared library."
- Vendor's own boundary statement: "ClamAV is not a traditional anti-virus or endpoint security suite. For a fully featured modern endpoint security suite, check out Cisco Secure Endpoint."
- Real-time protection (Linux only): "The ClamOnAcc client for the ClamD scanning daemon provides on-access scanning on modern versions of Linux. This includes an optional capability to block file access until a file has been scanned (on-access prevention)."
- Detection: "detects millions of viruses, worms, trojans, and other malware"; signature databases; "Signed signature databases ensure that ClamAV will only execute trusted signature definitions"; bytecode signature runtime for complex detection routines.
- Currency: "Advanced database updater with support for scripted updates, digital signatures and DNS based database version queries."
- Archive/packing coverage; malware and false-positive submission process to the vendor's threat organization with signature changes published in the official databases.

Observation: ClamAV realizes the evaluation + enforcement + currency machinery (signature evaluation, on-access prevention, database updates) without any management platform, fleet policy model, or console — the vendor itself says it is not an endpoint security suite. This calibrates the L0: the machinery is the Type's floor; the administered platform posture is the market form built on top of it.

## Cross-product Comparison

| Aspect | Microsoft Defender Antivirus | Sophos Endpoint Protection | Bitdefender GravityZone | ClamAV |
|---|---|---|---|---|
| Protection residency | built into Windows; protects the device itself | endpoint agent managed from Sophos Central | BEST agent on Windows/Linux/macOS | engine/daemon on the host (Linux on-access; mail-gateway heritage) |
| Evaluation triggers | always-on real-time + behavior monitoring; anomaly detection; cloud lookups | real-time scanning (on access) + scheduled scanning + download scanning | on-access + on-execute + on-demand | on-access (ClamOnAcc) + on-demand (clamscan/clamd) |
| Detection machinery | local + cloud ML, behavior analysis, heuristics, anomaly detection | signatures + cloud checks (Live Protection) + deep learning (no signatures) + runtime behavior | signatures + on-execute proactive + HyperDetect + Advanced Anti-Exploit | signatures + bytecode signatures |
| Intelligence currency | regular platform/engine/intelligence updates; cloud-delivered protection; offline intelligence provisioning | SophosLabs cloud checks during scanning | agent update machinery; update staging profiles | freshclam database updater; signed DBs |
| Verdict classes | malware; "apps deemed unsafe, but might not be detected as malware" | malware; risky file types; low-reputation downloads; PUA ("not malicious by design but potentially unsuitable for business") | malware (viruses, Trojans, spyware, rootkits, adware) | malware signatures |
| Enforcement | threats remediated in active mode; passive mode reports only | automatic cleanup; quarantine (SafeStore); restore via allowed applications; block execution/opening | disinfect → quarantine if not disinfectable; block; report-only mode | on-access prevention (block access until scanned); detection |
| Policy model | OS management stack (group policy/Intune-class); modes | per-user/device policies with module toggles + recommended defaults + warnings | policy engine with modules, inheritance, assignment to groups | configuration files; no fleet policy model |
| Fleet administration | organization's security reports; managed via MDE/Intune stack | Computers/Computer Groups; Events; global allow/block | Network inventory (groups, tags, status, tasks); dashboards; reports | none (toolkit) |
| Quarantine management | threats listed; remediation recorded | SafeStore with restore path | Quarantine page + API tasks | (not documented as a managed surface) |
| End-user surface | Windows Security app; notifications | desktop messaging notifications | agent notifications | none |
| Bundled modules beyond antimalware | (next-gen protection scope; wider platform adds more) | web control, peripheral control, application control, DLP, firewall, update management, DNS protection | firewall, network protection, device control, patch management, encryption, integrity monitoring, risk management | none |
| Coexistence posture | active/passive/disabled modes; passive only when onboarded to MDE | XDR Sensor variant runs alongside existing anti-malware (per EDR pass) | "EDR (Report only)" mode runs alongside other prevention; incompatible-software list documented | commonly deployed beside other tooling |
| Managed service tier | (platform-level offerings) | MDR service (per EDR pass) | MDR service line documented | none |

Cross-product commonalities (layer B, directly observed in ≥2 products):

1. Protection software resident on and executing on the protected endpoint itself (all four; ClamAV's on-access prevention is the minimal form).
2. Continuous evaluation of what the endpoint runs or encounters — on-access/real-time as the primary trigger, on-demand/scheduled scanning as the secondary sweep (all four; Sophos states the primacy of real-time explicitly).
3. Detection machinery combining maintained threat intelligence with techniques beyond exact signatures (heuristics/behavior/ML/cloud reputation) — observed in all four (ClamAV's bytecode signatures are its extension mechanism).
4. Security verdicts that distinguish malicious software from merely unwanted software (PUA/unwanted-app class documented by Microsoft and Sophos; Bitdefender's adware/spyware classes; ClamAV is signature-pure).
5. Enforcement on the verdict: block execution/access, disinfect, quarantine, delete (all four; report-only/passive modes exist as documented configurations of enforcement-capable machinery — Microsoft passive mode, Bitdefender report-only mode).
6. Quarantine as the standard containment state for items that cannot be safely cleaned, with a restore path (Sophos SafeStore, Bitdefender quarantine page/API; Microsoft remediation records).
7. Intelligence currency as a maintained service: regular definition/intelligence updates plus cloud lookups (all four; ClamAV's freshclam is the minimal form).
8. Exclusions machinery as the operational escape hatch, with explicit vendor warnings that exclusions reduce protection (Sophos, Bitdefender, Microsoft performance tuning).
9. Anti-tampering posture protecting the protection itself (Microsoft tamper protection, Bitdefender anti-tampering; Sophos adaptive protections against protection-disabling techniques).
10. Admin-side visibility: events/detections, protection health/status, reports (Microsoft security reports, Sophos Events/dashboards, Bitdefender monitoring/reports).
11. One-primary-prevention-product-per-endpoint coexistence rule with documented secondary postures (Microsoft passive mode; Bitdefender report-only mode; Sophos sensor-only variant per EDR pass).
12. License/plan tiering gating capability depth (Microsoft plans, Bitdefender license note, Sophos product tiers per EDR pass).

## Canonical Abstraction

### L0 — Defining Invariant

Four jointly-held structures. Remove any one and the product stops being recognizable as an Endpoint Protection Platform:

1. **The protected endpoint estate** — a population of endpoints carrying protection software that is installed on and executes on each protected machine itself, defending that machine. Remove → perimeter/gateway security (network/email security) or device management; the "endpoint" is gone.
2. **Threat evaluation of what endpoints run or encounter** — the protection continuously evaluates files, processes, scripts, downloads, and behavior on the endpoint against maintained threat intelligence and detection techniques (signatures, heuristics, behavioral rules, machine learning, cloud reputation) and produces security verdicts — malicious, unwanted, or clean. Remove → rule-based device enforcement without threat judgment (firewall/UEM compliance) or a plain updater.
3. **Prevention enforcement on the verdict** — when the verdict is malicious or unwanted, the protection stops it: blocks execution or access, disinfects or removes the item, or quarantines it so it can no longer run or be read. The protection outcome is the defining output. Remove → a detection-only scanner. (Report-only/passive modes are policy configurations of enforcement-capable machinery, documented by two sampled products; a product incapable of enforcement is a scanner utility, not protection.)
4. **Standing, maintained protection** — protection operates continuously (on-access/real-time) and its intelligence is kept current against new threats (definition/intelligence updates, cloud lookups), so the endpoint remains protected over time without reinstallation. Remove → a one-shot scan utility or a stale scanner.

Jointly-held is load-bearing:

- 1 without 2–4 = installed software with no security function.
- 2 without 1 = a remote/upload scanning service, not endpoint protection.
- 1+2 without 3 = detection and reporting only — the protection is gone.
- 1+3 without 2 = static rule blocking without threat judgment (host firewall/device-control territory).
- 2+3+4 without 1 = protection machinery without an administered endpoint estate — the engine/toolkit shape (ClamAV realizes this and its own documentation says it is not an endpoint security suite).

Historical/market-sample check (§24): the minimal core survives older and differently positioned shapes — the signature-era antivirus pattern (on-access scanner + signature updates + quarantine/disinfection) satisfies all four structures without cloud, ML, or consoles; ClamAV demonstrates the machinery in open-source form today; the managed enterprise AV suites of the 2000s (console + agents + policies) add the platform posture that the current market standardizes. The definition is therefore not over-fitted to the current cloud/ML implementation era. The consumer/self-administered antivirus posture realizes the same machinery without the organizational platform; it is recorded as a boundary question below, not absorbed silently.

### L1 — Common Mature Structure

Present in most mature modern products; not required for the Type:

- central management console (cloud-hosted dominant; on-premises documented) over the estate: deployment, groups/tags, policy assignment, fleet protection status
- protection policy model: per-user/device/group policies, module toggles, recommended/default settings with warnings when weakened, priority/inheritance
- exclusions machinery (policy-scoped and global; files, folders, websites, processes, PUAs) with explicit reduce-protection warnings
- scheduled/on-demand scanning alongside real-time protection
- quarantine management surface (view, restore, remove) with allow-listing as the restore path
- detection events surfaced to administrators; end-user notifications on detections
- protection health/status monitoring and reporting (agent status, currency, threats found)
- anti-tampering protection of the security software itself
- ransomware protection, exploit mitigation, and behavioral runtime protection modules
- unwanted-application (PUA) handling with business-need allow-listing
- web protection (malicious-website blocking, download reputation)
- agent deployment machinery and multi-OS coverage (Windows/macOS/Linux; mobile in some products)
- license/plan tiering

### L2 — Variant / Optional Structure

- bundled policy-suite breadth: host firewall, device/peripheral control, application control/allow-listing, DLP, DNS protection, update/patch management for OS and third-party apps, encryption management
- server protection as a separate product/tier vs the same agent
- platform-native posture: protection bundled with the OS, managed through the OS's own management stack
- report-only/passive operation modes for coexistence with another prevention product
- health-based automatic device isolation (observed in one sampled product — product-specific/optional)
- managed detection & response service tiers on top of the product
- MSP/multi-tenancy packaging
- consumer/self-administered posture: the same machinery without the organizational platform (boundary question recorded)
- AI-era detection engines (deep learning, cloud ML) — now standard, era-current

### L3 — Vendor-specific Structure (research notes only)

- Microsoft: active/passive/disabled mode table; passive mode gated on Defender for Endpoint onboarding; tamper protection interaction with group policy; Intelligence Security Graph; offline intelligence provisioning; performance analyzer; plan gating (Plan 1/Plan 2/Defender for Business); Windows Security app as the local surface; MpCmdRun command-line utility.
- Sophos: SafeStore quarantine with size/count limits; Live Protection/SophosLabs cloud checks; Deep Learning; CryptoGuard ransomware protection; Adaptive Attack Protection; device isolation on red health with green-health release; event journals; Threat Graph creation; global exclusions and allowed applications; desktop messaging customization; policy-scoped vs global exclusions; PUA exclusion by detection name.
- Bitdefender: BEST agent naming; Security Server central-scanning offload; HyperDetect; Advanced Anti-Exploit; anti-tampering; disinfect-then-quarantine flow; "EDR (Report only)" mode with full-license gating; policy inheritance rules; quarantine API tasks (list/remove/restore/add); Blocklist; PHASR; Risk Management module; incompatible-software list.
- ClamAV: clamd/clamscan/freshclam/ClamOnAcc component set; bytecode signature runtime; signed signature databases; DNS-based version queries; Talos submission flow; the vendor's own "not a traditional anti-virus or endpoint security suite" boundary statement.

## Vendor-specific Findings

- The enforcement vocabulary differs by product (disinfect→quarantine vs cleanup-to-quarantine vs remediate); the invariant is "verdicts are enforced against execution," not any specific action list.
- Two products document explicit secondary postures (Microsoft passive mode; Bitdefender report-only mode) that keep the machinery installed while another product holds the primary prevention role — the coexistence rule is a structural behavior of the market, not a single vendor's design.
- Health-based automatic isolation (Sophos) is a prevention-adjacent containment action that overlaps EDR's isolate action; single-product evidence — held as optional, not promoted.
- The PUA class is defined by business context rather than maliciousness (Sophos's definition is the clearest documented); verdict classes beyond malware are policy-managed.

## Boundary Findings

| Neighbor Type | Relationship | Distinction test ("remove what → becomes the other Type") |
|---|---|---|
| Endpoint Detection & Response / EDR (§15 sibling, processed — JOINT REVIEW) | closest sibling; same devices, usually same agent | EPP centers on preventing execution (verdict-driven blocking/cleaning of known and unwanted software); EDR centers on detecting what got through, investigating it, and responding. Remove investigation depth + retrospective telemetry + endpoint response → EPP. Remove prevention → pure EDR. Both pure poles have existed (classic signature AV without EDR; sensor-only EDR without prevention — Sophos XDR Sensor, Bitdefender report-only mode). Convergence on one agent is the market norm and is packaging, not Type identity. RESOLVED from this side: keep-both RATIFIED with center-of-gravity seam. |
| Endpoint Management / UEM (§14, processed) | different job on the same devices | UEM configures, complies, and manages devices; EPP protects them from malicious/unwanted software. Agents may be shared. EPP's device-control/application-control modules are prevention-policy machinery organized around threat verdicts; UEM's equivalents are configuration/compliance machinery. Remove threat evaluation + enforcement → UEM. |
| Email Security Gateway (§15, processed) | perimeter vs endpoint | The gateway is a checkpoint in the mail flow before mailboxes; EPP is resident on the endpoint. The ESG pass itself excludes "endpoint AV" from the gateway Type. Remove endpoint residency → gateway. |
| Network Security Platform (§15 sibling, unprocessed) | perimeter vs endpoint | Network security inspects traffic on the path; EPP judges software and behavior on the machine. EPP products bundle host-firewall modules — module, not the Type. Remove endpoint residency → network security. |
| Mobile Threat Defense (§15 sibling, unprocessed) | object-domain slice | Mobile endpoints are part of EPP estates in some products; the mobile-specialized pole is its own Type. Not absorbed here. |
| Cloud Workload Protection / CWPP (§15, processed) | sibling with converging machinery | CWPP's object is the server/container/cloud-workload estate with image/vulnerability context; EPP-for-servers is prevention for server operating systems within the endpoint frame. Boundary is object domain + workflow, not agent technology (per CWPP pass flag). |
| Patch Management (§14 sibling, unprocessed) | adjacent module | EPP's own intelligence/product updates are internal to the Type; EPP suites that patch OS/third-party apps carry a Patch-Management-shaped module. Remove the antimalware core → patch management. |
| Browser Security Platform (§15, processed) | adjacent | Browser security binds enforcement to the browsing session; EPP's web protection module is endpoint-resident traffic/file reputation enforcement. Remove session binding → EPP module. |
| Vulnerability/Risk Management modules (e.g., Bitdefender Risk Management) | adjacent analytics | Risk findings and vulnerability views are analytics over the estate, not prevention. Remove prevention → risk analytics. |
| Consumer antivirus (no directory leaf) | same machinery, different administration posture | Consumer AV realizes the four-structure machinery for one self-administered machine without the organizational platform (console, fleet policies, compliance posture). The leaf's market form is the organizational platform; the consumer pole is recorded as a taxonomy question, not silently absorbed. |

## Uncertainties

1. ESET, Kaspersky, Trend Micro, Avast not sampled (access failures / not attempted within budget). The classic European prevention-first suite pole is documented structurally via the sampled set's shared machinery, not observationally.
2. Detection-engine internals (model architectures, heuristic specifics, cloud lookup mechanics) are not documented at operational depth by any sampled vendor; observations describe inputs, triggers, and outputs, not engine internals.
3. Exact defaults (default verdict→action mappings, scan schedules, update frequencies, quarantine limits) are product- and plan-specific; none are generalized into the final document. Sophos SafeStore numeric limits are recorded here only.
4. CrowdStrike/SentinelOne prevention layers not sampled (docs unreachable, per EDR pass); the pure-play next-gen pole is represented at positioning level only.
5. Whether "servers" belong in the default object domain or as a variant: sampled products differ (Sophos splits Server into a separate product; Bitdefender policy modules cover Windows servers; Microsoft supports Windows Server). Held as an object-domain breadth variant, consistent with the CWPP boundary flag.
6. The consumer-antivirus taxonomy question (above) is a genuine directory gap: no leaf covers self-administered antivirus; this pass records it rather than restructuring the directory.

## Final Synthesis

An Endpoint Protection Platform is the prevention-first security application for an organization's endpoints. Its world is built from four jointly-held structures: a protected endpoint estate (protection software installed on and executing on each protected machine itself); threat evaluation of what those endpoints run or encounter (continuous on-access/real-time evaluation plus on-demand sweeps, fed by maintained threat intelligence and detection techniques from signatures through heuristics, behavioral rules, machine learning, and cloud reputation, producing malicious/unwanted/clean verdicts); prevention enforcement on the verdict (block execution or access, disinfect, remove, or quarantine so the item can no longer run — with report-only modes existing as documented configurations, not as the Type's floor); and standing, maintained protection (protection that runs continuously and stays current through definition/intelligence updates and cloud lookups, protected against tampering). Around this core, mature products add the platform layer that gives the Type its market name: a central console administering the fleet through policies, groups, exclusions, and allow/block lists; quarantine management; events, health monitoring, and reports; end-user notifications; and bundled policy modules (web control, device control, firewall, patching, DLP, encryption). The Type's boundaries are held by residency and job: EDR is the detection-and-response sibling on the same devices (joint review ratified keep-both with a center-of-gravity seam), UEM manages the same devices for configuration and compliance, gateways inspect flows before the endpoint, mobile and cloud-workload types slice the object domain, and patch management is a bundled module at most. The machinery core survives the signature era and the open-source toolkit form; the platform posture is the current market's dominant realization of it.
