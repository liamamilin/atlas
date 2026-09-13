# Research Notes — Deception Platform

Research date: 2026-09-10

## Research Goal

Understand what a Deception Platform (cyber deception technology) actually is as an Application Type: what objects exist inside it, who operates it, how work flows from decoy deployment to alert to response, and where its boundaries lie against neighboring security Types (SIEM, EDR/NDR, BAS, threat hunting, honeypots, ITDR).

## Initial Boundary

Initial hypothesis:

- A deception platform plants fake-but-plausible assets (hosts, services, shares, credentials, documents) inside an organization's environment; because legitimate users have no business touching them, any interaction is a high-fidelity alert, and the platform records what the interacting party did.
- Nearest neighbors: honeypots (precursor/research form), SIEM (aggregates its alerts), EDR/NDR (watch real assets, not fake ones), BAS (synthesizes attacks against real controls), threat hunting (human-initiated search), ITDR/identity security (overlaps on AD deception).
- Main confusion risk: honeypot heritage — the Type descends from honeypots but the product category is a centrally managed operational defense capability, not a research trap.

## Research Questions

1. What are the core objects? (decoys, lures/breadcrumbs, tokens, credentials, incidents, console)
2. What is the defining detection premise? (presumptive malice of decoy interaction)
3. What does the platform observe when a decoy is engaged?
4. How are decoys deployed, kept realistic, and tuned to avoid noise?
5. Who uses it and through which interfaces? (console, SIEM/webhook, the decoy surfaces themselves)
6. Where does the boundary with honeypots, BAS, SIEM, EDR, and ITDR sit?
7. Do older / open-source / differently-positioned forms (honeypots, T-Pot, token services) still fit the definition?

## Representative Products

Selected for market representation, documentation quality, product-philosophy diversity, and customer-tier spread:

1. **Thinkst Canary** (Thinkst Applied Research) — simplicity-first standalone pole; hardware/cloud/VM canaries + Canarytokens; SMB → enterprise; excellent public docs (docs.canary.tools, help.canary.tools).
2. **Fidelis Deception** (Fidelis Security) — network-forensics-centric enterprise/government pole; decoys + breadcrumbs + fake accounts + deceptive data; cyber terrain mapping; standalone or inside Fidelis Elevate XDR.
3. **SentinelOne Singularity Hologram / Singularity Identity** (ex-Attivo Networks, acquired 2022) — deception inside an XDR suite; network decoys + AD/identity deception; MITRE ATT&CK/D3FEND mapping.
4. **Proofpoint Shadow** (ex-Illusive Networks, acquired 2022) — agentless endpoint/identity deception; automation-first; part of Proofpoint Identity Threat Defense platform.
5. **T-Pot** (Deutsche Telekom Security, open source) — open-source multi-honeypot platform; the research/community pole used for the historical / market-sample check.

Acalvio ShadowPlex (enterprise autonomous deception) was also targeted but unreachable (503 on both attempts); see Source-access Limitation.

## Sources

- Thinkst — API docs: https://docs.canary.tools/ (incl. /guide/terminology) — fetched 2026-09-10
- Thinkst — Help Centre: https://help.canary.tools/ (Canarytokens section; "What are Canarytokens?" article) — fetched 2026-09-10
- Fidelis Security — https://fidelissecurity.com/ and https://fidelissecurity.com/solutions/deception/ — fetched 2026-09-10
- SentinelOne — Singularity Hologram datasheet (PDF, hubspotusercontent-na1.net), https://www.sentinelone.com/platform/identity/, https://www.sentinelone.com/press/sentinelone-completes-acquisition-of-attivo-networks/ — retrieved via search 2026-09-10
- Proofpoint — https://www.proofpoint.com/us/products/identity-threat-detection-response/shadow; Identity Threat Defense Platform solution brief (PDF); ITDR Buyer's Guide (PDF) — retrieved via search 2026-09-10
- T-Pot — https://github.com/telekom-security/tpotce (README) — fetched 2026-09-10
- Acalvio — https://acalvio.com/ and https://www.acalvio.com/ — both returned 503 on 2026-09-10 (abandoned after 2 attempts)

## Product Observations

### Thinkst Canary (Layer A — directly observed)

From docs.canary.tools terminology and help.canary.tools:

- **Birds / Devices / Sensors**: canary devices the customer purchases and connects to their Console; form factors: hardware, cloud (Azure, AWS EC2, GCP), VM (VMware, Hyper-V); also container canaries and virtual canaries.
- **Canarytokens**: "small pieces of software (ranging from URLs and hostnames, to Word documents, AWS credentials and Slack API tokens) that will alert you when triggered." Framed as "a simple way to tripwire things… you can deploy tokens in seconds." Token catalog observed in help centre: web bug, DNS, AWS API key, Azure login certificate, Word/Excel/macro, sensitive command, AD login, WireGuard VPN, cloned website, cloned CSS, Entra ID login, QR code, PDF, Slack API key, Windows folder, custom exe/binary, AWS S3 bucket, custom web image, Office 365 mail bug, slow/fast redirect, Google Docs/Sheets, Gmail, fake app, MySQL dump, credit card, fake SAML IdP app (Entra ID/Okta), CrowdStrike API key, browser cookie.
- **Breadcrumbs**: "small pieces of structured data (such as webpage shortcuts or SSH configuration entries) that create a link from a host system to one of your Birds to lure attackers towards it."
- **Console**: "the per-customer EC2 instance that includes a UI for managing your Canary setup. All your Sensors will reach out to your Console to check in and relay alerts."
- **Flocks**: logical groups of Birds, Canarytokens, and users "with different management or alerting rules"; per-flock settings, canary limits, pending queues, ignore lists (hostname, source port), change alerts, webhooks.
- **Incidents**: alert objects with actions and queries; notification channels include webhooks (generic, Splunk), syslog (RFC5424), email.
- **RBAC**: per-flock Managers (view + change settings) and Watchers (view only).
- **Mass deployment**: breadcrumbs and tokens deployable at scale via CrowdStrike Falcon, Jamf, SCCM/MEM + PowerShell, Ansible.
- **Positioning** (help article): "Canarytokens are a free, quick, painless way to help defenders discover they've been breached (by having attackers announce themselves.)" Tokens can be "implant[ed] … in your production systems rather than setting up separate honeypots."
- Ignore lists exist to suppress alerts from known scanners (hostname/source-port ignore lists) — evidence that the presumptive-malice premise needs operational tuning.

### Fidelis Deception (Layer A — directly observed)

From fidelissecurity.com/solutions/deception/:

- "By placing realistic decoys, breadcrumbs, fake accounts and data across your environment, it lures adversaries into revealing their presence and tactics early."
- "Interactions with endpoint and network deception assets are inherently suspicious and signal attacker presence. This approach eliminates false positives and reduces alert fatigue." — the presumptive-malice premise stated verbatim.
- Planted credentials and "sensitive-looking files act as bait… Any interaction reveals credential theft or data exfiltration activity immediately."
- "Continuously maps cyber terrain and provides risk analysis across terrains"; "Automatically update decoys to mirror real environments"; automated decoy creation, deployment, testing, and updating (FAQ).
- Threat protection use cases: credential theft detection, lateral movement detection, Active Directory deception ("Decoy Active Directory objects expose reconnaissance and credential harvesting activities").
- OT/ICS decoys ("highly authentic decoys that mirror real OT and ICS systems"); cloud and IoT resources "as deceptive objects."
- Active sandbox analysis: "safely detonates suspicious files and payloads in an isolated environment."
- Standalone ("a strong standalone deception solution") or integrated into Fidelis Elevate XDR; integrates with SIEM/security platforms (Splunk, Devo, etc.).
- FAQ definition: "Deception technology uses decoys, traps, and credentials that appear legitimate to attackers. When adversaries interact with these deceptive assets, the deception platform generates alerts and reveals attacker behavior."

### SentinelOne Singularity Hologram / Identity (Layer A — directly observed, via datasheet + product pages)

- Singularity Hologram: "leverages advanced, high-interaction deception and decoy technology to lure in-network attackers and insider threat actors into engaging and revealing themselves. By mimicking production OSes, applications, data, and more, Singularity Hologram uncovers covert adversary activity, collects high-fidelity telemetry, and garners actionable intelligence."
- Decoy breadth: decoy ICS-SCADA, SWIFT terminals, POS, VoIP, routers/switches, IoT devices, Windows and Linux OSes, serverless and storage cloud technologies; hardware and virtual decoys "for any location or data center."
- "Threat information from distributed decoys is aggregated to a Hologram Central Manager."
- Output: "ingestible, actionable TTP information and high-confidence, substantiated attack forensics"; visualize attacks over time; map events to MITRE ATT&CK D3FEND; playbooks.
- Singularity Identity: "Plant decoys and credentials that expose reconnaissance early"; AD/Azure AD deception; conditional access (session blocking, MFA re-authentication).
- Positioning: component of Singularity XDR; Attivo Networks acquisition completed May 2022 ("identity security and lateral movement protection company").

### Proofpoint Shadow (Layer A — directly observed, via product page + platform briefs)

- "Proofpoint Shadow uses modern deception technology… It uses agentless methods to actively engage attackers in your production environment for the sole purpose of detecting their existence."
- "active deception techniques to imitate credentials, connections, data, systems and other artifacts that appear useful to the attacker… early detection of both insiders and external attackers."
- Intelligent automation: "Shadow analyzes the endpoint landscape and designs tailored deceptions for each machine. It then deploys them through a one-click process. And it manages the ongoing process of adjusting and managing deceptions over time."
- Management console: "see how close attackers are to critical assets… a full timeline of attacker activity once deceptions are engaged… how attackers perceive the deceptive data."
- Automated creation of "hundreds of thousands of deceptive Microsoft Word and Excel documents… indistinguishable from the genuine article, right down to the usage of company logos and letterhead… loaded with fake data that sets off an alert as soon as an attacker tries to use the information."
- ITDR Buyer's Guide deception-artifact catalog: browser histories, database connections, scanner data, emails and Teams messages, FTP/RDP/PuTTY/SSH sessions, scripts, file shares, Windows credentials, ransomware deception, ADRecon/Bloodhound deceptions, SWIFT and mainframe deceptions; "orphaned Active Directory objects as deceptive breadcrumbs"; "Use of the production AD system only" (no fake AD domain with trust).
- Real-time forensic data collection from the endpoint: "details about the who, what, when and where of the attack."
- Part of Proofpoint Identity Threat Defense platform (with Spotlight); SaaS deployment.

### T-Pot (Layer A — directly observed; open-source pole)

- "The all in one, optionally distributed, multiarch honeypot platform, supporting 20+ honeypots and countless visualization options using the Elastic Stack, animated live attack maps."
- Honeypot catalog: cowrie (SSH/telnet), dionaea (malware capture), conpot (ICS/SCADA), dicompot (DICOM), medpot, mailoney (SMTP), elasticpot, redishoneypot, sentrypeer (SIP), snare/tanner (web), etc.; plus LLM-based honeypots (Beelzebub, Galah) since 24.04.1.
- Distributed deployment: Hive (central) + Sensors (honeypot hosts) transmitting event data to the hive; Kibana dashboards, attack map, CyberChef.
- Community data submission to Sicherheitstacho by default (opt-out) — a research/community-data orientation absent from commercial platforms.
- Disclaimer: "Honeypots - by design - should not host any sensitive data."
- Placement guidance: put it where you "suspect intruders in or from (i.e. the internet)"; forward broad port ranges to it.

## Cross-product Comparison

| Dimension | Thinkst Canary | Fidelis Deception | SentinelOne Hologram/Identity | Proofpoint Shadow | T-Pot |
|---|---|---|---|---|---|
| Decoy assets | canary devices (hw/cloud/VM) + tokens (URLs, docs, keys, logins) | decoys, breadcrumbs, fake accounts, planted credentials/data | high-interaction decoys (OS, ICS, SWIFT, POS, IoT, cloud) + AD decoy credentials | agentless imitations of credentials/connections/data/systems + deceptive docs | 20+ honeypot daemons (SSH, ICS, mail, DB, web…) |
| Lures/breadcrumbs | Breadcrumbs (shortcuts, SSH config entries) | breadcrumbs, lures | (datasheet: misdirection) | orphaned AD objects, planted files, browser history | (placement guidance only) |
| Presumptive-malice premise | "attackers announce themselves"; tripwire framing | "inherently suspicious… eliminates false positives" (verbatim) | "lure… into engaging and revealing themselves" | "for the sole purpose of detecting their existence" | implicit (honeypot traffic = attack) |
| Engagement observation | incident objects w/ source details; syslog/webhook events | attacker behavior/techniques; sandbox detonation | TTP data, forensics, attack visualization, D3FEND mapping | full attacker timeline, proximity to crown jewels, "how attackers perceive the deceptive data", endpoint forensics | full session logs in Elastic Stack |
| Management plane | per-customer Console (EC2), Flocks, RBAC | management + terrain mapping + auto decoy lifecycle | Hologram Central Manager; Singularity console | Shadow management console; one-click deploy; auto-adjustment | Hive + Kibana (self-managed) |
| Noise control | hostname/source-port ignore lists, per-flock limits | high-confidence framing; terrain-aligned placement | high-confidence telemetry | tailored per-machine deceptions | n/a (research posture) |
| Deployment automation | mass deployment via Falcon/Jamf/SCCM/Ansible | automated create/deploy/test/update decoys | ML-assisted deployment | analyzes endpoint landscape, designs + deploys per machine | installer + Ansible sensor deploy |
| Packaging | standalone (+ free token service) | standalone or Elevate XDR module | Singularity XDR component | Identity Threat Defense platform component | open-source self-hosted |
| Insider threat | yes (token misuse scenarios, e.g. cloud-admin snooping) | (implied) | explicit ("insider threat actors") | explicit ("insiders and external attackers") | n/a |
| Primary customer tier | SMB → enterprise | enterprise/government | enterprise | enterprise | community/research, any |

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

Three jointly-held structures, plus one binding:

1. **The deception surface** — platform-created decoy assets of no production function (emulated hosts/services, planted credentials, deceptive documents/data, triggerable tokens) deployed into the organization's own environment. Remove → a detection platform with nothing fake to trip on (generic IDS/alerting).
2. **The presumptive-malice engagement signal** — any interaction with a decoy is treated as a high-fidelity indicator of malicious activity and surfaced as an alert to defenders, because no legitimate business path touches a decoy. Remove → a research honeypot/lab or an unmonitored trap.
3. **The engagement observation** — the platform captures what the interacting party did (protocol-level detail, commands, credentials used, lateral-movement path, source) for triage, forensics, and attacker intelligence. Remove → a bare tripwire alarm.

Binding: **defender-operated, centrally managed fleet inside the organization's own environment** — a management plane that deploys, configures, monitors, and reports on the decoy fleet. Remove the managed-fleet plane → a standalone honeypot/trap (the precursor form), not a platform.

Joint load-bearing tests:

- 1 alone = a decoy fleet nobody watches (research toy)
- 2 without 1 = generic alerting with nothing to alert on
- 3 without 1+2 = packet capture / EDR telemetry
- 1+2 without 3 = bare tripwire
- 1+3 without 2 = unmonitored observation station
- 2+3 without 1 = detection engine with no deception surface

### L1 — Common Mature Structure

Present across the sample but not definitional:

- Lures/breadcrumbs (breadcrumbs, planted files, browser history, orphaned AD objects pointing at decoys)
- Credential seeding (fake credentials in AD/memory/files; credential-misuse detection)
- Deployment automation and coverage guidance (terrain mapping, auto decoy generation, mass-deployment tooling)
- SIEM/SOC/notification integrations (webhook, syslog, Splunk, email)
- Incident/alert views with attacker timelines and proximity-to-crown-jewels context
- Forensics capture on engagement (packet capture, endpoint forensic collection, sandbox detonation)
- Decoy realism maintenance (auto-updating decoys to mirror the changing environment)
- Console RBAC (per-flock managers/watchers at Thinkst; console roles elsewhere)
- Noise tuning (ignore lists for scanners, per-flock limits)
- ATT&CK-family mapping / TTP reporting (SentinelOne D3FEND mapping observed; Fidelis mentions ATT&CK mappings in Elevate)

### L2 — Variant / Optional Structure

- Decoy form factor: hardware/virtual/cloud/container appliances; agentless endpoint deception; identity/AD deception; canary files on real shares; standalone tokens
- Scope emphasis: network-centric (Fidelis, Hologram) vs endpoint/identity-centric (Shadow, Singularity Identity) vs device+token simplicity (Canary)
- Packaging: standalone product vs module of XDR/ITDR suite vs open-source self-hosted platform vs free token service
- Philosophy: simplicity-first (Thinkst) vs automation-first (Proofpoint) vs forensics/terrain-first (Fidelis) vs suite-integrated (SentinelOne)
- Managed-service delivery variants (SaaS console vs self-hosted console)
- Community/research orientation (T-Pot's shared data submission) vs operational-defense orientation

### L3 — Vendor-specific Structure (research notes only)

- Thinkst: Birds/Flocks/Canarytokens/Breadcrumbs naming; per-customer EC2 console; per-flock canary limits and pending queues; specific token-type catalog; free Canarytokens service.
- Fidelis: "cyber terrain" mapping and risk analysis across terrains; Elevate XDR correlation; OT/ICS decoy emphasis; Active Directory Intercept sibling product.
- SentinelOne: Hologram/Identity product naming; ATT&CK D3FEND mapping; conditional-access disruption (session blocking, MFA re-auth) tied to deception; ASI correlation; Storyline timelines.
- Proofpoint: agentless posture ("can't be disabled or circumvented… like agent-based solutions"); automated deceptive-document generation at scale with company branding; "how attackers perceive the deceptive data" intel; production-AD-only design (no fake domain/trust).
- T-Pot: Sicherheitstacho community data submission; LLM-based honeypots; specific honeypot daemon catalog.

## Vendor-specific Findings

See L3 above. None of these are promoted to the canonical core. Notably, the agentless-vs-agent-based decoy realization, the terrain-mapping feature, and the token-type catalog are all implementation choices, not Type structure.

## Boundary Findings

- **vs Honeypot (precursor / research form)**: single standalone honeypots (Honeyd-era, single-host T-Pot) satisfy decoys + signal + observation but lack the managed-fleet management plane; the product category "deception platform" is the centrally managed operational form. T-Pot's distributed hive/sensor mode shows an open-source platform can satisfy the full core; its community-data orientation marks the research pole. The Type is defined by the operational-defense framing (production environment, SOC alerting, managed fleet), not by decoy realism alone.
- **vs SIEM**: the deception platform is a high-fidelity alert *source*; the SIEM aggregates and correlates. Every commercial sample forwards alerts to SIEMs (webhook/syslog/Splunk). Remove the decoys and keep aggregation → SIEM.
- **vs EDR / NDR**: those watch *real* assets for signs of evil; deception watches *fake* assets whose only function is to be touched. Complementary; several vendors bundle both (SentinelOne, Fidelis), which is packaging, not identity.
- **vs Breach & Attack Simulation / Security Validation** (ratifying the BAS pass's flag from this side): BAS runs *synthetic attacker behavior* against *real controls* and records control responses; deception plants *fake targets* for *real attackers*. Different actor (defender-emulated vs actual adversary), different object (attack simulation vs decoy asset). Keep both. CONFIRMED.
- **vs Threat Hunting Platform** (ratifying the threat-hunting pass's flag from this side): deception passively generates alerts from decoy engagement; hunting is human-initiated search. Deception hits can trigger hunts. Keep both. CONFIRMED.
- **vs Vulnerability Management / Attack Surface Management**: those discover and track *real* exposure; deception *creates* fake surface. Note the name collision: Illusive's legacy "Attack Surface Manager" was credential-exposure reduction (a deception-adjacent capability), not the ASM Type.
- **vs Insider Risk Management**: decoys also catch insiders (explicit in Proofpoint and SentinelOne material), but IRM's object is human behavior monitoring; deception's object is the decoy asset. Overlap acknowledged; keep separate.
- **vs IAM / ITDR**: identity deception (decoy AD objects/credentials) overlaps ITDR territory; SentinelOne and Proofpoint package deception inside identity-threat platforms. The deception core (fake assets + presumptive-malice signal) is distinct from access management or identity-threat analytics; the overlap is a packaging seam.
- **"Remove what to become the other type" tests**: remove decoys → generic detection/alerting; remove presumptive-malice framing → research honeypot/lab; remove observation → bare tripwire; remove management plane → standalone honeypot; remove fake assets and keep synthetic attacks → BAS; remove the environment-internal binding and point traps at third parties → not this Type.

## Historical / Market-Sample Check

- The Type descends from honeypots (Honeynet Project, Honeyd, LaBrea, KFSensor era, late 1990s–2000s). Those satisfy decoys + interaction-as-signal + observation, but were typically single traps or research collections without a managed fleet or operational SOC integration — the precursor, not the platform.
- T-Pot (open source, actively maintained) satisfies the full core including a distributed hive/sensor management model — confirming the Type is not defined by commercial packaging.
- Free token-only services (Canarytokens) satisfy the tripwire legs (decoy artifact + presumptive-malice alert) without emulated hosts — confirming that emulated *hosts* are a common form, not the invariant; the invariant is the decoy *asset* of no production function.
- The check passes: older, open-source, and token-only forms all fit the three-structure core; nothing in the core is tied to the current enterprise-suite packaging moment.

## Uncertainties

- Acalvio ShadowPlex unreachable (503 ×2 on 2026-09-10); the enterprise autonomous-deception pole is covered by Fidelis/SentinelOne/Proofpoint instead. No Acalvio-specific claims are made.
- Precise operational facts (decoy-count limits, pricing, deployment sizing, exact notification latency) were not researched and are not stated anywhere.
- SentinelOne and Proofpoint evidence comes partly from datasheets/solution briefs (marketing-adjacent Tier 2) rather than operational help centers; workflow claims for those two are kept at the level the sources support.
- Market trend: deception is increasingly bundled into XDR/ITDR suites (SentinelOne, Fidelis, Proofpoint) while Thinkst remains standalone; whether the standalone category persists is a market question, not a structural one — not resolved here.

## Final Synthesis

A Deception Platform is a defender-operated security system whose defining core is three jointly-held structures: (1) a deception surface — decoy assets of no production function deployed into the organization's own environment; (2) a presumptive-malice engagement signal — any interaction with a decoy surfaced as a high-fidelity alert, because no legitimate business path touches it; (3) engagement observation — capture of what the interacting party did, for triage, forensics, and attacker intelligence — all held together by a central management plane over the decoy fleet. Lures, credential seeding, deployment automation, SIEM integration, forensics capture, and decoy-realism maintenance are the common mature structure; form factor (appliance/agentless/identity/token), scope emphasis, packaging (standalone vs suite vs open source), and philosophy are variant axes. The Type's boundaries: it is the fake-target complement to EDR/NDR (real assets), the passive-alert complement to threat hunting (human-initiated search), and the real-adversary complement to BAS (synthetic attacks); its precursor is the honeypot, from which it differs by the managed fleet and operational-defense framing.
