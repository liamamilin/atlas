# Container & Kubernetes Security

## Overview

A **Container & Kubernetes Security** application is security software specialized to the container estate: its managed objects are the container model's own artifacts and environments — container images, the containerized workloads running from them, and the cluster platform configuration beneath them — and its function is to assess and enforce security **in those objects' native terms**.

The defining core is small:

```text
Container estate as the managed object domain
├── container images (build-time, registry-addressed artifacts)
├── running containers / pods (runtime entities)
└── cluster platform configuration (namespaces, RBAC, pod security,
    network policy, control-plane components)
    └── security assessment and/or enforcement
        bound to those objects (findings and policies
        expressed as image / container / pod / cluster properties)
```

Everything else the market associates with the category — admission control, runtime sensors, compliance frameworks, SBOMs, consoles, CI integration — is standard equipment of mature products, not what makes the product a container-security product. A registry-and-pipeline image scanner with no cluster machinery, and a runtime detector with no image scanning, both remain recognizable members of this Type; a tool that manages clusters without security findings and policies does not.

## Users & Context

Primary users:

- **Security engineers / AppSec teams** — define scanning and admission policies, triage findings, investigate runtime events, own compliance reporting.
- **Platform / DevOps engineers** — onboard clusters and registries, install in-cluster components, tune gates so they do not block legitimate deployments.

Secondary users:

- **Developers** — consume scan results in the pipeline and fix images/manifests before deployment.
- **Compliance and audit functions** — consume framework reports (CIS benchmarks, NSA/CISA hardening guidance, Pod Security Standards conformance).
- **SOC analysts** — receive forwarded runtime events and admission decisions through SIEM/ticketing integrations.

The work context is the software delivery lifecycle of containerized applications: images are built in CI, stored in registries, deployed into clusters, and run under a platform whose configuration determines much of the risk. The security work is distributed across that lifecycle, which is why the Type's products typically appear both as in-cluster components and as central consoles.

## Core Model

### The Defining Core

**The container estate as the managed object domain.** Three object families, addressed in the estate's native vocabulary:

- **Container image** — the immutable, registry-addressed packaging artifact. It carries an operating-system layer, language dependencies, application files, and build-time configuration. It is the unit that gets scanned, signed, and gated. The image is what makes this Type *container* security rather than host security: risk is assessed on the artifact before and as it moves toward deployment.
- **Running container / pod** — the runtime entity instantiated from an image, together with its workload definition (the manifest that declares what to run and with which privileges). Runtime security observes what these entities actually do — processes, files, network — enriched with container and cluster context.
- **Cluster platform configuration** — the Kubernetes (or container-platform) control surface the workloads run under: namespaces, roles and bindings, pod security settings, network policies, and the platform components themselves (API server, kubelet, addons). This is what makes the Type *Kubernetes-native*: the platform ships its own security primitives, and these products assess conformance to them, enforce them as gates, and detect violations against them.

**Security assessment and/or enforcement bound to those objects.** The product produces findings — vulnerabilities, misconfigurations, exposed secrets, malware, runtime threats — and/or enforces policy — gating deployments, constraining runtime behavior — where both findings and policies are stated as properties of images, manifests, pods, and clusters. A capability that produces neither findings nor enforcement on container-estate objects is outside the Type, however management-oriented it is.

### Standard Capabilities of Mature Products

These are the capabilities the market expects; they extend the core without defining it:

- **Image vulnerability scanning at three lifecycle points** — in the pipeline (CLI scanners invoked from CI), in the registry (periodic scans of stored images), and at runtime (running workloads). The same image object is reassessed as it moves.
- **Misconfiguration and posture assessment** — evaluation of workload manifests and cluster configuration against hardening baselines: privileged containers, root users, capability sets, host mounts and host ports, secrets in environment variables.
- **Compliance reporting** — conformance reports against recognized frameworks, most prominently the CIS Kubernetes Benchmark, the NSA/CISA Kubernetes Hardening Guidance, and the Kubernetes Pod Security Standards (baseline and restricted levels).
- **Runtime threat detection with container/Kubernetes context** — behavioral rules over process, file, and network events, enriched with container, pod, and cluster metadata; analysis of Kubernetes audit logs as a detection source; drift detection (behavior departing from the image definition).
- **Admission control at deploy time** — a Kubernetes-native admission webhook that evaluates each pod-creation request against vulnerability, posture, and supply-chain policies and allows or rejects it before scheduling.
- **Findings prioritization and triage** — severity combined with context (whether the affected package is actually loaded, whether the workload is running, exploitability), plus risk-acceptance workflows so teams can record why a finding is not being fixed.
- **Supply-chain evidence** — SBOM generation for images, bill-of-materials for clusters (control-plane and node components with versions), and image signature validation against signing infrastructure.
- **Response actions** — containment executed from security events: stopping or killing containers, isolating network, quarantining files, deleting or restarting pods — with a recorded action history.
- **Estate onboarding machinery** — in-cluster components (privileged agents, admission controllers), registry connectors, CI plugins, and cloud-account connections.
- **Delivery surfaces** — a central console for findings and policies, CLI tools for pipelines, APIs, and forwarding into SIEM and ticketing systems.

### One Estate, Many Realizations

The core is written conceptually. Products realize the same objects differently:

```text
Concept:  Image as security object
Realizations:  pipeline CLI scan · registry-resident scanner ·
               runtime harvest of the running image · SBOM/KBOM attestation

Concept:  Cluster configuration as security object
Realizations:  API-based assessment via kubeconfig · in-cluster posture agents ·
               admission-time evaluation · compliance report generation

Concept:  Runtime visibility
Realizations:  kernel-level sensors (eBPF / kernel modules) ·
               Kubernetes audit-log analysis · cloud control-plane logs
```

A reader who has only seen one realization (for example, only a CI-embedded scanner) should still be able to recognize the others from this model.

## How It Works

The Type's work flows along the image lifecycle. A typical deployment path:

### 1. Connect the estate

```text
Install in-cluster components (agent / admission controller)
→ connect container registries
→ (optionally) connect CI systems and cloud accounts
→ the product builds an inventory of images, workloads, and clusters
```

Onboarding shape varies: some products deploy privileged in-cluster sensors; others operate entirely through the cluster API and registry APIs; many combine both.

### 2. Assess images before deployment

```text
Image built in CI
→ pipeline scanner produces findings (vulnerabilities, secrets,
  misconfigurations, malware)
→ registry scanner re-assesses stored images continuously
→ findings bound to the image, its packages, and its layers
→ SBOM / signature evidence attached where supported
```

### 3. Gate deployment

```text
Pod creation request reaches the cluster
→ admission webhook evaluates it against
  vulnerability / posture / supply-chain policies
→ allow → workload schedules
→ reject → workload never reaches a node; decision is logged
  (who attempted the deployment, which policy matched, why blocked)
```

The gate is the deploy-time expression of the same policies used for assessment. Vendor guidance for admission gates is explicit that overly strict policies can block legitimate deployments, and recommends testing gate policies in non-production environments before enforcing them broadly.

### 4. Detect and respond at runtime

```text
Sensors observe process / file / network activity in containers
→ events enriched with container, pod, and cluster context
→ rules flag threats (privilege escalation, shells, unexpected
  connections, drift from the image definition, suspicious
  API-server activity via audit logs)
→ analyst investigates (activity history, captures)
→ response actions contain the threat (stop/isolate/quarantine),
  recorded in an action history
```

### 5. Maintain posture and prove compliance

```text
Cluster configuration assessed against hardening baselines
→ posture findings per workload / namespace / cluster
→ compliance reports generated for recognized frameworks
→ remediation tracked; risk acceptance recorded where not fixed
```

### 6. Triage and feed the organization

```text
Findings prioritized by context (running? loaded? exploitable?)
→ assigned / exported to ticketing
→ events forwarded to SIEM
→ developers receive pipeline feedback; security owns policy
```

### Core vs Common vs Optional

**Defining core** — without these, not this Type:

- container-estate objects (images and/or running workloads and/or cluster configuration) as the managed domain
- security findings and/or enforcement expressed in those objects' native terms

**Standard capabilities** — present in most mature products:

- image scanning (pipeline / registry / runtime)
- misconfiguration & posture assessment
- compliance reporting (CIS / NSA-CISA / PSS)
- K8s-context runtime detection
- admission control
- prioritization & risk acceptance
- SBOM/KBOM & signature validation
- response actions
- console + CLI + integrations

**Variant / optional** — depends on product shape and customer:

- in-cluster sensors vs API-only visibility
- runtime prevention (kill/isolate) vs detection-only
- drift prevention, network policy generation, exposure analysis
- sandbox/dynamic analysis of images
- managed-distribution specialization (OpenShift, EKS, GKE, AKS)
- AI assistance

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Central console

The security team's primary surface.

- Purpose: manage the estate's security state — findings, policies, events, compliance.
- Typical information: image/workload/cluster inventory; findings by severity and lifecycle stage; runtime events; posture and compliance status; policy definitions.
- Primary actions: triage findings, accept risks, author/tune policies, investigate events, trigger response actions, generate reports.

### Pipeline / CLI scanner

The developer-facing surface.

- Purpose: assess images and manifests inside CI before they are pushed.
- Typical information: scan results per image (vulnerabilities, secrets, misconfigurations) with severity and fix guidance.
- Primary actions: scan, filter by severity, fail the build on policy violation, output machine-readable results.

### In-cluster components

The Kubernetes-native surfaces, operated through cluster tooling (Helm/Operator manifests, kubectl).

- **Admission controller** — a webhook registered with the API server; evaluates pod-creation requests; allow/reject decisions logged.
- **Node/cluster sensors** — privileged agents collecting runtime and configuration data.
- **Cluster scanners** — jobs that enumerate workloads, images, and configuration through the cluster API (requiring appropriately scoped read permissions).

### Registry connectors

Configuration surfaces binding the product to image registries, so stored images are scanned continuously without a pipeline.

### Forwarding targets

SIEM, ticketing, and messaging integrations through which runtime events and admission decisions reach the SOC and the broader organization.

## Important Rules / Behaviors

### Findings and policies speak the estate's language

A finding is bound to an image (with packages and layers), a workload (with its manifest), or a cluster object (namespace, role, node) — not to an abstract "asset". This binding is what allows the same finding to be tracked from pipeline to registry to runtime.

### The same image is reassessed across its lifecycle

Pipeline results, registry results, and runtime results are views of the same image object at different points. A vulnerability fixed in a rebuilt image appears as a new image version, not as an edit to the old finding.

### Admission gates can block deployments

Enforcement policies run in the deployment path of the cluster. Vendor documentation for admission gates states the risk directly: misconfigured or overly strict policies may block legitimate workloads, and teams are advised to test gates in non-production environments before broad enforcement. Gate decisions (who attempted what, which policy matched, allowed or rejected) are recorded as an audit trail.

### Runtime detection is context-enriched

Runtime rules evaluate behavior *relative to* the container and cluster context — a process running outside the image's definition, a shell in a workload that never runs shells, an API-server call from an unexpected identity. Drift from the image definition is a first-class detection category.

### Prioritization depends on runtime context

The market's dominant prioritization signal is whether the vulnerable artifact is actually in use — the package loaded, the workload running. Findings on running workloads outrank findings on dormant images; several products make "in use" an explicit triage dimension, and risk acceptance is a recorded decision rather than an informal ignore.

### The platform's own primitives are the baseline

Pod security levels, RBAC, network policies, and audit logging are defined by the container platform itself. Products assess conformance to those primitives and extend them with enforcement; they do not replace them. This is why compliance reports reference platform-published standards (Pod Security Standards baseline/restricted, CIS benchmarks, NSA/CISA guidance) rather than proprietary baselines alone.

## Variants

- **Single-function open-source tools** — a scanner only (images, manifests, clusters) or a runtime detector only; CLI-first, no console. The minimal realizations of the Type.
- **Container/K8s-specialized platforms** — the full build→deploy→runtime→posture stack as a standalone product; the classic pure-play shape.
- **Suite pillars** — the same capability set delivered as the container/workload pillar of a broader cloud-security platform (CNAPP/CWPP suites); the container slice remains a named product line inside the suite.
- **Kubernetes-native platforms** — products centered on managed distributions and cluster platforms (OpenShift, EKS, GKE, AKS), often with distribution-specific compliance content.
- **Posture-led vs runtime-led emphasis** — some products lead with scanning/posture and add runtime; runtime-heritage products (behavioral detection lineages) lead with runtime and add scanning.
- **Visibility posture** — sensor-based (privileged in-cluster agents), API-based (kubeconfig/registry access, no resident sensor), or hybrid.
- **Enforcement posture** — detection-only → alert/block gates → runtime prevention → drift prevention.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Cloud Workload Protection / CWPP | adjacent, heavy overlap | CWPP centers the running-workload estate (hosts/VMs first, containers as children) with runtime defense at its heart; this Type centers the container packaging model and cluster platform — image lifecycle, manifests, admission gates, cluster configuration. A registry/pipeline scanner with deployment gates and no host estate is this Type, not CWPP. Container runtime defense is the documented overlap zone. |
| CNAPP | umbrella | CNAPP spans the whole cloud estate (posture, vulnerabilities, runtime, identity entitlements); this Type is one object-domain pillar within it. Vendors themselves sell the container slice as a named line inside a CNAPP. |
| CSPM | adjacent | CSPM assesses cloud-account and service configuration; this Type assesses the container/cluster estate. Cluster-configuration posture (KSPM) is the bridge section, not the whole. |
| Software Supply Chain Security / SCA | adjacent | Those center the source dependency graph and build provenance; this Type centers images, registries, deployment, and clusters. Image scanning includes dependency vulnerabilities, and signature/attestation machinery is shared — but remove the image/cluster objects and only the dependency graph remains, which is the other Type. |
| Vulnerability Management | capability overlap | Generic vulnerability management is a program-level, estate-agnostic lifecycle (inventory, scans, remediation tracking). Here, vulnerability scanning is specialized to images and clusters and is bound to the deployment path. |
| Secrets Security | capability overlap | Detecting secrets embedded in images/manifests is a scanner capability here; enterprise secrets storage and rotation is the other Type. |
| Kubernetes Management Platform | same objects, different function | Management deploys, scales, and observes clusters; this Type assesses and enforces security on them. Remove findings and policies from this Type and it becomes management; add them to management and it becomes security. |
| WAF / API Security | different surface | Those protect north-south traffic to applications; this Type secures the container estate itself. |

The CWPP boundary is the most important one, because the two Types overlap on container runtime defense and image scanning. The structural difference is the center of gravity: the running-workload estate (hosts first) versus the container packaging model and cluster platform (images, manifests, gates, cluster configuration first).

## Representative Products

- **Sysdig Secure** — container/K8s runtime heritage (Falco lineage); full platform spanning pipeline/registry/runtime scanning, admission control, posture, and response.
- **Prisma Cloud Compute (Palo Alto Networks)** — suite-embedded container security (Compute Edition) with image/registry scanning, OPA-based admission control, and runtime defense.
- **Trivy** — open-source scanner (Aqua Security) covering images, manifests, and clusters; the minimal scanner-pole realization.
- **Falco** — CNCF open-source runtime detection engine; the minimal detection-pole realization.
- **Aqua Security Platform** — container-security pure-play vendor; Trivy's commercial parent (documented at product-page level in this research).

The defining core was checked against pre-Kubernetes container security (image/registry scanning without a cluster) and against single-function OSS tools, so it does not depend on any single era, deployment model, or business model.

## Sources

Research date: **2026-09-07**

- Sysdig Secure documentation — https://docs.sysdig.com/en/docs/sysdig-secure/ and https://docs.sysdig.com/en/sysdig-secure/admission-controller/
- Prisma Cloud Compute documentation — https://docs.prismacloud.io/ (documentation query interface)
- Trivy documentation — https://trivy.dev/latest/docs/ and https://trivy.dev/latest/docs/target/kubernetes/
- Falco documentation — https://falco.org/docs/
- Aqua Security product page — https://www.aquasec.com/products/container-security/
- Kubernetes documentation — https://kubernetes.io/docs/concepts/security/pod-security-standards/

> Sourcing limitations: Aqua's operational documentation is behind a sign-in wall (unreachable from the research environment), so its capabilities are recorded at product-page level only. Red Hat Advanced Cluster Security documentation was unreachable (access denied), so no product-specific claims are made about it. Precise operational parameters (scan intervals, timeouts, registry lists, default settings) observed in vendor documentation are intentionally not stated in this document; they remain in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis against CWPP/CNAPP/CSPM are recorded in the paired Research Notes.
