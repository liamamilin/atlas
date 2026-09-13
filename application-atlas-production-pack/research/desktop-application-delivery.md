# Research Notes — Desktop & Application Delivery

## Research Goal

Understand what the Application Type "Desktop & Application Delivery" (DIRECTORY §14, IT/Cloud/Infrastructure) actually is as a category of software: what objects exist inside such a product, what its administrators and end users do, what the delivery workflow looks like, and where its boundaries lie against neighboring Types (Application Deployment Management, Endpoint Management/UEM, Patch Management, RMM, remote access, virtualization management).

## Initial Boundary (hypothesis before research)

- Hypothesis: this is the "server-based computing / VDI / DaaS" family — centrally hosting desktops and applications on server or cloud compute and delivering them to users as remote sessions, without installing the software on the endpoint.
- Expected nearest neighbors: Application Deployment Management (installs apps onto endpoints), Endpoint Management / UEM (manages devices), Remote access / remote support (peer-to-peer session into one machine), Virtualization Management (manages host infrastructure), Cloud IDE (developer-audience session delivery).
- Unknowns going in: whether the leaf is really one Type or a conflation of two (desktop delivery vs application delivery); whether "Remote PC" remoting belongs inside; how cloud-native DaaS fits the classic on-prem broker model.

## Research Questions

1. What is a "published application / desktop" and how is it defined and organized?
2. How are users entitled to resources, and how does the connection get brokered to a host?
3. How is the host-side infrastructure modeled (session hosts, catalogs, host pools, farms)?
4. What does the end user see and use (native client, web client, seamless windows, full desktop)?
5. What per-session services exist (printing, drives, USB, profiles, multimedia, policies)?
6. What lifecycles/states matter (session states, persistent vs non-persistent assignment, image updates, autoscale)?
7. How do products differ in packaging philosophy (full-stack on-prem suite vs cloud control plane vs fully managed DaaS vs app-only streaming)?
8. What separates this Type from installation-based deployment and device management?
9. Historical check: do 1990s-era server-based computing products (terminal-server publishing) satisfy the definition?

## Representative Products

| Product | Why chosen | Evidence tier reached |
|---|---|---|
| Citrix Virtual Apps and Desktops | Category founder and reference implementation; enterprise tier | Tier 1 — official product docs (landing + technical overview TOC; body of delivery-methods page not captured, see Limitations) |
| Omnissa Horizon 8 (formerly VMware Horizon) | Major alternative full-stack VDI; different lineage | Tier 2 — official product page with component descriptions; docs portal URLs recorded but not fetched |
| Microsoft Azure Virtual Desktop | Cloud control-plane model; replaces classic RDS | Tier 1 — Microsoft Learn overview + terminology pages |
| Parallels RAS | Mid-market all-in-one philosophy; simplicity positioning | Tier 2 — official product page (rich technical FAQ) |
| Amazon WorkSpaces / WorkSpaces Applications (ex-AppStream 2.0) | Fully managed DaaS; app-only streaming pole (no full desktop required) | Tier 1 — AWS documentation |

Different philosophies covered: full-stack on-prem suite (Citrix, Horizon), cloud control plane (AVD), all-in-one mid-market (Parallels RAS), hyperscaler-managed desktops and pure app streaming (AWS).

## Sources

Fetched 2026-09-08:

- Citrix Virtual Apps and Desktops — product docs landing: https://docs.citrix.com/en-us/citrix-virtual-apps-desktops (fetched)
- Citrix — technical overview (TOC incl. delivery methods, HDX, machine catalogs, delivery groups, application groups, seamless, devices, printing, policies, Director, Autoscale): https://docs.citrix.com/en-us/citrix-virtual-apps-desktops/technical-overview (fetched)
- Citrix — delivery methods page: https://docs.citrix.com/en-us/citrix-virtual-apps-desktops/technical-overview/delivery-methods (fetched; body content not rendered in capture — limitation)
- Microsoft Learn — "What is Azure Virtual Desktop?": https://learn.microsoft.com/en-us/azure/virtual-desktop/overview (fetched)
- Microsoft Learn — "Azure Virtual Desktop terminology" (host pools, application groups, workspaces, session states): https://learn.microsoft.com/en-us/azure/virtual-desktop/environment-setup (redirected to /terminology, fetched)
- Omnissa — Horizon 8 product page (component descriptions: Connection Server, Horizon Client, Horizon Agent, UAG, AD; App Volumes; deployment options): https://www.omnissa.com/products/horizon/ (fetched)
- Parallels — RAS product page (app publishing, RDSH/VDI/remote PC, single console, gateway, HALB, FSLogix, MSIX App Attach/App-V, clients, peripherals, multi-tenancy): https://www.parallels.com/products/ras/ (fetched)
- AWS — "What is Amazon WorkSpaces?": https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces.html (fetched)
- AWS — "What Is Amazon WorkSpaces Applications?" (ex-AppStream 2.0): https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html (fetched)

Not reached: Omnissa docs portal (docs.omnissa.com returned 404 on both attempted paths); docs.vmware.com migrated to Broadcom portal (generic landing only); Citrix delivery-methods body text not captured (JS-rendered). Per evidence rules, Horizon and Parallels claims are calibrated to Tier-2 product-page evidence; no numeric limits or defaults asserted anywhere.

## Product Observations

### Citrix Virtual Apps and Desktops (Tier 1 — official docs structure)

Evidence: A (direct observation of official documentation structure; specific operational parameters not captured).

- Official docs organize the product as: install core components → install VDAs → create a site → create/manage connections to virtualization platforms (XenServer, VMware, Azure, AWS, GCP, Nutanix, OpenShift, Azure Local, SCCM, HPE, Oracle…) → prepare master images → create machine catalogs → create delivery groups → create application groups → set up StoreFront / Workspace → monitor with Director.
- "Machine catalogs" = collections of identical machines provisioned from a master image ("prepared image machine catalogs", "image management", machine identities: AD-joined, Entra hybrid joined, non-domain-joined).
- "Delivery groups" and "application groups" = the objects through which machines and applications are assigned to users ("Assign users and apps" section).
- "Publish" is a first-class verb: "Publish seamless applications", "Publish packaged applications" (app packages), "Publish UWP applications", "Linux VDA Published Applications", "Publish content".
- Remote PC Access is a documented deployment mode (remoting physical PCs); Server VDI also documented.
- Session services documented as first-class sections: printing (Universal Print Driver, client printer redirection, Universal Print Server), USB devices, client drive mapping, scanning (TWAIN/WIA/SANE), webcams, serial ports, multimedia (HTML5 video redirection, browser content redirection, Teams optimization), graphics (Thinwire, HDX 3D Pro, GPU acceleration), seamless windows (window dragging, system tray redirection).
- Policies engine with templates, prioritization, policy sets, and a large settings reference (ICA policy settings, profile management, load management, virtual IP, WEM).
- Operational machinery: Autoscale (schedule-based and load-based, cloud burst), load balancing machines, power management, Local Host Cache (resilience), zones, session resilience, VDA registration, delegated administration, Director monitoring (site analytics, application usage monitoring, probes, cost optimization).
- Companion products: Profile Management, Citrix Provisioning, User personalization layer.

### Omnissa Horizon 8 (Tier 2 — official product page)

Evidence: A for the component descriptions quoted on the vendor's own page; B when generalized.

- Self-definition: "a virtual desktop infrastructure (VDI) and app solution that allows organizations to provide users with secure access to full desktops or individual apps on any device while maintaining centralized control over performance, policies, and infrastructure."
- Named components: Horizon Connection Server ("brokers user connections to available desktops and applications... authenticates users via Active Directory, validates their entitlements, and directs them to the correct virtual desktop or app"); Horizon Client ("runs on user devices and launches virtual desktops or apps"); Horizon Agent ("installed on desktops, RDSH servers, or physical systems... delivers virtual desktop or app sessions to users through secure protocols"); Unified Access Gateway (secure external access); Active Directory for identity.
- App Volumes: "Manage and deliver applications on demand... centralized packaging and lifecycle management" (application layering).
- Dynamic Environment Manager: granular policies for clipboard, device redirection, printing, session actions.
- Security framing: "Keep data centralized and off the endpoint"; session recording; MFA/True SSO.
- Deployment breadth: on-prem (vSphere, Nutanix AHV, OpenStack, Red Hat OpenShift), public cloud (Azure, AWS, Google Cloud, Oracle, Alibaba), hybrid (burst, DR).

### Microsoft Azure Virtual Desktop (Tier 1 — Microsoft Learn)

Evidence: A.

- Self-definition: "a desktop and app virtualization service that runs on Azure"; "Deliver a full Windows experience... Offer full desktops or use RemoteApp to deliver individual apps."
- Object model (terminology page):
  - Host pool = "a collection of Azure virtual machines that are registered to Azure Virtual Desktop as session hosts"; sourced from the same image; two types: Personal (each session host assigned to an individual user) and Pooled (sessions load-balanced to any session host; multiple users per host).
  - Application group = "controls access to a full desktop or a logical grouping of applications that are available on session hosts in a single host pool"; two types: Desktop and RemoteApp; users can be assigned to multiple application groups across multiple host pools.
  - Workspace = "a logical grouping of application groups" that users see; each application group must be associated with a workspace.
- User sessions: active, disconnected (window closed without sign-out; reconnection redirects to the same session), pending (placeholder reserving a spot during sign-in).
- Management: Azure portal/CLI/PowerShell/REST to "create and configure host pools, application groups, workspaces, assign users, and publish resources"; autoscale; validation environment; session host configuration (service-managed lifecycle) vs standard management; hybrid variant (Azure Virtual Desktop on Azure Local).
- Clients: Windows App or Remote Desktop client; native app or HTML5 web client; reverse connections (no inbound ports).
- Image and updates: personal host pools patched with Windows Update/ConfigMgr-type tools; pooled host pools updated "by redeploying session hosts from updated images instead of traditional updates" — a defining operational pattern of the Type (patch the image, not the running fleet).
- FSLogix named as the profile-data approach for pooled hosts.

### Parallels RAS (Tier 2 — official product page)

Evidence: A for the vendor's own description; B when generalized.

- Self-definition: "a flexible virtual application and desktop delivery solution that empowers organizations of all sizes to work securely from anywhere, on any device"; FAQ: "centralizes applications and desktops on a server or cloud infrastructure, allowing users to securely access them from various devices... user authentication, load balancing, and encryption".
- Capabilities listed: application publishing; hybrid DaaS/VDI; remote to any device; multi-tenant deployment; high availability load balancing; reporting and monitoring.
- Administration: single console for "app and desktop management, image handling, reporting, gateway, load balancing, access control, authentication and authorization"; manage "virtual apps, desktops, and remote PCs based on user needs... VDI for specific use cases like contractors, while virtual applications cater to users needing only a single application."
- Integrations: hypervisors (VMware ESX, Hyper-V, Scale, Nutanix; API-based custom providers: Proxmox, KVM, Xen…), clouds (Azure, AWS EC2), and AVD management ("customize AVD workloads directly within the Parallels RAS administration console").
- Session services: peripherals (printers, scanners, smartcards) pass-through with admin restriction; selective multi-monitor; drag-and-drop local files; session pre-launch based on user habits.
- Packaging: built-in FSLogix support; integrated MSIX App Attach and App-V for app deployment to session hosts.
- Security: SSL/TLS + FIPS mode, built-in MFA and IdP integrations (Okta, Ping, Azure AD), rule-filter-based contextual access, included Secure Gateway, auditing/logs; Let's Encrypt certificate management.

### Amazon WorkSpaces / WorkSpaces Applications (Tier 1 — AWS docs)

Evidence: A.

- WorkSpaces: "provision virtual, cloud-based desktops known as WorkSpaces for your users" (Windows/Ubuntu/Rocky/RHEL); "Users can access their virtual desktops from multiple devices or web browsers."
- Two modes: WorkSpaces Personal (persistent, "provisioned for their exclusive use... similar to a physical desktop computer that's assigned to an individual") and WorkSpaces Pools ("non-persistent... hosted on ephemeral infrastructure").
- Bundles and custom images define hardware/software configurations; directory integration (AD/Entra); protocol choice (PCoIP or DCV); MFA; encryption; IP access controls; monthly/hourly billing.
- WorkSpaces Applications (formerly AppStream 2.0): "a fully managed application streaming service that provides users with instant access to their desktop applications from anywhere"; "manages the AWS resources required to host and run your applications, scales automatically, and provides access to your users on demand"; client or HTML5 web browser; "Your applications run on AWS compute resources, and data is never stored on users' devices"; single maintained version of each application. (Also documents AI-agent access via MCP — current-market layer, not definitional.)
- Confirms the app-only pole: application delivery does NOT require delivering a full desktop.

## Cross-product Comparison

| Structure | Citrix CVAD | Omnissa Horizon | Azure Virtual Desktop | Parallels RAS | AWS WorkSpaces(+Applications) |
|---|---|---|---|---|---|
| Centralized hosted execution (session hosts / VDI / remote PC) | ✔ (VDAs on servers/VMs; Remote PC Access) | ✔ (Agent on desktops, RDSH servers, physical systems) | ✔ (session host VMs) | ✔ (RDSH/VDI/remote PCs) | ✔ (managed hosts; WorkSpaces = desktops; Applications = app hosts) |
| Published named resources (apps and/or desktops) | ✔ "publish seamless applications", packaged apps, content | ✔ (full desktops or individual apps) | ✔ (application groups: Desktop / RemoteApp) | ✔ (application publishing) | ✔ (WorkSpaces bundles; Applications = streamed apps) |
| Per-user/group entitlement to resources | ✔ (delivery/application groups; delegated admin) | ✔ (Connection Server "validates their entitlements") | ✔ (users assigned to application groups) | ✔ (access control in console) | ✔ (users provisioned to WorkSpaces; app entitlements in Applications) |
| Broker/connection management + load balancing | ✔ (Delivery Controller; load balance machines; Local Host Cache) | ✔ (Connection Server brokering) | ✔ (load balancing breadth/depth; pending sessions) | ✔ (HALB) | ✔ (Personal assignment; Pools load balancing) |
| Image/catalog/fleet provisioning; persistent vs non-persistent | ✔ (master images → machine catalogs) | ✔ (desktop pools; App Volumes) | ✔ (host pools personal/pooled; golden image) | ✔ (image handling) | ✔ (bundles/images; Personal vs Pools) |
| Power management / autoscale | ✔ (Autoscale) | (not observed on fetched page — cloud/DR docs only) | ✔ (autoscale scaling plans) | ✔ (stop/deallocate VMs when unused) | (Pools scale automatically; Personal billing) |
| Display protocol + native clients + web client | ✔ (HDX/ICA; Workspace app; web) | ✔ (Blast Extreme named via docs link; Horizon Client) | ✔ (RDP-based; Windows App/Remote Desktop client; HTML5 web) | ✔ (Parallels Client for all platforms; HTML5 web) | ✔ (PCoIP/DCV; clients; web) |
| Peripheral/print/drive/USB redirection & session services | ✔ (extensive doc sections) | ✔ (peripheral support with IT control) | (named in RDP-property model; not itemized in fetched pages) | ✔ (peripherals pass-through, printers, scanners, smartcards) | (not itemized in fetched overview) |
| Session policy engine (clipboard, redirection, etc.) | ✔ (policies + settings reference) | ✔ (DEM granular policies) | ✔ (RDP properties/host pool settings — named, not itemized) | ✔ (rule-filter access; admin restrictions) | ✔ (IP allow-lists; encryption settings) |
| Profile management for non-persistent use | ✔ (Profile Management; user personalization layer) | ✔ (DEM; App Volumes writable volumes — via docs links) | ✔ (FSLogix) | ✔ (built-in FSLogix support) | ✔ (Pools: curated/ephemeral) |
| Admin console + monitoring/analytics | ✔ (Web Studio; Director) | ✔ (unified console) | ✔ (portal; AVD Insights) | ✔ (single console; reporting/monitoring) | ✔ (console; Advisor) |
| Secure remote access gateway / identity | ✔ (Citrix Gateway; FIDO2, smart cards, FAS) | ✔ (UAG; MFA, True SSO) | ✔ (reverse connect; Entra) | ✔ (Secure Gateway; MFA; IdPs) | ✔ (directory integration; MFA; IP access) |
| App packaging/lifecycle layering | ✔ (app packages; App Layering via companion products) | ✔ (App Volumes) | ✔ (MSIX/Appx formats; MSIX app attach named in ecosystem) | ✔ (MSIX App Attach + App-V integration) | ✔ (single-version app management) |

Readout: every sampled product holds the first five rows jointly — centralized hosted execution, published named resources, per-user entitlement, brokering/load balancing, and image-based fleet provisioning with persistent/non-persistent modes. These are the Type's skeleton. Rows 6–13 are very common mature structure (L1), with per-product gaps in what the fetched pages itemize rather than in what the products do.

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant (all four held jointly)

1. **Centralized hosted execution** — the delivered applications/desktops run on central compute (session hosts, VDI desktops, remote hosts) operated by the organization or its provider, not on the user's endpoint. Remove → install-based software distribution (Application Deployment Management) or a SaaS/web app portfolio; the Type disappears.
2. **Published resources under standing entitlement** — applications and/or desktops are surfaced as named, standing deliverables ("published" apps/desktops) that specific users or groups are granted access to as configuration, not as ad-hoc connections. Remove → raw remote access / ad-hoc RDP into machines; there is no "delivery" layer.
3. **Remote interactive session as the delivery vehicle** — the user receives a live, interactive session (full desktop or seamless application window) streamed from the host; execution and data remain remote while the interface is local. Remove → file/package download; the product becomes a distribution mechanism rather than a delivery service.
4. **A managed fleet behind the resources** — resources are backed by a maintained pool/farm of hosts provisioned from managed images/configurations that the platform provisions, assigns, load-balances, and reclaims. Remove → a single ad-hoc remote-access tool or screen share; there is nothing to "deliver" at scale.

Justification for minimality: AWS WorkSpaces Applications holds all four while never delivering a desktop; Citrix Remote PC Access holds all four while delivering physical PCs; historical terminal-server publishing (WinFrame-era server-based computing) holds 1–3 with a primitive form of 4 — the definition does not depend on hypervisors, cloud control planes, autoscale, HTML5 clients, or multi-session hosts, all of which are later refinements.

### L1 — Common Mature Structure (cross-product, evidence layer B)

- Connection brokering and load balancing across hosts; session reconnection to the user's existing session.
- Golden-image-based provisioning of host fleets (machine catalogs / host pools / bundles); persistent (personal) vs non-persistent (pooled) assignment as the two canonical fleet postures.
- Power management and autoscale (schedule- and load-based) for cost control.
- Client surface family: native clients per OS + browser (HTML5) client; full-desktop mode and seamless/application mode.
- Session services layer: printing (with universal print drivers), client drive mapping, USB and peripheral redirection, clipboard, multi-monitor, webcam/audio/video (incl. collaboration-app optimization).
- Session policy engine governing clipboard/redirection/session behavior, enforced per user/group/context.
- Profile management / user personalization so non-persistent sessions still carry user state (FSLogix-class containers).
- Central admin console + monitoring/analytics (sessions, machines, usage, cost) with delegated administration.
- Identity integration (directory/IdP, SSO, MFA) and a secure remote-access gateway component.
- Application packaging/lifecycle layering (MSIX/App-V app attach, app layering/volumes) to keep images lean and deliver apps on demand.

### L2 — Variant / Optional Structure

- Resource mix: apps-only (RDSH publishing; WorkSpaces Applications), shared desktops, personal VDI desktops, remote physical PCs — and the mix sold per use case (contractors → VDI; task workers → published apps).
- Deployment substrate: on-prem datacenter, private/public/hybrid cloud, hyperscaler-managed control plane (no customer-run brokers/gateways), fully managed DaaS.
- Host OS: Windows multi-session, Windows single-session, Linux (Ubuntu/Rocky/RHEL, Linux VDA).
- Endpoint posture: managed PC, BYOD, thin client, browser-only.
- Workload positioning: remote work/BYOD enablement, secure containment (keep data off endpoints), contractor/outsourcer access, high-graphics/GPU workloads, education labs, M&A/divestiture rapid provisioning, MSP multi-tenancy.
- Billing/commercial shape: concurrent-user licensing, per-user, hourly/monthly consumption (L3 detail per vendor; consumption-vs-subscription is a market-level variant).
- AI-era extensions (agent access to hosted apps via tool protocols) — current-market layer, not definitional.

### L3 — Vendor-specific (kept out of the final document)

- Citrix: VDA, Delivery Controller, StoreFront, Web Studio, Director, HDX/ICA virtual channels, Thinwire, Machine Creation Services, Citrix Provisioning, Local Host Cache, Zones, Workspace Environment Management, Autoscale (branded), App Layering, Remote PC Access (as named mode).
- Omnissa: Connection Server, Horizon Agent, Horizon Client, Unified Access Gateway, Blast Extreme, App Volumes, Dynamic Environment Manager, True SSO, Horizon Cloud.
- Microsoft: host pool / application group / workspace triad, RemoteApp branding, Windows multi-session OS exclusivity, FSLogix, Windows App client, reverse-connect architecture, Azure Local hybrid mode, validation environments.
- Parallels: RAS Console, Secure Gateway, HALB, session pre-launch (patented), concurrent-user single-license model, Custom Provider Framework, built-in Let's Encrypt management.
- AWS: WorkSpaces Personal/Pools, bundles, PCoIP/DCV choice, WorkSpaces Applications stacks/fleets/image builder, pay-as-you-go framing, MCP agent access.

## Vendor-specific Findings

- Citrix's documentation exposes the richest explicit machinery for resilience and scale (Local Host Cache, zones, session resilience, cloud burst tagging) — product-specific elaboration of L1 brokering/fleet concepts.
- AVD documents precise session-state semantics (active / disconnected / pending) and the "pooled hosts are patched by redeploying images, personal hosts by traditional updates" split — the cleanest official articulation of the image-as-patch-unit pattern; treat the pattern as L1 (all fleet products face it) and the exact wording as AVD-specific.
- Parallels markets session pre-launch and a single concurrent-user licensing model — commercial/UX differentiation, not structural.
- Omnissa and Parallels both position themselves explicitly against the other's enterprise competitor (Horizon as "Citrix alternative"; RAS as "Citrix alternative"/Horizon alternative) — market-structure evidence that these are one Type, not three.
- Citrix and Parallels can manage Azure Virtual Desktop workloads and AWS infrastructure through their consoles — cross-product convergence: the Type's concepts are becoming interoperable layers rather than siloed stacks.

## Boundary Findings

- **vs Application Deployment Management**: that Type's unit of work is a package installed onto a managed endpoint; execution moves to the device. Here execution never lands on the device; the unit of work is a published resource and a session. Removal test: strip centralized execution from this Type → you get a software distribution system; add endpoint installation to this Type → it becomes a deployment suite. Both leaves stand.
- **vs Endpoint Management / UEM**: UEM's managed object is the device (enrollment, configuration, compliance, wipe); this Type's managed objects are resources, hosts, and sessions. The vendors overlap deliberately (Omnissa sells Horizon beside Workspace ONE; Microsoft pairs AVD with Intune; WorkSpaces docs mention Intune enrollment of WorkSpaces) — integration neighbors, distinct Types.
- **vs Patch Management**: patch management targets the update state of installed software; this Type patches by image redeployment for pooled fleets as an implementation of keeping the fleet current, which is not its defining purpose.
- **vs Remote access / remote support tools**: those deliver a point-to-point session into one specific existing machine, typically unmanaged and unpublished. This Type is a standing, cataloged, entitled service across many hosts. The overlap case is real and internal to the Type: Citrix Remote PC Access and Horizon Agent-on-physical-PCs show remote-PC remoting absorbed as a mode of the delivery framework (evidence: both vendors' docs).
- **vs Virtualization Management**: virtualization management runs the hypervisor/host estate; this type consumes it (multiple products explicitly list supported hypervisors as connections, not as their own subject).
- **vs Cloud IDE / dev workspaces**: same delivery mechanics (session from central compute) but a developer-audience, code-centric object model; audience + object difference keeps them separate.
- **vs VPN / ZTNA**: network-layer reachability vs application-layer sessions; gateways inside delivery products exist to carry the session, not to open the network.
- **Historical check (§24 reasoning)**: mid-1990s server-based computing (terminal servers publishing applications, clients connecting over thin protocols) satisfies the L0 set — central execution, published apps, per-user grants, remote sessions — without hypervisors, pools, images, or web clients. Mainframe-era terminal sessions prefigure remote execution but lack the desktop/application resource model and are treated as prehistory, not membership. The definition therefore does not over-fit to the modern cloud/DaaS generation.
- **Internal cohesion**: "Desktop & Application Delivery" is one Type, not two. Every sampled product delivers both; application-only and desktop-only products are poles of one resource-mix variant, not separate Types.

## Uncertainties

- Horizon and Parallels evidence is Tier 2 (product pages). Their structural claims are corroborated by Tier-1 sources of the other three products (brokering, entitlement, gateways, profiles, image provisioning all exist cross-product), but product-specific operational details for Horizon/RAS were not verified against admin guides. No precise claims are made about them in the final document.
- Citrix delivery-methods body text was not captured (JS-rendered page); the Citrix observations rest on the docs' navigation structure, which is itself official Tier-1 documentation of the product's concept set, but per-feature behavior specifics were not read.
- Peripheral redirection and policy settings were itemized only in Citrix docs and Parallels/Horizon pages; AVD's equivalents (RDP properties) were named but not itemized in fetched pages — the final document therefore describes this layer generically.
- Licensing/commercial models are recorded per-vendor only and excluded from the final document.
- Historical member set (pre-hypervisor terminal-server products) was reasoned from type structure rather than re-researched from archived manuals; asserted only as a fit-check, not with product detail.

## Final Synthesis

Desktop & Application Delivery is the IT-operator Type whose system of record is the published resource catalog: applications and desktops that run on a centrally managed fleet and are delivered to entitled users as live remote sessions. Its defining act is keeping execution and data off the endpoint while making the software feel locally present. Around that core, mature products add brokering/load balancing, image-based fleet provisioning with persistent and non-persistent modes, autoscale, a rich session-services layer (printing, drives, peripherals, multimedia), policy engines, profile management, admin/monitoring consoles, gateways, and app-packaging/layering. The Type's market spans full-stack suites, cloud control planes, all-in-one mid-market tools, and hyperscaler-managed desktop/app streaming; the resource mix (apps, shared desktops, personal desktops, remote PCs) and deployment substrate are variants, not definitions.
