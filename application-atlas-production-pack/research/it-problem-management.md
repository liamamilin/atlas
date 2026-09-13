# Research Notes — IT Problem Management

Slug: it-problem-management
Directory leaf: IT Problem Management (§14 IT, Cloud & Infrastructure)
Research date: 2026-09-08
Methodology: update-v1 (WORKFLOW_v1.1 + WRITING_GUIDE_v1.1)

---

## Research Goal

Understand what an "IT Problem Management" application actually is as an Application Type: what objects exist inside it, how a problem moves from identification to closure, who participates, what rules govern the practice, and where its boundary lies against the neighboring Types that share vocabulary — Incident Management (processed), IT Change Management (processed), ITSM (unprocessed), Ticketing System (processed), CMDB (processed), AIOps (processed), Error Tracking / Bug Tracking (§12, unprocessed), Vulnerability Management (§15).

This is the IT/service-operations leaf. The directory keeps "problem" unambiguous here (no other "problem" leaves exist), but the practice is tightly interlocked with two already-processed §14 siblings, both of which pre-hung expectations for this pass:

- **incident-management pass (2026-09-08)**: "it-problem-management — downstream root-cause practice consuming post-incident output; Atlassian's own definition ('only those tasks required to mitigate impact and restore functionality') is the seam evidence."
- **it-change-management pass (2026-09-08)**: "it-problem-management (§14) — problem = root-cause elimination loop, change = its remediation output (problem→change chaining explicitly documented in a sampled vendor)."

## Initial Boundary (hypothesis before research)

- Core use: identifying and managing the *underlying causes* of one or more incidents (and potential future incidents), documenting workarounds, and driving the cause to elimination — often through change management. The incident record answers "what is broken and how do we restore it"; the problem record answers "why did this happen and how do we make it stop happening".
- Users: problem managers (process owners), IT service desk staff (apply workarounds, link incidents), technical specialist teams (root-cause investigation), IT operations engineers.
- Nearest neighbors: Incident Management (upstream evidence supplier), IT Change Management (remediation executor), ITSM (umbrella suite), Ticketing System (record machinery), CMDB (diagnosis context), AIOps (signal analysis), Error Tracking / Bug Tracking (software-defect objects).
- Unknowns: Is the workaround/known-error layer definitional or merely common? Is proactive problem detection definitional? Are specific RCA methods (five whys, fishbone) part of the Type? What closes a problem and what does closure tie back to?

## Research Questions

1. How do products and practice frameworks define a "problem", and what does the problem record carry?
2. What is the lifecycle/state model of a problem record?
3. How do problems get identified — reactive (from incidents) vs proactive (from trends/monitoring)? How are incidents linked to problems?
4. What does investigation/diagnosis look like in-product, and what context feeds it (incident data, CI/CMDB, monitoring, KEDB)?
5. What is the role of workarounds and known errors? Is a known-error database definitional or an implementation?
6. How does resolution and closure work — fix via change, direct fix, no-fault-found? What does closure tie back to?
7. Who uses it — which roles, with what authority?
8. What interfaces exist (queues, problem detail, RCA views, known-error surfaces, dashboards)?
9. What rules matter (priority from impact × urgency, closure rules, review practices)?
10. Where are the boundaries vs incident management, change management, ticketing, error/bug tracking, AIOps?

## Representative Products

Selected to span product philosophy and customer tier:

| Product | Philosophy | Customer tier | Evidence depth |
|---|---|---|---|
| Atlassian (Jira Service Management + official ITSM practice documentation) | dev-oriented ITSM; advocates blending problem and incident practices | small teams → enterprise, IT + dev | Tier 1–2 (official practice hub pages + incident-vs-problem page; product support docs unreachable) |
| ManageEngine ServiceDesk Plus | ITIL-certified mid-market suite with strong process documentation | mid-market → enterprise | Tier 2 (official product feature page with ITIL FAQ) |
| Freshservice (Freshworks) | SMB/mid-market SaaS, AI-forward | SMB → enterprise | Tier 2 (official ITIL problem-management process guide) |

ServiceNow (enterprise ITSM market leader) was attempted and failed (timeout — consistent with the incident-management and it-change-management passes, which also could not reach it). Enterprise-specific mechanics are therefore NOT asserted anywhere. iTop and GLPI (open-source poles with explicit Problem/KnownError objects) were attempted (2 URL variants each, 404) and abandoned per source-access rules — the open-source pole is held as an uncertainty, covered only by the historical/framework check.

## Sources

Fetched 2026-09-08:

- Atlassian — "What is problem management?" (official ITSM practice hub): https://www.atlassian.com/itsm/problem-management
- Atlassian — "Problem management vs. incident management" (official DevOps/incident-management page): https://www.atlassian.com/incident-management/devops/incident-vs-problem-management
- ManageEngine — ServiceDesk Plus problem management (product feature page, incl. ITIL FAQ): https://www.manageengine.com/products/service-desk/problem-management.html
- Freshworks — "ITIL problem management explained" (Freshservice official guide): https://www.freshworks.com/freshservice/itsm/problem-management/

Failed/abandoned per source-access rules:

- ServiceNow product page (https://www.servicenow.com/products/it-problem-management.html) → timeout (ServiceNow also unreachable in the incident-management and it-change-management passes)
- Atlassian JSM support doc (https://support.atlassian.com/jira-service-management-cloud/docs/reduce-future-incidents-with-problem-management/) → 404 (JSM product support docs unreachable, same as the incident pass)
- ManageEngine ITIL process guide (https://www.manageengine.com/products/service-desk/it-problem-management/) → 404 (the analogous /it-change-management/ guide exists; this one does not)
- iTop wiki (latest + 3_1_0 user-guide problem pages) → 404 ×2
- GLPI user docs (readthedocs helpdesk paths) → 404 ×2

Framework reference: ITIL definitions are quoted *within* the fetched vendor sources (Atlassian quotes ITIL's problem/known-error definitions; Freshservice quotes the ITIL 2011 glossary). No separate ITIL/Axelos source was fetched (paywalled) — ITIL is used as a shared reference frame the vendors themselves cite, not as an independent Tier-1 source.

---

## Product A — Atlassian (Jira Service Management + official practice documentation)

### Key observations (evidence layer A unless noted)

**Definitions.** "Problem management is the process of identifying and managing the causes of incidents on an IT service. It is a core component of ITSM frameworks." Quotes ITIL: "a problem is a cause, or potential cause, of one or more incidents." Known error (quoting ITIL): "a problem that has a documented root cause and a workaround." Workaround: "a temporary solution for reducing the impact of problems and keeping them from becoming incidents."

**Problem ≠ incident.** "Rolling back a recently deployed [change] may get the service operating again and end the incident, but the underlying problem remains." "An incident may be over once the service is up and running again, but until the underlying causes and contributing factors are addressed, the problem remains." "Problems are the root cause of those disruptive events [incidents]." Also: "There is often more than one root cause of an incident" — so cause analysis is plural, not singular.

**Process (6 steps).** 1. Problem detection (proactively find problems, or identify workarounds before future incidents). 2. Categorization and prioritization ("track and assess known problems"). 3. Investigation and diagnosis (identify underlying contributing causes and best remediation course). 4. Create a known error record (documented root cause + workaround; "typically stored in a document called a known error database"). 5. Create a workaround, if necessary. 6. Resolve and close the problem ("A closed problem is one that has been eliminated and can no longer cause another incident").

**JSM product capabilities.** "Links incidents to problems, supports root cause analysis and post-incident reviews, and tracks corrective actions through to completion."

**Relationship to other practices.** Change management: "When a change does cause disruption or downtime, that change is analyzed during incident and problem management processes." Knowledge management: workarounds flow into the knowledge base; "a healthy knowledge management practice can enable faster incident resolution and fewer incidents altogether."

**Philosophy (DevOps pole).** Atlassian advocates bringing problem and incident management closer together; a siloed problem team becomes "a dumping ground of problems… where problem issues go to die". The blameless postmortem is the bridge: "incident managers turn detective and turn to the task of problem management and prevention." Risk flagged: the less-urgent problem work "doesn't get deprioritized in favor of the in-your-face urgency of incident management."

## Product B — ManageEngine ServiceDesk Plus

### Key observations (evidence layer A unless noted)

**Positioning.** "Identify, investigate, and fix the causes of recurring incidents with AI-driven ITIL® problem management." ITIL FAQ: "ITIL defines a problem as a cause, or potential cause, of one or more IT incidents. Problem management is a procedural way to ensure that no repeat incidents occur by delving deep to find the root cause and fix it, all while reducing the severity of the incidents through suitable documentation of known problems and providing work-arounds."

**Three phases (FAQ).** 1. Problem identification ("identifying a problem, either through AI predictions or by grouping multiple incidents, and logging all the known information into a problem management tool"). 2. Problem control ("prioritizing, investigating, and analyzing the logged problem"). 3. Error control ("managing known errors and work-arounds logged in the KB periodically").

**Incident linking.** "Link multiple incident tickets about the same outage with a parent problem ticket." Organization-wide announcements to avoid duplicate incident tickets while a problem is under investigation.

**Record + templates.** Problem templates record "every aspect of your RCA, including assessing symptoms, understanding the impact, and other pertinent diagnoses" — dynamic, drag-and-drop customizable.

**RCA machinery.** Visual problem-management workflows on a drag-and-drop canvas, alignable to "popular RCA frameworks, such as the five whys"; automation for stakeholder RCA-progress notifications, field updates, approvals. Intelligent technician assignment for problem tickets (AI routing by historical data).

**Context via other practices.** "Analyze dependencies and impacts with the native CMDB… Associate configuration items, incidents, changes, and releases with problem tickets for enriched context and rapid resolution." (Problem→change/release association = the remediation handoff; CMDB = diagnosis context.)

**Known error + KB.** "Document the initial work-around and the resolution and convert the documentation into a repository of knowledge articles… Mark unresolved problems as known errors so that your IT technicians can quickly share work-arounds and focus on resolving underlying issues."

**Worked example (FAQ).** Recurring application-slowdown incidents → trend observed → logs analyzed (database deadlocks, query timeouts at peak) → network latency ruled out → five-whys/fishbone RCA → root cause: inefficient SQL queries in a new reporting module → permanent fix deployed (query optimization + materialized views). Illustrates reactive problem management end-to-end.

## Product C — Freshservice (Freshworks)

### Key observations (evidence layer A unless noted; page is part process guide, part product marketing — process claims cross-checked against A and B)

**Definitions.** Quotes ITIL glossary: problem management is "the process responsible for managing the lifecycle of all problems" so IT organizations can "proactively prevent incidents from happening and minimize the impact of incidents that cannot be prevented." Problem = "a cause or potential cause of one or more incidents"; incident = "an unplanned interruption to an IT service or reduction in the quality of an IT service." Analogy: "Incident management treats a symptom, while problem management diagnoses the underlying disease."

**Goals.** Prevent future incidents; prevent recurring incidents; minimize unavoidable impacts. "Problem management isn't about solving problems; it's about ensuring IT teams have fewer problems to solve."

**Two types.** Proactive (predict and prevent by eliminating root cause before incidents) and reactive (analyze recurring incidents toward long-term fix).

**Problem record fields.** Problem type and category, incident description, associated incidents, affected CIs (from CMDB), user information, status, resolution, closure. Prioritization = impact (number of users and CIs affected) × urgency (how quickly resolution is needed).

**Detection sources.** Incident trends, hardware/software failures, resource utilization/capacity issues, incident reports, users/technicians, ITSM software/machine monitoring.

**Process.** Detection → logging (categorization/prioritization) → investigation and diagnosis (review the KEDB for similar problems; loop in SMEs) → resolution, split into *problem control* (RCA → convert to known error → workarounds documented) and *error control* (permanent solutions for known errors; solution passed to the change management team) → closure (verify logged details, ensure change team has what it needs, review resolution + business impact, risk analysis for process improvement; "the problem (and any related incidents) can be closed").

**Problem manager role.** Analyzes historical and real-time incident data, identifies repeat incidents, coordinates each problem's lifecycle diagnosis→resolution, maintains an up-to-date problem queue and stakeholder communication, prioritizes with business context, documents workarounds + known errors into the KB and self-service.

**KEDB.** Problem managers "maintain your known-error database (KEDB) and document successful workarounds" — enables service-desk efficiency, automation, self-service portal.

**Tool capabilities listed.** Automate workflows (status tracking, associated-incident identification, closure communication); perform RCA and track resolution/workaround progress; create/maintain KEDB; link problems to incidents/changes/releases; provide agents workarounds with contextual links; build KB powering self-service; AI (predictive analytics, recommendations, chatbots).

---

## Cross-product Comparison

| Structure | Atlassian | ManageEngine SDP | Freshservice | Assessment |
|---|---|---|---|---|
| Problem as persistent record of a cause/potential cause of incidents | ✔ (definition + process) | ✔ (definition + templates) | ✔ (definition + record fields) | Universal in sample + ITIL frame — L0 candidate |
| Problem distinct from incident records; incidents linked to the problem | ✔ ("links incidents to problems") | ✔ ("parent problem ticket" for multiple incidents) | ✔ ("associated incidents" field) | Universal — L0 candidate |
| Investigation/diagnosis loop producing a recorded cause | ✔ (step 3; RCA in JSM) | ✔ (RCA workflows, five whys; symptoms+impact recorded) | ✔ (investigation & diagnosis step) | Universal — L0 candidate |
| Workaround documentation + known-error status | ✔ (known error record; workaround step) | ✔ (mark as known error; workaround→KB) | ✔ (problem control → known error → workarounds) | Universal — L0 candidate (known-error *database* as an object is an implementation) |
| Resolution routed to change management (permanent fix as a change) | ◐ (change analyzed when it causes problems; corrective actions tracked) | ✔ (associate changes/releases with problems) | ✔ ("solution is applied via change management") | Strong cross-product; held as L0 leg 3 with "commonly via change" phrasing (Atlassian's DevOps pole does not always formalize the handoff) |
| Closure ties back to the incident population | ◐ ("closed problem can no longer cause another incident") | ✔ (recurring-incident elimination framing) | ✔ ("the problem (and any related incidents) can be closed") | Universal — part of L0 leg 3 |
| CI/CMDB anchoring for diagnosis context | ◐ (via JSM Assets; not on the fetched page) | ✔ (native CMDB dependencies/impacts) | ✔ (affected CIs field) | Common mature structure (A-evidenced in 2/3) |
| Priority from impact × urgency | ◐ (categorization/prioritization step) | ◐ (impact assessment in templates) | ✔ (explicit impact × urgency) | Common mature structure |
| Proactive detection (trends/monitoring before incidents) | ✔ ("proactively find problems") | ✔ (AI problem prediction from clustered incidents) | ✔ (proactive problem management as a named type) | Common; NOT definitional (reactive core predates it) |
| RCA frameworks as product features (five whys, fishbone) | ◐ (blameless postmortem framing) | ✔ (alignable workflows) | ◐ (RCA technique blog linked) | Optional/variant — methodology is user practice, not product structure |
| KEDB as a distinct surface | ◐ ("typically stored in a… known error database") | ◐ (known errors logged in KB) | ✔ (KEDB named; reviewed during investigation) | Implementation varies: status on problem vs KB articles vs dedicated DB — conceptual layer is the known-error state, not the database |
| AI prediction/clustering | — | ✔ (Zia) | ✔ (Freddy AI capabilities) | Vendor-current, optional |
| Post-incident review linkage | ✔ (blameless postmortem as bridge) | — | ◐ (review at closure) | Common, packaging varies |

(✔ = directly observed; ◐ = present but weaker/indirect in the fetched source; — = not observed in fetched source. Evidence layer A throughout unless noted.)

## Abstraction Levels

### Level 0 — Defining Invariant (jointly held, minimal)

**The problem record of record + the root-cause investigation loop + the cause-directed disposition to closure.**

1. **The problem record.** A persistent, individually identified record of a suspected or confirmed underlying cause — or potential cause — of one or more incidents, held as an object distinct from the incident records it explains. It carries its state, a priority derived from impact and urgency, and an accumulating investigation trail. Remove it → a ticket backlog or an RCA document library; nothing manages the cause.

2. **The root-cause investigation loop (problem control).** The record is *worked as a diagnosis*: related incidents are linked as evidence, configuration/infrastructure context is consulted, investigation is performed, and the determined cause (including "no fault found" outcomes) is recorded on the record. Remove it → a list of complaints with no cause semantics; the cause-finding is what makes it "problem" management.

3. **The cause-directed disposition to closure (error control).** The record drives action against the cause and moves to a recorded closed disposition: a documented workaround (the known-error state) reduces the incident impact while the permanent resolution is pursued — commonly routed through change management — and closure ties back to the incident population the problem explains (a closed problem is one that can no longer cause incidents). Remove it → analysis with no operational consequence.

Jointly-held is load-bearing:

- 1 alone = ticket-type record with no cause semantics (Ticketing System territory)
- 2 without 1+3 = an RCA/postmortem artifact practice, nothing managed
- 3 without 1+2 = a remediation tracker with no diagnosis
- 1+2 without 3 = a diagnosis log that never lands operationally
- 2+3 without 1 = ephemeral investigation, no record to close or audit

### Level 1 — Common Mature Structure

- Incident linkage (multiple incidents attached to one problem; parent problem ticket)
- Known-error marking surfaced to the service desk (in-product state, KB articles, or a KEDB — implementations vary)
- CI/CMDB anchoring for diagnosis context (affected CIs, dependency/impact analysis)
- Priority model from impact × urgency (impact often counted in users and CIs affected)
- Change/release association for the permanent fix
- Problem queue with assignment/routing; problem templates; notifications/announcements to prevent duplicate incident reports
- Closure review; recurrence-focused metrics and reporting

### Level 2 — Variant / Optional Structure

- Proactive problem management (detection from trends, monitoring, capacity data before incidents occur) — common in mature products; reactive core predates it
- AI problem prediction / incident clustering / smart technician assignment
- RCA frameworks productized as structured workflows (five whys, fishbone) — methodology is user practice
- Standalone vs ITSM-suite-module packaging (in the sampled market, problem management nearly always ships as a module of an ITSM/ticketing product; a true standalone "problem-management-only" product is rare)
- DevOps blending (problem management fused with incident response and blameless postmortems, rather than a separate siloed team)
- MSP/cross-customer problem management

### Level 3 — Vendor-specific (Research Notes only)

- ManageEngine Zia problem prediction + intelligent technician assignment; organization-wide announcement banners
- Freshservice Freddy AI capabilities; KEDB surfaced as a named object; closure risk analysis step
- Atlassian blameless-postmortem-as-bridge positioning; "corrective actions tracked through to completion"
- ServiceNow state models — NOT captured (source unreachable); no claims made

## Vendor-specific / Rejected Findings

- **Rejected: "Problem management = an RCA methodology toolbox."** Five whys, fishbone, Kepner-Tregoe etc. are user methods that some products productize as workflow templates; the Type requires a recorded cause determination, not any specific technique.
- **Rejected: "A standalone known-error database is definitional."** The definitional layer is the known-error *state* (documented root cause + workaround attached to the problem). Whether it materializes as a status field, KB articles, or a dedicated KEDB surface is implementation.
- **Rejected: "Proactive problem management is definitional."** The reactive loop (recurring incidents → cause → fix) is the historical core; proactive detection is a common modern capability. Older/paper-era practice satisfies the core reactively.
- **Rejected: "A problem must have multiple incidents."** ITIL's own definition admits "cause or potential cause" (including potential/preventive problems), and major-incident problems exist (one incident can spawn a problem investigation). Multiplicity is the typical trigger, not the invariant.
- **Rejected: "Every problem's fix goes through change management."** In DevOps-flavored organizations the fix may be handled inside the team without a formal change record; the constant is that the problem is driven to a recorded disposition addressing the cause. "Commonly via change" is the calibrated phrasing.
- **Not claimed (unreachable evidence):** any ServiceNow-specific structure, any product's exact state names/labels, any numeric SLA or aging defaults.

## Boundary Findings

- **vs Incident Management (processed)** — the sharpest and pre-hung seam. The incident record answers "what is disrupted and how do we restore service"; its resolution is deliberately restoration-only (the incident pass quotes Atlassian: "only those tasks required to mitigate impact and restore functionality"). The problem record answers "why did this happen and how do we make it stop"; its closure requires the cause to be addressed. Atlassian's own seam quote: "rolling back a recently deployed [change] may get the service operating again and end the incident, but the underlying problem remains." One incident can close while its problem stays open; one problem explains multiple incidents. Both passes agree: keep-both, upstream/downstream siblings. **CONFIRMED from this side.**
- **vs IT Change Management (processed)** — the change record governs an authorized modification to the IT environment; the problem record holds a cause and drives its elimination. The permanent fix for a problem is *commonly executed as a change* (problem→change chaining documented in Freshservice and ManageEngine; pre-hung by the change pass), but the objects, loops, and goals differ: diagnosis loop vs modification-governance loop. The change pass's expectation is ratified from this side.
- **vs Ticketing System (processed)** — a problem is a specialization of the ticket: it adds cause semantics, the investigation loop, the known-error layer, and the incident-population linkage on top of generic demand-processing machinery. The ticketing pass already noted record specializations are consistent.
- **vs IT Service Management / ITSM (unprocessed)** — problem management is one governed practice/module inside the ITSM suite (module packaging observed in all sampled products). Expect the same suite-vs-practice seam the change pass handled; counterparty flag for the ITSM pass.
- **vs CMDB (processed)** — the CMDB is the record of what exists; problem investigation consumes CIs (affected CIs, dependency/impact context) and problem records may feed configuration hygiene. Neither is the other: record vs diagnosis loop.
- **vs AIOps (processed)** — machine analysis over the operational signal stream; its correlated-signal output feeds problem identification (incident clustering ≈ problem candidates), but its unit is the signal, not the managed cause record.
- **vs Bug Tracking System (§12, unprocessed)** — expectation: a bug is a software defect tracked to a code fix; a problem is an IT-operational cause of service disruptions whose disposition may be workaround, configuration fix, or change. In dev-centric organizations the same investigation may produce either object; the seam is the unit of record and the disposition semantics. Flag for the bug-tracking pass.
- **vs Error Tracking Platform (§12, unprocessed)** — expectation: aggregated software errors are a *signal input* that can trigger problems/incidents, not the cause record itself. Flag for the error-tracking pass.
- **vs Knowledge Management (inside ITSM suites)** — workaround articles published to the KB are the *output* of the known-error layer consumed by the service desk; knowledge management is the publication surface, not the diagnosis loop. Packaging overlap, not an alias.
- **vs Vulnerability Management (§15)** — security weaknesses have their own lifecycle (detection→remediation of the weakness); a problem may be raised when a vulnerability causes incidents, but the objects and rules differ. Name-adjacent only.
- **Taxonomy check:** the leaf is a legitimate standalone practice Type — a distinct object (problem record), distinct loop (root-cause elimination), distinct users (problem manager + specialist investigators). Not an Alias, not a Capability. The near-total module packaging (inside ITSM suites) is a market observation recorded under Variants, not an alias problem. No directory change needed.

## Historical / Market-Sample Check

- **Paper-era / ITIL-classical form:** a problem log (register of suspected causes), linked incident references, investigation notes, a root-cause memo, workaround circulated to the service desk, a fix request handed to change control, closure with the incident population referenced. Satisfies all three L0 legs with zero software — the definition holds for the pre-digital practice.
- **Early ITIL-tool era (2000s):** problem tickets with status, known-error flags, KEDB tables — same core, no AI/proactive machinery.
- **Modern SaaS + AI era:** problem prediction, clustering, automated routing — same core plus optional layers.
- The definition deliberately names no RCA technique, no specific state labels, no specific packaging, and does not require proactive detection or AI — so older, regional, open-source, and DevOps-blended realizations all fit.

## Uncertainties

1. **Enterprise-pole product evidence (ServiceNow) not captured** — the market leader's exact problem-record mechanics, state names, and KEDB handling are unverified. All enterprise-specific mechanics are excluded from the final document; cross-product claims rest on the three captured products.
2. **Open-source pole (iTop, GLPI) not captured** — their explicit Problem/KnownError object models would have strengthened the "one Type across packaging poles" claim; held as an uncertainty rather than asserted.
3. **Exact state labels** vary by product (e.g., known error as a status vs a derived record) — the final document states the conceptual lifecycle without claiming specific labels.
4. **Proactive detection depth** — AI prediction was observed in 2/3 sampled products; its universality across the market is unverified and it is held at the Optional tier.

## Final Synthesis

An **IT Problem Management** application is the IT organization's system of record for the *causes behind incidents*: a persistent, identified **problem record** (suspected/confirmed cause — or potential cause — of one or more incidents, distinct from the incident records it explains) is **worked through a root-cause investigation loop** (incidents linked as evidence, configuration context consulted, cause determined and recorded) and **driven to a cause-directed disposition** (workaround documented as the known-error state to reduce ongoing impact, permanent resolution pursued — commonly through change management — and closure tied back to the incident population the problem explains). Reactive (from recurring incidents) is the core; proactive (from trends and monitoring) is the common modern extension; RCA techniques, KEDB packaging, AI prediction, and suite embedding are variant/optional layers. The Type sits between Incident Management (which supplies the evidence and hands over post-incident output) and IT Change Management (which commonly executes the permanent fix), and is usually packaged as a module of an ITSM suite.
