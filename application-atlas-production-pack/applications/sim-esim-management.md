# SIM / eSIM Management

## Overview

A **SIM / eSIM Management** application is the system of record for a population of SIM credentials — physical SIM cards and eSIM profiles — through which devices connect to mobile networks. It holds every SIM as an individually identified record carrying its telecom identity data and its current lifecycle state; it brings SIMs into the system through a defined entry act (ordering, registration, provisioning, or personalization); it moves them through life with state changes that directly control whether the credential can access network services; and it retires them through a terminal act that cannot be undone.

The defining structure is small:

```text
SIM credential record
└── identity data (card identifier + subscriber identity)
└── lifecycle state
└── binding to device / subscription context
    └── population held and operated as a fleet
```

Everything else commonly associated with the category — usage dashboards, plan and bundle management, diagnostics, OTA applet updates, roaming steering, bootstrap profiles — is widespread in current products but is not what makes the product a SIM management system. Remove the credential population, its lifecycle, or its network-access meaning, and the product becomes something else: an asset registry, a generic lifecycle tracker, or network provisioning.

The "eSIM" half of the name is not a second application type. An eSIM profile is the same managed credential in downloadable form: it has identity data, lifecycle states, a binding, and a terminal state. What eSIM adds is a profile lifecycle — provision, install, enable, disable, delete — executed against embedded SIM chips (eUICCs) through remote SIM provisioning machinery.

## Users & Context

The primary users are operations people who run a fleet of SIMs rather than a single line:

- **Connectivity operations / fleet operators** (enterprise and IoT deployments): register SIMs into their account, assign them to devices, activate and suspend them as devices ship, idle, or retire, and investigate connectivity problems per SIM.
- **Operator SIM / fulfilment teams** (mobile network operators and MVNOs): manage the operator's SIM stock and its lifecycle from issuance to deactivation, run batch updates across the installed SIM base, and keep the credential data on the cards consistent with network and service changes.
- **Customer care / support roles**: look up an individual SIM's identity data, state, and history, and perform single-SIM corrections — status changes, reassignment, configuration updates.

Secondary concerns sit with administrators (permissions, workspace/account organization) and with integration developers, who drive the same operations programmatically through APIs.

The work environment is administrative: web consoles and portals organized around a searchable inventory of SIMs, plus APIs and CLIs for bulk and automated operation. The scale justification is fleet-shaped — hundreds to millions of credentials — which is why bulk operations and programmatic access are standard rather than exceptional.

## Core Model

### The Defining Core

**The SIM credential record.** The unit of record is the individual SIM — a physical card or an eSIM profile — held as a persistent record. Each record carries:

- **Identity data**: a card identifier (ICCID) that uniquely names the credential, plus subscriber identity data (IMSI, and commonly an assigned directory number, MSISDN) that the network uses to recognize the subscription. For an eSIM profile, the record additionally carries the provisioning details used to install it (a provisioning-server address and a matching/activation code).
- **Lifecycle state**: where the SIM currently stands — an entry state after registration, enabled states, blocked states, and a terminal state.
- **Binding context**: what the SIM is attached to — an assigned device, a subscriber account, a group or workspace — and, in mature products, device-side constraints such as an IMEI lock that ties the credential to specific hardware.

**The lifecycle.** Every researched product organizes the population around a state machine with the same shape, whatever the labels:

```text
Entry (registered / provisioned / personalized)
   → enabled (credential usable on the network)
   ⇄ blocked (temporarily unusable: suspended / inactive / standby)
   → terminal (terminated / deleted / deactivated — irreversible)
```

Exact state names vary by product (one product's "Issued" is another's "Ready"; one's "Deleted" is another's "Terminated"). The invariant is the pattern: a defined entry act, state changes that gate network usability, and a terminal state from which the credential does not return.

**Network-access credential semantics.** The SIM record exists because it is the credential through which a device authenticates to a mobile subscription. Its state is not decoration: a suspended or terminated SIM is refused by the network, and an enabled one is served. This is what separates the Type from asset management — the record's state has operational consequences in a live network.

### Capabilities Shared by Mature Products

These make SIM management practical at fleet scale. They are not the definition.

- **Inventory list surface** — a searchable, filterable table of all SIMs in the population, with bulk selection and bulk operations (activate, suspend, delete, reassign, export).
- **Per-SIM detail view** — all identifiers, current state, assignment, and the SIM's history.
- **Status / event history** — a per-SIM record of state changes and significant operations, viewable and commonly available via API.
- **Session and usage visibility** — whether the SIM is currently connected, when it was last online, and its data usage.
- **Device assignment** — linking the SIM record to a device record; in mature products the SIM list shows the assigned device, and assignment is a first-class action.
- **eSIM profile lifecycle** — ordering and provisioning profiles, tracking their install/enable state, and delivering them to devices via activation codes or QR codes.
- **Test states** — bounded trial states that allow limited traffic without full activation.
- **Expiration handling** — time-bounded credentials that expire or incur renewal consequences.
- **Programmatic control** — REST APIs (and commonly CLIs) exposing the same state operations as the console.
- **Organization primitives** — tags, groups, workspaces for structuring large fleets.

### One Structure, Many Implementations

```text
Concept:            SIM credential
Implementations:    personalized physical card (UICC), downloadable eSIM profile
                    on an eUICC chip, integrated SIM (iSIM) in a cellular module

Concept:            Entry act
Implementations:    order + registration (card/batch codes), manual registration
                    by card identifier, remote personalization at activation,
                    in-factory profile provisioning

Concept:            Blocked state
Implementations:    suspend (manual reactivation), inactive (data blocked,
                    SIM enabled), standby (auto-reactivates on connection attempt)

Concept:            Terminal state
Implementations:    delete (removed from inventory), terminate (subscription
                    cancelled, record later purged), deactivation (end of lifecycle)
```

A reader who has only seen one implementation — say, consumer eSIM activation by QR code — should still be able to recognize an operator running batch OTA campaigns over long-deployed plastic cards as the same application type.

## How It Works

### Bring SIMs into the system

```text
Order SIMs (or profiles) from the provider
→ receive physical cards / provisioned profiles
→ register them into the account
   (by card identifier or batch code, or auto-registered at order time)
→ SIMs appear in the inventory in an entry state
→ optionally apply initial configuration (group, policies, tags)
```

Registration is the act that turns a piece of plastic (or a provisioned profile) into a managed record. Operator-side products replace the physical step with remote personalization: the card ships generic and is personalized at activation time, collapsing many card variants into a single stock unit.

### Activate and put the credential to work

```text
Assign the SIM to a device (or ship it inside one)
→ activate the SIM
→ device connects; the network serves the credential
→ state, session, and usage become visible on the record
```

Activation is the pivot of the lifecycle: it is the moment the credential becomes usable, and in most products the moment charging begins.

### Manage the fleet through life

```text
Suspend / resume as devices idle or return to service
→ reassign SIMs between devices, groups, or workspaces
→ update configuration (speed, bundles, expiration, device locks)
→ monitor state, sessions, usage, and history per SIM
→ run bulk operations and batch updates across the fleet
```

This is the daily work of the application. Operator-side products extend it with over-the-air content management — updating files, applets, and settings on the cards themselves — and with fleet-wide campaigns (for example, enabling a new service generation on installed cards without replacement).

### Retire the credential

```text
Terminate or delete the SIM
→ network access ends permanently
→ the record may remain visible for a period, then is purged
→ replacement requires a new credential
```

The terminal act is deliberately irreversible. A terminated SIM cannot be re-enabled; a deleted SIM cannot be restored. This is a structural safety property, not a UI choice.

### The eSIM profile flow

```text
Order eSIM profiles → platform provisions them (order tracked to completion)
→ each profile held in a registered (not yet installed) state
→ install onto a device's eUICC via activation code or QR code
→ enable the profile on the device (device-side action)
→ platform tracks installed / enabled / disabled / deleted states
→ deleting a profile from a device does NOT retire the record —
   the SIM must also be terminated in the account
```

Two properties of this flow matter structurally. First, in the documented consumer-profile flow, installation is a one-way act: an installed profile is not reinstalled or moved to another device — replacing it means provisioning a new profile. Second, the device-side profile state and the account-side SIM state are tracked as related but distinct things — removing a profile from a phone does not cancel the subscription record.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### SIM inventory list

The primary surface: a table of every SIM in the population.

- typical columns: card identifier, subscriber identity, state, assigned device, technology/form factor, last activity
- primary actions: search, filter (by state, technology, assignment, attributes), bulk-select, bulk state changes, export

### SIM detail view

Everything about one credential.

- identity data, current state, assignment, form factor
- history of state changes and operations
- session status, usage, events, diagnostics
- primary actions: change state, assign/reassign, configure, terminate

### Registration / ordering surfaces

Where credentials enter the system.

- order SIMs or profiles; register received cards by identifier or batch code; track provisioning progress of profile orders
- primary actions: place order, register single/batch, auto-register, apply initial configuration

### Operator campaign and care tools

The operator-side realization adds:

- batch campaign management over the installed SIM base (content updates, service enablement)
- care-facing lookup of an individual subscriber's SIM data and history with correction updates

### API / CLI

The same operations exposed programmatically: query the inventory, read and change state, register, terminate, and pull history. Bulk and automated fleet work is normally done here rather than in the console.

## Important Rules / Behaviors

### State controls network access

The lifecycle state is the gate between the credential and the network. Blocked states refuse service; enabled states serve it. This is the operational meaning of the state machine.

### Terminal states are irreversible

Terminated or deleted credentials do not come back. Products make this explicit in their documentation and often require confirmation. Replacement means a new credential.

### Subscription state and session state are different things

A SIM's subscription state (whether the credential may be used) is independent of its session state (whether the device currently has a data connection). An enabled SIM can be offline; a suspended SIM cannot be online. Mature products surface both, and conflating them is a common operator error.

### State commonly couples to charging

The lifecycle state commonly affects what the credential costs — activation is typically when charging begins, blocked states reduce or stop fees, and long-idle states can trigger renewal charges. The exact fee rules vary by product and plan; the coupling itself is the recurring pattern.

### eSIM profile operations are split between platform and device

Provisioning, ordering, and state tracking happen in the management platform; installing, enabling, disabling, and deleting profiles happen on the device through its profile assistant. The platform tracks what it can observe, and the account-side record must be retired separately from the device-side profile.

### State changes are permission-gated and audited

Changing a SIM's state is a consequential act: consoles gate it behind permissions, record it in the SIM's history, and — in at least one researched product — explicitly bar even the vendor's own support staff from performing it on a customer's behalf.

## Variants

- **Operator-side SIM management** — run by a mobile network operator or MVNO over its own subscriber base: remote personalization at activation, OTA content and applet management, fleet-wide batch campaigns, care-tool workflows, roaming steering. The SIM population is the operator's issued base.
- **Enterprise / IoT-side SIM management** — run by a connectivity customer over its fleet: registration, device assignment, state control, usage visibility, diagnostics. The SIM population is the customer's purchased connectivity.
- **Physical-card management** — the classic form: stock, registration, assignment, swap, and retirement of plastic cards across form factors.
- **eSIM profile management** — the modern dominant form: downloadable profiles on embedded chips, ordered and provisioned remotely, installed via activation codes or QR codes, with consumer (zero-touch device-management deployment) and IoT (remote profile switching) standard families.
- **Consumer vs M2M/IoT provisioning regimes** — consumer eSIMs assume an interactive device and user; M2M/IoT regimes assume headless devices and remote, automated profile handling. The credential lifecycle is the same; the install and switching machinery differs.
- **Fee-coupled vs operationally-coupled lifecycles** — some products bind each state to explicit fee consequences; others treat states as purely operational and leave charging to separate billing machinery.

A variant remains a variant while the credential record, the lifecycle, and the network-access semantics hold. If the population stops being SIM credentials — if the objects become network equipment or customer accounts — the product has crossed into a neighboring type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Telecom Provisioning Platform | adjacent, network-side | activates services in network elements for a subscription; SIM management owns the credential population itself and its states |
| Subscriber Management | adjacent, customer-side | owns the customer/account/service relationship; the SIM is one credential attached to a subscriber, not the subscriber record |
| Telecom Inventory Management | adjacent, asset-side | tracks network equipment and physical assets; SIM management tracks access credentials whose state has live network meaning (physical SIM stock is the shared seam) |
| Telecom Number Management | adjacent, addressing-side | manages number ranges and assignments; a number is an address that can move between SIMs, while the SIM record persists |
| IoT Connectivity Management Platform | overlapping layer | operates the connectivity service (usage, plans, data pipelines, network services) for a device fleet; SIM management is the credential-population layer inside or beside it |
| Card Management System (banking) | analogous, different domain | manages payment smartcards and their lifecycle; the SIM's semantics are mobile-network authentication, not payment |

The most important boundary is with Telecom Provisioning: both "activate" things, but provisioning turns on network services for a subscription, while SIM management moves the credential itself through its lifecycle. An operator runs both; they are different systems with different objects of record.

## Representative Products

- **emnify** — enterprise IoT connectivity platform; SIM Inventory portal with SIM states (Issued / Activated / Suspended / Factory Test / Deleted), BIC-based registration, eSIM product family including bootstrap profiles
- **Soracom (Air for Cellular)** — developer-oriented IoT connectivity platform; SIM Management console with a full subscriber-status lifecycle (Ready / Testing / Active / Inactive / Standby / Suspended / Terminated), status history, and a documented eSIM profile order-and-install flow
- **G+D (Giesecke+Devrient), AirOn360 SDM** — operator-side SIM and device management: full lifecycle from issuance to deactivation, OTA personalization and updates, batch campaigns, plus an eSIM remote-provisioning platform family

The core model was checked across these poles — two enterprise/IoT platforms with different philosophies and one carrier-grade operator-side platform — and against the paper-era operator practice of stock ledgers, personalization records, and assignment logs, which satisfies the same structure with no modern machinery.

## Sources

Research date: **2026-09-09**

- emnify Documentation — SIM Inventory: https://docs.emnify.com/portal/sim-inventory
- emnify Documentation — SIM lifecycle management: https://docs.emnify.com/services/sim-lifecycle-management
- emnify Documentation — Register SIMs: https://docs.emnify.com/quickstart/register-sims
- emnify Documentation — eSIMs: https://docs.emnify.com/services/esims
- emnify Documentation — Consumer eSIM: https://docs.emnify.com/services/consumer-esim
- Soracom Developers Documentation — SIM Management: https://developers.soracom.io/en/docs/air/sim-management/
- Soracom Developers Documentation — Subscriber Status: https://developers.soracom.io/en/docs/air/subscriber-status/
- Soracom Developers Documentation — eSIM Profiles: https://developers.soracom.io/en/docs/air/esim-profiles/
- G+D — SIM & IoT Device Management (AirOn360 SDM): https://www.gi-de.com/en/digital-security/connectivity-iot/sim-device-management
- G+D — eSIM management & eUICC: https://www.gi-de.com/en/digital-security/connectivity-iot/esim-management

> Sourcing limitation: operator-BSS-side SIM management products (Cellusys, Comarch, Mobileum) could not be reached from the research environment (JS-rendered or blocked pages). The operator-side pole is evidenced through G+D's operator-facing product documentation, which is marketing-adjacent; claims about operator-side workflows are therefore stated at moderate strength. Precise operational details (exact fee schedules, numeric thresholds, plan vocabularies, per-product state-name tables) are intentionally not asserted in this document; they are recorded in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical market-sample check are recorded in the paired Research Notes.
