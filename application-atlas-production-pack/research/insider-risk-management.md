# Research Notes — Insider Risk Management

Research date: 2026-09-08
Directory leaf: Insider Risk Management (§15 Cybersecurity, Identity & Trust)
Slug: insider-risk-management

---

## Research Goal

Understand what an Insider Risk Management (IRM) application actually is as a software type: its defining structure, its core objects, its detection→triage→disposition workflow, its privacy governance layer, and its boundaries against the neighboring security/HR types (DLP, SIEM/UEBA, employee/user activity monitoring, corporate investigation management, fraud prevention).

## Initial Boundary (pre-research hypothesis)

- Core use: detect, evaluate, and manage risk posed by the organization's own people (employees, contractors) — data exfiltration, IP theft, sabotage, policy violation, fraud.
- Primary users: security/compliance analysts and investigators; HR/Legal participate in escalation.
- Nearest neighbors: DLP (content-centric), SIEM/UEBA (analytics-centric), User Activity Monitoring / employee monitoring (visibility without risk workflow), Corporate Investigation Management (formal legal investigation), Fraud Prevention (transaction-centric).
- Unknowns at start: whether the "case" object is definitional; whether privacy guardrails (pseudonymization) are definitional; whether enforcement/blocking is definitional.

## Research Questions

1. What is the core subject of record — alert? case? user risk profile? How do they relate?
2. What telemetry sources feed the system (endpoint agent, email, cloud, web, print/USB, HR systems)?
3. How is "risky" defined and scored (policies, indicators, thresholds, baselines, ML)?
4. What is the end-to-end workflow from signal to disposition?
5. Are privacy guardrails (pseudonymization, RBAC, audit) a stable structural layer?
6. How do HR/lifecycle signals (departures, stressor events) participate?
7. Where does the workflow end — what dispositions and escalations exist?
8. What separates IRM from DLP / UAM / SIEM / investigation management in observable product structure?

## Representative Products

| Product | Vendor positioning | Customer tier | Product philosophy | Evidence quality |
|---|---|---|---|---|
| Microsoft Purview Insider Risk Management | compliance solution inside M365/Purview suite | enterprise, suite-embedded | privacy-by-design compliance workflow; detection + triage + escalation, no inline blocking | Tier-1 (Microsoft Learn, 3 pages fetched) |
| DTEX (dtex.ai) | standalone "risk-adaptive security platform" for human/data/AI risk | enterprise, government | endpoint behavioral telemetry + forensics + threat hunting; separates IRM from its DLP/UAM/UEBA capabilities | Tier-2 (vendor site, 2 pages) |
| Teramind | insider threat detection / employee monitoring platform | SMB → enterprise, MSP channel | monitoring-first: high-fidelity endpoint telemetry, session replay, real-time blocking; sells Employee Monitoring and Insider Risk as separate solutions on one substrate | Tier-2 (vendor site, 1 rich page) |
| Mimecast Incydr (formerly Code42 / Incydr) | "adaptive data protection" / insider risk & data protection | mid-market → enterprise | data-exfiltration-first: file-movement telemetry across endpoint/email/cloud/browser, risk scored "tied back to your people", adaptive controls | Tier-2 (vendor site, 1 page) |

Proofpoint Insider Threat Management (former ObserveIT) was originally sampled as a fifth product; three fetch attempts (product page ×2, docs domain ×1) failed (404/transport). Dropped per source-access rules; not replaced with memory-based detail. Teramind's own comparison table characterizes "Proofpoint ITM" (role-based permissions, video session replay) — vendor-claimed, kept out of all canonical claims.

## Sources

- Microsoft Learn — "Learn about Insider Risk Management": https://learn.microsoft.com/en-us/purview/insider-risk-management (fetched 2026-09-08)
- Microsoft Learn — "Take action on Insider Risk Management cases": https://learn.microsoft.com/en-us/purview/insider-risk-management-cases (fetched 2026-09-08)
- Microsoft Learn — "Create and manage Insider Risk Management policies": https://learn.microsoft.com/en-us/purview/insider-risk-management-policies (fetched 2026-09-08)
- DTEX — homepage: https://dtexsystems.com/ (redirects to https://www.dtex.ai/) (fetched 2026-09-08)
- DTEX — "Insider Risk Management" capability page: https://www.dtex.ai/capabilities/insider-risk-management/ (fetched 2026-09-08)
- Teramind — "Insider Threat Detection" solution page: https://www.teramind.co/solutions/insider-threat-detection (fetched 2026-09-08)
- Mimecast — "Mimecast Incydr" product page: https://www.mimecast.com/products/incydr/ (fetched 2026-09-08)

Source-access limitation: no Tier-1 help-center documentation was reachable for DTEX, Teramind, or Incydr during this pass (only vendor marketing/product pages; support portals are login-gated or not attempted after product-page failures). Product-structure claims from those three are therefore calibrated as Tier-2 evidence; precise operational details are not asserted. Proofpoint is recorded as unreachable (3 failures).

---

## Product A — Microsoft Purview Insider Risk Management

### Key observations (Evidence layer A unless noted)

- Self-definition: "a compliance solution that helps minimize internal risks by enabling you to detect, investigate, and act on malicious and inadvertent activities in your organization." Risk classes named: data leakage/spillage, confidentiality violations, IP theft, fraud, insider trading, regulatory compliance violations, security violations.
- Stated design principles: Transparency (privacy by design), Configurable (policies by industry/geography/business group), Integrated (workflow across Purview), Actionable (reviewer notifications, data investigations, user investigations).
- Workflow is explicitly: Policies → Alerts → Triage → Investigate → Action.
- Policies: created from predefined templates (data theft by departing users; data leaks; data leaks by priority users / risky users; security policy violations ×4; patient data misuse; risky AI usage; risky browser usage; risky agents). A policy defines: users/groups in scope, which risk indicators are active, thresholds, content priorities, detection windows, and a triggering event that brings a user into active scoring (e.g., a DLP policy match, an HR-connector departure date, an Entra account deletion, a Defender for Endpoint alert). Policy health dashboard reports misconfiguration (missing indicators, no triggering event, HR connector not uploading, no devices onboarded, volume limits).
- Triggering events gate scoring: "Risk scores won't be assigned to user activities until … a triggering event" (policy-health message). Manual override: "Start scoring activity for users" adds users to policies immediately for a bounded period with a stated reason, bypassing the trigger; also CSV import of user lists.
- Indicators generate alerts when policy conditions match; alerts carry status (Needs review / Confirmed / Dismissed / Resolved) and severity (High/Medium/Low); alert queue + triage dashboards.
- Cases are "the core of Insider Risk Management": created by confirming an alert; each case focuses on one user; multiple alerts attach to the case. Case status Active/Closed; resolution classifications: Benign or Confirmed policy violation, with recorded "Action taken" reasons; notes are permanent (analyst notes + system-generated notes for status/assignment/escalation changes); contributors with temporary access grants; content download to case (Content explorer holds copies of files/email associated with alert activities); forensic evidence tab (visual captures); Activity explorer (timeline of risky activity); user risk score shown on case and recalculated periodically from active alerts plus "risk score boosters" (high-impact user, priority user group membership).
- Priority content: SharePoint sites, sensitive info types, sensitivity labels, file extensions, trainable classifiers raise scores; policies can be scoped to score only priority-content activity. "Cumulative exfiltration detection" uses ML against organization/peer-group norms (peer groups built from SharePoint usage, org hierarchy, or job titles). Sequence detection groups ordered activities into collection → exfiltration → obfuscation → clean-up.
- HR integration: HR connector (required for departing-user and risky-user templates) imports employment dates and stressor events (performance improvement, demotion); policy health warns when the connector stops uploading. Power Automate case flows: request information from HR, notify the user's manager, create ServiceNow records, notify users added to a policy.
- Actions on a case: send email notice from notice templates (reminder/training); escalate to eDiscovery (Premium) (creates a legal case with preservation/hold workflow); share with ServiceNow or email; resolve (Benign / Confirmed policy violation). Alerts can be exported to SIEM via Office 365 Management APIs.
- Privacy by design: "users are pseudonymized by default, and role-based access controls and audit logs are in place"; separate role groups (IRM / IRM Analysts / IRM Investigators); anonymization toggle; per-case contributor model; dedicated IRM audit log; administrative-unit scoping (region/department views).
- Analytics mode: evaluate potential insider risk across anonymized user activity without any configured policies; feeds policy recommendations and quick policies.
- Adaptive Protection associates insider risk levels with users (referenced via policy deletion warning). (Layer A for existence; details not explored.)
- Agent policies: policy dashboard separates "User policy" vs "Agent policy" (Copilot Studio / Foundry agents) — 2026-era extension of the insider concept to AI agents.

## Product B — DTEX

### Key observations

- Positions Insider Risk Management as a named capability of its platform, distinct from sibling capabilities: Risk-Adaptive DLP, User Activity Monitoring, UEBA/Behavior Analytics, Privacy & Trust, AI Risk Management. (A — the vendor itself treats IRM ≠ DLP ≠ UAM ≠ UEBA as product partitions.)
- IRM definition: "focuses on human risk, combining behavioral context, user activity monitoring (UAM), and deep visibility into how people interact with data and AI to surface intent and prevent insider-driven breaches." (A)
- Platform model: endpoint-collected "high-fidelity metadata, on and off network, 24/7, whether data is important at the time or not" → "patterns of behavior" correlation → "score behavioral intent": deviations mapped to "malicious, careless or compromised." Behavioral analytics "correlates multiple activities across devices into one risk score" (A — per-person risk aggregation).
- Behavioral indicators of risk framed as early warnings: "flight risk, overwork, system sabotage, or the precursors to data exfiltration." (A)
- "Insider Threat Kill Chain": visibility across stages "to identify, stop and investigate data loss attempts before exfiltration." (A — marketing framing)
- Threat hunting: proactive hunting for "low-and-slow" insiders over the insider-risk dataset with a query language and custom visualizations. (A)
- Use cases: organization leavers/joiners, privileged account misuse, shadow AI, foreign interference, third-party/contractor risk. (A)
- Privacy: "Pseudonymization" listed as a Privacy & Trust capability ("removes personal identifiers from activity data… eliminates… inherent bias") — opt-in capability, not stated as default. (A)
- Agentic AI triage/hunting/assistant agents (Triage Guardian "before elevating risk to analysts" — analyst triage remains the human gate). (A)
- Enterprise/government orientation; i3 insider-investigation services; MITRE association; government use cases. (A/B)

## Product C — Teramind

### Key observations

- Self-definition: "Insider Threat Detection Software for User Risk Monitoring and Data Protection"; "privacy-first insider threat monitoring with UEBA, providing full visibility into human operations and agentic AI." (A)
- Mechanism as stated: endpoint monitoring → activity logs with privacy safeguards (RBAC, PII/PHI masking, GDPR/HIPAA alignment) → UEBA baselines for "users, peer groups, and system entities" → anomaly detection → ML risk scores "assigned to incidents… so security teams can focus on urgent threats" → real-time policy enforcement ("customizable rule engines to proactively block unauthorized uploads, risky file access, or suspicious data movement in real-time") → "defensible audit evidence through session replays, OCR keyword indexing, and detailed activity timelines." (A)
- Use cases: stop exfiltration (uploads to unauthorized cloud, USB, printing/screen capture, personal email/messaging/AI tools); workplace toxicity/harassment detection; sabotage and financial fraud; privileged users; non-human identities/agentic AI; contractors/distributed teams; "Investigate Incidents with Defensible Evidence… support HR or legal proceedings." (A)
- Own taxonomy distinction: "Detection: identifying anomalous patterns…; Monitoring: gaining visibility…; Management: the holistic program encompassing governance, cross-functional working groups, policies, technical controls, incident response workflows, and employee training." (A — vendor articulates that the software is one instrument of a management *program*; useful calibration that "management" ≠ auto-adjudication.)
- Sells Employee Monitoring (workforce analytics/productivity) and Insider Risk Management (cybersecurity) as separate solution lines over the same monitoring substrate — evidence that the *job*, not the telemetry, defines the type. (A)
- Positions against DLP/SIEM/EDR: "DLP tools identify sensitive files based on static content rules but lack intent context. Teramind supplies behavioral history and visual evidence to reveal why data is moving and whether the action is legitimate." (A — vendor framing)
- Comparison table characterizes Proofpoint ITM, DTEX, Mimecast Incydr. (A as Teramind's claim; B-level at best for the competitors.)

## Product D — Mimecast Incydr

### Key observations

- Mimecast nav labels the solution family "Insider Risk Management & Data Protection"; Incydr is the product ("Address all forms of insider threats"). Use-case list includes "Internal Investigations." (A)
- Self-definition: "See and stop data exfiltration everywhere it happens, whether a human or AI agent is behind it… Mimecast Incydr sees, scores, and intelligently protects your data from day one. No tagging, no policies to configure." (A — the no-config claim is marketing positioning; the *scoring + protection* shape is the structural content.)
- Risk surfaces enumerated: "Email, endpoint, cloud, browser, and agentic, all visible from day one, scored for risk, and tied back to your people." (A — risk attributed to persons)
- Adaptive controls: "in-the-moment education to allow-with-justification to targeted blocking… an automated response that matches the risk"; scenarios named: "departing employees, unsanctioned MCP connections, movement of sensitive data, and shadow AI tools or agents." (A)
- Integrations: HCM, EDR/XDR, IAM "for risk context"; SIEM streaming (Splunk: "alerts and file activity… top exfiltration destinations, highest-risk users, and file events"), SOAR (Cortex XSOAR), EDR (CrowdStrike). (A)
- Privacy-by-design framing: lightweight agent, browser extension "only watches for risky data movement, not invasive probing." (A)
- Dashboards: AI agents, shadow AI, cloud storage, source-code movement; MIP tags + AI content inspection for PII/PCI. (A)
- Agent Risk Center: discovers AI agents, classifies their activity against rules, applies controls. (A)

---

## Cross-product Comparison

| Dimension | Microsoft Purview IRM | DTEX | Teramind | Incydr |
|---|---|---|---|---|
| Subject of risk | person (user); cases are per-user; user risk score | person; one risk score correlated across devices | person (user/peer-group baselines); risk scores on incidents | person; risk "tied back to your people" |
| Telemetry | M365 service logs (email/SharePoint/Teams/Entra), optional Defender endpoint signals, optional device indicators, forensic-evidence captures, HR connector | endpoint agent metadata, on/off network, continuous | endpoint agent (apps/web/files/USB/print/screen), session recording | endpoint agent + email/cloud/browser APIs, file-event telemetry |
| Risk definition | policy templates + indicators + thresholds + triggering events + priority content + sequence/cumulative-exfiltration ML | behavioral indicators (flight risk, overwork, sabotage, exfiltration precursors) + intent scoring | UEBA baselines + anomaly detection + rule engines + ML risk scoring | scored file-exfiltration risk out of the box; rules optional; adaptive scenarios (departing employees) |
| Alert/triage | explicit alert queue with statuses + severity; triage dashboards | alerts + Triage Guardian agent feeding analysts | risk-scored incident prioritization for security teams | scored risks + dashboards; adaptive response |
| Investigation | per-user case with activity explorer, content copies, forensic evidence, notes, contributors | hunting over behavioral dataset; i3 investigator services | session replay, OCR search, timelines as "defensible evidence" for HR/legal | file-level investigation; internal-investigations use case |
| Disposition | resolve Benign / Confirmed policy violation; notice; escalate to eDiscovery; SIEM/ServiceNow export | elevated to analysts / hunt output; containment via integrations | blocking/enforcement; evidence hand-off to HR/legal | education nudge / allow-with-justification / blocking; SIEM/SOAR |
| HR/lifecycle signals | HR connector (departures, stressor events) is a first-class input | leavers/joiners use case | contractors/HR/legal proceedings | departing-employee scenario; HCM integration |
| Privacy governance | pseudonymized by default, RBAC, audit log, anonymization toggle, admin-unit scoping | pseudonymization as a privacy capability | RBAC, PII/PHI masking, compliance alignment | lightweight/least-invasive collection framing |
| Enforcement | none inline (feeds DLP/Adaptive Protection) | via Risk-Adaptive DLP / integrations | real-time blocking native | adaptive: educate→justify→block |
| Packaging | suite module (compliance portal) | standalone platform, capability-partitioned | standalone platform; sibling Employee Monitoring line | standalone product inside human-risk suite |

## Abstraction Synthesis

### L0 — Defining Invariant

Three jointly-held structures; remove any one and the product stops being an Insider Risk Management application:

1. **The insider as the subject of record.** The organization's own people — employees, contractors, privileged users, and (newest) delegated AI agents — are held as identified entities to which observed activity and risk are attributed and accumulated. Risk is a property of persons, not of hosts, network segments, or transactions. (Remove → infrastructure monitoring / SIEM / fraud detection territory.)
2. **Risk evaluation of observed insider activity.** The system continuously collects evidence of what insiders do across organizational workplace systems (endpoints, email, collaboration and file services, web, removable media — the channel set is open-ended) and evaluates that activity against defined risk indicators/policies/scoring models, producing ranked human-risk signals (alerts, risk levels, risk scores) that prioritize which people and episodes warrant attention. (Remove → passive user-activity monitoring / raw telemetry store.)
3. **The human triage-and-disposition loop.** Security/compliance reviewers investigate prioritized signals in context (activity history, content, visual/forensic evidence), decide per person/episode whether the behavior is benign or a genuine risk, and route an outcome — dismiss, keep monitoring, notify/educate, or escalate to HR/legal/security response — with the system retaining the record of signals, evidence, judgment, and outcome. (Remove → a scoring engine or alert feed; the "management" is gone.)

Jointly-held is load-bearing:
- 1 alone = employee/user activity monitoring or an HR roster with surveillance.
- 2 alone = UEBA/rules engine; generic anomaly scoring.
- 3 alone = generic case-management tool.
- 1+2 without 3 = a risk dashboard; detection without management.
- 2+3 without 1 = generic security alert triage with no insider subject.
- 1+3 without 2 = an investigation log with no systematic detection.

### L1 — Common Mature Structure

- Alert queue with statuses (needs review/confirmed/dismissed/resolved-class states) and severity/priority ranking.
- Per-user investigation workspace: activity timeline/explorer over the person's history; drill-down to content (files/email) involved; evidence attachments (content copies, screenshots/forensic captures, session replay where offered).
- Case/triage record with notes, contributing reviewers, and a recorded disposition (benign vs confirmed violation class).
- Privacy governance layer: RBAC segmentation of who may see identified vs de-identified activity; pseudonymization/anonymization options (default-on in at least one product); audit trails of reviewer actions; masking of personal data.
- HR/identity integrations and lifecycle scenarios: departing-employee detection (leavers), stressor-event-informed policies, priority-user groups (executives, admins), contractor/third-party populations.
- Interop outward: SIEM export/streaming, SOAR/ticketing (ServiceNow-class), EDR context sharing, IAM/identity context.
- dashboards: risk overview, top-risk users, trend statistics; policy health/coverage reporting.

### L2 — Variant / Optional Structure

- Collection substrate: cloud-service-native signals only (no endpoint agent required) ↔ endpoint-agent-first forensics ↔ API/browser-extension collection.
- Enforcement posture: observe-and-escalate only (suite compliance model) ↔ inline blocking/response (monitoring-first model) ↔ adaptive graduated response (educate → justify → block).
- Privacy posture: pseudonymized-by-default ↔ configurable masking ↔ stealth monitoring modes.
- Detection sophistication: static indicators/rules ↔ UEBA baselines/peer groups ↔ ML sequence & cumulative-exfiltration models ↔ agentic-AI triage agents.
- HR mechanism: dedicated HR connector feeding employment events ↔ manual/CSV user-scoping ↔ HCM platform integration.
- Industry/scenario templates: healthcare patient-data misuse, regulated-industry compliance, shadow-AI/AI-agent oversight, DLP-triggered data-leak policies.
- Forensics depth: file/event timelines ↔ session recording with OCR ↔ visual forensic evidence captures.

### L3 — Vendor-specific (Research Notes only)

- Microsoft: Purview portal embedding; policy template names; eDiscovery (Premium) escalation; Adaptive Protection; Power Automate case flows; Teams case teams; Entra-based peer groups; notice templates; numeric policy limits and scoring-recalculation cadence; admin-unit scoping.
- DTEX: "Insider Threat Kill Chain" framing; metadata-count and activity-group marketing figures; patented-pseudonymization claim; i3 investigation services; agentic "Defenders" (Triage Guardian/Threat Hunter/Risk Assistant).
- Teramind: session replay + OCR indexing; stealth/visible monitoring modes; its four-vendor comparison table; "detection vs monitoring vs management" glossary; productivity/Employee Monitoring sibling line.
- Incydr/Mimecast: "no policies to configure on day one" positioning; Agent Risk Center; MCP gateway/Mihra agents; ROI/admin-time claims; FedRAMP plan variants.

## Rejected Findings (considered and NOT promoted)

- **Endpoint agent as definitional** — rejected: Microsoft's templates run on cloud-service signals without a mandatory endpoint agent; Incydr is API/browser-led. Collection substrate is a variant.
- **ML/behavioral baselining as definitional** — rejected: rule/indicator-based scoring is a complete, supported posture; ML is the modern common case, not the invariant.
- **Inline blocking as definitional** — rejected: Microsoft Purview IRM (the market's reference compliance implementation) does not block; enforcement is a variant posture.
- **Pseudonymization-by-default as definitional** — rejected: it is one pole of the privacy-posture variant (Teramind's monitoring-first pole sits in the same type); the privacy *governance layer* is L1, its default setting is L2.
- **HR connector as definitional** — rejected: the mechanism varies (connector/CSV/manual/HCM integration); the lifecycle scenario (departures/priority users) is L1, the mechanism L2.
- **"Case" object as a strict invariant** — softened: the per-person triage/disposition loop is invariant; whether it is implemented as a named case object (Microsoft), a hunting workflow (DTEX), or an investigation use case (Incydr) is product shape.
- **AI-agent oversight as definitional** — rejected: 2026-era extension present in sampled products' newest releases; the type predates it by a decade.

## Boundary Findings

- **vs Data Loss Prevention / DLP**: DLP's center of gravity is content — identify sensitive content by policy and protect/control its movement (block, wrap, encrypt). IRM's center is the person — accumulate behavioral risk, judge intent in context, disposition the human case. Observable seams: Microsoft documents DLP high-severity alerts as a *triggering input* to IRM policies (DLP feeds IRM); DTEX partitions Risk-Adaptive DLP and IRM as separate capabilities on one platform; Teramind positions its behavioral evidence as "why data is moving" versus DLP's static content rules. Remove the person-risk accumulation and triage loop, keep content rules + enforcement → DLP. Remove content inspection and keep the person loop → IRM. (Boundary requires joint review flag: many products bundle both; kept separate because each pole exists standalone with its own job.)
- **vs SIEM / UEBA**: analytics engines score events; IRM owns the person-level record and the disposition workflow, and exports alerts *to* SIEM (documented by Microsoft; Splunk streaming by Incydr). Remove the insider-subject case loop → alert analytics.
- **vs User Activity Monitoring / Employee Monitoring** (market category; no exact directory leaf — nearest: Productivity Activity Tracker, Digital Employee Experience Management): monitoring supplies visibility/productivity/compliance evidence; IRM adds risk evaluation and the disposition loop. Teramind sells both as separate solution lines on one substrate; DTEX lists UAM as a separate capability from IRM. Remove risk evaluation + disposition → monitoring.
- **vs Corporate Investigation Management (§11)**: formal legal/HR investigation case systems of record (matters, holds, findings) sit *downstream*: Microsoft escalates IRM cases into eDiscovery (Premium) rather than adjudicating discipline itself. IRM cases are risk-triage records, not legal matters.
- **vs Fraud Prevention Platform / Transaction Monitoring**: those center on customer transactions and accounts; IRM centers on workforce behavior against the organization. Fraud-by-an-insider appears in IRM as a scenario (Teramind lists financial fraud; Microsoft lists fraud among risk classes), but the transaction-graph machinery is not the IRM center.
- **vs EDR / XDR**: EDR is attacker/malware-centric endpoint response; IRM is behavior/intent-centric for authorized people (incl. compromised accounts as a scenario). EDR alerts can *feed* IRM scoring (Microsoft–Defender integration; Incydr–CrowdStrike integration).
- **vs Ethics & Conduct / Whistleblowing platforms**: those are report-initiated (a person reports conduct); IRM is observation-initiated (the system surfaces conduct from telemetry). Teramind's toxicity-detection use case straddles toward conduct monitoring, but its center remains security evidence.
- **Taxonomy check**: "Insider Risk Management" is used verbatim as a category name by Microsoft, DTEX, Teramind, and Mimecast — a real, established Type, not an alias or variant. Directory placement in §15 (Cybersecurity) is supported; the HR/finance adjacency does not warrant relocation.

## Historical / Market-Sample Check

Would older, regional, or differently positioned products fit the L0? Pre-ML insider-threat tooling (endpoint activity monitoring with policy-based alerting, reviewer triage, and case disposition — the classic government "insider threat program" toolchain) satisfies all three legs without ML, cloud, HR connectors, or adaptive controls. A manual-analyst variant (no scoring engine, reviewers working from search over activity logs) satisfies legs 1 and 3 and a degraded leg 2 — supporting the decision to phrase leg 2 as "evaluation against defined indicators/policies producing prioritized signals" rather than requiring a specific scoring technology. The definition does not depend on the current AI-agent or privacy-default moment.

## Uncertainties

- No Tier-1 operational documentation was reachable for DTEX, Teramind, or Incydr; their internal object models (whether alerts, cases, and risk profiles exist as named objects with specific states) are inferred from product pages at marketing granularity. Assertions about them are held at L1 strength ("mature products commonly…") rather than claimed as documented structure.
- Proofpoint ITM — one of the most-cited products in the category — is unverified this pass; its omission weakens coverage of the "ObserveIT-lineage" monitoring-first philosophy, partially compensated by Teramind's page.
- Whether the disposition loop is universal in the category's tail (very small-vendor UAM-with-risk-scoring products) is unverified; the boundary vs UAM could be fuzzier at the low end than the sampled enterprise tier suggests.
- Adaptive Protection (Microsoft) was only glimpsed via a policy-deletion warning; its mechanics were not researched.

## Final Synthesis

An Insider Risk Management application is an organization-side security/compliance system of record for managing the risk posed by the organization's own people. Its defining core is three jointly-held structures: (1) insiders as identified subjects to which observed activity and risk attach and accumulate; (2) continuous evaluation of workplace activity against defined risk indicators/policies into ranked human-risk signals; (3) a human triage-and-disposition loop that investigates prioritized signals in context, records a benign-vs-confirmed judgment per person/episode, and routes outcomes to monitoring, notification/education, or HR/legal/security escalation. Everything else — endpoint agents vs cloud signals, UEBA/ML, inline blocking, default pseudonymization, HR connectors, AI-agent oversight — is standard, variant, or vendor-specific structure, held out of the definition.
