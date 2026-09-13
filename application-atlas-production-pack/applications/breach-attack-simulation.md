# Breach & Attack Simulation

## Overview

A **Breach & Attack Simulation** application (commonly abbreviated **BAS**) safely executes controlled emulations of real attacker techniques inside an organization's own IT environment and records how each deployed security control responds to each one.

The problem it solves is specific: an organization owns many security controls — endpoint protection, email gateways, network firewalls, WAFs, DLP, SIEM detections — and none of them can be trusted to work just because they are installed and licensed. Controls are misconfigured, rules age, exceptions accumulate, and infrastructure drifts. Periodic manual testing (penetration tests) covers only a fraction of the environment at a point in time. A BAS application makes the answer to "would our defenses actually stop this attack?" continuously measurable, technique by technique, with recorded evidence.

The defining structure is small:

```text
Library of executable attack simulations
  (real attacker techniques, individually and chained into scenarios)
   ↓ safely run inside the organization's own environment
Deployed security controls under test
  (endpoint, email, network, web, DLP, SIEM, cloud)
   ↓
Recorded per-simulation control response
  (prevented / detected / logged / nothing — exact labels vary by product)
```

Everything else commonly seen in the market — MITRE ATT&CK mapping, scheduled campaigns, scoring, benchmarking, remediation guidance, compliance reporting — is standard capability layered on that loop, not what makes the product a BAS tool.

What it is not: it does not discover and manage software vulnerabilities (Vulnerability Management), it does not manage human-led testing engagements (Penetration Testing Management), and it does not discover what an organization exposes on the internet (Attack Surface Management).

## Users & Context

BAS is operated by the defending organization itself, inside its own environment. The user population is unusually multi-role because the output — proof of what defenses do and don't catch — is consumed differently by each function:

- **Security engineers / control owners** — deploy the simulation agents, verify that controls are correctly configured, and apply fixes when a gap is found. They use BAS to guard against configuration drift.
- **SOC analysts / blue teams and detection engineers** — check whether their detection content (e.g., SIEM rules, endpoint detections) actually fires on known attack behavior, and tune it using the simulation evidence.
- **Red and purple teams** — use automated simulation to cover routine technique testing, so their scarce manual effort goes to novel scenarios; some products let them chain custom attack actions and payloads.
- **Threat intelligence teams** — steer which simulations matter (which actors, which TTPs, which newly disclosed threats) and feed intelligence into custom simulations.
- **CISO / executives / compliance functions** — consume aggregated reporting: coverage, scores, trends over time, and audit-ready evidence that control effectiveness is being regularly tested.

The context is production infrastructure. Unlike lab-based malware analysis, the point is to exercise the *real* controls in the *real* environment — which is why safety mechanisms (below) are a structural part of the product rather than an option.

## Core Model

The system's world is built from five structures.

### 1. Attack simulation content (the central object)

A **simulation** is a controlled, executable enactment of one specific attacker behavior — a technique such as a credential-dumping sequence, a phishing payload delivery, a command-and-control beacon, a data-exfiltration transfer, or a web-attack request. Simulations are maintained as a **library or catalog**: curated by the vendor (or the open community), derived from real-world attacker tactics, techniques and procedures, and continuously extended as new threats appear. Mature products commonly organize the library by tactic/technique (frequently mapped to MITRE ATT&CK), by threat actor or malware family, and by the control it exercises.

Simulations also compose: a **scenario** is a chained sequence of techniques that emulates a multi-stage attack (for example initial access → execution → lateral movement → exfiltration), often packaged as an emulation of a known threat actor or a threat such as ransomware. Products also allow users to **build custom simulations** — chaining library actions or uploading their own payloads — so that testing can reflect the organization's specific risk profile.

### 2. Controls under test (coverage surfaces)

Every simulation exists to exercise one or more **security controls**. Mature products enumerate the surfaces they can test, and the recurring set across the researched sample is stable:

- endpoint defenses (EDR / XDR / antivirus)
- email security (gateways, malicious attachments and links)
- network defenses (firewalls, NGFW, IPS/IDS, segmentation)
- web defenses (WAF, secure web gateways, proxies, URL filtering)
- data loss prevention (DLP)
- SIEM / detection content (does the detection fire and alert)
- cloud and container controls

### 3. Execution machinery

Running simulations inside the customer environment requires delivery mechanisms. Two families coexist and are commonly mixed:

- **agents / simulators** — small software components deployed on endpoints or into network segments, which receive instructions and execute attack actions locally;
- **vector-based delivery without a local agent** — controlled phishing emails sent to designated mailboxes, web requests aimed at the organization's own applications or gateways, or network probes aimed at perimeter defenses.

### 4. Validation result

The result is the system's unit of truth. For each executed simulation the platform records how the defense chain responded. The observed vocabulary in the sample — *blocked, detected, logged, missed* — illustrates the pattern; exact labels and granularity vary by product. Each result carries the identity of the simulation, the technique, the control(s) involved, and evidence of the response. Results aggregate upward into coverage views: which techniques are defended, which are not, and how that picture changes over time.

### 5. The closed loop: gap → fix → re-test

A recorded gap is not the end state. Mature products attach **remediation guidance** to a failed simulation — often specific to the control vendor that failed (a prevention signature, a detection rule, a configuration change) — and then **re-run the same simulation** to prove the gap closed. This re-test discipline is what distinguishes a validation system from a testing utility that merely reports findings.

```text
Attack simulation library
   ↓ select / compose / schedule
Execution (agents + simulators, or email / web / network vectors)
   ↓ safely exercises
Security controls under test
   ↓
Validation result per simulation (prevented / detected / logged / missed)
   ↓ aggregate
Coverage & gap reporting (technique coverage, scores, trends)
   ↓
Remediation guidance → re-test the same simulation → confirmed closure
```

## How It Works

The operating loop in a typical deployment:

**1. Establish execution capability.** Deploy agents/simulators into the environments to be tested, and configure non-agent vectors (designated mailboxes, target URLs, network paths). Connect to the controls whose response will be judged — commonly via SIEM/EDR integrations, so that "did it alert" can be verified programmatically as well as visually.

**2. Select and scope simulations.** Choose from the library — by technique, by threat actor, by scenario (e.g., ransomware emulation), or by the control to be tested — or compose custom simulations. Scope them to the right environment segment and to controls that should see them.

**3. Execute.** Run on demand or as scheduled, recurring campaigns; continuous operation is a selling point of the category because defenses and threats both change. Execution is deliberately safe and non-destructive (see Rules below).

**4. Observe and attribute.** For each simulation, determine what the control chain did: was the payload blocked at the gateway, did it execute and get caught by the endpoint, did it raise an alert in the SIEM, was it merely logged, or did nothing react at all. The platform records this per simulation and per control.

**5. Report and prioritize.** Aggregate into dashboards and reports: technique-coverage views (frequently rendered against the MITRE ATT&CK matrix), severity-ranked gap lists grouped by control category or vendor, trend lines across repeated campaigns, and executive summaries. The output feeds security-engineering work queues and, in many products, ticketing systems directly.

**6. Fix and re-test.** Apply the remediation guidance (often vendor-specific to the failed control), then re-run the same simulation. The loop closes when the recorded outcome flips from missed to blocked/detected — and stays closed on subsequent scheduled runs.

**7. Keep content current.** The library grows continuously with newly observed attacker techniques, malware campaigns, and disclosed vulnerabilities, so the organization's readiness is measured against the current threat landscape rather than last year's.

## Interfaces

All researched products are console applications (web UI) with APIs; the surfaces below are described conceptually and named differently per product.

- **Simulation library / catalog browser** — the content entry surface. Typical information: technique name and mapping (e.g., ATT&CK ID), threat actor or malware association, targeted control, description. Primary actions: browse/filter, select for a run, inspect technique detail.
- **Scenario / attack-chain designer** — compose ordered chains of techniques into a scenario, optionally with custom payloads. Primary actions: add/reorder actions, set targets, save as reusable scenario.
- **Execution manager** — schedule and control runs. Typical information: target environment/agents, planned simulations, schedule, run status. Primary actions: run now, schedule recurring, stop.
- **Agent / simulator inventory** — deployed execution components and their health, hosts/segments they cover. Primary actions: deploy, group, troubleshoot.
- **Results and coverage views** — the primary analytic surface. Typical information: per-simulation outcome, per-control performance, technique-coverage matrix, gaps ranked by severity, trends across runs. Primary actions: filter, drill into a result's evidence, rank/group.
- **Remediation guidance** — per failed simulation: what to change on which control, often with vendor-specific content. Primary actions: view guidance, export/create ticket, trigger re-test.
- **Reporting surface** — executive and compliance-oriented summaries: scores, improvement over time, framework-mapped evidence. Primary actions: generate/share reports.
- **Integration configuration** — connections to SIEM, SOAR, EDR, ticketing; API keys.
- **API** — machine access to run simulations and pull results for automation pipelines.

## Important Rules / Behaviors

- **Safety is structural.** Simulations are designed to be non-destructive and safe to run in production: they mimic attack behaviors (payloads, traffic, sequences) without causing the real damage the mimicked malware would cause. Products additionally expose execution guardrails — scope restrictions, controlled execution with audit records, role-based authorization — because the platform is, by construction, a framework for running attack techniques inside a live estate. Who may launch which simulation against which environment is therefore a governed permission surface.
- **The control response is the finding.** A simulation "fails" not when the technique executes (that is often the point — to test downstream detection), but when the intended defensive response does not happen. The expected response is part of each test's definition.
- **Re-testing proves closure.** Results are treated as claims until a re-run of the same simulation confirms the fix. Repeated scheduled runs also catch regressions when configurations drift again.
- **Content freshness is a first-class property.** The library is continuously maintained (vendor research teams, threat-intelligence ingestion, community collections in the open-source case); stale attack content makes the validation meaningless, and how quickly new threats become runnable simulations is an explicit evaluation criterion in the market.
- **Results are ranked and grouped for actionability.** Gaps are typically ordered by severity/potential impact and grouped by control category, control vendor, or environment, so that engineering teams can act on them in bulk.
- **Coverage is expressed against shared frameworks.** MITRE ATT&CK is the dominant organizing framework for both content and results, giving the organization a common language for what is and isn't defended.
- **Evidence supports governance needs.** Recorded runs, responses, and re-validation results double as audit evidence for requirements that call for regular testing of the effectiveness of security measures (a recurring compliance driver named across the sample).

## Variants

- **Technique-level simulation vs full-path emulation.** One philosophy runs many granular techniques and grades each control response individually; another executes chained, exploitation-led attack paths end-to-end (often marketed as "automated penetration testing" or "automated red teaming") and reports the reachable attack paths. Both sit in the same market and frequently inside one platform as separate modules.
- **Delivery form.** Vendor-operated SaaS; self-hosted deployments for restricted environments; fully managed services where the vendor runs the testing; and open-source adversary-emulation frameworks used as self-managed BAS tooling.
- **Agent-based vs agentless.** Products differ in how much they deploy into the environment versus drive tests through email/web/network vectors alone.
- **Scope emphasis.** Endpoint-centric validation, email-gateway validation, network/perimeter validation, cloud- and identity-focused testing (e.g., credential exposure), or whole-estate attack-path testing.
- **Umbrella platforms.** Most commercial vendors now position BAS as one capability inside a broader "security validation" / "exposure validation" / continuous-threat-exposure-management platform, alongside exposure inference, attack-path validation, and remediation orchestration. The attack-execution-and-validation loop described above remains the engine of those platforms.
- **AI depth.** Products increasingly add generation of new simulations from threat intelligence (reports, CVE IDs, actor names) and AI-assisted orchestration of the validate→fix→re-test loop.
- **Phishing as shared surface.** BAS email simulations deliver phishing-style payloads to measure gateway and endpoint response. Security-awareness tooling sends phishing to measure and train employee behavior. The delivery mechanism overlaps; the measured object decides the type — control response belongs to BAS, human behavior to awareness tooling.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Vulnerability Management | closest operational partner | VM discovers and manages software vulnerabilities across assets and drives patching; BAS runs attacker behavior to see whether deployed controls stop it. BAS output can re-prioritize the VM backlog, but VM owns the vulnerability record and patch lifecycle |
| Penetration Testing Management | adjacent | PTM manages human-led, scoped, point-in-time engagements (rules of engagement, findings, retests); BAS is automated, continuous, and safe-by-design. "Automated pentesting" products straddle the seam |
| Security Validation Platform | sibling / umbrella overlap | Several vendors brand this exact capability "security validation" or "exposure validation"; the boundary between the two directory leaves deserves joint review (see Sources note) |
| Attack Surface Management | complementary discovery | ASM discovers what the organization exposes on the internet (outside-in inventory); BAS executes attacks against controls to record their response. ASM informs what to test; BAS tests it |
| SIEM / SOC tooling | control under test | The SIEM is one of the defenses being validated, not the validator; BAS supplies known-bad activity with known-expected detection outcomes |
| Deception Platform | different actor, different object | Deception plants fake assets to catch real attackers; BAS runs synthetic attacker behavior against real controls |
| Security Awareness Platform | phishing overlap only | Awareness measures and trains employee behavior; BAS measures control response. The email-phishing mechanism is shared surface, not shared purpose |
| Threat Intelligence Platform | consumer vs producer | TIP tracks external adversaries and indicators; BAS consumes that intelligence to make simulations relevant and current |
| DAST | different target | DAST tests the security of an application itself; BAS web coverage tests the protective control (e.g., WAF) in front of it |

## Representative Products

- **Picus Security** — BAS-native platform; technique-level validation with a large maintained threat library, vendor-specific mitigation content, and re-test loops.
- **SafeBreach** — BAS-native vendor positioned within a continuous-exposure-management platform; published a widely referenced definition of the category.
- **Pentera** — full-path automated security validation; emulates complete attack chains across internal, external, and cloud environments with remediation orchestration and revalidation.
- **Apache Caldera** (formerly MITRE Caldera) — open-source adversary-emulation platform explicitly built for autonomous breach-and-attack-simulation exercises; useful as the vendor-neutral structural anchor.

Other vendors commonly associated with this market (e.g., AttackIQ, Cymulate) could not be reached during this research pass; no product-specific claims are made about them here.

## Sources

Research date: **2026-09-06**

- Picus Security — Breach and Attack Simulation product page: https://www.picussecurity.com/platform/breach-and-attack-simulation
- Picus Security — Platform overview: https://www.picussecurity.com/platform
- SafeBreach — "What is breach and attack simulation (BAS)?": https://www.safebreach.com/breach-and-attack-simulation
- Pentera — Platform: https://pentera.io/platform/
- Pentera — What Is Automated Security Validation: https://pentera.io/solution/what-is-asv/
- MITRE — Caldera contribution announcement: https://caldera.mitre.org/
- Apache Caldera — project page: https://caldera.apache.org/
- Apache Caldera — documentation (terminology: agents, abilities, adversaries, operations): https://caldera.readthedocs.io/en/latest/

> Sourcing limitation: vendor help centers and login-gated product documentation were not accessible in this research pass; all product claims are calibrated to official public product pages. AttackIQ (attackiq.com) and Cymulate (cymulate.com) returned access errors on repeated attempts and were excluded from all operational claims. Precision figures used in vendor marketing (library sizes, response-time SLAs, integration counts) are intentionally not repeated as facts in this document. The distinction between this Application Type and the related "Security Validation Platform" directory entry is flagged for joint review, because sampled vendors use both names for overlapping scopes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis are recorded in the paired Research Notes.
