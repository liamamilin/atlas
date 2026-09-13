# Research Notes — EV Charging Network Management

Research date: 2026-09-08
Slug: ev-charging-network-management
Directory leaf: EV Charging Network Management (§19 Energy, Utilities & Telecommunications)

## Research Goal

Understand what an "EV charging network management" application actually is as an operator-side software type: what objects it manages, how it connects to charging hardware, what its daily operational loop looks like, and where it ends relative to the commercial layer (session billing/roaming) and adjacent types (fleet charging, energy management, IoT platforms).

Pre-hung joint-review obligation: the sibling pass `ev-charging-billing-roaming` (processed 2026-09-08, see STATUS.md Boundary Issues) recommends that this pass define its core as **charger-fleet operations WITHOUT session commercialization**, holding session revenue/billing/roaming as the sibling leaf's object even inside bundled products. This note holds that seam symmetrically.

## Initial Boundary

Working hypothesis at start:

- What: the operator-facing system for running a network of EV charge points (charging stations / EVSE) — connecting chargers, monitoring live status, handling faults remotely, managing locations and access, smart charging / load management, maintenance follow-up.
- Who: charge point operators (CPOs); also site hosts' operations teams (workplace, hospitality, retail, municipal), charger manufacturers' back offices, and white-label platform operators.
- Nearest neighbors: EV Charging Billing & Roaming (commercial layer over the same sessions), EV Fleet Charging Management (§18; vehicle-side), Energy Management System / DERMS / VPP (grid/energy side), Utility Field Service / CMMS (maintenance), Industrial IoT Platform (generic connected-device shape), driver-facing charger directory apps (consumer side).
- Main confusion risk: the market sells one product family ("EV charging management platform", CPMS) that bundles this Type and the billing/roaming Type as separately named modules.

## Research Questions

1. What are the core objects? (charge point / station / EVSE, connector, location/site, session, alert, ticket, token/driver, charging profile)
2. What is the charger-connection model? (central-system ↔ charge point relationship; protocol role — OCPP vs proprietary)
3. What is the daily operations loop? (monitor → alert → diagnose → remote fix → escalate to field maintenance?)
4. What role does the charging session play here (operational event) vs in billing (commercial CDR)?
5. What does smart charging / load management mean at site level?
6. What interfaces exist (dashboard, map, charger detail, alerts/tickets, config, driver app, API)?
7. Which states and rules matter (charger online/offline, connector states, session lifecycle, firmware updates, power limits)?
8. Where does this Type stop and billing/roaming begin (symmetric seam)?
9. How do variants differ (public CPO vs workplace/depot vs charger-vendor back office vs white-label multi-brand)?
10. Does the definition survive thin/historical samples (pre-cloud OCPP back offices, vendor-proprietary networks)?

## Representative Products

Selected for market representativeness + documentation completeness + different product philosophies + different customer tiers:

| Product | Pole | Customer tier | Fetched |
|---|---|---|---|
| Virta (Virta Hub CPMS) | full-service CPMS + energy services, EU | CPOs / eMSPs / site hosts (workplace, airports, hotels) | Yes (root + Hub CPMS page) |
| Driivz | enterprise platform suite with named Operations Management module | largest global CPOs, fuel retail, utilities, automakers | Yes (root + Operations Management page) |
| Last Mile Solutions | white-label full-stack platform (NL/EU) | CPOs, MSPs, installers, fleets | Yes (root + Station management page) |
| SteVe (open source) | minimal OCPP back office since 2013 — thin-ancestor check | small CPOs, manufacturers, developers | Yes (GitHub README) |
| Open Charge Alliance (OCA) | protocol body — grounding for the charger↔central-system relationship | standards context | Yes (protocols pages) |

Dropped after repeated fetch failures (network-restriction rule): ChargeLab (chargelab.com ×2, docs.chargelab.co 400), AMPECO (ampeco.io transport error ×2 incl. billing pass), SWARCO (404), ChargePoint (timeout). North-American market breadth is therefore under-sampled; assertions calibrated accordingly.

## Sources

- Virta — homepage: https://www.virta.global/ ; Virta Hub CPMS: https://www.virta.global/charging-solution/virta-hub-cpms
- Driivz — homepage: https://driivz.com/ ; Operations Management: https://driivz.com/platform/operations-management/
- Last Mile Solutions — homepage: https://www.lastmilesolutions.com/ ; Station management: https://www.lastmilesolutions.com/station-management/
- SteVe — GitHub README: https://github.com/steve-community/steve
- Open Charge Alliance — Protocols: https://openchargealliance.org/protocols/ ; OCPP page: https://openchargealliance.org/protocols/open-charge-point-protocol/
- Sibling research: research/ev-charging-billing-roaming.md (seam symmetry)

Not reachable on this date: vendor help centers / user guides (Virta support KB, LMS developer documentation, Driivz help), OCPP specification text itself (only OCA summary pages). See Sourcing Limitation at the end.

## Product Observations

### Virta (Virta Hub CPMS)

Evidence layer: A (direct, official pages).

- Self-definition: "Take care of your whole charging network with our Charge Point Management System (CPMS)"; "monitor your charging stations, view everything there is to know about your EV drivers, and set your charging prices — all with just a few clicks and in one system."
- Named module areas: Charging station management; Insights & reports; AI & automation; EV driver management; Tariff management; Energy management.
- Charging station management: "Remote monitoring — monitor all your charge points in real time to keep an eye on your whole network's health and performance"; "Access management — manage access to your charge points. Choose between private and public charging"; "Unlimited organisational hierarchy — create and manage sub-organisations for better oversight and reporting."
- Hardware posture: "supports over 2,000 charger models", pre-configured or connect your own; customer quote: migration of existing chargers without replacing them; quote: "grant access to, unlock specific EV chargers and update them at any time."
- Insights & reports: network performance, utilisation, session behaviour ("session duration, energy per session, start times and authentication methods"), business-ready reports.
- AI & automation: "Automatically detect and resolve selected charger issues to keep charging stations available"; uptime framing.
- Energy management (site-level): Dynamic Load Management ("define the maximum power delivered to all of your chargers"), Adaptive Load Management (site's overall electrical usage), Congestion Management, capacity allocation, session priority, and rotation ("putting some charging sessions on hold when not enough charging power is available").
- Organizational shape: sub-organisations; driver groups; home/workplace/public/fleet charging use cases under one platform.

### Driivz (Operations Management module)

Evidence layer: A (direct, official pages).

- Family structure: platform modules named "Operations Management", "EV Charging Billing", "Energy Management System", "Mobile App and Web Portal", "Reporting and Analytics" — operations and billing are separate named modules of one suite (confirms sibling joint-review note).
- Operations Management page: "Optimize all operational aspects of your EV charging business to maintain stability and availability of your network. Efficiently manage chargers, drivers, hosts, sites, fuel cards, RFID tokens, roaming partners, and more."
- Network health: "Monitor your network 24/7 using intuitive visual dashboards, comprehensive alert management and detailed logs." Named "Alert Management System (AMS)": 24/7 proactive monitoring, logs a wide variety of events, auto-detection and self-healing algorithms; "Issues that are not managed automatically generate an alert and most of those can be fixed remotely from Driivz's Operator Portal."
- Remote actions (explicit list): "activate/de-activate a charger, start/stop a charging session, update firmware, and more"; FAQ adds "activating a charger, and enabling a charging session … all without having to send out a field technician."
- Operational value framing: availability ↑ utilization ↑ revenue; fewer field-technician dispatches ↓ TCO.
- Platform hierarchy: operator → sites → chargers (diagram named "Driivz platform hierarchy"); scalable across "chargers, charger models, drivers, charging events, roaming partners, billing transactions, payment gateways, sites, properties, RFID tokens, users and operators."
- Connectivity: OCA-certified for OCPP 1.6 and 2.0.1 ("used as a golden node by the OCA to certify other OCPP implementations"); "Connect with any OCPP-compliant charger — 2,200 supported charger models"; customization for not-fully-compliant chargers; standards list: OCPP 2.0.1, ISO 15118, AutoCharge, Plug&Charge, V2G, OpenADR.
- Roaming interfaces listed as integrations: OCPI, OCHP, OICP, eMIP (inter-network data exchange sits at the seam with the sibling Type).
- APIs: "Driver management (enrolment, update, RFID management)", "Station control", "Initiating external transactions", CDR export for external billing/ERP/CRM integration.
- Vendor-specific (do not generalize): "self-healing algorithms" branding, Driivz AI / Network Optimizer, migration methodology claims ("tens of thousands of chargers … within a matter of a few months"), "up to 6X EV charging on site" capacity claim.

### Last Mile Solutions (Station management)

Evidence layer: A (direct, official pages).

- Family structure: menu splits "Management tools for CPO/MSP" (Station management, Smart energy management, Hardware integration, 24/7 helpdesk as a service) from "Commerce" (Billing as a service, Payment as a service, Branded environments, Roaming) — same bundled-family/sepately-named-module pattern.
- Station management definition: "Configure, monitor, and manage all chargers from one central platform."
- Three surfaces described: Live monitoring ("track charge sessions and station status live; auto-create tickets and sync with ERP system via API"); Station control ("manage protocols, names, and roaming settings; use station groups for consistent configurations"); Remote configuration ("set pricing, access rules, and energy mix; define ownership, cost center, and payout rules").
- FAQ (operational detail): "monitor status in real time, retrieve diagnostics, and remotely perform actions such as restarting chargers, unblocking connectors, or starting and stopping sessions"; "Whenever a charge station triggers an alarm — for example, due to going offline or a connector fault — a maintenance ticket is automatically generated. Each ticket includes key details such as issue type, timestamp, and status. Maintenance actions can be logged, tracked, and integrated into your ERP or service management system via our extensive platform API."
- Bulk management: "either individually or in bulk using charge groups"; technical settings (communication protocols, station names, diagnostic access) vs commercial/administrative parameters (station ownership, cost centers, revenue beneficiaries, subscriptions, pricing, access rules, roaming settings).
- Performance insights: "track charger usage, uptime, and energy delivered. Filter by location or client."
- Scale claim: 364,000 charge points directly connected (marketing number — not used in final doc).
- Adjacent services at edges: 24/7 helpdesk as a service (managed operations flavor); smart energy management incl. VPP case quote (energy-services seam).

### SteVe (open-source thin ancestor)

Evidence layer: A (direct, official README).

- Self-definition: "SteVe - OCPP server implementation in Java … open-source EV charging station management system since 2013"; name from German "Steckdosenverwaltung" (socket administration); "provides basic functions for the administration of charge points, user data, and RFID cards for user authentication."
- Minimal workflow: register a charge point (enter its ChargeBox ID) → charge point is configured to communicate with the CentralSystemService endpoint (SOAP or WebSocket/JSON) → "As soon as a heartbeat is received, you should see the status of the charge point in the SteVe Dashboard."
- Feature surface (screenshot inventory): Connector Status; Data Management — Charge Points / OCPP Tags / Users / Charging Profiles / Reservations / Transactions; Events — Security Events / Status Events / Installed & Signed Certificates; Operations — OCPP v1.2 / v1.5 / v1.6 (remote command console); Settings; APIs. Supports OCPP 1.2S/1.2J/1.5S/1.5J/1.6S/1.6J.
- What it has: charge points, live status, transactions, user/RFID-token auth, charging profiles (smart charging), reservations, event logs, remote OCPP operations.
- What it has NOT: no billing, no tariffs, no invoicing, no settlement, no driver app, no roaming. Transactions are logged as operational records; nothing prices them.
- Interpretation: this is the load-bearing minimal shape of the Type — and it independently confirms the seam with the billing sibling (SteVe stops exactly where session commercialization would begin).

### Open Charge Alliance (protocol grounding)

Evidence layer: A (direct, standards-body pages).

- "OCPP is the global open communication protocol between charging stations and charging management systems." Terminology: Charging Station (CS) ↔ CSMS (Charging Station Management System); industry also says "central system".
- OCPP 1.6 (2015): SOAP and JSON versions; "Smart Charging support for load balancing and use of charge profiles"; "(local) list management support"; "Additional status"; message-sending requests.
- OCPP 2.0.1 (2020): "Device Management — features to get and set configurations and also to monitor a Charging Station"; improved transaction handling; added security; ISO 15118 support; display/messaging. Approved as IEC 63584 in 2024.
- OCPP 2.1 (2025): ISO 15118-20 with bidirectional power transfer; V2X functional block; DER Control block; "Improved Smart Charging"; "Possibility to resume transactions after a forced reboot"; authorization options incl. ad hoc payment and dynamic QR codes.
- Interpretation: the protocol family itself names the Type's signature machinery — station monitoring, configuration get/set, transaction handling, smart-charging profiles, status events, security events, firmware-capable device management. OCPP is the common implementation substrate, not the definition (proprietary-protocol networks exist in the same shape).

## Cross-product Comparison

| Capability | Driivz | Virta | Last Mile Solutions | SteVe (ancestor) |
|---|---|---|---|---|
| Charger fleet of record (stations + connectors, identified, at locations) | ✓ (chargers, sites, properties; platform hierarchy) | ✓ (charging stations across locations; org hierarchy) | ✓ (stations; ownership/cost-center config) | ✓ (Charge Points registry, ChargeBox IDs) |
| Live two-way charger connection (status/events in, commands out) | ✓ (24/7 monitoring, AMS, remote actions) | ✓ (real-time remote monitoring; unlock/update) | ✓ (live monitoring; remote actions) | ✓ (OCPP heartbeat/status + Operations console) |
| Connector/charge-point status model | ✓ (network health dashboards) | ✓ (network health & performance) | ✓ (station status live) | ✓ (Connector Status view) |
| Charging sessions as operational events | ✓ ("charging events", start/stop remote) | ✓ (session behaviour analytics) | ✓ ("track charge sessions … live") | ✓ (Transactions log) |
| Alerts on faults + remote diagnosis | ✓ (AMS, alert management, logs) | ✓ (AI & automation: detect and resolve issues) | ✓ (alarms → tickets; diagnostics retrieval) | partial (status/security events, no ticketing) |
| Remote fix commands (restart, unlock connector, activate/deactivate) | ✓ (activate/deactivate, start/stop session, firmware) | ✓ (unlock, update, grant access) | ✓ (restart, unblock connectors, start/stop sessions) | ✓ (OCPP remote operations per version) |
| Maintenance follow-up (tickets / escalation) | ✓ (reduce field-technician dispatch framing) | implied via uptime automation | ✓ explicit (auto tickets, ERP sync, logging/tracking) | ✗ |
| Locations/sites + organization hierarchy | ✓ (sites, properties, operators) | ✓ (locations, sub-organisations) | ✓ (locations, clients, ownership) | ✗ (flat registry) |
| Smart charging / load management | ✓ (dynamic load balancing, peak shaving, ToU) | ✓ (DLM/ALM, congestion, rotation) | ✓ (smart charging + local grid configuration) | partial (OCPP charging profiles only) |
| Firmware / configuration management | ✓ (firmware update in remote fixes; configs) | ✓ ("update them at any time") | ✓ (protocols, names, bulk via groups) | ✓ (OCPP config/operations) |
| Driver/token administration (RFID, access) | ✓ (drivers, RFID tokens, fuel cards) | ✓ (EV driver management, access mgmt) | ✓ (access rules; charge cards elsewhere) | ✓ (Users, OCPP Tags) |
| Performance analytics (utilization, uptime, energy) | ✓ (reporting module) | ✓ (insights & reports) | ✓ (usage, uptime, energy delivered) | ✗ |
| Driver-facing app/web | ✓ (named module) | ✓ (EV driver services, app) | ✓ (branded environments) | ✗ |
| Station/tariff pricing config | separate billing module | tariff management module | remote config incl. pricing | ✗ |
| Roaming / partner data exchange | ✓ (OCPI/OCHP/OICP/eMIP) | ✓ (roaming capability) | ✓ (roaming settings on station; Roaming as a Service) | ✗ |
| Billing / settlement | ✓ separate named module | ✓ separate capability | ✓ separate named service | ✗ — none |

Reading: the first six rows hold across all four products including the 2013-era open-source ancestor → canonical core candidates. Ticketing, hierarchy, analytics, smart-charging depth, driver surfaces, tariffs, roaming, billing vary → common/optional/adjacent layers.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (minimal)

Three jointly-held structures. Remove any one and the product stops being recognizable as this Type:

1. **The operator's charger fleet of record.** Persistent, individually identified charging equipment — charge points (stations) with their connectors — deployed at known locations, held as the operator's own managed assets. Remove it → a driver-facing charger directory/finder (chargers you don't operate) or a vehicle-side fleet system.
2. **The live charger management connection.** The system is the operational communication counterpart of the chargers (the CSMS / central-system role): it continuously receives status, events and transaction notices from the chargers and can issue operational commands back to them. Remove it → a static asset registry / GIS layer / spreadsheet of installed chargers.
3. **The operational loop.** The running practice of turning connection data into a live serving picture — charger connectivity (online/offline), connector states, charging sessions as observed operational events — and acting on it: alerts on faults and remote diagnosis and fix (restart, unlock, reconfigure, update firmware) so chargers keep serving. Remove it → a connectivity middleware/SDK or a passive telemetry pipe.

Jointly-held is load-bearing: 1 alone = asset inventory; 2 alone = protocol relay; 3 without 1+2 = nothing to operate; 1+2 without 3 = a connected-asset list with no operations; 1+3 without 2 = periodic audits, not a live network.

Sessions appear here strictly as operational events (started/stopped, energy delivered, identity of who charged). The moment sessions are priced and money is settled, the sibling Type (EV Charging Billing & Roaming) begins.

Historical/thin check passed: SteVe (2013, on-prem, no cloud, no automation) satisfies all three legs — registered charge points, OCPP heartbeats/status/transactions, remote OCPP operations — with none of the modern layers. Vendor-proprietary back offices (periodic polling of own-brand chargers, remote reboot) satisfy the abstract core with a proprietary protocol in place of OCPP, so OCPP belongs to L1/common-implementation, not L0.

### L1 — Common Mature Structure

Present across the researched commercial products (and in the protocol family itself) without being definitional:

- Location/site management: addresses, geodata, access rules, public/private classification; site groups.
- Organization hierarchy: operator → sub-organizations, brands, cost centers; multi-tenant white-label operation.
- Charging session records as operational history (who, when, energy, duration) feeding utilization/performance analytics (uptime, energy delivered, usage patterns).
- Maintenance follow-through: escalation of unfixable faults to field maintenance, auto-tickets from alarms, ERP/service-management sync (explicit in 2/4 sample, implied in a third; absent in the minimal ancestor → common, not definitional).
- Driver & credential administration: driver accounts/groups, RFID/charge-card tokens, access rules (the authorization machinery rides the charger connection; it gates billing in the sibling Type — held common here, not definitional).
- Smart charging / load management: site power caps, load balancing across connectors, peak shaving, schedules, session prioritization/rotation.
- Firmware and configuration management: remote configuration get/set, update campaigns, bulk operations via station groups.
- Alerting and event logs: alarms, status events, security events (protocol-level machinery per OCA).
- APIs for integration (billing/CRM/ERP, station control, data export).
- Driver-facing surfaces (white-label app/web: find station, start/stop charge) at the consumer edge.
- Roaming/partner data exchange: publishing station/EVSE data to roaming partners (the data-exchange leg sits at the seam with the sibling Type).

### L2 — Variant / Optional Structure

- Tariff configuration on stations (pricing display / ad-hoc rates) — station-level slice of the sibling Type's tariff engine.
- Maintenance workflow depth beyond the basic escalation (full ticket lifecycle, ERP/service-desk integration, helpdesk staffing) — packaging-dependent.
- Managed operations flavor: 24/7 helpdesk as a service attached to the platform.
- Reservations (present even in the minimal ancestor; product-dependent).
- Energy-services extensions: VPP/DR participation, battery/solar orchestration at sites, V2G — seams toward EMS/DERMS/VPP territory.
- Depot/fleet-flavored configuration: vehicle priority, depot power strategies — seam toward EV Fleet Charging Management.
- Payment terminals / ad-hoc card payment at chargers — per the sibling pass, kept inside the billing Type only where the session/CDR structure carries it; terminal-first shapes border Payment Processing.
- Charger-vendor-locked CSMS (own hardware only) vs hardware-agnostic independent platforms — a packaging continuum, not a type difference.
- AI/self-healing automation of issue resolution (era-current).

### L3 — Vendor-specific (Research Notes only)

- Driivz: "Alert Management System (AMS)" branding; "self-healing algorithms"; Driivz AI / Network Optimizer / Version 9; OCA "golden node" certification role; migration-methodology claims; "up to 6X on-site capacity" and "2,200+ charger models" marketing numbers.
- Virta: Virta Priority / Virta Preconnect / Capacity Maximiser branded load-management features; Virta CO₂ Cashback; Northe fleet-services line; "2,000+ charger models".
- Last Mile Solutions: evc-net service-status domain; "364,000 charge points directly connected" scale claim; ERP-sync specifics; Alliance program.
- SteVe: RWTH Aachen 2013 origin; GPL-3.0; Powerfill managed-cloud relation; JDK/MySQL stack details.

## Vendor-specific Findings

See L3. None of these may define the Type. Marketing precision (scale numbers, capacity multipliers, migration timelines) deliberately excluded from the final document.

## Boundary Findings

- **vs EV Charging Billing & Roaming (sibling, §19) — the primary seam.** Split test, held symmetrically:
  - Remove session commercialization (tariffs → CDR pricing → multi-party settlement/roaming money) → what remains is exactly this Type; SteVe demonstrates it stands alone (full operational shape, zero commercial layer).
  - Remove charger operations entirely → pure roaming hubs and clearing houses demonstrate the commercial layer stands alone (sibling pass evidence).
  - Bundled reality: Driivz ships "Operations Management" and "EV Charging Billing" as separately named modules; Last Mile Solutions splits "Management tools for CPO/MSP" from "Commerce"; Virta's Hub (station management) sits beside "Payments and invoicing"/"Roaming" capabilities. Same product family, two Types.
  - Secondary seams: authorization machinery straddles (credential checks ride the charger connection but gate billing — held common-mature in both passes, definitional in neither); EVSE/station data exchange with roaming partners borders this leaf (data plumbing here, commercial purpose in the sibling); per-charger ad-hoc card payment sits at the Payment Processing boundary.
- **vs EV Fleet Charging Management (§18).** Infrastructure operator's chargers are the managed subject here; the fleet operator's vehicles, missions and charging costs are the subject there. Depot CPMS deployments overlap in features (priority charging, depot load strategies) but the organizing subject differs; if the vehicle fleet, not the charger fleet, is the system of record, it is the other Type.
- **vs driver-facing charger directory / finder applications.** Directories aggregate chargers the app's operator does not control; this Type requires operatorship — the managed chargers are the operator's own assets whose behavior the system can change. Remove operatorship → directory.
- **vs Energy Management System / DERMS / Virtual Power Plant.** Site-level load management inside this Type serves charger operations (protect the site connection, allocate power, rotate sessions). Grid-market participation, DER orchestration across assets, and battery dispatch are other Types; energy-services extensions here are L2 seams.
- **vs Industrial IoT Platform.** Same abstract shape (connected device fleet, telemetry, commands) — but the EVSE-specific operational semantics (connector states, session events, charge-point commissioning, charger-aware commands like connector unlock, smart-charging profiles) are this Type's signature; a generic IIoT platform lacks them.
- **vs Utility Field Service Management / CMMS.** Charger maintenance exists here as follow-through (tickets, field escalation, ERP sync handoff); the maintenance system of record for a service organization remains the other Type. The handoff (auto-ticket → external service management) is the documented interaction.
- **Remove/keep summary:** remove the live connection → asset registry (another Type space); remove the charger subject → generic IoT platform; remove the operator perspective → driver directory; remove session commercialization → still this Type; add session commercialization → the sibling Type.

## Uncertainties

- Vendor help centers, user guides and the OCPP specification text were not reachable; observations rest on product pages, FAQs, and the SteVe README. All final-document assertions are calibrated to that level — no numeric limits, default timings, or exact state enumerations are claimed.
- Exact connector-state vocabulary: status reporting and a connector-status model are directly evidenced (OCA "additional status"/device management; SteVe Connector Status view; product dashboards), but the precise protocol state names were not verified against the spec text; the final document deliberately describes states conceptually.
- North-American market breadth under-sampled (ChargeLab, AMPECO, ChargePoint unreachable); both are known CPMS vendors from the sibling pass's context, but no direct observations were used from them.
- The split between "network management" and "energy management" modules inside one product (Driivz, Virta, LMS all ship both) is a packaging fact; whether site-level load management belongs in L1 was judged from its cross-product presence — it is held common, not definitional, because the minimal ancestor operates fully without it.
- SteVe has reservations but no ticketing/analytics; some commercial products may likewise omit reservations — reservations therefore held optional.

## Final Synthesis

EV Charging Network Management is the operator-side system of record for running a fleet of EV charge points: a persistent registry of the operator's own charging stations and connectors at locations; a live two-way management connection in which the system is the chargers' operational counterpart (receiving status, events and session notices; issuing remote commands); and a continuous operations loop that keeps the network serving — live health picture, fault alerting, remote diagnosis and fix. Mature products add maintenance follow-through (tickets, field escalation), sites and organizational hierarchy, session analytics, driver/credential administration, smart charging and load management, firmware/configuration campaigns, APIs, driver surfaces, and partner data exchange. Session pricing, invoicing, settlement and roaming money belong to the sibling Type EV Charging Billing & Roaming, even when one product ships both as modules of a single "charging management platform".
