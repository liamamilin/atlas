# Research Notes — Container & Kubernetes Security

## Research Goal

Understand what "Container & Kubernetes Security" is as an Application Type: what object domain it manages (images, containers, pods, clusters), which security functions are specialized to that domain (image scanning, admission control, runtime detection, cluster posture), how the work flows across the image lifecycle (build → registry → deploy → runtime), how it integrates with Kubernetes-native machinery (admission webhooks, DaemonSets, operators, RBAC), and how the Type is bounded against CWPP, CNAPP, CSPM, Software Supply Chain Security, Vulnerability Management, and the Kubernetes Management Platform.

Context: the CWPP pass (research/cloud-workload-protection-cwpp.md) flagged heavy overlap and recommended joint review — "container runtime defense, image/registry scanning, and admission control all sit inside the sampled CWPPs' scope; working seam = estate breadth (host/VM estate plus container children, cross-platform) vs container/K8s-native depth". This pass researches the sibling leaf on its own terms and tests whether that seam holds from this side.

## Initial Boundary (working hypothesis before research)

- Core purpose: security software specialized to the container estate — container images as build-time artifacts, running containers/pods as runtime entities, and the Kubernetes cluster platform configuration — as opposed to generic host or cloud-account security.
- Nearest neighbors: CWPP (broader workload estate, runtime-defense heart), CNAPP (umbrella), CSPM (cloud account config posture), Software Supply Chain Security / SCA (source dependency graph), Secrets Security, Vulnerability Management (generic vuln program), Kubernetes Management Platform (§14 — same objects, management not security function).
- Main unknowns: (1) is this a distinct Type or merely an object-domain slice of CWPP/CNAPP; (2) which functions are definitional vs common (is admission control required? runtime detection?); (3) does the core survive pre-Kubernetes container security and single-function OSS tools.

## Research Questions

1. What objects does the product manage: images, registries, clusters, nodes, pods/containers, namespaces, workloads, RBAC, network policies, control-plane components?
2. What are the main workflows: image scanning (pipeline/registry/runtime) → admission control at deploy → runtime detection → response → posture/compliance?
3. How does the product integrate with Kubernetes-native machinery (admission webhooks, CRDs/operators, DaemonSets, kubeconfig/API access)?
4. What is K8s-specific vs generic container security? Does the core require Kubernetes at all?
5. What compliance surfaces exist (CIS Kubernetes Benchmark, NSA/CISA Hardening Guidance, Pod Security Standards)?
6. Who uses it (security team vs platform team vs developers) and through which interfaces (console, CLI, kubectl-native components, SIEM forwarding)?
7. Where exactly is the seam with CWPP, and can it be stated as a structural test?

## Representative Products

| Product | Why selected | Evidence reached |
|---|---|---|
| Sysdig Secure | container/K8s runtime heritage (Falco); full container/K8s security platform | A — docs TOC + admission-controller body page + prior CWPP-pass body observations |
| Prisma Cloud Compute (Palo Alto Networks) | suite-embedded container security (Compute Edition); Twistlock heritage | A — docs via query interface (image/registry scanning, admission control, runtime, compliance) |
| Trivy (Aqua Security, OSS) | open-source scanner pole; single-function minimal realization | A — full docs TOC + Kubernetes target body page |
| Falco (CNCF, OSS) | open-source runtime-detection pole; single-function minimal realization | A — docs home body page |
| Aqua Security Platform | container-security pure-play vendor; Trivy's commercial parent | B- — product page only (docs behind sign-in, 2 attempts across passes) |
| Red Hat Advanced Cluster Security (RHACS) | K8s-native platform pole (StackRox heritage) | Unreachable — docs.redhat.com 403/503 (2 attempts). Market context only; no capability claims |
| Kubernetes official documentation | platform-native security machinery the products build on | A — Pod Security Standards body page + security doc-tree structure |

## Sources

- Sysdig Secure docs — https://docs.sysdig.com/en/docs/sysdig-secure/ (TOC, fetched 2026-09-07; A) and https://docs.sysdig.com/en/sysdig-secure/admission-controller/ (body, fetched 2026-09-07; A)
- Prisma Cloud Compute docs — https://docs.prismacloud.io/ via documentation query interface (fetched 2026-09-07; A)
- Trivy docs — https://trivy.dev/latest/docs/ (TOC) and https://trivy.dev/latest/docs/target/kubernetes/ (body, fetched 2026-09-07; A)
- Falco docs — https://falco.org/docs/ (body, fetched 2026-09-07; A)
- Aqua Security — https://www.aquasec.com/products/container-security/ (product page, fetched 2026-09-07; B-); docs.aquasec.com unreachable (sign-in wall)
- Kubernetes — https://kubernetes.io/docs/concepts/security/pod-security-standards/ (body, fetched 2026-09-07; A); security doc-tree (Pod Security Admission, RBAC good practices, security checklist, hardening guides) observed in TOC
- Red Hat Advanced Cluster Security — https://docs.redhat.com/... (403, 503 — unreachable)
- Internal alignment: research/cloud-workload-protection-cwpp.md, research/cnapp.md, research/cloud-security-posture-management-cspm.md (boundary context)

## Product Observations

### Product A — Sysdig Secure (Layer A)

From docs TOC (2026-09-07) and admission-controller body page; plus CWPP-pass body observations (threats UX, response actions, activity audit, captures):

- **Onboarding by estate member**: Kubernetes clusters via "Sysdig Shield" (cluster-shield DaemonSet including admission controller, Rapid Response, kube-audit integration); hosts via Host Shield (Linux/Windows, as container or package); serverless via embedded workload agents; cloud accounts agentlessly; **Pipeline Scanning** via CLI scanner (with IaC mode and VM mode); **Registry Scanning** via registry scanners for JFrog Artifactory, AWS ECR, Azure ACR, Google Artifact Registry, Harbor, IBM CR, Nexus, OpenShift registry, Quay.io.
- **Admission Controller (body page, direct quotes)**: "a Kubernetes-native component that evaluates resource creation requests after they are authenticated and authorized, but before they are deployed to the cluster. It applies real-time security policies from posture controls to image scanning rules to block non-compliant workloads at deploy time." Features: **Deploy-Time Image Scanning** (block workloads using images with CVEs, misconfigurations, or policy violations "before scheduling to a node"); **Kubernetes Audit Logging** ("record API-level admission decisions, including who attempted deployments, when, and why actions were allowed or blocked"); **Kubernetes Posture Enforcement** ("preventing privileged containers, enforcing non-root users, or applying resource limits", policies assignable per Zone e.g. staging vs production). Architecture: standard Kubernetes **ValidatingAdmissionWebhook** / Dynamic Admission Controller; API server sends AdmissionReview requests; webhooks "must either allow or reject the resource, but cannot modify"; timeout with failure_policy (Fail/Ignore). Results viewable in Events Feed and CLI. Vendor warns misconfigured policies "may block deployments".
- **Admission policy families**: Posture Admission Policies, Supply Chain Admission Policies, Vulnerability Admission Policies.
- **Inventory**: Resources, **Kubernetes Live**, Network, Zones (scoping), Search (SysQL query language).
- **Threats**: Events feed; Investigate (Activity Audit, Captures, **Kubernetes Audit Logging**); Respond (Rapid Response, Response History, Response Actions — container kill/stop/pause, process kill, file quarantine, network isolate, pod delete, rollout restart, snapshots per CWPP pass).
- **Threat detection policies**: Falco rule libraries including a dedicated **Kubernetes Audit Falco Library**; Kubernetes Audit Policy; Drift Detection Policy; Malware Control; FIM; workload policies.
- **Vulnerabilities**: findings split by **Pipeline / Registry / Runtime**; "In Use" prioritization; Accepted Risk; lifecycle/EOL visibility; vulnerability feeds.
- **Posture / Compliance**: posture findings; compliance findings (framework reports).
- **Supply chain policies**: **Image Signature Validation** (integrations with Sigstore, GitHub+Sigstore, self-hosted Sigstore, RHTAS).
- **Network**: Netsec Policy Generation (Kubernetes network policy generation); Advanced/Validated Network Exposure.
- **Integrations**: SIEM/data-platform forwarding (Splunk, QRadar, Sentinel, Chronicle, Elasticsearch, Kafka, webhooks...), AppSec (Snyk, Docker Scout, Checkmarx), Jira/ServiceNow, CI plugins (Jenkins, GitHub Actions, GitLab), Backstage, VS Code; KSPM listed under classic agent requirements.
- **AI**: Sysdig Sage (threats, VM, search), MCP server.

### Product B — Prisma Cloud Compute Edition (Layer A)

From docs query interface (2026-09-07):

- **Image scanning**: Defender harvests an **image manifest** (OS/package-manager details + executable details) → Console correlates against the **Intelligence Stream** (per-distro CVEs, un-packaged software CVEs, open-source library CVEs). Scan triggers: periodic by Console, on container start by Defender, or manual via **twistcli** (CI).
- **Registry scanning**: scan rules under Defend > Vulnerabilities > Images > Registry settings; scans public/private registries; periodic (documented default 24h, configurable); discovers repositories/tags then scans discovered images with a configurable cap.
- **Admission control**: **dynamic admission controller for Kubernetes/OpenShift built on Open Policy Agent (OPA)**; rules in **Rego** that "allow or deny pods (alert/block)"; Console pushes policies to Defender for enforcement; decisions logged.
- **Runtime defense**: runtime host protection (malware, networking, log inspection, file integrity, activities, custom events); some detections can be prevented; disabled by default via empty host runtime policy.
- **Kubernetes compliance**: container-focused controls (e.g. NET_RAW capability enabled, secrets in clear-text env vars, running as root) plus Istio compliance checks (mutual TLS, RBAC posture).
- (From CNAPP pass: Defender family spans container/host/orchestrator/serverless/app-embedded; Compute Edition self-hostable; inventory includes Compute Workloads family — hosts, containers, images, functions.)

### Product C — Trivy (Layer A, OSS scanner pole)

From docs TOC + Kubernetes target body page (2026-09-07):

- **A scanner with multiple targets**: Container Image, Filesystem, Rootfs, Code Repository, VM Image, **Kubernetes**, SBOM. Scanners: Vulnerability, Misconfiguration, Secret, License.
- **Kubernetes cluster scanning** (`trivy k8s`): "Trivy can connect to your Kubernetes cluster and scan it for security issues". It differentiates: (1) **cluster infrastructure** (api-server, kubelet, addons), (2) **cluster configuration** (Roles, ClusterRoles), (3) **application workloads**. "The container image is scanned separately to the Kubernetes resource definition (the YAML manifest)". Image scanned for vulnerabilities/misconfigurations/exposed secrets; manifest scanned for vulnerabilities (OSS libraries, control-plane and node components), misconfigurations, secrets.
- **Operates through the Kubernetes API**: requires a role/cluster-role with `list` on all resources in core/apps/batch/networking.k8s.io/rbac API groups; node-collector jobs need additional permissions (nodes/proxy, pods/log, jobs, namespaces).
- **Node-Collector**: a scan job collecting node configuration parameters, evaluated against Kubernetes hardening (e.g. **CIS benchmark**) → infrastructure assessment and CIS compliance reports.
- **Compliance reports out of the box**: NSA/CISA Kubernetes Hardening Guidance, CIS Kubernetes Benchmark, CIS for RKE2/EKS, **Pod Security Standards Baseline / Restricted**.
- **KBOM** (Kubernetes Bill of Materials): manifest of control-plane components, node components, addons with versions/images; CycloneDX output; scannable for vulnerabilities.
- **Trivy Operator**: installable inside the cluster for continuous scanning.
- **Supply chain**: SBOM generation, attestation (cosign), VEX; CI/CD integrations (GitHub Actions, GitLab CI, CircleCI, ...); Kyverno policy integration; misconfiguration checks with Rego custom checks; KSV check IDs referencing PSS Restricted controls (e.g. KSV001 privilege escalation → securityContext.allowPrivilegeEscalation).

### Product D — Falco (Layer A, OSS runtime-detection pole)

From docs home body page (2026-09-07):

- "Falco is a cloud native security tool that provides **runtime security across hosts, containers, Kubernetes, and cloud environments**... a monitoring and detection agent that observes events (such as Linux kernel events and other data sources through plugins) and delivers real-time alerts based on custom rules. Falco also enhances these events by integrating contextual metadata from **container runtimes and Kubernetes**."
- Mechanism: parses Linux syscalls from the kernel at runtime → asserts the stream against a rules engine → alerts on violation. Drivers: modern eBPF probe (default) or kernel module.
- Default rules detect: privilege escalation using privileged containers, namespace changes (setns), writes to well-known directories, unexpected network connections, spawned shells (sh/bash/...), SSH binaries, mutation of coreutils/login binaries, etc.
- **Plugins** extend event sources: **Kubernetes Audit Events**, CloudTrail, Okta.
- Outputs: stdout, file, syslog, spawned program, HTTP endpoint; falcosidekick ecosystem project forwards to many channels.
- Deployment: Kubernetes Operator, Helm, container, host packages. CNCF graduated project, originally created by Sysdig.
- Detection + alert only — no image scanning, no admission control, no console (in the OSS core).

### Product E — Aqua Security Platform (Layer B-, product page only)

From https://www.aquasec.com/products/container-security/ (2026-09-07); docs behind sign-in — no operational claims:

- Positioning: "Complete lifecycle container security... from build through runtime". Three pillars on the page: **Find & Remediate Risks Early** (automated image scanning in the DevOps pipeline: known vulnerabilities, hidden malware, embedded secrets, misconfigurations, open-source issues — "with a premium version of the award-winning cloud native security scanner Aqua Trivy"); **Enforce Security Guardrails** ("assurance policies that permit only container images that meet all compliance standards to pass through", per-pipeline/environment risk thresholds); **Detect & Stop Runtime Attacks** (granular runtime policies, **drift prevention**, threat response).
- Additional named capabilities: Dynamic Threat Analysis (DTA) — "run container images in a secure virtual sandbox" for fileless/zero-day threats; vulnerability prioritization using "exploitability, risk score, severity, and whether the workloads are running"; compliance reporting across "NIST, PCI DSS, GDPR, and CIS Benchmarks".
- Vendor structure: Container Security, Kubernetes Security, CWPP, CSPM, Serverless as separate product pages under an Aqua CNAPP platform — the vendor itself maintains the container/K8s slice as a named product line beside CWPP.
- No operational detail asserted (docs unreachable).

### Product F — Kubernetes platform-native security machinery (Layer A, platform docs)

From kubernetes.io (2026-09-07) — the machinery the products assess, enforce, and integrate with:

- **Pod Security Standards**: three levels — **Privileged** ("purposely-open, and entirely unrestricted"), **Baseline** ("prevents known privilege escalations", lists enforced/disallowed controls e.g. hostProcess, hostPorts, capabilities), **Restricted** ("current Pod hardening best practices"). Enforcement via the built-in **Pod Security Admission** controller or namespace labels; tasks docs cover "Enforce Pod Security Standards by Configuring the Built-in Admission Controller".
- Security doc-tree: Cloud Native Security, Pod Security Admission, Service Accounts, RBAC good practices, Secrets good practices, Multi-tenancy, Hardening Guides (authentication, scheduler...), API-server bypass risks, Linux kernel security constraints, Security Checklist, Application Security Checklist.
- Admission extension points: ValidatingAdmissionWebhook / Dynamic Admission Control (referenced directly by Sysdig's docs), AdmissionReview API.
- Audit: cluster auditing (API audit logging) — the log stream K8s-aware detection consumes.
- Significance for the Type: the platform itself ships the security primitives (PSS, RBAC, audit, admission webhooks); the Application Type's products assess conformance to them, enforce them as gates, and detect violations against them. This is what makes the Type K8s-*native* rather than merely host-security-redeployed.

### Product G — Red Hat Advanced Cluster Security (unreachable)

docs.redhat.com returned 403 then 503 (2 attempts). No capability claims. Market context only: RHACS (StackRox heritage) is the K8s-native commercial platform pole; its existence is consistent with the structural pattern observed in the fetched sample but is not used as evidence for any specific capability.

## Cross-product Comparison

| Dimension | Sysdig Secure | Prisma Cloud Compute | Trivy (OSS) | Falco (OSS) | Aqua (page-level) |
|---|---|---|---|---|---|
| Image vulnerability scanning | ✔ pipeline/registry/runtime findings | ✔ Defender manifest → Console; twistcli CI | ✔ image target (vuln/misconfig/secret) | ✘ | ✔ (page-level) |
| Registry scanning | ✔ 9 named registries | ✔ periodic registry scans | ✔ private-registry auth for image pulls | ✘ | ✔ (implied) |
| Misconfiguration assessment (manifests/workloads) | ✔ posture policies | ✔ compliance checks (root, NET_RAW, secrets) | ✔ KSV checks vs PSS | ✘ | ✔ (page-level) |
| Cluster posture / compliance frameworks | ✔ posture + compliance findings; KSPM | ✔ K8s + Istio compliance checks | ✔ CIS K8s, NSA/CISA, PSS Baseline/Restricted, node-collector | ✘ | ✔ CIS/NIST/PCI (page-level) |
| Admission control at deploy | ✔ ValidatingAdmissionWebhook; vuln/posture/supply-chain policies | ✔ OPA/Rego dynamic admission controller | ✘ (Kyverno integration tutorial only) | ✘ | ✔ assurance gates (page-level) |
| Runtime threat detection w/ container+K8s context | ✔ Falco libraries; drift detection; K8s audit policy | ✔ runtime defense (host policy; prevent mode) | ✘ | ✔ core purpose (syscalls + K8s metadata) | ✔ runtime protection + drift prevention (page-level) |
| Response actions | ✔ kill/isolate/quarantine/pod delete/rollout restart | ✔ Defender enforcement (prevent) | ✘ | ✘ (alerts only; falcosidekick forwards) | ✔ "block attacks" (page-level) |
| K8s audit-log analysis | ✔ Kubernetes Audit Logging + Falco K8s-audit library | (audit-log integrations per CNAPP pass) | ✘ | ✔ K8s audit plugin | — |
| SBOM / KBOM | (lifecycle visibility) | (code-to-cloud mapping per CNAPP pass) | ✔ SBOM + **KBOM** (CycloneDX) | ✘ | — |
| Image signature validation | ✔ Sigstore integrations | (supply-chain policies per CNAPP pass) | ✔ cosign attestation | ✘ | — |
| CI/CD integration | ✔ Jenkins/GitHub/GitLab plugins; CLI scanner | ✔ twistcli | ✔ CI tutorials | ✘ | ✔ pipeline scanning (page-level) |
| Console / UI | ✔ full SaaS console | ✔ Console (self-hostable) | ✘ CLI + reports | ✘ CLI + outputs | ✔ (platform) |
| Deployment form | SaaS + in-cluster Shield (DaemonSet) | SaaS or self-hosted Console + Defenders | CLI binary; optional Operator | agent (eBPF/module) via Operator/Helm | SaaS platform + agents |
| Scope posture | container/K8s-first platform with host/serverless/cloud breadth | suite pillar (Compute Edition) inside CNAPP | single-function scanner (multi-target) | single-function runtime detector | container/K8s product line inside CNAPP |

Reading: image scanning + misconfiguration/posture assessment + K8s-context runtime detection are present across the commercial sample; admission control and response actions are present in the platforms but absent in the OSS single-function poles; SBOM/KBOM and signature validation are newer common additions. No single function family is present in every product — but every product's function is expressed in container/K8s object terms.

## Abstraction Levels

### L0 — Defining Invariant

1. **The container estate as the managed object domain** — the product's security objects are the artifacts and environments of the container model: container images (immutable, registry-addressed build artifacts), the containerized workloads running from them (containers/pods), and/or the cluster platform configuration those workloads run under (namespaces, RBAC, pod security, network policy, control-plane components). At least one of these object families, addressed in the estate's native terms (image, container, pod, namespace, cluster).
2. **Security assessment and/or enforcement bound to those objects** — the product produces security findings (vulnerabilities, misconfigurations, exposed secrets, malware, runtime threats) and/or enforces policy (gates deployment, blocks runtime behavior) where both the findings and the policies are expressed in container/K8s terms.

Test: remove the container/K8s object domain → generic Vulnerability Management, CWPP, or EDR. Remove the security function → Kubernetes Management Platform. Both removals destroy the Type; nothing smaller does.

Deliberately NOT in L0 (checked against the sample): Kubernetes itself (Docker-era container security without a cluster still fits — the cluster is the dominant modern realization, not the definition); admission control (absent in Trivy/Falco); runtime sensors (absent in Trivy); consoles (absent in OSS poles); CI integration; compliance frameworks; SBOM/KBOM; signature validation; response actions.

### L1 — Common Mature Structure

Present across most of the commercial sample (and partially in OSS poles):

- **Image vulnerability scanning** at pipeline (CLI in CI), registry (periodic scans of registry contents), and runtime (running workloads) — the same image object assessed at three lifecycle points.
- **Misconfiguration / posture assessment** of workload manifests and cluster configuration against hardening baselines (privileged containers, root users, capabilities, secrets in env vars).
- **Compliance reporting** against recognized frameworks: CIS Kubernetes Benchmark, NSA/CISA Hardening Guidance, Pod Security Standards (directly observed in Trivy; posture/compliance findings in Sysdig and Prisma; page-level at Aqua).
- **Runtime threat detection with container/K8s context** — behavioral rules over process/file/network events enriched with container, pod, and cluster metadata; Kubernetes audit-log analysis as a detection source.
- **Admission control at deploy time** — a Kubernetes-native webhook evaluating pods against vulnerability/posture/supply-chain policies, allowing or rejecting before scheduling (Sysdig, Prisma; Aqua page-level).
- **Findings prioritization and triage** — severity plus context (in-use packages, running workloads, exploitability); risk acceptance workflows.
- **SBOM/KBOM generation and image signature validation** — supply-chain evidence for images and clusters (Trivy, Sysdig; newer common additions).
- **Response actions** — containment (kill/isolate/quarantine) executed from events, with recorded history (platforms).
- **Estate onboarding machinery** — in-cluster components (DaemonSets, operators, admission webhooks), registry connectors, CI plugins, cloud-account connections.
- **Console + CLI + API** delivery, with forwarding to SIEM/ticketing.

### L2 — Variant / Optional Structure

- **Function breadth**: single-function OSS tools (scanner-only, detection-only) ↔ full platforms covering build→deploy→runtime→posture.
- **Scope posture**: container/K8s-specialized product ↔ pillar inside a CWPP/CNAPP suite ↔ K8s-native platform for managed distributions (OpenShift/EKS/GKE/AKS specialization appears in registry/compliance lists).
- **Visibility mechanism**: in-cluster sensors (eBPF/kernel-module agents, DaemonSets) ↔ API/manifest-only scanning (kubeconfig-based, agentless) ↔ registry/CI-only; often combined in one product.
- **Enforcement depth**: detect-only ↔ alert/block admission ↔ runtime prevention (kill/isolate) ↔ drift prevention (block out-of-image processes/files).
- **Deployment posture**: SaaS console ↔ self-hosted console ↔ pure CLI/OSS.
- **Network security depth**: network policy generation, exposure analysis (container network surface).
- **Sandbox/dynamic analysis** of images before deployment (Aqua DTA, page-level).
- **AI assistance** (era-common: Sysdig Sage, agentic response at Aqua).

### L3 — Vendor-specific (research notes only)

- Sysdig: Shield/Cluster Shield naming, Rapid Response, Zones scoping, SysQL, Sage, Falco heritage (Falco itself is CNCF, not vendor-specific).
- Prisma Cloud: Defender agent family, twistcli, Intelligence Stream, Rego/OPA admission implementation, Compute vs Enterprise Edition split, self-hostable Console.
- Aqua: assurance policies, Dynamic Threat Analysis sandbox, drift prevention branding, "premium Trivy" relationship, Aquademy.
- Trivy: Node-Collector, KBOM term, Trivy Operator, KSV check-ID vocabulary, AVD (Aqua Vulnerability Database) references.
- Falco: falcoctl, falcosidekick, drivers (eBPF probe/kernel module), rules-file format.
- RHACS: unreachable — nothing asserted.

## Rejected Findings (considered, not promoted)

1. **"Admission control is definitional"** — rejected: Trivy and Falco (both legitimately container/K8s security tools) have no admission control; it is the deploy-time expression of assessment capabilities, not the defining core.
2. **"Runtime sensors/agents are definitional"** — rejected: Trivy scans clusters through the Kubernetes API with no resident sensor; agentless and CI-only postures are documented. The sensor is the common mechanism, not the invariant.
3. **"Kubernetes is definitional"** — rejected: Docker-era container security (image + registry scanning without a cluster) and today's Docker-only solutions (Aqua maintains a Docker Security solution page) fit the core. The cluster is the dominant modern surface, not the definition.
4. **"Compliance frameworks (CIS/NSA) are definitional"** — rejected: they are the content of posture assessment, common but not invariant; a scanner with no compliance reports is still this Type.
5. **"Console/dashboard is definitional"** — rejected: OSS poles are CLI-only.
6. **"This Type = CWPP restricted to containers"** — rejected as a definition (see Boundary Findings): the container Type's center of gravity includes build-time (image/registry/pipeline) and deploy-time (admission) and cluster-configuration surfaces that CWPP does not center; the runtime-defense overlap is real but partial.

## Boundary Findings

1. **vs CWPP** — the flagged seam holds from this side. CWPP centers the **running-workload estate** (hosts/VMs first, containers as children) with runtime defense as its heart; Container & Kubernetes Security centers the **container packaging model and cluster platform**: the image lifecycle (build → registry → deploy gate → runtime), the workload manifest, and the cluster configuration. Structural test: a product that only scans images in registries/CI and gates deployments (no host estate) is this Type, not CWPP; a product whose estate is hosts/VMs with container children is CWPP. Overlap zone: container runtime defense — both Types claim it; documented as the joint-review zone (consistent with the CWPP pass flag).
2. **vs CNAPP** — CNAPP is the umbrella over the whole cloud estate (posture + vulnerabilities + runtime + identity); container/K8s security is one object-domain pillar. Sampled vendors themselves sell the container slice as a named product line inside a CNAPP (Aqua; Prisma Compute Edition). Test: add cloud-account posture + identity entitlements + data/API posture → CNAPP.
3. **vs CSPM** — CSPM assesses cloud-account/service configuration; this Type assesses the container/cluster estate. The bridge concept is KSPM (Kubernetes security posture management) — cluster-config posture, which sampled products include as a section, not the whole.
4. **vs Software Supply Chain Security / SCA / SBOM Management** — those center the source dependency graph and build pipeline provenance; this Type centers the image/registry/deployment/cluster lifecycle. Overlap: image scanning includes OS-package and language-dependency vulnerabilities, and signature/attestation machinery is shared. Test: remove the image/cluster objects (keep source repos + dependencies) → SCA/SSCS.
5. **vs Secrets Security** — secrets detection *inside images/manifests* is a scanner capability here; enterprise secrets storage/rotation is the other Type.
6. **vs Kubernetes Management Platform (§14)** — same object domain, different function: deploy/scale/observe vs assess/enforce/gate. Test: remove security findings/policies → K8s management.
7. **vs Vulnerability Management (§15)** — generic vuln-program lifecycle (asset inventory, scan scheduling, remediation SLAs) vs container-estate-specific scanning/gating. Container security products embed image-vuln management as a capability; the standalone Type is program-level and estate-agnostic.
8. **去掉什么就变成另一个 Type**: remove the container/K8s object domain → CWPP/EDR/generic VM; remove the security function → K8s Management Platform; remove the image/cluster estate (keep source deps) → SCA/SSCS; remove runtime+cluster depth (keep cloud account config) → CSPM; umbrella over all estates → CNAPP.

## Historical / Market-Sample Check

- **Pre-Kubernetes container security** (Docker-era image scanning, registry-integrated vulnerability scanning, mid-2010s): image as object + security findings — satisfies L0 with no cluster machinery. The core therefore must not require Kubernetes, admission control, or cluster posture. ✓ (definition written container-estate-first)
- **Single-function OSS tools** (Trivy scanner-only; Falco detection-only; both current and widely deployed): each satisfies L0 with one function family. The core therefore must not require platform breadth (console, admission, response). ✓
- **K8s-native platforms** (Sysdig, Prisma Compute, RHACS-pole): satisfy L0 with the full stack. ✓
- **Suite-embedded realizations** (Compute Edition inside Prisma CNAPP; Aqua container line inside Aqua CNAPP): the same capability set delivered as a pillar. ✓
- Conclusion: the definition survives all four generations/shapes; nothing in L0 is era- or business-model-specific.

## Uncertainties

1. RHACS (the K8s-native platform pole) unreachable — the sample's K8s-native pole is evidenced by Sysdig/Prisma/Trivy/Falco K8s machinery instead; RHACS-specific structure unverified.
2. Aqua operational detail unverified (docs behind sign-in) — its capabilities are recorded at page level only.
3. Exact market boundary between "Container Security" and "Kubernetes Security" product naming (Aqua ships both pages) — treated as one Type here; naming is vendor packaging, not structure.
4. Whether the market will keep this leaf distinct from CWPP/CNAPP or absorb it entirely into CNAPP packaging — recorded as the standing joint-review flag; this pass holds the object-domain seam as the working boundary.
5. Network-policy generation and exposure analysis depth varies; not deeply researched (single-product depth at Sysdig).

## Final Synthesis

Container & Kubernetes Security is the security layer specialized to the container estate. Its managed objects are the container model's own artifacts and environments: images (build-time, registry-addressed), the containers/pods running from them, and the cluster platform configuration beneath them. Its function is security assessment and enforcement expressed in those objects' native terms — findings about images, manifests, and cluster configuration; policies that gate deployments and constrain runtime behavior. Around this minimal core, mature products assemble a stable standard structure: image scanning at pipeline/registry/runtime, misconfiguration and posture assessment against recognized hardening baselines (CIS, NSA/CISA, Pod Security Standards), K8s-context runtime threat detection with audit-log analysis, admission control at deploy time, findings prioritization with risk acceptance, SBOM/KBOM and signature evidence, response actions, and console/CLI/API delivery with SIEM/ticketing forwarding. The Type's poles: single-function OSS tools (scanner-only, detection-only), container/K8s-specialized platforms, suite pillars inside CWPP/CNAPP offerings, and K8s-native platforms for managed distributions. The boundary with CWPP is an object-domain and center-of-gravity boundary (running-workload estate vs container packaging model + cluster platform), with container runtime defense as the documented overlap zone; the boundary with CNAPP is umbrella-vs-pillar; the boundary with Kubernetes Management is function (assess/enforce vs deploy/operate).
