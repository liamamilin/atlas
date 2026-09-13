# Outage Management System / OMS

## Overview

An **Outage Management System (OMS)** is the utility's outage-response system of record. It turns signals that customers have lost power — telephone calls, meter pings, device alarms — into predicted outage events placed on the network model, groups related signals into single events, dispatches and tracks field crews through restoration, keeps estimated restoration times in front of both operators and customers, and closes each event as a cause-coded record that feeds the utility's reliability reporting.

The defining structure is small:

```text
Network connectivity model (who is served through which devices)
└── Incoming outage signals → predicted outage event (the unit of record)
    └── Crew dispatch & restoration loop
        └── Completed, cause-coded event → reliability record
```

Everything else commonly associated with modern outage management — smart-meter integration, public outage maps, text notifications, storm consoles, mobile crew apps, reliability indices — is widespread standard capability, not part of the definition. In particular, an OMS does not have to operate the network in real time: monitoring live voltages and remotely controlling field devices is the territory of the real-time control platform (the ADMS/SCADA estate). A standalone OMS predicts, dispatches, and records while the network itself is operated elsewhere — or by no software at all.

## Users & Context

The primary users are the people who run outage response, in shifts, around the clock:

- **trouble-call takers / customer service representatives** — answer customer calls, find the caller's account, record what the caller reports, and let the system attach the call to the right outage
- **outage coordinators / dispatchers** — watch the event list, confirm and group events, assign and track crews, maintain estimated restoration times
- **distribution system operators** — in utilities where the OMS shares a control room with the real-time platform, the same operators who watch the network also work the outage events

Secondary users:

- **field crews** — receive outage tickets on mobile devices, report progress and restoration from the field, sometimes offline
- **customer-facing staff and the public** — read the outage map or portal, report outages, check status
- **reliability / operations engineers** — consume the completed-event record for reliability statistics and regulatory reporting; maintain the model the predictions depend on
- **management and support staff** — follow large events through view-only storm consoles and summary reports

The work context swings between everyday faults (a handful of calls, one crew) and major storms (call surges, mutual-assistance crews from other utilities, executives watching view-only screens). The same system serves both; storm conditions typically change how restoration times are calculated and who can see what.

## Core Model

### The Defining Core

Three structures, held together. Remove any one and the product stops being an outage management system:

**1. The outage event as the unit of record.** A persistent, individually identified record of one outage condition on the network. It is opened when signals arrive, carries the affected customers, the predicted (and later confirmed) outage device, its lifecycle state, timestamps, and an estimated restoration time, and it is closed only when restoration is complete and a cause has been recorded. The event is the hub: calls, meter signals, crews, damage assessments, and switching actions all attach to it.

**2. Signal-to-event prediction and grouping on the network connectivity model.** The system holds the network as a connectivity model — which customers are served through which transformers, fuses, and feeders. Incoming signals are matched against this model: a call from a known service point predicts the upstream device that likely failed; several calls from the same stretch of feeder are grouped into one event; a meter ping or a breaker-lockout alarm can confirm or refine the prediction. Moving a call to a different device re-runs the prediction and may regroup events. This model-based prediction is the OMS's distinctive intelligence — it is what turns a pile of phone calls into a located, sized, workable outage.

**3. The crew dispatch and restoration loop.** Crews are assigned to events and tracked through states — assigned, dispatched, en route, on site, released (labels vary by product). Restoration is recorded in stages, and each stage updates the affected-customer count; partial restorations are first-class (part of a feeder back on while the faulted section is still being repaired). Completion requires structured cause codes — what failed, where, why — which is what makes the event record usable for reliability statistics afterward.

```text
Customer loses power
→ signal arrives (call / meter ping / device alarm)
→ matched against the connectivity model → predicted outage device
→ related signals grouped into ONE outage event
→ event confirmed; estimated restoration time set
→ crew assigned → dispatched → on site
→ restoration in stages; affected-customer counts update
→ event completed with cause codes → reliability record
```

### Standard Capabilities

Mature products commonly add the layers below. They make the system practical and are near-universal in current products, but they are modules and integrations, not the definition — vendors ship several of them as separately licensed or optional components.

- **Estimated restoration time as a maintained field** — operators update it as conditions change; large events carry a system-wide estimate; the value is published outward to customers.
- **Customer communication** — outbound notifications by phone, text, email, and social media; some products add callback queues for proactively calling customers back; administrative tools for managing contact lists and alert templates.
- **Public outage map / customer portal** — a map of active outages with restoration estimates, where customers can report an outage and check their own status.
- **Smart-meter (AMI) integration** — meter pings, last-gasp-style loss-of-power signals, and voltage readings that confirm or shrink outage extents; some products let authorized call-takers ping a meter during a call.
- **SCADA / device-alarm integration** — breaker lockouts and protective-device operations arrive as prediction inputs; where restoration automation exists in the wider estate, its events are captured in the OMS as records.
- **Fault-location analysis** — probable fault points computed from the fault current measured at the protective device, narrowing the patrol.
- **Damage assessment** — structured assessment records with statuses (new, assessing, assessed, fixed), including partial-information assessments during storms.
- **Critical-customer tracking** — in some products, flags for hospitals, emergency services, and life-support customers that raise an event's priority.
- **Reliability reporting** — customer-minutes interrupted accumulated per restoration stage; indices in the SAIDI/SAIFI family; completed events can be excluded from the indices only with a recorded reason.
- **Storm mode** — a behavior switch for mass-outage conditions: different restoration-time calculations, view-only environments for management, storm reports.
- **Mobile field apps** — outage tickets, assessments, and the live model on crew devices, commonly usable with poor or no connectivity.
- **Switching representation on the model** — the dispatcher can represent what crews are doing to the network: open and close equipment, create open points, install jumpers — so the model reflects restoration state, not just the as-built plan.

### One Structure, Many Implementations

```text
Concept:            Incoming outage signals
Implementations:    call-taker entry, IVR auto-attendance, customer portal reports,
                    smart-meter pings, device/SCADA alarms

Concept:            The connectivity model
Implementations:    imported from the utility GIS, maintained in a shared circuit model,
                    vendor network-model management tools

Concept:            Crew coordination
Implementations:    dispatcher boards, mobile crew apps (online or offline), radio-era practice

Concept:            Customer communication
Implementations:    IVR outbound calls, SMS/email/social publishing, public web outage maps,
                    call-center callback queues
```

A reader who has only seen a modern cloud deployment with meter pings and a public map should still be able to recognize the older shape — a call taker, a wall map of the feeder system, a dispatcher with a radio, and a paper outage ticket — as the same system of record.

## How It Works

### The trouble loop

The daily defining workflow:

```text
Customer calls (or a meter reports loss of power, or a device alarms)
→ call taker finds the customer's account and records the call
→ the system predicts the outaged device from the connectivity model
→ the call joins an existing event or a new event is created
→ dispatcher confirms the event; sets/updates the estimated restoration time
→ crew assigned and dispatched; status tracked (en route → on site)
→ fault located (patrol, fault-current analysis); repairs made
→ restoration recorded in stages; affected-customer counts fall
→ event completed with cause codes; reliability record updated
```

Two behaviors make this loop more than a work-order queue. First, **events are predicted, not just entered**: the system proposes the failed device, and correcting a call's device re-runs the prediction and can regroup events. Second, **restoration is staged**: a single event can be partially restored several times, and each stage's customer-minutes accumulate for the reliability record.

### Storm operations

Under mass outages the same loop scales: surging calls are absorbed by grouping rules and automated attendance, restoration-time calculations switch to storm behavior, damage assessments and callback queues scale up, and view-only consoles extend visibility to management and support staff. Mutual assistance — crews borrowed from neighboring utilities — is coordinated either inside the OMS's storm tooling or in a separate cross-utility coordination product that hands crew rosters to each utility's own system.

### Where the OMS sits relative to real-time operations

When the OMS is deployed alongside a real-time control platform, the division of labor is stable: the control platform watches the network and operates devices; the OMS owns the outage record, the crews, and the customer conversation. Automation on the control side (for example, automatic fault isolation and restoration) produces events that flow into the OMS as records to be worked and completed. In a standalone deployment, the OMS receives device alarms and meter data as inputs and represents switching and restoration on its model, but the switching itself is executed in the field.

### Capability tiers

**Defining core** — without these, not an OMS:

- the outage event as a persistent, completable record
- signal-to-event prediction and grouping on the connectivity model
- crew dispatch and staged restoration tracking

**Standard capabilities** — present in most mature products:

- maintained restoration estimates, customer notifications, public outage map/portal
- meter and device-alarm integration, fault-location analysis, damage assessment
- critical-customer flags, reliability reporting, storm mode, mobile field apps

**Optional / variant** — depends on scale, region, and packaging:

- mutual-assistance coordination, DER dispatch during outages, water/gas-carrier variants,
  cloud deployment, regional reliability-reporting regimes

## Interfaces

Described in conceptual terms; exact layouts and names vary by product.

### Event list / trouble summary

The work queue of outage response.

- typical information: active events with call counts, customers out, estimated restoration time, assigned crews, storm status
- primary actions: open an event, acknowledge, filter, update estimates in bulk

### Event details

The tabbed record of one outage event.

- typical information: callers and their accounts, customers out (with critical-customer breakdown), predicted device, restoration log by stage, crews and contact times, damage assessments, cause codes, attached switching records
- primary actions: update the restoration estimate, group/ungroup calls, assign crews, record restoration stages, complete the event with cause and remedy

### Call entry screen

The call taker's surface.

- typical information: customer account search results, call history, current outages affecting the account
- primary actions: record a call (including partial-information calls), attach it to an event, cancel a call, create a non-outage ticket

### Crew board

The dispatcher's view of field resources.

- typical information: crews, their makeup, their current state and assignment
- primary actions: assign to an event, advance through states, release

### Network viewer with outage symbols

Where the model becomes visible: the feeder system drawn with outage and call symbols, colored by state.

- typical information: predicted outage devices, affected areas, restoration state
- primary actions: inspect a device, trace upstream/downstream, represent switching actions

### Public outage map / customer portal

The customer-facing surface.

- typical information: active outages, estimated restoration times, safety information
- primary actions: report an outage, check status of one's own service

### Mobile field app

The crew's surface.

- typical information: assigned outage tickets, the network model, assessment forms
- primary actions: accept and work tickets, report restoration, complete assessments — often offline

### Storm console and reports

- typical information: system-wide outage picture, restoration progress, storm reports
- primary actions: set system-wide estimates, override calculations, export reports

## Important Rules / Behaviors

- **Events are predicted, then confirmed.** The system proposes the failed device from the connectivity model; operators confirm or correct. Corrections re-run the prediction and can regroup calls into different events.
- **The restoration estimate is a living field.** It is set at event creation, updated as conditions change, and can be overridden manually; under storm conditions the calculation behavior itself changes.
- **Restoration is staged, and customer-minutes are what accumulate.** Each restoration stage updates affected-customer counts and accumulates interruption duration; the completed event's cause codes and durations are what reliability statistics are computed from.
- **Exclusions from reliability indices require a recorded reason.** Completed events can be kept out of the statistics, but only with an auditable justification — the record is regulatory-grade.
- **Signals converge; one condition, one event.** Calls, meter pings, and device alarms describing the same condition attach to the same event; grouping rules are configurable.
- **The OMS records response; it does not necessarily operate the network.** Remote control of field devices belongs to the real-time control platform where one exists; the OMS represents switching and restoration on its model and tracks what was done.
- **Prediction quality is bounded by model quality.** The connectivity model — who is served through what — must be kept current with the field; a stale model mispredicts, which is why model maintenance is a standing discipline around the system.
- **Everything is attributed and retained.** Call times, crew contact times, restoration stages, and post-completion edits leave audit trails, because the record feeds regulatory reliability reporting.

## Variants

- **Packaging** — a standalone OMS product (common at cooperatives and municipal utilities); an OMS module licensed as part of an integrated real-time platform; an OMS product inside a control-center software suite. The integrated realization dominates the current large-utility market, but the standalone pole is a real, documented market.
- **Utility scale and type** — investor-owned utilities, cooperatives, municipals; the loop is identical, the scale of storm operations differs.
- **Carrier** — electric is canonical; the same outage-response pattern is sold for water systems, where "outage" means loss of supply rather than loss of power. The electric specifics (phases, feeders, protective devices) are content inside the objects, not the structure.
- **Storm and mutual-aid machinery** — built into the OMS's storm mode, or shipped as a separate cross-utility crew-coordination product that works regardless of which OMS a utility runs.
- **Automation depth** — from fully manual response to environments where restoration automation on the control side feeds events into the OMS automatically.
- **Deployment** — on-premises control-room heritage versus web and cloud delivery; customer-facing portals are web-native in current products.
- **Regional regimes** — reliability-index definitions, regulatory reporting obligations, and safety-document conventions vary by jurisdiction; products adapt through configuration.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Advanced Distribution Management System / ADMS | sibling; the most important boundary | The ADMS operates the network in real time: live telemetry on a connected electrical model, supervisory control of devices, network applications. The OMS owns the outage-response loop. Strip real-time monitoring/control from an ADMS and an OMS-centric system remains; strip the outage loop and the ADMS remains. In integrated products the OMS is a layer of the ADMS on one model. |
| SCADA | substrate / input | Telemetry acquisition and remote control organized as points and devices; its alarms are prediction inputs to the OMS. SCADA holds no outage events, crews, or restoration records. |
| Grid Operations Platform | family umbrella | The market's umbrella name for the control-room estate; the OMS is its outage-layer member. The family map lives in that document. |
| DERMS | sibling layer | Coordinates distributed energy resources as a fleet; during outages it may act as an execution arm, but the outage event, crews, and restoration record live in the OMS. |
| Utility GIS | model source | Holds the as-built geographic asset records from which the OMS's connectivity model is typically derived or kept current; no operational loop. |
| Utility Customer Information System / CIS | data source | Holds the customer identity, phone, and service-point data the OMS matches callers against. Call logging without network-model prediction is trouble-call logging, not outage management. |
| Advanced Metering Infrastructure / AMI · Meter Data Management | signal source | Collects meter data; pings and loss-of-power signals refine and confirm outages. Neither manages the response. |
| Utility Field Service Management | shares dispatch machinery | Centers on scheduled service work orders against appointments; the OMS centers on unplanned outage events predicted on the network model. |
| Emergency Management Platform | adjacent | Coordinates all-hazards response; the OMS centers the outage restoration loop on the network model. Storm/mutual-aid coordination overlaps and is sometimes a separate product. |
| Incident Management (IT) | name collision only | IT incident response over software services; unrelated domain and objects. |
| Order Management System / OMS (commerce) | name collision only | Merchant order lifecycle management; shares the acronym, nothing else. |

## Representative Products

- **Oracle Utilities Network Management System (NMS)** — integrated platform whose outage-management layer (trouble management, crews, call entry, callbacks, storm management, service alerts) is documented in a public user guide; large-utility pole
- **Milsoft OMS** — standalone outage management for cooperatives and municipal utilities, predicting on a shared circuit model with mobile field and storm/mutual-aid companion products; the standalone pole
- **SurvalentONE OMS** — a separately documented OMS product composing a modular real-time platform, with dedicated call-handler, customer-portal, dashboard, damage-assessment, and mobile-crew components; mid-market modular pole
- **AspenTech OSI Outage Management System** — an OMS product inside a control-center software suite, with a companion mobile field app; suite-embedded pole

The defining core was checked against the standalone, non-real-time pole and against the paper-era outage-response practice (call takers, circuit maps, radio dispatch, paper tickets) to avoid defining the Type by the current integrated implementation.

## Sources

Research date: **2026-09-09**

- Oracle Utilities Network Management System documentation library (Release 25.12), including the Network Management System User Guide table of contents and the separate OMS for Water user guide — https://docs.oracle.com/en/industries/energy-water/network-management-system/index.html
- Milsoft Utility Solutions — Outage Management, FieldSyte, and StormSyte product pages — https://www.milsoft.com/engineering-operations/outage-management/
- Survalent — SurvalentONE OMS and SurvalentONE Call Handler product pages — https://www.survalent.com/products/outage-management-system-oms/
- AspenTech — Digital Grid Management suite page (OMS named within the suite) — https://www.aspentech.com/en/products/suites/digital-grid-management

> Sourcing limitations: individual Oracle user-guide topic pages timed out from the research environment; the OMS layer's page-level detail rests on the fetched table of contents plus page-level observations carried from the paired ADMS research (fetched 2026-09-06 from the same documentation library). AspenTech's OMS is evidenced at suite and product-naming level only. No pricing, numeric limits, default values, or algorithm details are asserted anywhere in this document.

Detailed evidence, product-by-product observations, the cross-product comparison, and the boundary analysis (including the resolution of the joint-review flag with the ADMS research) are recorded in the paired Research Notes.
