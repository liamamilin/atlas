# Research Notes — Breach & Attack Simulation

Slug: breach-attack-simulation
Research date: 2026-09-06
Methodology: v1.1 (update-v1/). Evidence layers: A = directly observed on an official source fetched in this pass; B = cross-product commonality across the sample; C = canonical inference from cross-product comparison and boundary reasoning.

---

## Research Goal

Understand what a Breach & Attack Simulation (BAS) application actually is as a software type: its core objects, the execution/validation loop, who operates it, what rules make it safe and credible, and where its boundary sits against Vulnerability Management, Penetration Testing Management, Attack Surface Management, Security Validation (sibling leaf), SIEM/SOC tooling, Deception, and Security Awareness products.

## Initial Boundary

Working hypothesis before research:

1. Core use: safely emulate real attacker techniques against the organization's own production security controls and record whether those controls prevent/detect/log each one.
2. Primary users: security engineering, SOC/blue teams, detection engineers, red/purple teams, CISO for reporting.
3. Nearest neighbors: Vulnerability Management, Penetration Testing Management, Security Validation Platform (sibling leaf), Attack Surface Management, SIEM, Deception Platform, Security Awareness Platform, Threat Intelligence Platform.
4. Likely boundary: BAS answers "do my deployed controls stop this attack behavior?"; VM answers "where is software vulnerable and what should be patched?"; ASM answers "what of ours is exposed on the outside?"; PTM manages human-led engagements.
5. Unknowns: exact object model (technique vs scenario vs campaign), outcome taxonomies, how safety is enforced, how deep the "security validation" umbrella overlaps the sibling leaf.

## Research Questions

- What is a "simulation" concretely (unit of attack content, delivery mechanism)?
- What does the system execute against (which controls, which vantage points)?
- What outcome states exist and how are they attributed (control prevented / detected / logged / missed)?
- How is safety guaranteed (non-destructive execution in production)?
- How is attack content organized and kept current (ATT&CK, threat actors, scenarios, custom chains)?
- What is the operational loop (run → observe → report → fix → re-test)?
- Who uses it and what surfaces do they face?
- What integrations make the result actionable (SIEM, SOAR, ticketing)?
- Where is the line vs pentest/VM/ASM, and vs the "security validation" umbrella naming?

## Representative Products

Selection rationale: market representativeness + different product philosophies + different delivery models + a vendor-neutral open-source anchor for the historical check.

| Product | Philosophy / position | Evidence level in this pass |
|---|---|---|
| Picus Security | BAS pioneer; technique-level validation; "Autonomous Exposure Validation Platform" with BAS as one product | A (official BAS product page + platform page fetched) |
| SafeBreach | BAS-native vendor repositioned as CTEM / "Exposure Validation Platform"; published a category-defining BAS guide | A (official BAS guide page fetched; product structure from site nav) |
| Pentera | Full-path automated security validation ("real exploitation, not simulation" pole); internal/external/cloud kill-chain emulation | A (official platform page + ASV definition page fetched) |
| Apache Caldera (ex MITRE Caldera) | Open-source adversary-emulation platform; explicitly "designed to run autonomous breach-and-attack simulation exercises" — platform-native/historical check | A (official site + official docs fetched) |
| AttackIQ | Commonly cited BAS vendor | positioning only — attackiq.com returned 403 twice; no claims made |
| Cymulate | Commonly cited BAS / security-validation vendor | positioning only — cymulate.com returned 403 twice; no claims made |

## Sources

Official surfaces fetched 2026-09-06:

- Picus — Breach and Attack Simulation product page: https://www.picussecurity.com/platform/breach-and-attack-simulation
- Picus — Platform overview ("Autonomous Exposure Validation Platform"): https://www.picussecurity.com/platform (fetched as /platform root)
- SafeBreach — "What is breach and attack simulation (BAS)?" guide: https://www.safebreach.com/breach-and-attack-simulation
- SafeBreach — product structure evidence from site navigation (CTEM Platform, Exposure Validation Platform → Validate (BAS) + Propagate (attack path validation), SafeBreach-as-a-Service)
- Pentera — Platform page: https://pentera.io/platform/
- Pentera — "What Is Automated Security Validation (ASV)?": https://pentera.io/solution/what-is-asv/
- MITRE — Caldera contribution announcement: https://caldera.mitre.org/
- Apache Caldera — project page: https://caldera.apache.org/
- Apache Caldera — official documentation: https://caldera.readthedocs.io/en/latest/

Unreachable / degraded:

- AttackIQ — https://attackiq.com/ and /products/firedrill/ — HTTP 403 ×2 → abandoned per network rule; excluded from operational claims.
- Cymulate — https://cymulate.com/ and /platform/ — HTTP 403 ×2 → abandoned; excluded from operational claims.
- No vendor help-center / login-gated product documentation (SafeBreach support portal, Picus support) was accessed; all claims below stay at official product-page level.

## Product Observations

### Picus Security (evidence layer A)

From https://www.picussecurity.com/platform/breach-and-attack-simulation :

- Category definition (vendor-authored FAQ): "BAS is a technology that safely and continuously emulates real adversary techniques against your security controls to measure how they perform."
- Value proposition: "See what your EDR, SIEM, NGFW, WAF, email gateway and other controls block, detect, log, and miss." → four-level outcome vocabulary observed (blocked / detected / logged / missed).
- Closed loop: "When a control fails, Picus provides a vendor-specific fix and lets you re-run the same simulation to prove the gap is closed."
- Coverage surfaces enumerated: Web application attacks (WAF), Network attacks (NGFW & IPS), Endpoint attacks (EDR/XDR/AV), Data exfiltration (DLP), Email attacks (email gateway), Malicious traffic (URL filtering).
- Content machinery: "Picus Threat Library" (vendor-claimed 30,000+ TTPs, thousands of scenarios; maintained by Picus Labs with a 24-hour SLA for critical threats) + "Picus Mitigation Library" (vendor-specific prevention signatures and detection rules). Numeric figures are vendor claims — recorded as L3.
- MITRE ATT&CK mapping of results ("map coverage and gaps at a glance").
- Customization: "Picus Threat Builder — chain attack actions and upload custom payloads"; AI Threat Builder turns threat reports/CVE IDs/actor names into ATT&CK-mapped runnable simulations.
- Reporting: executive reports, custom dashboards, readiness/performance trends, peer benchmarking.
- Safety: FAQ — "designed to validate security controls safely in production without disrupting users, systems, or business operations."
- Compliance framing: supports requirements for regularly testing the effectiveness of technical measures (GDPR, ISO 27001, PCI DSS, NIST 800-53 named).
- Platform context: BAS is one of three products (BAS / Autonomous Penetration Testing / Exposure Validation); platform positions a continuous validation loop (ingest exposures → route by testability → validate → decide → ticket (Jira/ServiceNow) → revalidate).
- From customer reviews displayed on the page: "customize the campaign or schedule the assessment periodically, to test protection measure implemented on network, endpoint and email" → scheduling/periodic assessment observed; 75+ integrations claim.

### SafeBreach (evidence layer A)

From https://www.safebreach.com/breach-and-attack-simulation (vendor-authored category guide):

- Category definition: "BAS is a highly automated solution that safely runs real-world attacks against production applications and infrastructure in an organization's own IT environment."
- Mechanism: "leverage the tactics, techniques, and procedures (TTPs) used by cyber adversaries to mimic real attacks… simulators are deployed in different areas of an organization's network to facilitate attack execution. Users can then continuously run attack scenarios to monitor whether the organization's security controls effectively detect, prevent, and mitigate the attacks. BAS platforms will aggregate simulation results in the form of visualizations, dashboards, and reports."
- Control coverage enumerated: DLP; email controls; endpoint controls (EDR/XDR); network controls (firewalls, NGFW, segmentation, IPS/IDS, network behavior/traffic analysis); SIEM controls; web controls (web gateways, proxies, URL filtering); cloud and container controls.
- Content: attack simulations informed by threat intelligence, research, and MITRE ATT&CK; number and quality of "preconfigured attack scenarios" / playbooks as a buying criterion; new alerts/vulnerabilities/TTPs added quickly.
- Prioritization: results "ranked by severity or potential impact", grouped by category (network/web/endpoint/email), by vendor and operating system; "before-and-after" metrics for remediation.
- Integrations: SIEM, SOAR, threat intelligence; "ingesting indicators of compromise (IOCs) and TTPs from threat intelligence feeds to create custom attacks"; API for moving data in/out; "dozens of security solutions" out of the box.
- Teams described: CISOs (risk decisions, board communication, budget), boards/executives, red teams (automate/streamline), blue teams (validate controls, prioritize remediation), purple teams, penetration testers (validate their own results), threat-intelligence teams (choose what to run), security operations (validate SIEM/SOC detection), security engineers (guard against security drift, validate configuration).
- Category comparisons stated by the vendor: BAS vs penetration testing (manual, point-in-time, skill-dependent vs continuous validation), BAS vs red teaming (cost/scaling), BAS vs attack path management / ASM / VM ("identify possible attack paths… don't involve actual attacks… don't trigger any controls"; "ASM provides crucial knowledge about attack surfaces and vulnerabilities, while BAS validates security controls and identifies gaps").
- CTEM framing: BAS most impactful in the validation and prioritization phases of the CTEM cycle.
- Product structure (nav): CTEM Platform; "Exposure Validation Platform" with products "Validate" (BAS) and "Propagate" (attack path validation); "SafeBreach-as-a-Service" (managed delivery).

### Pentera (evidence layer A)

From https://pentera.io/platform/ and https://pentera.io/solution/what-is-asv/ :

- Positioning: "Security Validation Platform for Exposure Reduction"; category self-name "Automated Security Validation (ASV)"; "challenges the entire IT attack surface (internal, cloud, and external) by safely emulating attacker behavior, delivering real-time security validation at enterprise scale."
- Products: Pentera Core ("execute complete kill chains to expose how an attacker can bypass security, move laterally, escalate privileges, and reach critical assets within your internal environments"), Pentera Surface ("run real attacks to prove how attackers can gain initial access through web applications, internet-facing systems, and exposed identities"), Pentera Cloud (cloud identity and hybrid environments), Pentera Resolve ("prioritize and fix validated attack paths with automated remediation, then re-test to confirm measurable exposure reduction").
- ASV pillars: "Low touch" (agentless security validation anywhere), "Continuous coverage" (anytime, on-demand, across the entire attack surface, external & internal), "Real attacks" ("emulate the latest tactics, techniques, and procedures").
- Comparison table on the ASV page: Vulnerability Assessment / Breach & Attack Simulation / Penetration Testing / External Attack Surface Management as distinct approaches; Pentera row claims "Real exploitation / no simulation" — a deliberate philosophy pole within/next to the BAS category.
- Loop: Ingest & Normalize → Deduplicate → Enrich → Prioritize → Assign & Route (tickets to owners) → Revalidate ("re-test to ensure exposure reduction", audit-ready proof).
- Roles enumerated: vulnerability management teams, SOC managers/blue teams, red teams/pentesters, CISO/executives, compliance/governance teams, cloud architects.
- Compliance: maps validated findings to controls, records runs, revalidation results, and control responses for frameworks (PCI DSS, SOC 2, ISO 27001, NIST, DORA, NIS2…); "Controlled execution with audit proof" (nav).
- Technique examples observed: credential/password cracking against Active Directory ("Credential Exposure"), ransomware emulation tests to assess EDR effectiveness.
- Services: SECTOR11 adversarial testing services (managed), Security Validation Advisory.

### Apache Caldera — open-source anchor (evidence layer A)

From https://caldera.mitre.org/ , https://caldera.apache.org/ , https://caldera.readthedocs.io/en/latest/ :

- Self-description: "an adversary emulation platform designed to easily run autonomous breach-and-attack simulation exercises"; "simulates real-world cyber attack behaviors so organizations can test, validate, and improve their defenses"; built on MITRE ATT&CK; used for red teaming, purple teaming, security validation, research. (MITRE contribution to Apache Incubator announced May 2026; "nearly a decade of development".)
- Core object model (official docs): Agents (deployed on hosts, report back over C2 contacts), Abilities (individual attack actions/TTPs with executors and payloads, ATT&CK-mapped), Adversary Profiles (ordered collections of abilities emulating a threat actor or behavior chain), Operations (a run of an adversary profile against the agent population; can be scheduled), Operation Reports / event logs (per-step results), plus Facts/Fact Sources, Planners (decision logic), Objectives (goals).
- Delivery: self-hosted core system (C2 server with REST API + web UI) and plugins (TTP collections e.g. Stockpile; reporting e.g. Debrief; ATT&CK visualization e.g. Compass; agents e.g. Sandcat; roles/access plugin).
- Use cases: autonomous adversary emulation; "test & evaluation of detection, analytic and response platforms… network & host defenses, logging & sensors, analytics & alerting, and automated response"; manual red-team augmentation; research.

### Cross-check note

Three independent vendor definitions (Picus, SafeBreach, Caldera) converge on the same structure: safe/automated/continuous execution of real attacker behaviors inside the organization's own environment to test defenses. This supports a small L0 with high confidence (layer B → C).

## Cross-product Comparison

| Dimension | Picus | SafeBreach | Pentera | Caldera |
|---|---|---|---|---|
| Central content object | threat simulations in Threat Library (TTPs, scenarios) | preconfigured attack scenarios/playbooks informed by TI + ATT&CK | emulated attack paths / kill chains per environment | Abilities → Adversary Profiles |
| Execution substrate | agents + control-specific vectors (email/network/web/endpoint) | "simulators deployed in different areas of the network" | agentless ("low touch") + in-environment execution | self-hosted server + Agents on hosts |
| Controls under test | EDR, SIEM, NGFW, WAF, email gateway, DLP, URL filtering | DLP, email, EDR/XDR, network, SIEM, web, cloud/container | internal network, external perimeter, cloud/identity (defenses exercised en route) | network & host defenses, logging/sensors, analytics/alerting, automated response |
| Outcome vocabulary | blocked / detected / logged / missed | detect / prevent / mitigate | validated attack findings + revalidation | operation reports/event logs per step |
| ATT&CK mapping | automatic on results | content informed by ATT&CK | TTP emulation (ATT&CK referenced via red/purple use cases) | built on ATT&CK |
| Loop closure | vendor-specific fix + re-run same simulation | prioritize remediation; before/after metrics | Resolve: fix → re-test → proof of reduction | reports (plugin); manual follow-up |
| Content freshness | vendor research team + AI builder from intel | TI feeds → custom attacks (IOC/TTP ingestion) | vendor research (Labs) | community/vendor TTP plugins |
| Delivery | SaaS platform | SaaS + SafeBreach-as-a-Service | platform (SaaS/self-hosted posture not asserted) | open-source self-hosted |
| Umbrella naming | "Autonomous Exposure Validation Platform" (BAS = one product) | "CTEM Platform" / "Exposure Validation Platform" (Validate = BAS) | "Security Validation Platform" / ASV | adversary emulation platform |

## Canonical Model

### L0 — Defining Invariant

The smallest structure without which the product stops being recognizable as Breach & Attack Simulation:

1. **Executable attack-simulation content** — a maintained, first-class library of controlled attack enactments derived from real attacker behavior (individual techniques and/or chained scenarios), extendable/customizable.
2. **Controlled execution inside the organization's own environment** — the simulations are actually run (not merely inferred or checked) against the organization's deployed security controls, in a deliberately safe, non-destructive manner.
3. **Per-simulation recorded control response** — for each executed simulation, the system records how the defenses responded (prevented / detected / logged / nothing; exact labels vary by product), as the validation result.

Tests: remove the library → ad-hoc offensive tooling / a pentest toolkit, not BAS; remove in-environment execution → a threat-intelligence or exposure-inference product; remove the recorded control response → an attack launcher, not a validation system.

Historical/market-sample check: Caldera (open-source, platform-native, ~a decade old) satisfies all three without commercial scoring, benchmarking, or compliance modules; older practice analogs (manual red-team toolkits) satisfy none of them as a system property (no first-class validated-catalog + recorded per-technique control outcomes). L0 holds without over-fitting to the current "exposure validation" umbrella.

### L1 — Common Mature Structure

- MITRE ATT&CK mapping of attack content and/or results; coverage views organized by technique/tactic.
- Enumerated control-coverage surfaces: endpoint (EDR/XDR/AV), email gateway, network (NGFW/IPS/segmentation), web (WAF/proxy/URL filtering), DLP, SIEM/detection content, cloud/container.
- Execution machinery with deployment options: agents/simulators inside the environment; non-agent vectors (controlled email deliveries, web requests, network probes).
- Continuous/scheduled campaigns and on-demand runs.
- Result aggregation: dashboards, reports, severity ranking, grouping by control category/vendor; security-posture scoring/trends over time.
- Remediation guidance on failure (often vendor/control-specific) and re-test of the same simulation to prove closure (closed loop).
- Integrations: SIEM, SOAR, EDR, ticketing; APIs.
- Role model serving multiple functions: security engineering, SOC/blue team, detection engineering, red/purple team, threat intelligence, CISO/executive reporting; RBAC in enterprise products (Caldera exposes an access plugin; Pentera documents controlled execution with audit proof).
- Content freshness processes: vendor research teams, threat-intel ingestion (IOC/TTP → custom simulations).

### L2 — Variant / Optional Structure

- Philosophy pole: technique-level granular simulation (many small actions with per-technique outcomes) vs full-path kill-chain emulation (chained exploitation with end-to-end attack-path findings; Pentera explicitly claims "real exploitation / no simulation"). The two poles coexist inside the same market category and often inside one platform (Picus BAS vs APV/EXV; SafeBreach Validate vs Propagate).
- Delivery form: SaaS multi-tenant; self-hosted; open-source framework; fully managed service (vendor-run testing).
- Scope emphasis: endpoint-centric, email-centric, network-centric, cloud/identity-centric (e.g., AD password cracking), or whole-estate attack-path testing.
- Agent-based vs agentless validation.
- Umbrella expansion: BAS as one module of "security validation / exposure validation / CTEM" platforms alongside exposure inference, attack-path validation, automated pentesting, remediation orchestration.
- Scoring/benchmarking against peers; compliance-framework evidence mapping (GDPR/ISO/PCI DSS-style "regularly test effectiveness" requirements as a buying driver).
- Purple-team automation depth (auto-generated detection rules / SIEM content tuning).
- AI depth: intel→simulation builders, agent-orchestrated loops, natural-language interaction.
- Phishing as shared surface with Security Awareness tooling: BAS email simulations target mailbox/gateway controls. Whether sampled products ship employee-training-shaped phishing modules was **not observed** in the reachable sample (see Uncertainties); the boundary is drawn on the primary measured object (control response vs employee behavior).

### L3 — Vendor-specific (research notes only)

- Picus: Threat Library (vendor-claimed 30,000+ TTPs; 24-hour SLA for critical threats), Mitigation Library, AI Threat Builder (~9-minute claim), Picus Swarm AI agents, Blue Report / Red Report, Purple Academy, peer benchmarking, 75+ integrations claim, "2x control effectiveness in 3 months" style marketing figures.
- SafeBreach: SafeBreach Helm (AI infrastructure layer), Validate/Propagate product split, SafeBreach-as-a-Service, CTEM-platform positioning, SafeBreach Labs research hub, State of the Breach report.
- Pentera: Core/Surface/Cloud/Resolve product split, "Automated Security Validation (ASV)" trademark, Pentera Peer AI co-pilot, SECTOR11 services, ISO/IEC 42001 AI-governance framing, ASV-vs-BAS comparison table.
- Caldera: Ability/Adversary/Operation/Agent/Facts/Planners/Objectives object names, Sandcat agent, Stockpile TTP collection, plugin architecture, Apache Incubator governance (2026).
- AttackIQ / Cymulate: unreachable in this pass; no vendor-specific findings recorded.

## Boundary Findings

- **vs Vulnerability Management** (sharpest functional seam): VM discovers and manages software vulnerabilities (CVE-driven, asset population, patch lifecycle). BAS executes attacker behavior to observe whether deployed controls prevent/detect it. A fully patched-environment VM program can still fail BAS (misconfigurations, drift, blind spots); BAS never owns the patch/vuln-record lifecycle. Complementarity is explicit in vendor material (validated exploitability re-ranks the VM backlog).
- **vs Penetration Testing Management**: PTM manages human-led engagement lifecycle (scope, rules of engagement, findings, retest). BAS is automated, continuous, technique-level, and safe-by-design. Straddle: vendors sell "automated pentesting" (Pentera Surface/Core, Picus APV) — exploitation-led full-path emulation; the boundary is drawn at engagement-management vs continuous automated validation, and is a named tension inside the category (Pentera's "real exploitation / no simulation" claim).
- **vs Security Validation Platform (sibling leaf, unprocessed)**: umbrella overlap is real. All three commercial products in this sample self-name under "security validation" / "exposure validation"; G2 category = "Breach and Attack Simulation", Frost Radar category = "Automated Security Validation". If the sibling leaf is kept distinct, the workable seam is: BAS = the attack-execution-and-control-response surface; security validation (umbrella) adds non-execution verdict layers (e.g., Picus Exposure Validation "proves exploitability without firing an exploit") and program-level aggregation. **Joint-review flag recorded.**
- **vs Attack Surface Management** (sibling, already documented): ASM discovers and inventories the organization's externally exposed assets (outside-in, no pre-known asset list); BAS runs attacks against controls to record control response. SafeBreach states the complementarity directly ("ASM provides knowledge about attack surfaces… BAS validates security controls"). ASM feeds scope/intel into BAS; BAS can validate what ASM exposes.
- **vs SIEM / SOC tooling**: the SIEM is a control under test, not the validator. BAS generates known-bad activity with known-expected detection semantics; SIEM-facing use (detection engineering validation) is a primary L1 use case, not a separate type.
- **vs Deception Platform**: deception plants fake assets/credentials to catch real attackers; BAS runs synthetic attacker behavior against real controls. Different actor (defender-initiated vs attacker-initiated), different object (fake target vs simulated attack).
- **vs Security Awareness Platform**: both send phishing; awareness measures/trains employee behavior, BAS measures control response (email gateway, EDR). Where a BAS product ships people-focused phishing modules, it is a variant capability; the primary tracked object decides the type.
- **vs Threat Intelligence Platform**: TIP tracks external adversaries/indicators; BAS consumes TI (IOCs/TTPs) to build relevant simulations. Consumer vs producer of the same intelligence.
- **vs DAST**: DAST tests the security of the application itself; BAS web coverage (e.g., WAF testing) tests the protective control in front of the application.
- **"Remove what to become the other type" tests**: remove execution, keep vuln records → VM; remove automation/safety and make it human-led engagement → pentest; remove own-environment scoping → internet-wide scanning/ASM; remove attack content and keep fake assets → deception; remove control-response tracking → raw red-team tooling (Caldera's manual red-team mode is explicitly a secondary use, which supports this line).

## Uncertainties

- Exact outcome-state labels beyond Picus's blocked/detected/logged/missed were not verifiable for other vendors (help centers login-gated); the final document therefore says "labels vary" and uses the observed vocabulary as an example.
- Precision claims (library sizes, SLA windows, time-to-simulation figures, integration counts) are vendor marketing figures — kept in Research Notes as L3, excluded from the final document.
- Whether "agentless" in Pentera's sense eliminates deployed components entirely, or reduces them (its own page claims agentless validation "anywhere"), could not be verified at docs level; final document keeps deployment machinery at concept level (agents/simulators and/or agentless vectors).
- AttackIQ and Cymulate operational models unverified (403 ×2 each). Category membership of those two names is common knowledge but was not verified in this pass; the final document mentions them only with an explicit "not researched here" qualifier.
- Whether any sampled BAS product ships employee-training-shaped phishing (people-simulation) modules could not be confirmed; the awareness-platform boundary is therefore written purely on the primary-measured-object criterion, without claiming such modules exist in the sample.
- The exact relationship between the BAS leaf and the Security Validation Platform leaf cannot be settled unilaterally; recorded as a boundary issue for joint review.

## Final Synthesis

A Breach & Attack Simulation application is a validation system built around a maintained library of executable, real-world-derived attack simulations that are safely run inside the organization's own environment against its deployed security controls, with each simulation's control response (prevented / detected / logged / missed) recorded and aggregated into coverage and gap reporting. Mature products wrap this loop with ATT&CK mapping, scheduling, remediation guidance with re-testing, integrations into SIEM/SOAR/ticketing, multi-role reporting, and continuously refreshed content; delivery and philosophy vary along a technique-level ↔ full-path-emulation axis and a SaaS ↔ self-hosted ↔ managed ↔ open-source axis. The category is currently being rebranded from inside as "security validation" / "exposure validation", which overlaps the sibling directory leaf and is flagged for joint review. The defining core deliberately excludes vulnerability-record lifecycle (VM), engagement management (pentest), outside-in discovery (ASM), fake-asset detection (deception), and employee-behavior training (security awareness).
