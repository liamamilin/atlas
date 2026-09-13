# EV Charging Network Management

## Overview

An **EV Charging Network Management** system is the operator-side system of record for running a fleet of EV charge points: it holds the operator's charging stations as individually identified managed assets, is the chargers' live operational counterpart (receiving their status and events, issuing commands back to them), and runs the continuous operations loop — monitoring, fault alerting, remote diagnosis and fix — that keeps the network serving drivers.

The defining structure is small:

```text
Charger fleet of record (the operator's own charge points + connectors, at locations)
└── Live charger management connection (status/events in · commands out)
    └── Operational loop (health picture → alerts → remote diagnosis and fix)
```

Everything else commonly associated with these products — site and organization hierarchies, utilization analytics, driver and charge-card administration, smart charging and site load management, firmware campaigns, white-label driver apps, roaming data exchange — is widespread in current products but does not define the Type. A 2013-era open-source back office with a registry, heartbeats and remote commands, and a charger vendor's own proprietary tool for its own hardware, both fit the definition without any of the modern layers.

When the center of gravity shifts to making the charging session earn money (tariffs, invoicing, settlement between companies, roaming), the product is drifting toward a different Application Type (EV Charging Billing & Roaming). When it shifts to the vehicles rather than the chargers, it is fleet territory.

## Users & Context

The primary user is the **charge point operator (CPO)** — a company that owns or operates charging stations as its business: public network operators, fuel retailers, utilities, real-estate and mobility companies. Their operations teams work in the system daily; the rhythm is continuous network operations (watch status, resolve faults, onboard chargers), not one-off projects.

Secondary users shape the same system from other angles:

- **Site hosts and facility operations** (workplaces, hotels, retail, municipalities) — operate chargers at their own locations, monitor health and usage, manage who can charge.
- **Charging service providers / e-mobility providers** — when they also operate points or resell a white-label platform, their staff administer stations, drivers, and access under their own brand.
- **Charger manufacturers** — some run the same kind of back office for their own installed hardware.

The system is back-office software: web consoles for operators, plus machine interfaces (APIs), with the driver-facing app as a separate consumer surface at the edge.

## Core Model

### The Defining Core

```text
Charge Point (station) — persistent, individually identified
└── Connectors (the addressable delivery points)
    deployed at Locations
        ↕ live management connection (status/events in · commands out)
Charging Session — observed operational event (who, when, energy delivered)
        ↕
Operational loop: health picture → alerts → remote fix → maintenance follow-up
```

Three structures. If any one is removed, the product is no longer recognizable as this Type:

- **The charger fleet of record.** Every charge point the operator runs — and its individual connectors — is a persistent, identified record bound to a location. Without this, the product is a driver-facing directory of chargers someone else operates.
- **The live charger management connection.** The system is the operational communication counterpart of the chargers (in industry terms, the "central system" the charge points talk to). It continuously receives what the chargers report — connectivity heartbeats, connector and charger status, fault events, session starts and stops — and it can issue operational commands back: restart or activate/deactivate a charger, unlock a connector, start or stop a session, change configuration, update firmware. Without this two-way relationship, the product is a static asset registry or a spreadsheet of installed hardware.
- **The operational loop.** The connection's data is turned into a live serving picture — which chargers are online, which connectors are available, occupied, unavailable or faulted, which sessions are running — and the operator acts on it: alerts on failures and remote diagnosis and fix (logs and diagnostics, restart, unlock, reconfigure, update firmware). Without this loop, the product is a connectivity pipe, not network management.

### Charging sessions here vs. elsewhere

In this Type, a charging session is an **operational event**: it was authorized, it started, energy was delivered, it stopped, and the charger reported it. Sessions feed occupancy views, uptime and utilization analysis. What sessions never carry in this Type is commercial life — pricing them, invoicing them, and settling money between driver, provider, operator and site host is the job of EV Charging Billing & Roaming, even when one product ships both halves as separate modules.

### Capabilities Shared by Mature Products

A typical modern product carries most of these. They make the Type practical; they are not what makes it this Type:

- **Location and site management** — addresses, geodata, access conditions, public/private classification; site groups for consistent configuration.
- **Organization hierarchy** — the operator's own structure (sub-organizations, brands, cost centers) so large and multi-brand networks can be governed in one system.
- **Session records and performance analytics** — who charged, when, how much energy; utilization, uptime, and usage patterns that inform where to expand.
- **Maintenance follow-through** — when a fault cannot be fixed remotely, the loop hands off to field maintenance: in mature products alarms become tracked tickets, often synced into external service-management or ERP systems.
- **Driver and credential administration** — driver accounts and groups, RFID / charge-card tokens, access rules (private vs public). The authorization check itself rides the charger connection; its commercial consequences belong to the billing Type.
- **Smart charging / load management** — site-level power limits, load balancing across connectors, peak shaving, schedules, session prioritization and rotation when power is short.
- **Firmware and configuration management** — remote configuration, update campaigns, bulk operations across station groups.
- **Event and security logs** — charger alarms, status events, security events, retained for diagnosis and audit.
- **APIs** — station control and data export for integration with billing, CRM/ERP, and service-management systems; partner data exchange (publishing station data to roaming partners) at the edge.
- **Driver-facing surfaces** — a white-label app or web portal (find station, start/stop charge) operated at the consumer edge of the same platform.

### One Structure, Many Implementations

The core is conceptual; products realize it differently:

```text
Concept:      Charger management connection
Realizations: the open OCPP protocol family (station ↔ central system),
              charger vendors' proprietary protocols for their own hardware

Concept:      Connector serving state
Realizations: a per-connector status model (in service / in use /
              unavailable / faulted — exact vocabulary varies by product)

Concept:      Remote fix
Realizations: a generic OCPP command console,
              curated one-click actions in an operator portal,
              automated self-healing rules
```

A reader who has only seen one implementation (a cloud platform with branded dashboards) should still be able to recognize a minimal on-premise back office, or a vendor-locked tool, as the same Type.

## How It Works

### Commission a charger

```text
Register the charge point in the fleet of record (its identity, its location)
→ configure the charger to talk to the management system
→ first contact: the charger reports in (heartbeat, its connectors, its capabilities)
→ configure its behavior (access rules, power settings, what it displays)
→ the station goes live in the operator's network picture
```

### The daily operations loop

This is the heart of the Type:

```text
Watch the network picture (map / status board: online, occupied, faulted)
→ an alarm or anomaly appears (charger offline, connector fault, failed session)
→ diagnose remotely (logs, diagnostics, last events)
→ fix remotely where possible: restart or re-activate the charger,
  unlock a stuck connector, restart a session, reconfigure
→ verify recovery — the connector returns to serving state
→ if hardware must be touched: raise a maintenance ticket,
  hand it to field service / an external system, track to closure
```

Mature products automate part of this loop — detecting known failure patterns and applying standard fixes automatically — so that operator attention concentrates on what automation cannot resolve.

### A charging session, operationally

```text
Driver authorizes at the charger (app, card, token)
→ charger reports the session start; connector becomes occupied
→ energy is delivered and metered
→ charger reports the session stop; connector returns to available
→ the session is retained in the network's operational history
```

The operator's stake in this loop is availability and correctness — did the session start and stop cleanly, did the charger report honestly. What the session costs and who pays is out of scope here.

### Smart charging at a site

```text
Define the site's power budget and rules (cap, schedules, priorities)
→ the system allocates available power across active connectors
→ when power is short: lower charging rates, hold or rotate sessions
→ the site never exceeds its connection capacity; charging continues within it
```

### Keep the fleet current

```text
Group stations → push configuration or firmware updates as a campaign
→ track which chargers took the update, retry failures
→ the network stays consistent without on-site visits
```

### Defining vs common vs optional

**Defining core** — charger fleet of record; live charger management connection (status in, commands out); the operational loop from monitoring to remote diagnosis and fix.

**Standard in mature products** — locations and organization hierarchy; session history and utilization analytics; maintenance follow-through (tickets, field escalation); driver/credential administration; smart charging and site load management; firmware/configuration campaigns; event logs; APIs; driver-facing app; partner data exchange.

**Optional / variant** — deep maintenance workflow integration (service-desk/ERP lifecycles, staffed helpdesk); reservations; energy-services extensions (VPP/DR, battery orchestration, V2G); depot/fleet-flavored power strategies; payment terminals at chargers; tariff display on stations; AI-driven self-healing.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Network status board / map

The operator's primary entry surface.

- the whole fleet at a glance: stations and connectors with live serving states, on a map or in filterable lists
- typical information: station name/location, connector states, connectivity, active sessions
- primary actions: search and filter, open a station, acknowledge alerts

### Station / charger detail

The working surface for one managed asset.

- connector states, current or last session, event and error history, configuration, firmware version
- primary actions: restart / activate / deactivate, unlock connector, start or stop a session, change configuration, push firmware, retrieve diagnostics

### Alerts and tickets

The fault-handling surface.

- open alarms with severity, affected station/connector, timestamps; tickets auto-created from alarms with issue type and status
- primary actions: triage, diagnose, execute remote fixes, escalate to field maintenance, track to closure, sync to external service systems

### Site and organization administration

- locations with their stations, access rules (public/private), organization hierarchy and sub-organizations
- primary actions: onboard a charger, assign to site and organization, set access, configure groups and bulk settings

### Driver and token administration

- driver accounts and groups, charge cards/RFID tokens, access rights
- primary actions: register or block credentials, set access rules per group or station

### Analytics / reports

- utilization, uptime, energy delivered, session patterns, per site or per client
- primary actions: inspect trends, generate and export reports

### Driver app / web portal (edge surface)

- the consumer face of the network: find stations, charge, see history — operated under the network's brand but distinct from the operator console

### API

- station control, session and status data, credential management, and data export — the integration spine toward billing, CRM/ERP, and service-management systems

## Important Rules / Behaviors

### Status is reported, not commanded

The system does not decide that a charger is online or faulted — the charger reports it. The operator's picture is only as truthful as the chargers' reporting, which is why connectivity itself (heartbeats, last-seen) is a monitored property: a charger that stops reporting is treated as a fault even if it may still be delivering power.

### A connector's state drives everything

Availability shown to drivers, whether a session can start, and alert logic all hang off the per-connector state model. Marking a connector unavailable is an operator action that takes it out of service without touching hardware.

### Remote fixes fail offline

Every operational command depends on the live connection. A charger that is offline cannot be restarted, unlocked, or reconfigured remotely — which is precisely why those cases flow to maintenance tickets and field service instead. The boundary between "fix remotely" and "dispatch a technician" is a structural line in this Type.

### Access control lives at the charger

Who may charge is enforced at the charge point against credentials the system administers (cards, tokens, app identities). The same machinery can also gate what a session costs — but the entitlement-to-billing logic belongs to the commercial Type.

### Smart charging constrains without breaking sessions

Power allocation can lower charging rates, hold, or rotate sessions when a site's capacity is short — the session continues, bounded by the site's electrical reality rather than by user intent.

### Alarms become managed work

In mature products a fault is not just a notification: alarms convert into tracked maintenance work — tickets with issue and status, handed to field service or synced into external service-management or ERP systems, and tracked to closure. The network management system is where the operational record of "what broke and what was done" accumulates.

## Variants

- **Public-network CPO platform** — multi-country, multi-brand, large fleets of stations; organization hierarchies, roaming data exchange, and expansion analytics matter most.
- **Workplace / destination host operations** — smaller fleets at owned locations; access management for employees and guests, simple monitoring, integration with facility operations.
- **Charger-vendor back office** — the manufacturer's own system for its own hardware; same operational core, hardware-locked perimeter.
- **White-label platform operation** — the operator runs the system for many brands as sub-organizations, each with its own stations, drivers and surfaces.
- **Managed-operations flavor** — the platform is sold together with a staffed helpdesk that performs the operations loop on the customer's behalf.
- **Depot / fleet-flavored deployment** — chargers operated for a fleet's needs (priority charging, depot power strategies); overlaps with EV Fleet Charging Management, from which side the vehicles remain the subject.
- **Energy-services-extended** — the same network doubles as a flexible energy asset (VPP/DR participation, battery and solar orchestration, V2G); a growing but optional layer.

A variant remains a **Variant** unless it changes the core subject — chargers operated as infrastructure — into something else (vehicles, money, grid assets).

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| EV Charging Billing & Roaming | sibling / complement | this Type operates the chargers (connect, monitor, fix, configure, smart-charge); that Type operates the money (tariffs on sessions, invoicing, multi-party settlement, roaming). Products bundle both as separately named modules; SteVe-like minimal back offices prove this layer stands alone |
| EV Fleet Charging Management | adjacent (different subject) | manages the charging of an operator's vehicles (depot strategies, vehicle-charger assignment, fleet costs); here the chargers, not the vehicles, are the system of record |
| Energy Management System / DERMS / Virtual Power Plant | adjacent | grid-scale and site energy orchestration across assets; here load management exists only to serve charger operations at sites |
| Utility Field Service Management / CMMS | downstream handoff | charger faults escalate into maintenance work orders; the service organization's system of record remains the other Type |
| Industrial IoT Platform | structural analogy | same connected-device shape (telemetry in, commands out), but without EVSE-specific semantics (connector states, sessions, charge-point commissioning, charger-aware commands) |
| Driver-facing charger directory / finder | opposite side | aggregates chargers the app's operator does not control; here the managed chargers are the operator's own assets and can be changed by the system |
| Parking Management Platform | co-located asset | chargers often stand in managed parking assets; parking's core is the parking space and its occupancy, not the charging equipment's serving state |

The most important boundary is with **EV Charging Billing & Roaming**: the market sells one product family ("EV charging management platform") containing both halves as separately named modules. The split test is consistent — remove tariffing, invoicing and settlement and what remains is charger operations; remove charger operations entirely (as pure roaming hubs do) and the commercial Type stands on its own.

## Representative Products

- **Virta** (Virta Hub) — full-service European CPMS: station management, driver management, load management, white-label operation for CPOs and site hosts
- **Driivz** — enterprise platform whose suite ships "Operations Management" and "EV Charging Billing" as separately named modules; large multi-country CPO networks
- **Last Mile Solutions** — white-label full-stack platform splitting "Station management" (this Type) from "Billing as a Service" (the sibling)
- **SteVe** — open-source OCPP back office (since 2013); included as the minimal-shape check: charge points, live status, transactions, remote commands — no commercial layer

The definition was checked against the minimal open-source sample and vendor-proprietary network shapes (not only modern cloud suites) to avoid defining the Type by the current dominant packaging.

## Sources

Research date: **2026-09-08**

Primary vendor surfaces (official pages and FAQs, fetched live):

- Virta — homepage: https://www.virta.global/ ; Virta Hub CPMS: https://www.virta.global/charging-solution/virta-hub-cpms
- Driivz — homepage: https://driivz.com/ ; Operations Management: https://driivz.com/platform/operations-management/
- Last Mile Solutions — homepage: https://www.lastmilesolutions.com/ ; Station management: https://www.lastmilesolutions.com/station-management/
- SteVe — GitHub README: https://github.com/steve-community/steve
- Open Charge Alliance — Protocols: https://openchargealliance.org/protocols/ ; OCPP: https://openchargealliance.org/protocols/open-charge-point-protocol/

> Sourcing limitation: vendor help centers / user guides and the OCPP specification text itself were not reachable from the research environment on this date; observations rest on product pages, FAQs, and the SteVe README. Assertions are calibrated to that level: no numeric limits, exact state-name enumerations, or default timings are stated. Three candidate products (ChargeLab, AMPECO, ChargePoint) were dropped after repeated fetch failures, so North-American market breadth is under-sampled.

Detailed product-by-product observations, the cross-product comparison matrix, and the historical / market-sample breadth check are recorded in the paired Research Notes.
