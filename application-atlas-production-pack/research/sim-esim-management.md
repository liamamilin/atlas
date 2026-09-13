# Research Notes — SIM / eSIM Management

Research date: 2026-09-09
Leaf: SIM / eSIM Management (§19 Energy, Utilities & Telecommunications)
Slug: sim-esim-management

## Research Goal

Understand what a SIM / eSIM Management application actually is from real products: what the managed object is, what lifecycle it moves through, how eSIM changes (or does not change) the model, who operates the system, and where its boundaries lie against Subscriber Management, Telecom Provisioning, Telecom Inventory Management, and IoT connectivity platforms.

## Initial Boundary

Initial hypothesis (pre-research):

- The Type manages the SIM credential population — physical SIM cards and eSIM profiles — through a lifecycle: entry into the system, activation, in-life state changes, retirement.
- Neighbors: Subscriber Management (customer/account side), Telecom Provisioning Platform (network-service activation side), Telecom Inventory Management (network equipment), Telecom Number Management (MSISDN ranges).
- Open question: is the enterprise/IoT "SIM management" surface (IoT connectivity platforms) the same Type as the operator-side SIM lifecycle system, or a sibling?

## Research Questions

1. What is the SIM as a managed object — what identifies it (ICCID / IMSI / MSISDN / profile), what state does it carry?
2. What lifecycle do SIMs move through, and which transitions are irreversible?
3. How does eSIM change the model — profile lifecycle, eUICC host, RSP roles, install/enable/delete?
4. How is a SIM bound to a device / subscription, and how does rebinding work?
5. What in-life operations exist (suspend/resume, reassignment, configuration, monitoring)?
6. What interfaces and roles exist (console, API, care tools, batch campaigns)?
7. What rules matter (state constraints, charging coupling, security, permissions)?

## Representative Products

Selected for market representativeness, documentation completeness, and pole diversity:

| Product | Pole | Why selected |
|---|---|---|
| emnify | Enterprise/IoT connectivity platform (cloud-native portal + API) | Excellent public docs; SIM Inventory + SIM lifecycle management pages |
| Soracom | Enterprise/IoT connectivity platform (developer console + API/CLI) | Excellent public docs; full subscriber-status state machine + eSIM profile state machine |
| G+D (Giesecke+Devrient) AirOn360 SDM / eSIM management | SIM vendor / operator-side (MNO customers) | Carrier-grade OTA SIM lifecycle (issuance→deactivation) + eSIM RSP platform definitions |

Attempted and abandoned (source-access limitations):

- Cellusys (SIM Lifecycle Management, operator pole) — site JS-rendered, content unreachable (2 attempts).
- Comarch (telecom SIM card management) — 403/404.
- Mobileum — 404 on guessed path.
- Twilio Super SIM docs — 404 (IoT business transferred to KORE).

Consequence: the operator-BSS pole (inventory/personalization/assignment inside an operator's BSS) is evidenced only through G+D's operator-facing SDM documentation. Assertions about operator-side workflows are calibrated accordingly (see Uncertainties).

## Sources

Tier 1 (official operational documentation):

- emnify Documentation: https://docs.emnify.com/ — SIM Inventory (https://docs.emnify.com/portal/sim-inventory), SIM lifecycle management (https://docs.emnify.com/services/sim-lifecycle-management), Register SIMs (https://docs.emnify.com/quickstart/register-sims), eSIMs overview (https://docs.emnify.com/services/esims), Consumer eSIM (https://docs.emnify.com/services/consumer-esim)
- Soracom Developers Documentation: https://developers.soracom.io/en/docs/ — Air for Cellular overview (/en/docs/air/), SIM Management (/en/docs/air/sim-management/), Subscriber Status (/en/docs/air/subscriber-status/), eSIM Profiles (/en/docs/air/esim-profiles/)
- G+D: SIM & IoT Device Management (AirOn360 SDM) (https://www.gi-de.com/en/digital-security/connectivity-iot/sim-device-management), eSIM management & eUICC (https://www.gi-de.com/en/digital-security/connectivity-iot/esim-management)

Tier 2 (official product pages): G+D pages above double as product pages; emnify/Soracom pages are user guides (Tier 1).

## Product A — emnify (IoT SuperNetwork)

### Key observations (Evidence layer A unless noted)

**SIM Inventory (portal page).** "Provides a complete list of your registered SIMs." Columns: ICCID (with Luhn check digit), MSISDN, SIM Status, Device name (assignment; or "Not assigned"), Technology (Standard SIM / M2M eUICC (eSIM) / Consumer eSIM / iSIM). Detail view adds: SIM ID (used as `sim_id` in REST API), assigned device ID, IMSI, SIM form factor, connectivity type, SIM type/quality grade. Additional views: Events (logs) and Statistics (aggregated usage) "if the SIM has been assigned to a device and is Active."

**SIM states (SIM lifecycle management page).** Five states configurable via the SIM Inventory or the SIM REST API:

- **Issued** — initial state after the SIM has been registered to an account; not usable; no traffic or charges; can be patched to Factory Test; "impossible to transition the SIM back to Issued once it has been in another state."
- **Activated** — enabled, can use network services if connected to a device with configured policies; chargeable if activated anytime during the month.
- **Suspended** — temporarily blocks an Activated SIM from network access; can be reactivated and suspended again at any time.
- **Factory Test** — enabled, limited traffic within defined data/SMS thresholds, then automatically moves to Activated.
- **Deleted** — permanently removes the SIM from the SIM Inventory; cannot be restored for network access.

Also documented: an Activated SIM assigned to a Disabled endpoint still accrues costs — "be sure to suspend the assigned SIM to avoid unexpected charges" (state coupling between SIM and device objects).

**Entry into the system (Register SIMs).** SIMs enter via registration: auto-register at order time (recommended), or manual registration using the BIC (Batch Identification Code) printed on the card (BIC1, individual) or packaging (BIC2, batch); single-SIM or SIM-batch registration; optional auto-activate and device creation at registration; bulk registration via REST API. Ordering from the SIM Shop expands inventory.

**Exit (Delete SIMs).** Permanent deletion, individually or by uploaded list, with confirmation; deleted SIMs "no longer usable for network access and cannot be recovered"; reduces signaling and costs.

**Bulk operations.** Create devices (with service/coverage policies, tags, IMEI lock option), Deactivate SIMs (no undo), Transfer SIMs between Workspaces (multi-workspace customers).

**eSIM (services/esims).** Product types: Standard UICC; Classic eSIM (M2M, SGP.02); Consumer eSIM (SGP.22); Advanced eSIM (IoT, SGP.32); iSIM. "eSIM profiles that can be downloaded onto physical eSIMs." Bootstrap eSIMs (consumer SGP.22 / IoT SGP.32) ship with an emnify profile enabling connectivity used to download further profiles. Multi-IMSI applet with per-country preferred IMSI lists and automatic switching.

**Consumer eSIM activation (services/consumer-esim).** Activation methods: MDM (zero-touch, large-scale; pushes SM-DP+ address or activation code), QR code, activation code (LPA string), Apple Universal Link. Comparison table of methods (user interaction, scale suitability, automation).

## Product B — Soracom (Air for Cellular)

### Key observations

**SIM Management screen (console).** "Where you'll find most SIM management functions": view details of registered IoT SIMs, search, change status, adjust speed class, more. List columns: SIM ID, Name, Group, ICCID, IMSI, MSISDN, IP address, Status, Last online, Last location update, Country/Area, Plan, Bundle(s), Subscription, Module Type (form factor; `profilePackage` for eSIM profiles), Speed class, Expiry Date/Time, IMEI Lock, Termination Protection, Tags. CSV download of the full SIM list. Search by attributes (Name, Group, SIM ID, IMSI, MSISDN, ICCID, Serial Number, Tag); filters by session status, subscriber status, subscription, module type.

**Actions on SIMs.** Session actions (remote access, web terminal, ping, SMS, packet capture, delete session); SIM actions (Activate / Deactivate / Standby / Suspend / Terminate; Add Subscription; Add Virtual SIM; Change bundle; Transfer to another operator / Cancel transfer); Settings (change group, expiration, speed class, IMEI lock, termination protection); Logs & diagnostics (run diagnostics, view logs, view data usage). Certain actions only available for a single selected SIM.

**Subscriber Status (the lifecycle).** "Each Soracom IoT SIM has a Status that indicates its subscription state. This status determines whether the SIM can communicate with the cellular network and which subscription fees may apply."

- **Ready** — set automatically upon SIM registration; ready for activation.
- **Testing** — temporary testing mode, limited communication without usage fees within predefined limits; requires advance application.
- **Active** — fully enabled; sub-states ONLINE/OFFLINE reflect whether a data session exists.
- **Inactive** — enabled but data sessions blocked (stop data usage while keeping the SIM enabled).
- **Standby** — disabled but automatically reactivates when a device attempts to connect.
- **Suspended** — disabled; cannot connect until manually reactivated.
- **Terminated** — subscription permanently cancelled; "permanent and irreversible action"; terminated SIMs remain visible for a duration then are automatically removed.

**Subscriber status vs session status.** Two independent state dimensions: subscriber status (subscription state: connectivity permissions + billing behavior) vs session status (Online/Offline: whether a data session currently exists). "These two states are independent."

**Status ↔ capabilities ↔ fees.** A capabilities/fees matrix per status: data communication, SMS, basic fee, usage fees, renewal fee, reactivation fee. Renewal fees apply when a SIM remains in Ready/Standby/Suspended beyond plan-dependent periods; reactivation fees apply when leaving Standby/Suspended. Billing rules vary by subscription plan.

**Status update history.** Registrations, status changes, speed-class changes, bundle changes, group changes, subscription-container additions are recorded and viewable per SIM ("Update history" tab). API: `listSimStatusHistory`.

**Programmatic control.** REST APIs per state transition: `activateSim`, `deactivateSim`, `setSimToStandby`, `suspendSim`, `terminateSim` (plus `/subscribers/` equivalents). SAM (permission) users need `Query:searchSims` and `Group:listGroups` to access the SIM Management screen. "For security reasons, Soracom support agents cannot change SIM statuses on behalf of customers."

**Registration & orders.** SIMs purchased directly are pre-registered to the account; reseller SIMs must be manually registered one at a time (by ICCID/serial). Orders can carry initial Group/Speed Class/Tags applied to all SIMs on registration.

**eSIM Profiles (platform-side profile lifecycle).** Subscription plans available as downloadable eSIM profiles (SGP.22 consumer; device needs an LPA). Order flow with order statuses: Draft → Confirmed → In Progress → Completed / Failed. Per-profile statuses: **Registered** (provisioned and registered to the account, not yet installed) → **Installed** (installed on device, not yet enabled) → **Activated** (enabled on device) → **Deactivated** (disabled on device) → **Deleted** (deleted from device). Installation via QR code or activation code (CSV carries SIM ID, ICCID, IMSI, subscription, **SM-DP+ address**, **Matching ID**, activation code, profile status, installed/modified times). Enabling is device-side via the LPA — "eSIM profiles cannot be enabled from the User Console." Once installed, a profile "cannot be reinstalled again or transferred to another device." Deleting a profile from the device does not terminate the SIM in the account — "make sure to terminate it from your account in order to avoid unnecessary fees."

## Product C — G+D AirOn360 SDM / eSIM management (operator-side)

### Key observations (Tier 2 product pages; marketing-adjacent, calibrated)

**Positioning.** "SIM & Device Management (SDM) ensures seamless connectivity, security, and control over mobile services" for mobile network operators. AirOn360 SDM "allows mobile network operators to remotely manage and update information stored on SIM cards and eSIMs – such as SIM files and applets – via Over-The-Air (OTA) technology... This solution enables full lifecycle management of SIMs, from issuance to deactivation."

**Lifecycle span.** "SIM cards can be managed throughout their lifecycle, from initial provisioning to decommissioning." OTA updates fix bugs, add files and applets, enhance security.

**Operator use cases.**

- Remote SIM activation: "Most SIMs – even eSIMs - need to be personalized and configured for certain services to work properly. This typically happens at the Point of Sale (PoS). AirOn360 SDM performs the required SIM personalization upon SIM activation remotely."
- Optimized SIM logistics: multiple SIM profiles (per subscriber group / MVNO) create stock-keeping and logistics cost; the platform reduces this "to a single stock keeping unit" — profiles and corporate identities created remotely as cards are activated.
- SIM update: remote file-system / applet / device-setting updates to SIMs in the field "during their entire lifetime."
- 5G enabling: remotely convert non-5G SIMs into "Transitional 5G SIMs" without SIM replacement.
- Device detection: real-time device detection and capability information.
- Roaming steering: steer traveling subscribers to preferred roaming partners via PLMN batches / downloaded network lists.

**Operations shape.** "MNOs can run batch campaigns to update the entire SIM fleet anytime, by themselves, or perform individual updates easily – e.g. through customer care teams." Business Intelligence / Customer Care: "search and view subscriber information and history on the SIMs with the possibility to send correction updates," plus testing, verification, monitoring and reporting tools. Deployment: SaaS or on-prem.

**eSIM conceptual model (eSIM management page).**

- "eSIM management - also known as - subscription management": two components — the eUICC chip in the device, and the eSIM management platform enabling Remote SIM Provisioning (RSP): "Specific eSIM profiles can be easily loaded, replaced or removed over-the-air."
- eUICC vs eSIM: "The eUICC is the SIM card or chip equipped with an operating system that enables remote management and can be remotely personalized with a network operator's credentials. The eSIM, in contrast, is the operator profile that is securely downloaded onto the eUICC."
- Security: GSMA-governed PKI; GSMA certification for ecosystem participants.
- Solution family: consumer eSIM, automotive, IoT eSIM (SGP.32 RSP), in-factory profile provisioning (IFPP), M2M (long-lived fleets).

## Cross-product Comparison

| Dimension | emnify | Soracom | G+D AirOn360 SDM |
|---|---|---|---|
| Operating party | enterprise IoT customer | enterprise IoT customer | MNO / MVNO (operator staff, care teams) |
| Unit of record | SIM (ICCID, MSISDN, IMSI, SIM ID) | SIM / subscriber (SIM ID, ICCID, IMSI, MSISDN, serial) | SIM fleet; subscriber information held on SIMs |
| Form covered | Standard SIM, M2M eUICC, Consumer eSIM, iSIM, downloadable profiles | physical SIMs, virtual SIMs, downloadable eSIM profiles | SIM cards and eSIMs (OTA-managed) |
| Entry into system | order (SIM Shop) + registration via BIC, auto-register, API bulk | order (pre-registered) or manual registration by ICCID/serial | personalization/provisioning (remote at activation; single-SKU logistics) |
| Lifecycle states | Issued → Activated ⇄ Suspended; Factory Test; Deleted | Ready → (Testing) → Active ⇄ Inactive; Standby; Suspended; Terminated | issuance → in-life OTA updates → deactivation |
| Terminal state | Deleted — permanent, unrecoverable | Terminated — "permanent and irreversible" | deactivation (end of lifecycle) |
| State semantics | state controls network use + charging | state controls connectivity permissions + billing behavior | state/lifecycle controls what is on the SIM and its services |
| Binding | assign to device (device name/ID on SIM record) | group membership; IMEI lock; transfer to another operator | subscriber association; device detection |
| In-life operations | activate/suspend, bulk ops, workspace transfer | status changes, speed class, expiration, bundles, IMEI lock, termination protection, diagnostics | OTA file/applet updates, batch campaigns, 5G enablement, roaming steering |
| Monitoring | Events + Statistics per SIM | session status, data usage, last online, diagnostics, logs, status history | monitoring/reporting tools; subscriber info + history |
| eSIM profile lifecycle | profile types + bootstrap + activation methods (QR/LPA/MDM/Universal Link) | full profile state machine: Registered → Installed → Activated → Deactivated → Deleted; order state machine | RSP platform: profiles "loaded, replaced or removed over-the-air" |
| Interfaces | Portal (SIM Inventory), REST API | User Console (SIM Management), REST API, CLI | operator platform, care tools, batch campaigns; SaaS or on-prem |
| Permissions | portal roles (implied) | SAM permissions gate screen access; support agents barred from status changes | operator roles (care vs campaign) |

### Stable commonalities (Evidence layer B)

1. **The SIM as individually identified persistent record** carrying telecom identity data (ICCID universally; IMSI/MSISDN commonly) and a lifecycle state — all three.
2. **A state machine controlling network usability** — all three; states differ in name but the pattern (entry state → enabled state → blocked states → terminal state) is identical.
3. **Irreversible terminal state** — emnify Deleted ("cannot be restored"), Soracom Terminated ("permanent and irreversible"), G+D deactivation as lifecycle end.
4. **Entry-by-registration/provisioning** — all three have a defined act that brings a SIM into the managed population (BIC registration / manual registration / remote personalization).
5. **In-life state changes as the daily work** — suspend/resume, reassignment, configuration — all three.
6. **Per-SIM history/audit** — Soracom status history (explicit), emnify Events view, G+D "subscriber information and history on the SIMs."
7. **Bulk/fleet operations** — all three (bulk actions; batch processing; batch campaigns).
8. **eSIM profile as a downloadable, remotely managed credential** — all three, with the profile lifecycle layered on top of the SIM lifecycle.

### Product-specific (Evidence layer A, not generalized)

- emnify: BIC codes, SIM Shop, Factory Test state, Workspace transfers, charge-on-activation rule.
- Soracom: fee coupling per state (renewal/reactivation fees), Standby auto-reactivation, subscriber-vs-session status duality as named concept, support agents barred from status changes, eSIM profile order state machine, plan vocabulary.
- G+D: single-SKU SIM logistics, Transitional 5G SIM conversion, roaming steering via PLMN batches, device-detection-driven configuration.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

Three jointly-held structures:

1. **The SIM population of record** — persistent, individually identified records for each SIM credential (physical card or eSIM profile), each carrying its telecom identity data (ICCID-class identifier; subscriber identity such as IMSI/MSISDN) and its current lifecycle state. Remove → generic asset/inventory registry.
2. **The lifecycle over that population** — a defined entry act (registration/provisioning/personalization) brings each SIM into the system; state-changing operations (activate, suspend/resume, reassign, configure) move it through life; a terminal operation (terminate/delete/deactivate) ends it, and the terminal state is irreversible. Remove → static registry.
3. **Network-access credential semantics** — the SIM record is the credential through which a device authenticates to and uses a mobile subscription; its state governs whether that credential can access network services, and the record carries the binding to device/subscription context. Remove → asset lifecycle management with no telecom meaning; the "SIM" in the Type name dies.

Jointly-held load-bearing:

- 1 alone = SIM stock spreadsheet / asset registry
- 2 alone = generic lifecycle tracker
- 3 alone = network provisioning territory (Telecom Provisioning Platform)
- 1+2 without 3 = asset lifecycle management
- 1+3 without 2 = static credential registry
- 2+3 without 1 = provisioning operations with no population memory

### L1 — Common Mature Structure

- Inventory list surface with search, filters, bulk selection and bulk operations
- Per-SIM detail view: identifiers, state, assignment, history/events, usage
- SIM↔device assignment (and device-side context: IMEI lock)
- Status/event history per SIM
- Session/usage visibility (online state, data usage, last seen)
- eSIM profile lifecycle (order → provision → install via activation code/QR → enable → disable → delete) with platform-side status tracking
- Test/trial states with bounded usage
- Expiration handling
- API/CLI programmatic control
- Tags/groups for fleet organization
- Ordering/procurement integration (SIM shop / orders)

### L2 — Variant / Optional Structure

- **Operating party**: operator-side (MNO/MVNO: OTA SDM, remote personalization, single-SKU logistics, roaming steering, 5G enablement, care-tool workflows) vs enterprise/IoT-side (fleet usage, plans/bundles, diagnostics, workspace organization)
- **Fee coupling to states**: explicit per-state fee matrices and renewal/reactivation fees (one sampled product) vs charge-on-activation (another) vs not surfaced
- **State vocabulary**: Issued/Ready; Activated/Active; Deleted/Terminated — labels vary; the pattern is invariant
- **Subscriber-status vs session-status separation**: explicit named duality in one product; implicit elsewhere
- **eSIM RSP standard family**: SGP.02 (M2M), SGP.22 (consumer), SGP.32 (IoT); bootstrap profiles; in-factory provisioning
- **Consumer eSIM activation channels**: QR code, LPA activation code, MDM zero-touch, platform-specific links
- **Multi-IMSI / subscription containers / automatic network switching**
- **Physical substrate**: plug-in form factors, embedded (MFF2/MFF4), iSIM; quality grades
- **Deployment**: SaaS vs on-prem; multi-workspace/multi-tenant organization
- **Auto-reactivation semantics** (Standby) vs manual-only reactivation (Suspended)

### L3 — Vendor-specific (Research Notes only)

- emnify: BIC1/BIC2 codes, SIM Shop, Factory Test Mode thresholds, SuperNetwork framing, Workspace transfer billing implications
- Soracom: plan01s/plan-D/plan-US… vocabulary, speed classes, coverage types (Global/Japan), renewal-fee tracking date, Napter/Peek/Harvest service mesh, SAM user model, 24h draft-order expiry
- G+D: AirOn360 branding, SmartRoam Hybrid, "Transitional 5G SIM" concept, Kaleido vendor positioning

## Boundary Findings

- **vs Telecom Provisioning Platform**: provisioning activates network services in network elements (subscription registers); SIM management owns the credential population itself. The SIM record's activation state is credential-side; HLR/HSS subscription activation is network-side. Remove the SIM population focus and the credential-state machine → Telecom Provisioning territory.
- **vs Subscriber Management**: subscriber management owns the customer/account/service relationship; the SIM is one credential attached to it. The object of record here is the SIM, not the subscriber. (Operator products surface "subscriber information on the SIM" — the SIM remains the anchor.)
- **vs Telecom Inventory Management**: inventory management tracks network equipment/assets; SIM management tracks access credentials. Physical SIM stock is inventory-like (the stock leg is shared), but credential semantics + network-access binding are the differentiators. Remove credential semantics → asset inventory.
- **vs Telecom Number Management**: numbers (MSISDN ranges) are addresses; SIMs are credentials. A number can be reassigned across SIMs; the SIM record persists through number changes.
- **vs IoT connectivity management platforms**: the CMP's center of gravity is the connectivity service (usage, plans, data pipelines, network services); SIM management is the credential-population layer inside it. In the researched sample, enterprise IoT platforms embed SIM management as their inventory/lifecycle layer; operator-side SDM platforms embed it as the OTA credential layer. This leaf documents the SIM-management core common to both; the connectivity-service layer is common-adjacent, not definitional. **Boundary note for STATUS.md**: the directory has no separate IoT-connectivity-management leaf; if one is added later, the seam is "credential population + lifecycle" (this Type) vs "connectivity service operation" (that Type).
- **vs Card Management System (banking)**: both manage smartcard credentials; the SIM's semantics are mobile-network authentication and subscription access, not payment.

**"Remove what to become the neighbor" tests:**

- Remove the SIM credential semantics (keep customer/account) → Subscriber Management
- Remove the population-of-record (keep network activation) → Telecom Provisioning
- Remove credential semantics (keep physical stock) → Telecom Inventory Management
- Remove the lifecycle (keep only stock lists) → inventory spreadsheet, not this Type

## Historical / Market-Sample Check

Would older, regional, platform-native products still fit the L0?

- Paper-era operator SIM office: a stock ledger of SIM cards by ICCID batch, personalization records (IMSI/keys written at a personalization center), an assignment log binding each ICCID to a subscriber account, activation lists sent to network provisioning, and swap/termination records. This satisfies all three L0 legs — population of record, lifecycle with terminal states, credential semantics — with no OTA, no eSIM, no portal, no API. **Historical check passed at class level.**
- Regional/MVNO variants: an MVNO managing SIMs through a host operator's platform, or a regional operator with locally personalized stock — both satisfy the L0; the RSP machinery is not required.
- eSIM is the modern dominant implementation of the credential (a downloadable profile on an eUICC host instead of a personalized physical card), not a second Type: the profile has identity data, lifecycle states, binding, and terminal states — the same structure. The eSIM profile lifecycle is held as the modern realization of the same lifecycle leg, with the profile-state machine (Registered→Installed→Activated→Deactivated→Deleted) as common mature structure.

## Uncertainties

1. **Operator-BSS pole under-sampled**: Cellusys/Comarch/Mobileum unreachable (JS-rendered/403/404). Operator-side inventory/personalization/assignment workflows are evidenced through G+D's operator-facing SDM pages (Tier 2, marketing-adjacent). Claims about operator-side workflows are written at moderate strength; no precise operator-side workflow details are asserted.
2. **State-name universality**: exact state labels (Issued vs Ready, Deleted vs Terminated, Inactive vs Suspended semantics) vary by product; only the pattern is asserted as invariant.
3. **Fee coupling**: per-state fee matrices observed in one product in detail (Soracom) and charge-on-activation in another (emnify); the general claim "state commonly couples to charging" is written at common-mature strength, not definitional.
4. **eSIM profile state machine**: fully documented in one product (Soracom); emnify documents profile types/activation but not the same per-profile state vocabulary. The profile lifecycle is held as common-mature (cross-checked against G+D's RSP description: "loaded, replaced or removed over-the-air"), while the exact five-state vocabulary is product-specific.
5. **Whether the market treats "SIM management" and "IoT connectivity management" as one or two Types**: recorded as a boundary note; this pass treats SIM management as the credential-population layer.

## Final Synthesis

SIM / eSIM Management is the credential-population system of record for mobile connectivity: it holds every SIM — physical card or eSIM profile — as an individually identified record carrying its telecom identity data and lifecycle state; it brings SIMs into the system through a defined entry act (ordering/registration/provisioning/personalization); it moves them through life with state-changing operations (activate, suspend/resume, reassign, configure, monitor) whose states directly govern whether the credential can access network services; and it retires them through an irreversible terminal act. eSIM does not create a second Type: the eSIM profile is the same managed credential in downloadable form, adding a profile lifecycle (provision → install → enable → disable → delete) executed against eUICC hosts through RSP machinery. The Type is realized on two poles — operator-side (OTA SIM lifecycle for an MNO's fleet: personalization, batch campaigns, care workflows) and enterprise/IoT-side (fleet SIM management inside connectivity platforms: assignment, usage, diagnostics) — sharing one core.
