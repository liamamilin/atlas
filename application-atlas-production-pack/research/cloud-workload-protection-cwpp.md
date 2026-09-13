# Research Notes — Cloud Workload Protection / CWPP

## Research Goal

Understand what a Cloud Workload Protection Platform (CWPP) actually is and how it works: what a "workload" is in this context, how the product sees into running workloads, what it detects and enforces, how detection flows into investigation and response, and how the Type is bounded against CSPM, EDR, CNAPP, Container & Kubernetes Security, and Vulnerability Management.

## Initial Boundary (pre-research hypothesis)

- Core purpose: runtime defense of running server workloads in cloud (VMs, containers/Kubernetes, serverless) — distinct from configuration assessment (CSPM).
- Nearest neighbors: CSPM (config posture), CNAPP (umbrella), EDR/EPP (endpoint object domain), Container & Kubernetes Security (object-domain slice), Vulnerability Management (vuln program), SIEM/SOAR/XDR (downstream correlation).
- Main unknowns: (1) is CWPP still a distinct Type in 2026 or merely a CNAPP pillar; (2) does the sensor/agent remain definitional given agentless scanning; (3) how deep is the overlap with the Container & Kubernetes Security leaf.

## Research Questions

1. What object set does a CWPP protect — hosts/VMs, containers, pods, nodes, serverless functions?
2. What sensor/instrumentation forms exist (kernel agent, eBPF, DaemonSet, sidecar, app-embedded, serverless layer, agentless snapshot, cloud-log ingestion)?
3. What does the product detect at runtime (malware, behavioral, drift, FIM, K8s audit) and how are rules/policies organized?
4. What happens after detection: triage, investigation artifacts, response actions, response history/revert?
5. How do vulnerability findings (pipeline/registry/runtime) fit into the same product?
6. What is enforced vs detected only? Where is blocking optional?
7. Who operates it (security ops, DevOps/platform teams) and through which interfaces?
8. What integrations exist (SIEM, ITSM, ticketing, cloud-native security services)?
9. Where does the cloud-control-plane detection slice (CloudTrail/K8s audit logs) belong — inside CWPP or adjacent?
10. How is the product packaged: standalone CWPP, CNAPP pillar, platform-native, EDR-converged, self-hosted?

## Representative Products

Sample selected for market representation, documentation completeness, and distinct product philosophies / customer tiers:

| Product | Philosophy / position | Evidence status |
|---|---|---|
| Microsoft Defender for Cloud — Defender for Servers | platform-native heritage, now multi-cloud + on-prem; EDR-converged (reuses Defender for Endpoint machinery); agentless-heavy Plan 2 | A — two Tier-1 Microsoft Learn pages fetched in full |
| Sysdig Secure | container/K8s runtime heritage (Falco); sensor family (Shield) + agentless cloud connections; deep response actions | A — docs TOC + 3 body pages fetched |
| Prisma Cloud (Palo Alto Networks) | CNAPP with explicit Runtime Security (Defend) pillar; Compute Edition self-hosted CWPP; Enterprise Edition SaaS | A — docs index + Defender Types page (markdown) fetched |
| FortiCNAPP (formerly Lacework) | agentless-heritage CNAPP; anomaly/polygraph visualization | B/C — documentation index + Administration Guide TOC only |
| Trend Micro (Server & Workload Protection / Vision One) | archetypal agent-based CWPP incumbent | Unreachable — docs timed out / "article unavailable" (2 attempts). Market context only |
| Aqua Security | container-security pure-play | Unreachable — docs behind sign-in (1 attempt). Market context only |
| CrowdStrike Falcon Cloud Security | EDR-heritage cloud workload protection | Unreachable — JS-only docs (1 attempt). Market context only |

Rationale: the first four span platform-native vs third-party, sensor-first vs agentless-inclusive, EDR-converged vs runtime-heritage vs posture-heritage, SaaS vs self-hosted. Trend Micro and Aqua anchor the market context (the term "workload protection" originates in this vendor family) but contribute no operational detail in this pass.

## Sources

Evidence layers: A = directly observed on official product documentation; B = cross-product commonality across the observed sample; C = structure-level / index-level only.

- Microsoft Learn — "Plan a Defender for Servers deployment" — https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-servers-introduction (fetched 2026-09-07; A)
- Microsoft Learn — "Overview of Defender for Servers in Defender for Cloud" — https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-servers-overview (fetched 2026-09-07; A)
- Sysdig docs — Secure documentation tree (TOC) — https://docs.sysdig.com/en/docs/sysdig-secure/ (fetched 2026-09-07; A-structure)
- Sysdig docs — "Threats Overview" — https://docs.sysdig.com/en/sysdig-secure/threats-overview/ (fetched 2026-09-07; A)
- Sysdig docs — "Response Actions" — https://docs.sysdig.com/en/sysdig-secure/response-actions/ (fetched 2026-09-07; A)
- Prisma Cloud docs — llms.txt documentation index — https://docs.prismacloud.io/llms.txt (fetched 2026-09-07; A-structure)
- Prisma Cloud docs — "Available Defender Types" — https://docs.prismacloud.io/content-collections/runtime-security/install/deploy-defender/defender-types.md (fetched 2026-09-07; A)
- Prisma Cloud docs — home (Compute Edition = "Self-hosted cloud workload protection... protect hosts, containers, and serverless") — https://docs.prismacloud.io/ (fetched 2026-09-07; A)
- Fortinet docs — FortiCNAPP product page + Administration Guide (index/TOC level) — https://docs.fortinet.com/product/forticnapp , https://docs.fortinet.com/document/forticnapp/latest/administration-guide (fetched 2026-09-07; C)
- Prior sibling pass: research/cloud-security-posture-management-cspm.md (CSPM observations; used only for boundary cross-reference)

Unreachable (recorded per source-access limitation): docs.trendmicro.com (timeout + "article unavailable"), cloudone.trendmicro.com (404 portal shell), docs.aquasec.com (sign-in wall), docs.crowdstrike.com (JavaScript-only shell). No operational claims about these vendors are made below; they appear as market context and in product lists only.

## Product observations

### Microsoft Defender for Cloud — Defender for Servers (A)

- Object domain: Windows and Linux machines across Azure, AWS, GCP, and on-premises. AWS/GCP/on-prem machines onboarded as Azure Arc VMs to unlock full features. Plans enabled at subscription level; per-resource enable/disable granularity (product-specific mechanics).
- Two plans (P1/P2). P1 = EDR-focused; P2 adds agentless machine scanning (software inventory, vulnerability assessment, secrets scanning, malware detection without an agent), FIM, just-in-time VM access, DNS alerts, OS-baseline (MCSB) assessment, network map, periodic OS updates.
- Defender for Endpoint integration: the EDR agent is automatically onboarded to supported machines; vulnerability management features flow from Microsoft Defender Vulnerability Management. This is direct evidence of EDR/CWPP machinery convergence inside one product.
- Agent posture shift: documentation states the product no longer uses the Log Analytics agent or Azure Monitor Agent for most plan features — agentless scanning + Defender for Endpoint integration replaced them. Direct evidence that "kernel/host agent" is not definitional even for one vendor's full-featured plan.
- Detection: real-time threat detection with security alerts; analytics/ML and threat-intelligence sources; integrated alerts/incidents in the Defender portal.
- Managed service extension: Defender Experts for Servers — Microsoft analysts triage/investigate/contain incidents on protected machines (sold separately). Evidence of an MDR-style layer on top of workload protection.
- Deployment planning artifacts: Log Analytics workspace for FIM/data ingestion, Azure Machine Configuration extension for OS assessment, agent/extension inventory, data-collection rules.
- Evidence layer: A (all above directly observed).

### Sysdig Secure (A)

- Onboarding: cloud accounts (AWS/Azure/GCP/OCI) connected agentlessly (config + audit-log ingestion); Kubernetes clusters via Sysdig Shield (cluster-shield DaemonSet incl. admission controller, Rapid Response, kube-audit integration); hosts via Host Shield (Linux/Windows, as container or package); serverless via embedded workload agents (ECS Fargate, Cloud Run, Azure Container Apps; agent embedded in image or via task-definition instrumentation); classic agent documented as legacy path.
- Runtime threat detection and response explicitly described as "uses Falco to monitor running workloads for suspicious activities". Threat detection policy library includes: Linux/Windows Workload policies, Malware Control, FIM, Drift Detection, Kubernetes Audit, cloud audit-log policies (AWS CloudTrail, Azure Platform Logs, GCP Audit Logs), identity-provider policies (Okta/Entra), ML-based policies (Workload ML), plus a Falco rule reference library; policies manageable and tunable; threat exclusions supported.
- Threats UX: Overview dashboards (All/Kubernetes/Cloud/Host) with events by severity (H/M/L/I), top policies/rules, MITRE ATT&CK mapping, drill-down to event feeds; filters by cluster/namespace/workload (K8s) or platform/account/region/user (cloud).
- Investigation: Activity Audit, Captures (system-call captures), Kubernetes audit logging.
- Response: Response Actions executed from the Events feed — containment actions (container kill/stop/pause, process kill incl. ancestor line, file quarantine, network isolate, delete pod, rollout restart) and data-gathering actions (volume snapshots); actions gated by RBAC permissions; per-action enable/disable with "least privilege" provisioning; Response History page records executions; revert supported for some actions; AI "response advice" available.
- Vulnerability management inside the same product: findings across pipeline (CLI/IaC), registry scanners, and runtime; "in use" risk spotlight; accepted-risk workflow; feeds and reporting.
- Also present (same platform, sibling modules): posture (KSPM/CPM), compliance, identity/CIEM, data security, network exposure — the CNAPP shape with Runtime/Threats as one pillar.
- Governance/integration: teams & zones scoping, custom roles with fine-grained permissions, SIEM/data-platform forwarding (Splunk, Sentinel, QRadar, Google SecOps, Kafka, S3, webhooks…), Jira/ServiceNow, plugin library, APIs.
- Evidence layer: A (docs TOC + three body pages).

### Prisma Cloud (A)

- Positioning (from docs home): Enterprise Edition = SaaS CNAPP ("code to cloud"); Compute Edition = "Self-hosted cloud workload protection — protect hosts, containers, and serverless… run in cloud, on-prem, or air-gapped environments". Direct vendor use of "CWPP" as a self-description in 2026 — strong evidence the Type term is alive.
- Runtime Security architecture: agent-based security features require deploying "Defenders", which "enforce the policies you set in the Prisma Cloud console". Defender types matched to asset type: single Container Defender (runs as container; protects containers + host; "richest set of capabilities"), single Host Defender (systemd/Windows service; hosts without containers), Orchestrator Defenders (K8s/OpenShift/ECS/GKE/Tanzu — DaemonSet deployment), Serverless Defender (embedded per function; Lambda layer), App-Embedded Defender (for container-on-demand services where host hooks are abstracted — Fargate sidecar injection via task-definition manipulation; Dockerfile embedding method; manual method). Auto-defend can deploy Defenders automatically on AWS/Azure/GCP.
- Agentless Scanning: separate capability per cloud (AWS/Azure/GCP/OCI) with modes and results pages — evidence of agentless/snapshot scanning coexisting with sensors.
- Components: Radar (host/VM discovery), Serverless Radar, Intelligence Stream, Advanced Threat Protection, WildFire settings, container runtime support, telemetry, custom feeds, rule ordering/pattern matching, scan intervals.
- Policies: Workload Protection Policies, Prisma Cloud Threat Detection, Anomaly Policies, Attack Path Policies, IAM policies, network exposure policies — a policy family spanning runtime + posture.
- Alerts: alert rules explicitly "for Cloud Workloads" as a separate rule type from cloud-infrastructure alert rules; alert status reasons; suppression; "View and Respond to Prisma Cloud Alerts".
- Inventory: Compute Workloads Inventory as a distinct inventory family (hosts, containers, images, functions) within a broader asset inventory.
- Roles: platform (Enterprise) roles vs Compute roles; access keys; SSO; collections/tags for scoping.
- Integrations: cloud-native security services (GuardDuty, Inspector, Security Hub, Google SCC, Security Lake), SOAR (XSOAR), SIEM (Splunk), scanners (Qualys, Tenable), ticketing/chat (Jira, ServiceNow, Slack, Teams, PagerDuty), webhooks.
- Evidence layer: A (index + Defender Types body page + home page).

### FortiCNAPP (formerly Lacework) (C — structure-level only)

- Administration Guide TOC: onboarding dashboard/tasks; cloud account integration (configuration + CloudTrail/Activity-log/Audit-log integrations for AWS/Azure/GCP/OCI, incl. EKS/GKE audit logs; automated/guided/CLI/Terraform/manual methods); Kubernetes compliance integration; console overview with Polygraphs — dedicated visualizations of host, container, Kubernetes, and cloud activities (the Lacework "polygraph" heritage); Dashboard; Explorer (query builder, saved queries, risk score, graph views, workflows); Threat Center; plus (from product page) Agent Support, Alerts Reference, LQL reference, Policies guide.
- Separate legacy product "FortiCWP" still listed in the catalog — naming heritage, not asserted further.
- Evidence layer: C — index/TOC only; no operational mechanics asserted. Used to confirm the runtime/investigation surfaces exist and that agentless + agent paths coexist in a CNAPP with Lacework runtime heritage.

### Trend Micro / Aqua / CrowdStrike (market context only)

- Not fetchable in this environment (see Sources). No operational claims. Market context from the research frame: Trend Micro's Server & Workload Protection (Deep Security lineage) is the archetypal agent-heritage CWPP with host-based control modules; Aqua is a container-security pure-play; CrowdStrike extends endpoint-agent machinery to cloud workloads. These positions are consistent with the structural pattern observed in the fetched sample but are NOT used as evidence for any specific capability claim.

## Cross-product Comparison

| Dimension | Defender for Servers | Sysdig Secure | Prisma Cloud (Runtime/Compute) | FortiCNAPP (structure) |
|---|---|---|---|---|
| Protected object set | Windows/Linux VMs (multi-cloud + on-prem via Arc) | K8s clusters, hosts, containers, serverless tasks, cloud accounts | Hosts, containers, K8s, serverless, container-on-demand | Hosts, containers, K8s, cloud activities |
| Sensor forms | EDR agent integration; agentless scanning; (workspace-based FIM) | Shield (cluster/host/serverless-embedded); classic agent; agentless cloud connections | Defenders (container/host/orchestrator/serverless/app-embedded); agentless scanning; auto-defend | Agent (support matrix); agentless cloud integrations |
| Detection policy model | Microsoft-authored analytics + plan features; benchmarks (MCSB) | Falco-based rule library, per-source policies (workload/K8s audit/cloud logs/FIM/malware/drift/ML), tuning + exclusions | Workload protection policies + threat detection + anomaly policies; rule ordering | Policies guide; alerts reference |
| Event UX | Alerts/incidents in Defender portal; recommendations | Threats overview + events feed (severity, top policies/rules, MITRE) | Alert rules for cloud workloads; alert statuses; dashboards | Threat Center; Polygraphs; Explorer |
| Investigation | Portal investigation; expert service | Activity audit, captures, K8s audit | Investigate/query platform (RQL) | Explorer queries/graphs |
| Response | EDR containment (via integrated EDR); managed analysts (experts service) | Response actions (container kill/stop/pause, process kill, file quarantine, network isolate, pod delete, rollout restart, snapshots) + history + revert | Defenders "enforce" policies (runtime blocking); alert response views | (not asserted — index level) |
| Vulnerability mgmt | Agent-based + agentless vuln scanning; TVM integration | Pipeline/registry/runtime findings; in-use spotlight; accepted risk | Agentless scanning results; registry scanning; vuln dashboards | (agent support; vuln surfaces not asserted) |
| Cloud-control-plane slice | Defender for DNS; network layer (Azure) | CloudTrail/Azure platform/GCP audit-log policies | GuardDuty/Inspector/Security Hub integrations; audit-event queries | CloudTrail/Activity/GKE-EKS audit integrations |
| Packaging | Plan inside platform security center (SaaS) | CNAPP-shaped platform (Threats one pillar) | SaaS CNAPP (Enterprise) + self-hosted CWPP (Compute) | CNAPP |
| Adjacent modules in same product | CSPM (foundational), Defender VM, DNS | Posture, CIEM, data security, network, compliance | CSPM/IAM/network/data/appsec/code | Posture, compliance, CIEM heritage |

### Common mature structure (B-layer, observed across ≥2 products)

1. Managed inventory of the running workload estate (hosts/VMs + containerized workloads; cluster/namespace/workload scoping).
2. Workload-type-matched instrumentation forms (host agent, cluster DaemonSet, embedded/sidecar for sandboxed/serverless, plus agentless/snapshot and cloud-log ingestion paths in most sampled products).
3. Policy-governed runtime threat detection with built-in rule libraries + custom rules + tuning/exclusions; severity-ranked security events bound to workload context.
4. Investigation artifacts (activity/audit views, captures/snapshots; graphs/polygraphs in two products).
5. Response: alert-driven response actions with recorded history (containment breadth varies); enforcement/blocking exists where sensors can act.
6. Vulnerability management of workloads (pipeline/registry/runtime) inside the same product, with runtime "in-use" prioritization appearing in sensor-first products.
7. Forwarding to SIEM/ITSM/chat; RBAC/SSO with scoped visibility (teams/zones/collections); APIs; audit logs; dashboards.
8. File integrity monitoring, malware control, drift detection present in ≥2 sampled products (not universal).

## Canonical abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (minimal)

1. **Running-workload estate as the managed object set** — VM/hosts and the containerized/ephemeral workloads they run; the product maintains a workload inventory as its organizing spine.
2. **Runtime visibility into those workloads** — the product must see what happens inside running workloads (processes, files, network, container/pod activity). Mechanism is NOT prescribed: deployed sensor is the common form; agentless snapshot scanning and cloud-control-plane log analysis are variant mechanisms that appear in mature products (sometimes in the same product).
3. **Policy-governed runtime threat detection producing per-workload security events** — detection bound to a specific workload/inventory object, ranked by severity, driven by vendor+customer policy.
4. **Response/containment path on the workload** — the loop must end in action on or about the workload (alert → triage → investigate → respond), not merely reporting.

Remove inventory → generic alert feed; remove runtime visibility → CSPM; remove workload binding/object domain → generic EDR/XDR; remove response loop → pure telemetry. All four are needed.

### L1 — Common Mature Structure

- workload-type-matched sensor family (host agent, cluster DaemonSet, embedded/sidecar/serverless layer); auto-deployment
- agentless scanning coexisting with sensors (vuln/software/malware/secrets)
- built-in detection libraries (behavioral rules, malware control, FIM, drift, K8s audit, cloud audit logs) + custom rules + tuning/exclusions
- events feed with severity + MITRE-style mapping + drill-down to workload context
- investigation artifacts (activity audit, captures/snapshots, process ancestry)
- response actions incl. containment + response history + (where supported) revert; RBAC-gated execution
- workload vulnerability management (pipeline/registry/runtime) with in-use prioritization
- admission/registry/pipeline controls for container estates
- SIEM/ITSM/chat forwarding, webhooks, APIs; RBAC/SSO, scoping constructs (teams/zones/collections/account groups); product audit trails; dashboards
- posture/compliance/identity sibling modules sharing the inventory (the CNAPP shape)

### L2 — Variant / Optional

- platform-native (single-cloud) vs third-party multi-cloud control plane
- EDR-converged (same agent machinery as endpoint products) vs runtime-heritage (container/IDS lineage) vs posture-heritage (agentless-first)
- on-prem/hybrid/air-gapped coverage vs cloud-only
- serverless function runtime protection (deep embedded agents) vs serverless covered by scanning only
- self-hosted console vs SaaS-only; managed analyst/MDR layer sold atop
- enforcement depth: detection-only vs policy-driven blocking vs auto-quarantine
- packaging: standalone CWPP vs CNAPP pillar vs plan within a platform security center
- pricing/licensing units (host/node/core/credit) — observed to exist, details not asserted

### L3 — Vendor-specific (kept out of final document)

- Defender for Servers plan split (P1/P2), 500-MB ingestion benefit, Defender Experts service, Azure Arc mechanics, MCSB naming
- Sysdig: Falco rule heritage, Shield naming, SysQL, Zones, Sage AI, per-action least-privilege provisioning, driver/socket path defaults
- Prisma: Defender type names, Fargate sidecar injection mechanics, WildFire/Radar/Intelligence Stream names, Compute-vs-Enterprise split, TAS Defender
- FortiCNAPP: Polygraph visualization, LQL, FortiCloud login, FortiCWP legacy product
- Trend Micro module set (anti-malware/IPS/FIM/firewall/log inspection) — from model memory only, UNVERIFIED in this pass; not used as evidence anywhere

### Rejected findings (anti-overfitting)

- "CWPP requires a kernel/host agent" — rejected. Defender for Servers P2 runs most features agentless; Sysdig connects cloud accounts agentlessly; Prisma ships agentless scanning beside Defenders. Abstraction: "runtime visibility", not "agent".
- "CWPP is cloud-only" — rejected. On-prem/hybrid coverage is directly documented (Defender for Servers on-prem via Arc; Prisma Compute self-hosted incl. air-gapped). The Type's object is the server workload estate wherever it runs; "cloud" is the dominant context, not the boundary.
- "Blocking/prevention is definitional" — rejected. Detection-first postures are fully valid; blocking is policy- and sensor-dependent.
- "Serverless protection is definitional" — rejected. Deep embedded serverless agents appear in one sampled product family; others scan or omit.
- "Cloud-control-plane detection (CloudTrail etc.) is part of CWPP" — kept OUT of the definition; it is a common adjacent data source in the same console (marker: several products put it in sibling policies).
- Precise numbers (severity ladders, plan features, limits) — vendor-specific; excluded from the canonical document.

## Boundary Findings

- **vs CSPM (sibling leaf, already documented)**: CSPM evaluates standing configuration of cloud resources agentlessly; CWPP defends running workloads with runtime visibility and response. Reciprocal structural test holds both ways (remove runtime visibility → CSPM; remove config evaluation → CWPP). Products bundle both; the artifact families stay distinct (posture findings vs runtime events) even in one console.
- **vs CNAPP**: CNAPP is the umbrella (CSPM + CWPP + CIEM/DSPM/KSPM/etc.). CWPP remains the runtime-defense pillar. Market packaging has folded most CWPP sellers into CNAPP suites, but the runtime pillar persists as a distinct structure — and at least one vendor still self-describes its self-hosted product as a CWPP (A-layer evidence). No directory change; recommend joint review when the CNAPP leaf is processed.
- **vs EDR / EPP**: same machinery family (process/file/network behavioral detection, containment) but different object domain and operational context: user endpoints vs server workloads including container/ephemeral/cluster context and image/package vulnerability corpus. Convergence is real and directly observed (one sampled product reuses its EDR agent for servers; several EDR vendors sell cloud workload protection from the same agent). Structural test: remove servers/containers/cluster context → EPP/EDR; remove laptops/phones → CWPP. The Type boundary rests on object domain + operational workflow, not on agent technology.
- **vs Container & Kubernetes Security (separate leaf)**: heavy overlap — container runtime defense, image scanning, admission control are all inside CWPP's scope in the sampled products. The dedicated leaf is best understood as the container/K8s object-domain specialization (registry/pipeline/admission depth, K8s-native surfaces). Flag for joint review: possible partial redundancy; center-of-gravity difference is the broader host/VM estate in CWPP vs container-native depth in the sibling.
- **vs Vulnerability Management**: workload vuln scanning is a module inside CWPP; the VM leaf is the enterprise-wide program (assets, remediation SLAs, scanning infrastructure). CWPP's contribution is the runtime context ("in use", exploitability in running estate).
- **vs SIEM/SOAR/XDR**: CWPP is a detection source and response executor for workloads; SIEM/SOAR correlate across sources. Forwarding integrations are the seam (observed in all fetched products).
- **vs Attack Surface Management**: external vantage vs in-workload sensor vantage; no overlap in mechanism.
- **vs Patch Management**: CWPP surfaces missing patches/vulns on workloads; patch deployment belongs to patch/endpoint management (one sampled product offers OS-update enablement as a feature — bridge case, noted).

### "Remove X → another Type" tests

- Remove runtime visibility (keep config evaluation) → CSPM.
- Remove the server-workload object domain (keep behavioral detection + containment) → EDR/XDR.
- Remove workload inventory + policy scoping (keep event feed) → generic log/alert pipeline.
- Remove response loop (keep detection) → workload telemetry product, no longer a protection platform.

## Historical / market-sample check (pre-freeze)

- Older host-IPS/server-security agents (pre-container era, physical + virtualized servers) satisfy the minimal core: workload estate (hosts), sensor, policy-governed detection, response. The core therefore must not require containers/Kubernetes.
- Platform-native cloud security centers (provider security services) satisfy the core with their own sensor/cloud-log mechanisms — so the core must not require a third-party agent either.
- On-premises/air-gapped deployments satisfy the core — "cloud" cannot be a hard requirement of the definition.
- The original 2016-era CWPP formulation (agent-centric host controls) was checked against this: the agent is the historical common implementation, not the invariant; the invariant is workload-scoped runtime defense.

## Uncertainties

- Trend Micro, Aqua, CrowdStrike operational details unverified this pass (source-access limitation). The agent-heritage pole is therefore evidenced only via Prisma/Sysdig/FortiCNAPP structure and market context; no Trend-specific claims are made.
- Enforcement/blocking depth across products: directly observed only as "Defenders enforce policies" (Prisma) and Sysdig's containment actions; Microsoft's containment rides on its EDR integration. Generalization ("mature products commonly provide response actions, depth varies") is calibrated to this.
- Whether the Container & Kubernetes Security leaf should remain a separate Type is unresolved — flagged for joint review.
- Serverless depth market-wide (beyond the two sampled implementations) unverified.
- Licensing/pricing mechanics not researched (out of scope; excluded from claims).

## Final Synthesis

A CWPP is the runtime-defense layer of the security stack for server workloads. Its world is built from: a managed inventory of the running workload estate (hosts/VMs and the containers, pods, and functions they carry); instrumentation that gives the product visibility into what those workloads actually do (deployed sensors matched to workload type being the common form, with agentless snapshot and cloud-log mechanisms as documented variants); a policy layer (built-in libraries + customer rules + scoping) that governs what is detected and, where sensors can act, what is blocked; security events bound to workload context (severity, MITRE mapping, drill-down); an investigation path (activity audit, captures, ancestry); and a response path (containment/process/network/file actions with recorded, sometimes reversible, history). Around this core, mature products add workload vulnerability management, admission/registry controls, posture/identity/data sibling modules, and forwarding into SOC tooling. The Type survives the market's CNAPP consolidation as a structurally distinct pillar — and its boundary with EDR is an object-domain boundary, not a technology boundary.
