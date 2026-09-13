# Research Notes — Environmental Incident Management

Research date: 2026-09-08
Slug: environmental-incident-management
Directory leaf: Environmental Incident Management (§21 Environment, Sustainability & Climate)

## Research Goal

Understand what an Environmental Incident Management application really is from real products: what the core record is, what users do around it, how the work flows from event to closure, what rules matter, and where the boundary lies against the EHS/HSE Platform, Environmental Compliance Management, Contaminated Site Management, and other "incident" Types.

## Initial Boundary (hypothesis before research)

- Hypothesis: operator-side (regulated organization) software for recording, responding to, investigating, and reporting unplanned events with environmental consequence — spills, releases, exceedances, odors, environmental damage.
- Users: site personnel (reporters), EHS/environmental coordinators (processors), environmental managers (investigators/approvers), corporate EHS (analytics), sometimes external agencies (report recipients).
- Nearest neighbors: EHS/HSE Platform (multi-domain register), Environmental Compliance Management (obligation-driven), Contaminated Site Management (site-centered downstream), Emergency Management Platform (public sector), Incident Management (§14, IT — same word, different world), Outage Management System (§19).
- Unknowns: whether the market realizes this as a standalone Type or as an environmental class inside EHS incident registers; how strong the regulatory-notification machinery is; whether monitoring exceedances are in scope.

## Research Questions

1. What exactly is an "environmental incident" in product terms — which event classes are in scope (spill/release, exceedance, odor/noise, damage, near miss)?
2. What does the incident record carry (environmental characterization: substance, media, quantity, severity)?
3. What is the lifecycle: capture → triage → notify → respond → investigate → correct → report → close?
4. How is the regulatory dimension realized (reportability determination, agency notification, report generation, retention)?
5. How does the environmental class relate to safety incidents in the same products (shared register vs separate)?
6. What integrations anchor the incident (facility/asset, chemical inventory, permits, monitoring data)?
7. Who uses which surface (reporter vs processor vs manager)?

## Representative Products

Selected for market representation + documentation accessibility + different product philosophies + different customer tiers:

| Product | Pole | Why sampled |
|---|---|---|
| Quentic (Incidents & Observations module) | European, ISO-anchored EHS suite; environmental damage as a case class | mid-market/European pole; strong module page |
| Intelex (Safety Incident Management application) | configurable app-library EHSQ platform; environmental spills/releases as incident types with regulatory form generation | mid/enterprise North American pole |
| Cority (Incident Management within CorityOne) | enterprise EHS+ platform; incident management as platform-level solution | enterprise pole |
| Sphera (Incident Management within SpheraCloud EHS&S) | operational-risk-led suite; low-barrier workforce reporting (First Report portal) | safety-culture-led pole |
| Locus Technologies (Spill Management app) | environmental-data-led vendor; spill/incident as environmental record in an environmental platform | environmental-first pole (the cleanest point realization) |

Also observed but not sampled as evidence sources: Donesafe (HSI Donesafe) — EHSQ platform with incident + environmental modules (homepage-level evidence only; environmental-incident deep page 404). Enablon (Wolters Kluwer) — unreachable (403), recorded as limitation.

## Sources

All fetched 2026-09-08 (Tier 1/2 — official vendor product pages; help-center-level operational docs were not reachable for any sampled product):

- Quentic — https://www.quentic.com/ ; https://www.quentic.com/software/incidents-observations/
- Intelex — https://www.intelex.com/ ; https://www.intelex.com/products/environment/all-applications/ ; https://www.intelex.com/products/applications/incident-management-software/
- Cority — https://www.cority.com/solutions/environmental-management/ ; https://www.cority.com/corityone/incident-management-software/
- Sphera — https://sphera.com/ ; https://sphera.com/solutions/environment-health-safety-sustainability/health-and-safety-management-software/incident-management-software/
- Locus — https://www.locustec.com/ ; https://www.locustec.com/applications/ehs-compliance/spill-management/

Failed/abandoned (per source-access rules): enablon.com (403), wolterskluwer.com Enablon page (403), donesafe.com/environmental-incident-management/ (404), sphera.com/solutions/environmental-performance/ (404), locustec.com/applications/spill-reporting/ (404), intelex.com/ehs-software/environmental-incidents/ (redirects to homepage — see Product Mismatch note below).

## Product Observations

### Quentic — Incidents & Observations module (Evidence layer A)

- Module framed as "EHS incident reporting software": report and analyze EHS cases; positions beyond reacting to accidents — proactive culture, positive and negative cases.
- **Case reporting**: "comprehensive set of predefined use cases for issues such as property and environmental damage, compliance or quality issues", plus further classification "according to your individual standards". → environmental damage is a first-class case class; taxonomy is customer-configurable.
- **Case processing**: "customizable notification rules… alert relevant parties immediately when reports are received. Differentiate which people are informed for various incident categories or consequences depending on the organizational or site structure."
- **Review and investigation**: assign priorities during initial review; in-depth investigation; AI to identify causes and assess risks; findings initiate "corrective and preventive actions that eliminate future deficiencies".
- **AI-powered 5-why analysis**: structured workflow through the 5-why chain; suggestions for descriptions/follow-up questions/answers.
- **Evaluation and reports**: incidents "fully documented and verified. Data is auditable and can be converted into reports"; "Accident reports are generated immediately in the appropriate form for official bodies"; dashboards with KPIs and trends.
- **AI-powered case & pattern analysis**: regular scans of incident reports for "correlations, trends, and hotspots".
- Mobile app for reporting on the move.
- Packaging note: environmental incidents are one class inside an EHS-wide incident module; Quentic's separate Environmental Management module tracks resources/costs (measurement side, not incidents).

### Intelex — Safety Incident Management application (Evidence layer A)

- "Gather, organize and automatically report an incident using OSHA, RIDDOR, WCB, ISO, EPA or other regulatory forms." → regulatory form generation spans safety AND environmental agencies (EPA named).
- "Create unique forms for injuries (including SIFs and pSIFs), illnesses, near misses, property damage, environmental hazards, and more, including AI-assisted inputs."
- "Customizable Forms: …for incidents including employee, property and environmental types."
- FAQ defines the system: "a series of tasks and workflows taken to resolve workplace incidents, such as injuries and illnesses, environmental spills or property damage."
- "Intelex software can track workplace injuries, illnesses, near-misses, environmental spills, property damage, equipment failures, unsafe conditions and more."
- "A safety incident report… identify the root cause of the event and corrective actions taken to eliminate the risks."
- Features: key incident metrics (DART, TRIR, LTIR — safety metrics), configurable dashboards, mobile app with offline, near-miss reporting with AI-enhanced descriptions, visual tools (body mapping, geolocation, photos, voice notes).
- Demo copy: "Generate out-of-the-box forms or design your own; create incident reports via mobile and offline; intelligent workflows to schedule tasks and due dates; root cause analysis and risk assessments; corrective and preventative actions; visualize key safety metrics."
- Packaging note: the environmental suite page (all-applications) lists ESG/permit/compliance/waste/water/air-type applications but NO dedicated environmental-incidents application; incident management sits under Health & Safety. The historical deep URL /ehs-software/environmental-incidents/ now redirects to the homepage — evidence of packaging drift toward a unified incident application with environmental incident types (single-source observation).

### Cority — Incident Management within CorityOne (Evidence layer A)

- "Capture and classify incidents with configurable workflows, severity scoring, and standardized data models to ensure consistency across sites and teams."
- "Incident Reporting and Data Capture: fast, mobile-first… guided forms, offline access, and real-time submissions."
- "Task and Action Management: assign, track, and verify corrective and preventive actions with automated workflows… accountability and timely resolution."
- "Compliance and Audit Readiness: maintain complete audit trails, regulatory alignment, and documentation to support compliance reporting and internal or external audits, including alignment with ISO 45001, ISO 14001, ISO 9001, and OSHA reporting requirements." → ISO 14001 named: environmental management-system alignment is part of the incident compliance posture.
- Mobile solutions for field reporting (offline).
- "Insights and Reporting Analytics: dashboards, trend analysis… surface root causes and CAPA recommendations."
- Flow: "Report & Record Incidents Consistently → Investigate Root Causes & Take Action → Analyze Trends & Prevent Recurrence."
- Cortex AI with "human-in-the-loop" for data collection and CAPA/root-cause recommendations.
- Packaging note: Environmental Cloud (air/waste/water/chemicals/compliance) is measurement/program-centric and separate; incident management is a platform-level solution. Environmental incidents not prominent on the current incident page — environmental depth lives in the Environmental Cloud; the incident module is EHS-wide.

### Sphera — Incident Management within SpheraCloud EHS&S (Evidence layer A)

- "software interface that leads users through each step of reporting an incident, near miss or any observation that could be a potential risk."
- **First Report portal**: "enables your entire workforce to accurately report events and observations… accessible from any location at any time; easy to use with mobile, touchscreen and kiosk devices; works without a specific user account; allows anonymous reporting; increases reporting adoption." → low-barrier capture surface as a named capability.
- Loop: "Investigate reported incidents based on data. Identify root causes. Take corrective action. Analyze trends to prevent future events."
- "Analyze incidents and address risk at a local and global level. Automate repeatable tasks using smart alerts and risk aggregation."
- Suite context: Actions, Analytics, Audits modules alongside; incident management is one module of the Health & Safety platform.
- Packaging note: Sphera's environmental side is "Environmental Accounting" (air/GHG, refrigerant, waste, water emissions) — measurement-centric; incident management sits under Health & Safety. Environmental incidents not prominent on the incident page.

### Locus Technologies — Spill Management app (Evidence layer A)

- Environmental-first vendor ("unified, audit-grade… platform for EHS compliance, ESG, and water"; "scientist driven").
- "Locus Incident Management :: Spills" — "Track any type of spill incident per your business requirements."
- "Get ahead of spills with mobile field-logging coordinates and activities then instantly sync back to the office for follow-up." → field capture with location coordinates; offline mobile ("Track spills in the field, even when offline, with Locus Mobile").
- "Built-In Analysis: perform root-cause analyses and document corrective actions with built-in tools and dashboards."
- "Facility Management: track new and modified equipment associated with regulated facilities—fully integrated with our Facilities Management app." → incident anchored to regulated facility/equipment context.
- "Task Management: send follow-up actions automatically from the inspection task completion checklist—fully integrated with Locus Task Management app."
- "Spill Response: route spill response based on spill type with configurable workflows." → response routing driven by incident classification.
- "Track and manage spill-related activity with configurable dashboards and flexible reporting."
- "Integrate with regulatory content providers for the latest regulatory updates."
- Platform context: 30+ apps, no-code configuration, custom apps; separate "Safety & Incident Management" app (OSHA 300 reports) exists alongside — spills app is the environmental-regime twin.

## Cross-product Comparison

| Dimension | Quentic | Intelex | Cority | Sphera | Locus |
|---|---|---|---|---|---|
| Environmental incident as… | case class ("environmental damage") in EHS incident module | incident types ("environmental spills/hazards") in incident application | part of EHS-wide incident capture (ISO 14001 alignment named) | events/observations in H&S incident module (environmental not prominent on page) | dedicated spill/incident app (environmental-first) |
| Capture surface | web + mobile app | mobile + offline; out-of-box or custom forms | mobile-first guided forms, offline | First Report portal: any device, kiosk, no account, anonymous | mobile field logging with coordinates, offline |
| Classification | predefined use cases + customer classifications | unique forms per incident type | configurable workflows, severity scoring, standardized data models | guided step-by-step reporting | spill type drives response routing |
| Notification | customizable notification rules by category/consequence/site | intelligent workflows schedule tasks | automated workflows | smart alerts | follow-up actions auto-sent |
| Investigation | priorities; AI 5-why | root cause analysis + risk assessments | guided root cause methodologies | investigate → root causes | built-in root-cause analyses |
| Corrective actions | corrective & preventive actions from findings | corrective & preventative actions | assign/track/verify CAPA | take corrective action | document corrective actions |
| Regulatory facing | "appropriate form for official bodies"; auditable | OSHA/RIDDOR/WCB/ISO/EPA forms; auto-report | audit trails; ISO 14001/45001/9001 + OSHA alignment | (not prominent) | regulatory content providers; regulated facilities |
| Analytics | dashboards, KPIs, trends; AI pattern/hotspot scan | dashboards; incident metrics | dashboards, trend analysis, AI CAPA recs | trend analysis, risk aggregation | configurable dashboards, flexible reporting |
| Anchor integrations | org/site structure | ERP/HR integrations | platform-wide (analytics, mobile, docs) | SpheraCloud suite | Facilities Management + Task Management apps |

**Stable commonalities (present in all or nearly all sampled products):**
1. A persistent incident record anchored to site/facility and time.
2. Low-barrier capture (mobile, offline, guided forms; Sphera adds anonymous/kiosk).
3. Classification/severity driving routing and workflow.
4. Notification/escalation machinery.
5. Investigation with root-cause tooling.
6. Corrective/preventive action tracking to closure.
7. Regulatory-facing posture (forms for official bodies, audit trails, ISO/regulatory alignment).
8. Dashboards/trend analytics over the incident base.

**Divergences (packaging, not structure):**
- Environmental incidents are realized as a class inside an EHS-wide incident register (Quentic, Intelex, Cority, Sphera) or as an environmental-first dedicated app (Locus spills).
- Regulatory form generation breadth varies (Intelex names EPA/OSHA/RIDDOR/WCB; Quentic says "official bodies" generically).
- AI assistance is current-generation (Quentic 5-why + pattern scan; Cority Cortex AI; Intelex AI-assisted inputs) — era-current, not definitional.

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant

Three jointly-held structures. Remove any one and the product stops being an environmental incident management application:

1. **The environmental incident of record** — a persistent, individually identified record of one unplanned event with actual or potential environmental consequence (release/spill, exceedance, environmental damage, near miss with environmental potential), anchored to a site/facility and a point in time, carrying environmental characterization: what was released or impacted, to which environmental media (air/water/soil/land), at what scale/severity.
   - Remove → generic case/task management or an ops log with nothing environmental.
2. **The response–investigation–correction loop** — the incident is worked, not just logged: immediate response/containment recorded against the incident, cause investigated (root-cause tooling), corrective and preventive actions assigned, tracked, and verified to closure.
   - Remove → an incident log/register; the "management" is gone.
3. **The regulatory-facing compliance posture** — the record is maintained as defensible compliance evidence: classification against reportability, internal escalation and external agency notification/report generation where required, audit trail and retention.
   - Remove → internal-only event tracker; the environmental-regulatory dimension (what separates this from generic property-damage incident tracking) is gone.

Jointly-held is load-bearing:
- 1 alone = incident log
- 2+3 without 1 = generic case management
- 1+2 without 3 = internal ops/safety incident tracker (drifts toward safety incident management)
- 1+3 without 2 = report form with no management loop

### L1 — Common Mature Structure

- Mobile/field capture with offline support, photos, location/coordinates
- Guided, configurable incident forms; customer-definable taxonomies
- Severity/risk scoring; classification-driven routing
- Notification/escalation rules (who is told, by category/severity/site)
- Root-cause analysis tooling (structured methodologies, e.g. 5-why)
- Corrective/preventive action management (often a shared platform action engine)
- Regulatory report generation in agency-acceptable forms; audit trail
- Dashboards, KPIs, trend/pattern analysis over the incident base
- Integration with facility/asset registers, task management, chemical/permit context
- Low-barrier/anonymous reporting portals (workforce adoption)

### L2 — Variant / Optional Structure

- **Packaging**: environmental class within an EHS-wide incident register (dominant market shape) vs environmental-first standalone app (spill/release-centric)
- **Event-class emphasis**: spill/release-centric (oil & gas, chemical, transport), exceedance/compliance-centric (manufacturing, utilities), complaint-driven intake (community odor/noise)
- **Monitoring linkage**: exceedances from emissions/effluent monitoring as incident triggers (adjacent to Environmental Monitoring/CEMS)
- **Downstream linkage**: incident → contaminated-site/remediation record handoff
- **AI assistance**: cause suggestion, pattern/hotspot detection, report drafting (era-current)
- **Multi-jurisdiction form libraries** vs single-regime
- **Emergency/crisis escalation** integration for severe events
- **Claims/insurance linkage**

### L3 — Vendor-specific (kept in Research Notes)

- Quentic: "Incidents & Observations" module name; AI 5-why chain; positive+negative case culture framing; Quentic App; German hosting/ISO certificate positioning.
- Intelex: app-library packaging; SIF/pSIF; DART/TRIR/LTIR safety metrics; named form standards (OSHA 301/300/300A in FAQ, RIDDOR, WCB, EPA); offline mobile.
- Cority: CorityOne five-cloud architecture; Cortex AI "human-in-the-loop"; myCority mobile.
- Sphera: First Report portal (kiosk, anonymous, no account); SpheraCloud; smart alerts/risk aggregation.
- Locus: Locus Platform 30+ apps; no-code custom apps; spill-response routing by spill type; SOC 1/2 Type 2; uptime statistics; "scientist driven" positioning.

## Rejected Findings

- "Environmental incident management = a module of an EHS platform" — rejected as a definition; packaging varies (Locus is environmental-first). The Type is defined by regime depth, not by packaging.
- "Safety metrics (TRIR/DART) are part of the Type" — rejected; those are safety-regime metrics appearing because sampled products are EHS-wide. Environmental incidents have their own measures (release quantities, media affected, exceedance counts) — observed only weakly at page level; kept out of the core.
- "AI investigation is definitional" — rejected; era-current capability (2026 generation), absent from the historical shape.
- "Spill response routing is definitional" — rejected; single-product (Locus) evidence; held as variant depth of the response leg.

## Boundary Findings

1. **vs EHS/HSE Platform (§21, processed 2026-09-08)** — keep both. The EHS platform's defining core is the organization-wide multi-domain occurrence register + shared corrective-action loop; this Type is the environmental-regime depth: environmental characterization (substance/media/quantity), environmental regulatory handling (agency notification/reporting), environmental response (containment/cleanup). The EHS pass itself held environmental point leaves as "domain point systems; the EHS platform commonly embeds equivalents as modules." Market reality: 4 of 5 sampled products realize environmental incidents inside an EHS-wide register; 1 (Locus) is environmental-first. The leaf documents the environmental-regime depth wherever packaged. Removal tests: remove the multi-domain register → EHS platform; remove environmental depth → this leaf collapses into the platform's safety incident module.
2. **vs Environmental Compliance Management (§21, processed 2026-09-08)** — keep both. That Type is obligation-driven (register of legal requirements → recurring conformance work → evidence-backed status). This Type is event-driven (unplanned event → response/investigation/notification → closure). An incident can create an obligation (report to agency), but the center of record differs: event vs requirement. Removal test: remove the event → compliance management; remove the obligation register → incident management.
3. **vs Contaminated Site Management (§21, processed 2026-09-07)** — keep both. A spill/release is one discovery path into a contaminated site record; that Type is site-centered with a years-long lifecycle (investigation → remediation → monitoring → closure). This Type is event-centered with a short-horizon lifecycle (response → investigation → actions → closure). Handoff: a severe incident may open a site record downstream.
4. **vs Emergency Management Platform (§24)** — different seat and object: public-sector multi-hazard emergency operations (EOC, alerts, resources) vs operator-side environmental compliance events. Environmental emergencies may escalate toward emergency management, but the record systems differ.
5. **vs Incident Management (§14, IT)** — same word, different world (IT service incidents vs environmental events). No structural relationship beyond generic case-management shape. (Consistent with the EHS pass finding.)
6. **vs Outage Management System (§19)** — utility outage events center on service restoration; environmental consequences may be recorded as incidents, but OMS is not an environmental record system.
7. **vs Environmental Monitoring Platform / CEMS (§21)** — measurement-centric (continuous data, limits, exceedance events) vs event-centric (unplanned incidents). An exceedance may be raised as an incident; the CEMS pass holds the data-handling compliance record as its core.
8. **vs Hazardous Materials Management (§21)** — materials/chemicals of record vs events. A release incident references a material; the material system does not manage the event.
9. **vs Safety Incident Management (in-suite sibling)** — sibling classes in the same register in most products. Environmental incidents center on environmental media and agency reporting; safety incidents on injury/illness and worker-compensation/OSHA-type reporting. Where a product carries both in one register, that is packaging, not a boundary failure.

## Historical / Market-Sample Check

- Paper-era check: a spill log book + agency incident report form + cleanup record + investigation notes + corrective-action list satisfies all three L0 structures without software-era features. Passes.
- Regional check: US spill reporting practice (release notification to agencies), EU/German environmental incident practice (Störfall-class events, permit-exceedance reporting), UK environmental permitting — same structures under different vocabularies. The core does not depend on any single regime's form names.
- Platform-native check: ERP-embedded or GRC-suite incident modules carry the same core as a module (packaging variant). Under-sampled (Enablon unreachable) — kept general.
- Era check: AI investigation, pattern detection, anonymous kiosk portals are current-generation; the core stands without them.

## Uncertainties

1. Enablon (enterprise GRC-suite pole) unreachable (403) — claims about that packaging are general, not evidence-backed in detail.
2. Donesafe environmental-incident deep page 404; only homepage-level evidence — not used as a sampled product.
3. Help-center-level operational documentation (exact status models, numeric reportable-quantity thresholds, retention periods, deadline values) was not reachable for any sampled product; the final document deliberately avoids such precision.
4. Whether monitoring exceedances are raised as incidents in-product (vs in the monitoring system) could not be confirmed at page level — held as variant/adjacent, not core.
5. The Intelex dedicated "Environmental Incidents" application appears retired/folded into the unified Incident Management application (deep URL now redirects) — single-source packaging-drift observation, not generalizable.

## Final Synthesis

Environmental Incident Management is the operator-side system of record for unplanned events with environmental consequence. Its defining structure is three jointly-held things: the environmental incident of record (persistent, identified, site/time-anchored, environmentally characterized — what was released, to which media, at what scale); the response–investigation–correction loop (immediate response recorded, cause investigated, corrective/preventive actions tracked to verified closure); and the regulatory-facing compliance posture (reportability classification, escalation and agency notification/report generation where required, audit-ready retention). Around that spine, mature products standardize low-barrier mobile/field capture, classification-driven routing and notification, root-cause tooling, shared corrective-action engines, regulatory report generation, and trend analytics. The market realizes the Type in two packagings — as the environmental class of an EHS-wide incident register (dominant) or as an environmental-first incident/spill application — and the leaf documents the regime depth, not the packaging. Boundaries: obligation-driven compliance management is the process twin; contaminated-site management is the downstream site-centered Type; the EHS platform is the multi-domain container; IT incident management merely shares the word.
