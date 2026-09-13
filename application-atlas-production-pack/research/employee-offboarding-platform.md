# Research Notes — Employee Offboarding Platform

Research date: 2026-09-06
Slug: employee-offboarding-platform
Directory leaf: Employee Offboarding Platform (§09 HR, Workforce & Talent)

## Research Goal

Understand what an Employee Offboarding Platform actually is as an Application Type: what central objects it manages, what work it coordinates, who performs it, how the process is anchored in time, and where its boundary lies against HRIS termination workflows, Employee Onboarding Platforms, HR case management, IT-driven deprovisioning, and exit-interview/employee-listening software.

## Initial Boundary (working hypothesis before research)

- Core guess: software that turns an employee departure into a managed, tracked process — a case/checklist per departing employee, coordinated across HR, IT, payroll, manager, facilities, anchored on the last working day.
- Likely confusions:
  - HRIS (termination as a record event vs offboarding as an orchestrated process)
  - Employee Onboarding Platform (mirror journey; often the same product)
  - IT/IAM/UEM deprovisioning (executing access removal vs coordinating it)
  - Exit interview / employee listening tools (feedback instrument vs process orchestration)
  - HR Case Management / ESM (service-request framing vs lifecycle-event framing)
- Unknowns: is there a pure-play offboarding product category, or does offboarding always ship embedded in a wider HR platform? What is in scope (access? assets? final pay? alumni?)?

## Research Questions

1. What is the central record? How is a departure initiated and by what data (reason, dates)?
2. What is the task model? Who owns tasks, how are deadlines defined, how is completion tracked?
3. How is the process anchored in time (before/after the last working day)?
4. What task categories appear (assets, access, paperwork, handover, feedback, communications)?
5. Does the platform itself revoke access / compute final pay, or does it delegate/integrate?
6. What roles and surfaces exist (HR admin, task performers, manager, departing employee)?
7. How do exit reasons (resignation / dismissal / retirement / transfer) shape the process?
8. What happens after the last day (records retention, alumni, rehire)?
9. How is the capability packaged in the market (standalone, HRIS module, journey suite)?
10. Where is the boundary against onboarding, HRIS, IAM/UEM, HR service delivery, and exit-survey tools?

## Representative Products

Selection rationale: market representation + documentation completeness + different product philosophies + different customer tiers/packaging.

| Product | Category / philosophy | Tier of evidence |
|---|---|---|
| Personio | European SMB/mid-market core HR (HRIS) with onboarding/offboarding workflows | Tier 1 (Help Center articles, server-rendered) |
| Click Boarding | Standalone employee-transition journey platform (pre/on/offboarding), slots between ATS and HRIS | Tier 2 (product pages + FAQs) |
| HR Cloud | HR suite with a dedicated offboarding feature; multi-location / frontline emphasis; runs alongside external payroll | Tier 2 (dedicated offboarding product page + FAQs) |
| Qualtrics (Exit Interviews) | Boundary probe: exit-feedback/listening instrument, not process orchestration | Tier 2 (product page) |

Products attempted but not reachable (see Source-access Limitation): Rippling (help center is a JS shell; blog URLs 404), SAP SuccessFactors (SAP Help Portal JS shell, 3 attempts incl. legacy viewer), ServiceNow docs (JS app), HiBob help (login wall), BambooHR help (401), Enboarder (404).

## Sources

- Personio — "Offboarding: Should You Have a Process In Place?" (HR Lexicon): https://www.personio.com/hr-lexicon/offboarding/
- Personio Help Center — "Best Practice: Offboarding Templates and Steps": https://support.personio.de/hc/en-us/articles/115002543825-Best-Practice-Offboarding-Templates-and-Steps
- Personio Help Center — "Create onboarding and offboarding workflows": https://support.personio.de/hc/en-us/articles/115002529589-Create-onboarding-and-offboarding-workflows
- Click Boarding — "Employee Offboarding Software": https://www.clickboarding.com/platform/offboarding/ (plus site nav: preboarding/onboarding/offboarding as platform pillars)
- HR Cloud — "Employee Offboarding Software": https://www.hrcloud.com/employee-offboarding-software
- Qualtrics — "Exit Interview Software": https://www.qualtrics.com/employee-experience/exit-interviews/

## Product Observations

### Product A — Personio (evidence layer A unless noted)

- Offboarding is implemented as **onboarding/offboarding workflows** composed of **steps**, **groups**, and **templates** (Help Center, Tier 1).
  - **Step** = an action/task an employee or team must complete. Three step types: general step (with item types: text information, document for download, employee attribute, profile picture, checkbox, fill text field, enter URL, upload document), **email action** (send manually / on due date / when previous steps are completed), email invitation (onboarding-oriented).
  - **Group** = responsibility group (e.g., HR team, IT team); all members get a task notification on their homepage, but only one member needs to complete the task.
  - **Template** = ordered set of steps with a responsible person/group and a deadline per step; assigned to employees to run their offboarding; different templates for different employment types (e.g., full-time vs working students).
- **Time anchoring**: "Offboarding steps are triggered based on the following deadlines: 'Before termination or the last working day (if set)' or 'After termination or the last working day (if set)'." The last working day is set when terminating the employee in their profile; organization chooses termination date vs contract end date as last working day; steps fall back to the termination date.
- **Best-practice dismissal template steps** (documented example): promote job (HR); offboarding email to the departing employee; move departing employee to a restricted employee role "Offboarding" (access limited to certain sections); create + send employment reference (EU-style reference letter); departing employee downloads personal documents (bulk export); final meeting with supervisor; return of work equipment (employee: mobile phone, laptop, key/chip cards + damage note); close accounts (IT team checkbox); email to IT to collect equipment, auto-sent when previous steps are completed.
- **Exit-reason templates**: best practices give separate templates for dismissal, resignation, and retirement — same step set with timing differences; retirement template drops the employment-reference step.
- **Permissions**: creating workflows requires an account-configuration permission; assigning a step grants the assignee **limited extra access** (view/update data tied to that step, open the profile header) even if their normal role permissions wouldn't allow it. A dedicated restricted employee role gives departing employees limited access during the process.
- **Oversight**: an Automations area with onboarding/offboarding **widgets** showing all employees currently on offboarding paths.
- **Exit survey**: separate Personio Surveys feature can automate offboarding (exit) surveys with participants added at exit (Tier 1 search results).
- HR Lexicon (Tier 2/3, conceptual framing): offboarding defined as disengaging an employee from their position after they decide to leave or their contract is terminated; the "opposite of onboarding"; benefits framing: protect company information (equipment return + access disabling), minimize disruption, feedback, knowledge capture, boomerang likelihood, employer brand. Suggested process steps: plan/checklist, inform colleagues, handover plan, paperwork (resignation/termination letter on file; settle owed money with accounting/finance), retrieve assets + revoke IT access ahead of departure, exit interview, human goodbye.

### Product B — Click Boarding (evidence layer A for its own claims)

- Positions the platform around **employee transitions**: "Preboarding. Onboarding. Offboarding. Crossboarding. M&As. Promotions. — One platform"; "Clients focus on their preboarding, onboarding, or offboarding first — whichever is most impactful; then they expand... It's all standard."
- "Our platform slots between your ATS and HRIS and makes any employee transition easier, whether it's offboarding, preboarding, onboarding, M&A, or something else." (FAQ)
- Offboarding pillar claims (Tier 2, vendor claims): standardized mandatory forms + eSignature + steps "always updated"; "structured employee offboarding processes for every type of exit"; exiting employee feedback; **intra-team notifications for tasks needing completion**; "real-time updates to IT, HR, and managers"; customer testimonial: "Not only does Click Boarding offboard employees through a streamlined, compliant process, but it also removes a user's access to files or data behind the organization's firewall" (testimonial-level claim of access-removal capability).
- Compliance emphasis: state-mandated separation notice requirements (US), I-9 fine framing on the compliance page; "Handle all mandatory forms and processes across your organization — faster and still with empathy."
- Alumni/boomerang framing: "leave a lasting positive impression to encourage more boomerang employees and happy alumni."
- FAQ: offboarding duration shaped by remote/international circumstances, exit interviews, document signatures, COBRA/benefits sign-off, equipment returns (US-specific elements named).

### Product C — HR Cloud (evidence layer A for its own claims)

- Dedicated offboarding product page (Tier 2). Central pitch: "HR Cloud gives every exit one workflow and one owner"; "runs each departure as a checklist rather than a memory exercise."
- Example exit checklist bound to a departing employee (Engineering, last day Aug 15, 0/4 complete): Return company laptop (Manager, Aug 14); Revoke system access (IT, Aug 15); Sign separation agreement (HR, Aug 15); Return building badge (Facilities, Aug 15).
- **Trigger**: "A resignation, termination, retirement or transfer starts the clock. HR Cloud loads the right template — the checklist adapts to the reason"; a **Terminate Employee form and its approval request** is shown as the triggering workflow.
- **Task model**: "Every revocation is a task with an owner and a due date — not an email request"; "IT gets its own tasks, on its own deadline"; "Reminders by email and text, then escalation."
- **Access**: "Access revocation is assigned as a task with an owner and a due date to the team that controls it, typically IT, with reminders and escalation if it's not marked complete" (FAQ) — i.e., the offboarding platform coordinates, the IT function executes.
- **Assets**: "Equipment like laptops and badges is tracked as a task tied to the departing employee's record, with an owner and due date, not a note in an email thread"; "Assets tracked as records."
- **Paperwork**: "Final paperwork, acknowledgements and any required notices are sent, signed and stored inside the same flow, with a timestamp on every signature"; "The exit interview is part of the checklist"; "They keep access long enough to finish."
- **Oversight**: "One dashboard confirms what's still open — which exits are done, which are overdue, and who owns the step that's holding things up — filtered by location, department or date"; progress reports with completion/overdue counts per employee; separate checklists per team (e.g., all-employee, IT, LA/local).
- **Segmentation**: different checklists by role, worker type (hourly vs salaried), or location; targets multi-location organizations, frontline/deskless workforces, lean HR teams, complex multi-stakeholder exits; explicitly not for a 20-person office with three exits a year ("A shared document genuinely works at that size").
- **Record continuity**: "Onboarding and offboarding run on the same employee record... when someone comes back... you rehire onto the record you already have." One record from first day → last day → rehire.
- **Payroll boundary**: "HR Cloud runs the exit itself — the tasks, the owners, the approvals and the signed documents — while your payroll platform stays the system of record for pay and employment data. Nothing migrates." Integrates with ADP, UKG, Workday, Paychex; "What moves between HR Cloud and your payroll platform, and in which direction, depends on the platform and the plan."
- **Frontline reach**: an AI follow-up agent ("Maya") chases incomplete tasks by text message ("no app to install, no portal password"), replies land on the same exit record (vendor-specific).

### Boundary probe — Qualtrics Exit Interviews (evidence layer A for the distinction)

- Exit interview software: HRIS integration triggers an exit survey when a departure is confirmed; survey delivery across channels; analytics (sentiment/themes), routing to action planning, lifecycle analytics.
- No task orchestration: no asset return, no access revocation tasks, no separation paperwork/e-signature, no checklist ownership — its unit of work is feedback collection and analysis, not the wind-down process. Confirms exit-interview tooling is a sibling capability (a task category inside offboarding), not the same Type.

## Cross-product Comparison

| Dimension | Personio | Click Boarding | HR Cloud | Interpretation |
|---|---|---|---|---|
| Central record | Offboarding workflow/template assigned to a departing employee (steps + deadlines) | Structured offboarding workflow per exit type | Exit checklist bound to departing employee's record, one workflow/one owner | **Shared: a per-departure process record anchored on the employee** |
| Time anchor | Steps triggered "Before/After termination or the last working day" | Not stated (implied around the departure) | Checklist deadlines tied to last day (Aug 14/15 example) | **Shared: employment-end date is the process clock** |
| Exit reason drives process | Dismissal / resignation / retirement templates (best practice) | "Structured offboarding processes for every type of exit" | Resignation / termination / retirement / transfer each auto-load their own checklist | **Shared: reason-conditioned templates** (B) |
| Task fan-out | Groups (HR team, IT team) + responsible persons | Intra-team notifications; real-time updates to IT/HR/managers | Tasks with owner + due date to Manager/IT/HR/Facilities | **Shared: cross-functional task assignment with owners** |
| Access revocation | IT-team checkbox step "close accounts"; restricted "Offboarding" employee role for the leaver | Customer testimonial claims access removal behind firewall (testimonial-level) | Task with owner/due date assigned to IT ("the team that controls it"), reminders + escalation | **Shared: coordinated as a tracked task delegated to IT**; native execution not evidenced in sample |
| Asset/equipment return | Return-of-work-equipment step (mobile/laptop/keys + damage) filled by employee; email to IT when previous steps complete | Equipment returns named in FAQ | Assets tracked as tasks/records tied to the employee's record | **Shared: asset return as tracked tasks** |
| Paperwork / e-signature | Document steps, employment reference, document module | Mandatory forms + eSignature, "always updated" | Generated, signed (timestamped), stored in same flow; US separation notices | **Shared: separation paperwork generated/signed/stored** |
| Exit feedback | Separate Surveys feature automates offboarding surveys | Exiting employee feedback in the flow | Exit interview is part of the checklist | **Common: exit feedback as an embedded or adjacent step** (B) |
| Reminders/automation | Deadline triggers reminders and tasks; email actions auto-fire | Automated notifications | Reminders by email/text, then escalation | **Shared: automated chasing** |
| Oversight | Automations widgets (employees on offboarding paths) | Completion-rate claims | Dashboard: done/overdue/owner, filter by location/dept/date; progress reports | **Shared: in-flight oversight surface** |
| Departing employee surface | Offboarding email; restricted role to download documents; employee fills equipment form | Forms/feedback to the exiting employee | Keeps access long enough to finish; signs paperwork; mobile/no-login reach for frontline (vendor-specific SMS agent) | **Shared: the leaver participates in their own exit** |
| System-of-record stance | Termination recorded on employee profile in the HRIS; last-working-day choice (termination vs contract end) | Slots between ATS and HRIS; syncs HRIS | Runs alongside payroll/HRIS; payroll stays system of record; one employee record first day→last day→rehire | **Shared: anchored on the HR employment record; offboarding is the process layer over it** |
| Packaging | Core HR module (on-/offboarding) | One pillar of a journey platform | Feature of an HR suite (dedicated page) | **No sampled vendor sells offboarding purely standalone** |
| Geography/regulation flavor | EU (employment reference / Arbeitszeugnis-style) | US (state separation notices, I-9, COBRA) | US-heavy (I-9 & E-Verify suite context) | Regional compliance packs are variant-level (B/C) |

## Canonical Model (abstraction ladder)

### L0 — Defining Invariant

The smallest structure without which the product stops being an offboarding platform:

```text
Departure of an identified employee recorded as a managed process
└── anchored on the employment end (termination date / last working day)
    └── a tracked, owner-assigned set of wind-down tasks
        └── tracked to completion against the departure
```

Four properties:

1. **Departure-as-process**: a per-employee separation case/checklist exists as a managed object (not just an HR record flag).
2. **Employment-end anchor**: task timing is organized relative to the termination/last working day.
3. **Owner-assigned task set**: the work is decomposed into tasks assigned to specific people/functions with deadlines.
4. **Completion tracking with oversight**: the process has observable state (open/completed/overdue) that HR oversees.

Remove any one: without 1 it's just an HRIS termination event; without 2 it's generic task management; without 3 it's a shared checklist (which vendors themselves name as the thing they replace); without 4 it's an email thread. Historical check (§24-style): a legacy HRIS termination workflow with a printed checklist satisfies 1–4; modern SaaS adds templates, automation, and integrations on top — the definition does not depend on the current SaaS packaging. Phone numbers, SMS chasing, e-signature, alumni portals are not required.

### L1 — Common Mature Structure (evidence layer B across the sample)

- Reusable offboarding templates/workflows, conditioned on exit reason (resignation / dismissal / termination / retirement / transfer) and optionally on employment type / location
- Standard task categories: equipment/asset return; access & account closure (as tasks); separation paperwork generation + e-signature + storage; knowledge/handover & final meeting; exit interview / feedback; final communications; role backfill/promotion action
- Deadline anchoring before/after the last working day; automated reminders and escalation
- Cross-functional fan-out to HR, IT, payroll, manager, facilities, and the departing employee
- Restricted continued access for the departing employee long enough to complete their part; scoped access for task performers
- Oversight surface: in-flight exits, per-employee progress, overdue items
- Integration posture: departure data from the HR record (HRIS), documents/payroll outputs handed to the systems that own them
- Record retention after departure (documents/history kept on the employee record)

### L2 — Variant / Optional Structure

- Packaging: HRIS-embedded module vs journey-platform transition vs suite feature vs (in enterprise HCM/ESM contexts) lifecycle-event/case workflows
- No-login/mobile reach for frontline/deskless workers (SMS chasing)
- Alumni/boomerang programs and rehire onto the same record
- Native HR+IT unification (platform triggers/verifies access removal via integrations) vs pure task delegation
- Regional/regulatory packs: US separation notices/COBRA; EU employment references; final-pay/PTO settlement variance
- Crossboarding (internal transfer) as a sibling journey sharing the machinery
- Exit-feedback analytics depth (adjacent listening products)
- Rehire/boomerang handling

### L3 — Vendor-specific (research notes only)

- Personio: steps/groups/templates permission model; step-permission override; "Offboarding" employee role; flowers-for-retirement template item; Automations widgets; employment-reference document step (EU practice)
- HR Cloud: "Maya" SMS follow-up agent; "one workflow, one owner" positioning; checklist-by-location (e.g., LA); explicit not-a-fit statement for tiny offices
- Click Boarding: "slots between your ATS and HRIS" positioning; transition-pillar packaging (pre/on/off/crossboarding, M&A); US state-separation-notice compliance library claims
- All completion-rate/time-savings figures on vendor pages are marketing claims, not operational facts

## Vendor-specific Findings

See L3 above. Notable: only one product (Personio) documents a permission-override mechanism for task performers (single-source → keep product-specific); only HR Cloud documents SMS escalation and explicit payroll-boundary stance (single-source); Click Boarding's access-removal claim is testimonial-level only.

## Boundary Findings

1. **vs HRIS (Human Resource Information System)**: the HRIS holds the employee record and the termination event; offboarding is the process layer that orchestrates the wind-down. Structural test: remove the orchestrated task process → what remains is an HRIS termination record. Remove the employment record → the offboarding case has nothing to anchor on. In the sample, offboarding always lives on top of an HR record (native in HRIS, or synced with HRIS/payroll for standalone journey platforms).
2. **vs Employee Onboarding Platform (sibling leaf)**: perfect mirror symmetry — same machinery (templates, steps, owners, deadlines, employee-facing journeys), opposite direction (join vs leave). The sample suggests one shared "employee transition/journey" structure with two primary journeys; several vendors ship onboarding+offboarding+crossboarding as one product. Candidate for joint review when Employee Onboarding Platform is processed; documented as related-but-separate leaves for now.
3. **vs IAM / IGA / UEM deprovisioning**: offboarding platforms coordinate the *decision and accountability* (task "revoke access", owner IT, due date); identity/endpoint systems *execute* entitlement removal and device wipe. In the sample, actual revocation execution was never evidenced inside the offboarding platform itself (HR Cloud FAQ explicit: assigned to "the team that controls it"). Remove the employment case and the task fan-out → what remains is access governance/lifecycle automation.
4. **vs HR Case Management / Employee Service Management / ESM**: case management is service-request-shaped (an employee asks for something; a case is triaged and resolved). Offboarding is lifecycle-shaped (the organization initiates a separation; a template fans out). Enterprise HR service delivery suites may model offboarding as lifecycle events/cases — a packaging overlap to note, not a structure identity (not directly researched; enterprise docs unreachable — assertion kept weak).
5. **vs Exit interview / employee listening software** (Qualtrics probe): the survey instrument collects and analyzes departure feedback; it does not own assets, access, paperwork, or task completion. Exit feedback appears inside offboarding as one optional task category, and dedicated listening products integrate with the HRIS-triggered departure event. Distinct Types.
6. **vs Payroll**: final pay/PTO settlement stays with the payroll/finance system of record; offboarding feeds it data (last day, balances context) and tracks the administrative steps. Evidenced by HR Cloud's explicit boundary stance and Personio's finance-team coordination framing.
7. **Packaging observation (taxonomy)**: all three sampled implementations ship offboarding *inside* a wider product (HRIS core HR, journey platform, HR suite); none of the sampled vendors markets a pure-play standalone offboarding platform. The Type is structurally real (shared core model across very different products) but the market has no pure-play anchor — recorded as a boundary issue for STATUS.md.

## Uncertainties

- Enterprise HCM (SAP SuccessFactors, Workday, Oracle) and HR-ESM (ServiceNow) offboarding structures could not be verified — all help surfaces were JS apps or login walls. Claims about those ecosystems are inference from the reachable sample and general market structure, kept weak in the final document.
- Whether any product executes directory-level access revocation natively (vs delegating to IT or triggering via integration) is not verifiable from the reachable evidence; the one access-removal claim found is a customer testimonial, not documentation.
- Precise deadline/reminder mechanics beyond Personio's documented behavior (before/after last-working-day anchoring) are not documented across the sample; no numeric time windows are claimed anywhere.
- Final-pay/benefits handling (e.g., US COBRA) appears only in vendor FAQ/marketing lists; treated as an integration/output boundary, not an in-platform capability.
- The EU employment-reference step (Personio) is regionally specific; whether EU-only markets universally require such steps was not researched.

## Final Synthesis

An Employee Offboarding Platform is the process layer for the end of an employment relationship. Its defining core is small: a per-departure process record bound to an identified employee, anchored on the employment end date, that decomposes the wind-down into owner-assigned, deadline-tracked tasks and tracks them to completion under HR oversight. Around that core, mature products add the same furniture: reason-conditioned templates; the recurring task categories (assets, access closure, separation paperwork + e-signature, handover, exit feedback, communications); automated reminders and escalation; an oversight dashboard; restricted continued access for the leaver; and integration boundaries with the systems that own execution — HRIS as the record of employment, payroll as the owner of final pay, IT/identity systems as the executors of access removal. The market packages this structure as an HRIS module, a journey-platform transition, or a suite feature; the Type is defined by the structure, not by the packaging.
