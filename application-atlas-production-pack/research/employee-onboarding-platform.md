# Research Notes — Employee Onboarding Platform

Research date: 2026-09-06
Slug: employee-onboarding-platform
Directory leaf: Employee Onboarding Platform (§09 HR, Workforce & Talent)

## Research Goal

Understand what an Employee Onboarding Platform actually is as an Application Type: what central record it manages, when the process begins and ends, who performs the work, how tasks are structured and tracked, how the new hire participates, how the capability is packaged in the market, and where its boundary lies against ATS, HRIS, offboarding platforms, learning platforms, IT provisioning, employee-experience platforms, and the identically named Customer Onboarding Platform.

## Initial Boundary (working hypothesis before research)

- Core guess: software that turns an employee's joining into a managed, tracked process — a per-new-hire case/checklist running from offer acceptance through pre-boarding, day one, and early tenure, fanned out across HR, manager, IT, payroll, and the new hire.
- Likely confusions:
  - ATS (recruiting ends → onboarding begins; offer-acceptance seam)
  - HRIS (system of record vs process layer; onboarding often bundled inside HRIS)
  - Employee Offboarding Platform (mirror sibling; usually the same product)
  - Corporate LMS / Employee Learning Platform (training tasks vs training system)
  - IT provisioning / IAM joiner automation (coordinating account creation vs executing it)
  - Customer Onboarding Platform (§07 sibling with the same name, different subject)
  - Employee Experience Platform (broader consolidation of workforce-experience domains)
- Unknowns: does the platform create the employment record or presuppose it? How far does "onboarding" extend (day one only? 30-60-90 days?)? Is there a pure-play standalone category? How region-specific are the compliance steps?

## Research Questions

1. What is the central record? When is it created and from what trigger (offer accepted, candidate→employee conversion, manual entry)?
2. What is the task model — templates, steps, owners, deadlines? What step content types exist?
3. What is the time anchor (start date as process clock; pre-boarding window; day one; early tenure)?
4. What recurring task categories appear (record creation, paperwork/e-signature, compliance forms, IT accounts, equipment, workplace, welcome/orientation, buddy, meetings, training)?
5. What does the new hire do themselves (account creation, profile, documents, signatures, hardware choice, confirmations)?
6. What roles and surfaces exist (HR admin, manager, IT, other functions, new hire)?
7. Does the platform own the employment record and payroll, or run beside/above them?
8. How is the capability packaged (HRIS module, journey platform, suite feature, orchestration layer)?
9. Which parts are region- or segment-specific (US I-9/E-Verify/tax withholding; EU social-security/tax-ID/student enrollment; frontline no-login)?
10. Where is the boundary against ATS, HRIS, offboarding, LMS, IT provisioning, EX platforms, and customer onboarding?

## Representative Products

Selection rationale: market representation + documentation completeness + different product philosophies (HRIS-native wizard, journey platform between ATS and HRIS, frontline-first suite, enterprise experience orchestration) + different customer tiers (SMB → mid-market → enterprise).

| Product | Category / philosophy | Tier of evidence |
|---|---|---|
| Personio | European SMB/mid-market core HR; onboarding as steps/groups/templates workflows on the employee record | Tier 1 (Help Center, server-rendered) |
| GoCo | US SMB HRIS; onboarding as "Hiring Workflows" + Hiring/Onboarding Wizard with embedded compliance | Tier 1 (Help Center, server-rendered) |
| Click Boarding | Standalone employee-transition journey platform positioned "between ATS and HRIS"; mid-market/enterprise, high-turnover | Tier 2 (product pages + FAQ) |
| HR Cloud | HR suite with dedicated Onboard product; "onboarding layer" running above external payroll/HRIS; frontline/industry emphasis | Tier 2 (product page + FAQ) |
| Enboarder | Enterprise "journey orchestration / AI orchestration layer" above the HR and IT stack; experience-first | Tier 2 (product pages) |

Products not directly researched (previous sibling-leaf runs found them JS shells or login walls; not retried): Workday, SAP SuccessFactors, ServiceNow, Rippling, HiBob, BambooHR help center.

## Sources

- Personio Help Center — "Create onboarding and offboarding workflows": https://support.personio.de/hc/en-us/articles/115002529589-Create-onboarding-and-offboarding-workflows
- Personio Help Center — "Common onboarding templates and steps": https://support.personio.de/hc/en-us/articles/115002474325-Best-Practice-Onboarding-Templates-and-Steps
- GoCo Help Center — "What are Hiring Workflows and how do I customize them?": https://help.goco.io/en/hiring-workflows
- GoCo Help Center (index; workflows/documents/payroll/benefits sections): https://help.goco.io/en/
- Click Boarding — "HR Employee Onboarding Software": https://www.clickboarding.com/platform/onboarding/ (plus site nav: Preboarding / Onboarding / Offboarding pillars)
- HR Cloud — "Employee Onboarding Software": https://www.hrcloud.com/employee-onboarding-software
- Enboarder — root / platform / solutions pages: https://enboarder.com/ (Preboarding & Compliance, Employee Onboarding, Frontline Onboarding, Employee Transitions, Offboarding, New Hire Ramp Plans, New Hire Learning)
- Sibling research (context, not primary evidence): research/employee-offboarding-platform.md (2026-09-06)

## Product Observations

### Product A — Personio (evidence layer A; Tier 1)

- Onboarding is implemented as **workflows** composed of **steps**, **groups**, and **templates** (Help Center, Tier 1).
  - **Step** = an action or task an employee or team must complete; steps are built once and reused across templates. Three step types: general step (with item types: text information, document for download, employee attribute, profile picture, checkbox, fill text field, enter URL, upload document), **email action** (send manually / on due date / when previous steps are completed), **email invitation** (welcome email to new joiners).
  - **Group** = responsibility group (e.g., "HR team", "IT team"); all members receive the task notification on their homepage, but only one member needs to complete it.
  - **Template** = ordered set of steps, each with a responsible person/group and a deadline ("the deadline triggers reminders and tasks"); different templates per employment type (permanent employees vs interns/working students).
- **Trigger from recruiting**: templates can be assigned directly "when employees have been hired from Recruiting (when a candidate profile is converted to an employee profile)".
- **Email invitation step** (new-hire welcome): selectable sections — create-your-account (prompts the new joiner to create their Personio account and begin setting up their employee profile), workplace location (address + map + directions), meet your team (manager and peers overview), custom section (with contact person). Some sections are locked/mandatory.
- **Documented best-practice permanent-employee template** (task taxonomy in the vendor's own example):
  - HR team — create employee file: employee attributes (status, hire date, contract end date, supervisor, probation length, weekly hours), work-schedule and time-off-policy checkboxes, upload work contract
  - HR team — invite new employee: create/record email account, send login invitation
  - HR team — welcome email to all active employees (announcing the new colleague, with attribute variables and profile picture)
  - Supervisor — set up workplace: assign workplace, issue keys/entry cards, set up workspace
  - IT team — create accounts: email account, Personio account (checkboxes)
  - Supervisor — welcome letter (personal greeting)
  - Employee — submit documents: signed work contract, confidentiality agreement (uploaded and linked to document categories)
  - Employee — choose hardware (laptop model checkboxes); Supervisor — order hardware
  - HR team — 1st workday: handover document + information brochure (download + confirmation checkboxes)
  - Supervisor — feedback meeting: make appointment for first feedback meeting
  - Employee — check all functions: verify drive access, database, email, printer/scanner, phone (with a call test)
  - Employee — safety briefing: download evacuation plan, confirm understanding
  - Employee — fill in profile: birthday, nationality, address, phone numbers, tax identification number, social security number, health insurance type/provider, emergency contacts
  - Interns/working-students variant adds: upload confirmation of enrollment; time-tracking instruction email
- **Permissions**: creating workflows requires an Account Configuration > On/Off-boarding permission; assigning a step grants the assignee **limited extra access** (view/update data tied to that step, open the employee's profile header) even when their usual role permissions would not allow it.
- Related surfaces documented in the section: Automations area (monitoring workflows), electronic signature requests on employee documents, email templates.
- Offboarding runs on the same machinery (steps/groups/templates, deadline anchoring before/after the last working day) — see sibling research notes for detail.

### Product B — GoCo (evidence layer A; Tier 1)

- The onboarding capability is named **"Hiring Workflows"**: "a template that you can customize for your different employee types, such as an employee vs. a contractor... a series of tasks or items to be completed by the HR Admin (the hiring process) and the new hire (the onboarding process)".
- Operates **with the Hiring and Onboarding Wizard**: the admin enters the hire; the new hire completes their onboarding through the wizard. One-off tasks or full workflows can be added before/after the employee is onboarded/hired; a separate workflow (e.g., a New Hire Training workflow) can be embedded to auto-start when onboarding completes.
- **Hiring portion (admin)**: basic info (work email, phones, location, division, department), custom fields, compensation (job title, employment type, wage type/rate, stock options), work groups, labor allocations, offer letter template, documents, review settings (state tax withholdings, payment method collection), **invite email or text message** with dynamic variable fields and attachments.
- **Onboarding portion (new hire)**: personal info (name, legal sex/gender identity/pronouns with required/optional/hidden controls), contact info, emergency contacts, additional custom fields, **tax withholding (federal/state)**, **payment information**, **employment eligibility (I-9)**, documents.
- **Customization model**: templates editable/duplicable/archivable; each task optionally customizable or locked; "Reset & Publish" can push template edits onto already-active workflow instances (hiring workflows only).
- **Oversight**: a Workflows overview screen showing all new hires and where they are in the hiring/onboarding process; "Active Workflows" tab filterable by workflow and employee progress.
- Default **"Existing Employee Hiring Workflow"** — a simplified variant for current employees being added during implementation (skips data the company already has; archived after implementation).
- Suite context: documents ("Magic Documents") with e-signature; benefits enrollment, payroll, time tracking as sibling suite modules; E-Verify and background-check (Checkr) integrations listed in the marketplace; onboarding invite by email or SMS.

### Product C — Click Boarding (evidence layer A for its own claims; Tier 2)

- Positioning: "HR Employee Onboarding Software"; the platform "neatly slots between ATS and HRIS"; "purpose-built for mid-market and enterprise teams and high-turnover needs".
- Pillars: **Preboarding** ("start your candidate's transition... digital engagement that sets them up for a better day one"), **Onboarding** ("deliver top-notch, fully-guided employee experiences... nail 90-day retention"), Offboarding, plus Employee Retention (pulse checks, predictive indicators), HR Activities (drag-and-drop workflows), M&A.
- Onboarding claims (Tier 2): "easy-to-use workflow builder allows flexibility to cater steps and content by role, function"; "administer new hire activities for long-term success — customized workflows that enforce company goals, culture, and tools for success... integrated into Microsoft Teams"; "facilitate early engagement... personalized experiences to build a sense of belonging... predictive indicators help you identify who's taking off vs. who's struggling"; crossboarding (internal transitions) and reboarding supported.
- Standard capabilities named on the page: "Standard eSignature, I-9 verification, tax wizard, email builder, AI assistant, MS Teams integration".
- FAQ (vendor-claimed capability set): onboarding automation spans "I-9 verification to tax forms, uniform orders, getting to know your team, and much more"; preboarding engages new hires before day one to stop "new hire ghosting"/no-shows; surveys and structured check-ins support early engagement.
- Integration claims: large integration list across ATS and HRIS/payroll vendors (marketing-level).

### Product D — HR Cloud (evidence layer A for its own claims; Tier 2)

- Positioning: "The AI Onboarding Layer for the Employee Lifecycle" — "from preboarding to offboarding, HR Cloud sits above your HR and payroll stack to coordinate forms, compliance, tasks, and cross-functional employee journeys"; "Your payroll remains the system of record."
- Journey stages presented: 01 Preboarding, 02 Day One Experience, 03 Forms & e-sign, 04 Automated I-9 & E-Verify, 05 Tasks & reminders, 06 Transitions.
- Preboarding: "branded new-hire portal", "documents before day one", "no company email required" — mobile-first for hourly and mid-market new hires.
- Data flow framing: "new-hire data syncs automatically" from the payroll/HRIS system of record; "documents return to the right record"; the platform is presented as the "employee experience layer" with the outcome "forms signed, I-9 complete, ready for Day 1".
- FAQ definition (vendor's own Type definition): "Employee onboarding software is a platform that automates the process of bringing a new hire from offer acceptance to productive work. It handles document collection, I-9 and E-Verify compliance, e-signatures, role-based task assignments, and progress tracking."
- Buyer guidance (vendor's stated differentiators): native payroll integration; built-in I-9/E-Verify with audit-ready trails; mobile-first access for non-desk workers; role-based workflow configuration HR can update without IT; completion-rate dashboards by department, location, and manager; SMS communication for frontline.
- **Maya** (vendor-specific): an AI onboarding agent that reaches new hires via SMS on any phone — "no app download, no portal login, just a text message with the next task" — aimed at frontline/high-volume teams (healthcare, retail, construction).
- Industry framing: healthcare (credential tracking, license expiration reminders), manufacturing (safety/equipment/plant-specific steps), construction (no desk/company email), retail & hospitality (seasonal high-volume, reusable workflows, local manager tasks).
- Offboarding is the named mirror module (exit checklists with owner/deadline tasks — documented in the sibling leaf's research).

### Product E — Enboarder (evidence layer A for its own claims; Tier 2)

- Positioning: "The AI Orchestration Layer for the Employee Lifecycle" — "sits above your HR and IT stack to orchestrate complex, cross-functional employee journeys"; "acts as a system of action above your existing HR stack".
- Journey scope: onboarding, internal mobility, parental leave, offboarding, M&A, reorganization — "personalized by geography, business unit, role, stakeholder, and employee".
- Preboarding & Compliance: "offer letter to day one readiness".
- Frontline: "mobile-first, no-login experiences" — "SMS and WhatsApp delivery", "no passwords, portals, or apps needed", multilingual support.
- Enablement layer (adjacent capability set): role-based enablement; "agentic, personalized 30-60-90 plans for each new hire"; new-hire learning via "drip-feed LMS content & assess new hire knowledge".
- AI: embedded AI assistants (conversational guidance grounded in company content, "reduce HR tickets"), AI agents that "create 30-60-90 plans", "coordinate stakeholders", monitor engagement signals.
- Stakeholder framing: HR teams, IT, managers, buddies named as participants; enterprise trust framing (SOC 2 / GDPR / ISO 27001, regional login instances).

## Cross-product Comparison

| Dimension | Personio | GoCo | Click Boarding | HR Cloud | Enboarder | Interpretation |
|---|---|---|---|---|---|---|
| Trigger / entry point | Candidate profile → employee profile conversion from Recruiting; template assigned | Hire entered by admin → Hiring/Onboarding Wizard starts | New-hire data from the ATS ("slots between ATS and HRIS") | Accepted offer; "new-hire data syncs automatically" from payroll/HRIS | HRIS-connected journeys (preboarding from offer) | **Shared: the process starts at the hiring event (offer accepted / hire recorded), before the start date** |
| Central record | Onboarding workflow assigned to the employee's profile | Workflow instance per new hire | Guided journey per new hire | New-hire portal + workflow record | Journey per new hire | **Shared: a per-new-hire process record with observable state** |
| Time anchor | Per-step deadlines set in the template ("the deadline triggers reminders and tasks") | Tasks before/after onboarding or hire | Preboarding → day one → 90-day retention framing | Preboarding → Day One Experience → tasks & reminders → transitions | Offer letter → day one → 30-60-90 ramp | **Shared: the employment start date is the process clock; a pre-start window exists** |
| Template model | Templates per employment type (permanent vs working students) | Templates per employee type (employee vs contractor), per department (paid tier), embeddable sub-workflows | "Steps and content by role, function, you name it" | Role/location/workflow configuration; reusable workflows for seasonal volume | Personalized by geography, business unit, role, stakeholder | **Shared: reusable templates conditioned on worker/role attributes** (B) |
| Task fan-out | Groups (HR/IT) + responsible persons (supervisor, employee); one member completes for the group | HR admin (hiring) + new hire (onboarding); embedded workflows auto-start | HR & TA teams; "new hire activities" | HR, managers, cross-functional tasks & reminders | HR, IT, managers, buddies; AI agents "coordinate stakeholders" | **Shared: cross-functional owner-assigned tasks; the new hire is one of the workers** |
| New-hire participation | Email invitation → account creation → profile completion (attributes, documents, hardware choice, confirmations) | Wizard completion: personal info, contacts, tax withholding, payment, I-9, documents | Guided experiences; Teams delivery | Branded mobile portal; documents before day one; no company email needed | Mobile no-login journeys; SMS/WhatsApp; AI assistant Q&A | **Shared: the new hire actively completes their own steps before day one** (B) |
| Paperwork & compliance | Document upload/download steps linked to document categories; e-signature as adjacent feature; EU attributes (tax ID, social security, health insurance, student enrollment) | Federal/state tax withholding, payment info, I-9, "Magic Documents" with signature | eSignature, I-9 verification, tax wizard | Forms & e-sign; automated I-9 & E-Verify; credential tracking (healthcare) | Preboarding compliance (offer letter to day one) | **Shared: signature-ready document flows; compliance content is region-specific** (B) |
| IT / equipment / workplace | IT team: create accounts (checkboxes); supervisor: workplace, keys, workspace; employee: choose hardware, verify functions | Suite-adjacent (task level; provisioning not documented) | Uniform orders named in FAQ | Equipment handoffs; site-ready framing | Coordination with IT systems via integrations (orchestration claim) | **Shared: IT accounts/equipment appear as assigned tasks**; native provisioning execution evidenced nowhere in sample (B, with E claiming integration orchestration at marketing level) |
| Welcome & socialization | Welcome email to all employees; email invitation with "meet your team"; welcome letter from supervisor | Customizable invite email/text with variables | Culture content, sense of belonging, check-ins | Branded welcome, day-one experience | Team/buddy elements; AI guidance | **Common: welcome communications and team introduction as built-in step types** (B) |
| Training / ramp | Not in core workflow (suite has separate learning adjacencies); time-tracking instruction email for students | Embedded "New Hire Training" workflow auto-starts after onboarding | "New hire activities for long-term success"; 90-day framing | Industry training steps (safety) | 30-60-90 ramp plans; drip-fed LMS content | **Common-to-optional: training/ramp extension; depth varies strongly** (B) |
| Payroll / record stance | HRIS is the record; workflows live on employee profiles | Payroll/benefits native in the same suite | Syncs HRIS | "Your payroll remains the system of record"; runs alongside ADP/UKG/Workday | "Sits above your HR stack"; "system of action" | **Shared: employment record and pay remain in the HRIS/payroll systems; onboarding is the process layer** (B) |
| Oversight | Automations area (workflow widgets) | Workflows overview; Active Workflows filtered by progress | Predictive indicators (who's thriving vs struggling) | Completion-rate dashboards by dept/location/manager; compliance visibility | Journey dashboards; engagement signals | **Shared: in-flight oversight surface over all onboarding cases** (B) |
| Variant journeys on same machinery | Offboarding; employment-type variants | Contractor vs employee; existing-employee variant; rehire | Crossboarding, reboarding, M&A | Offboarding mirror module | Transitions, leave, M&A, reorganization | **Shared: onboarding shares its machinery with sibling lifecycle journeys** (B) |
| Packaging | Core HR (HRIS) module | SMB HRIS feature | Standalone journey platform between ATS & HRIS | Suite product ("Onboard") + modular add-ons | Enterprise orchestration layer | **No sampled vendor sells onboarding only as a pure-play point tool; every implementation is a module/layer of a wider product** |

## Canonical Model (abstraction ladder)

### L0 — Defining Invariant

The smallest structure without which the product stops being an onboarding platform:

```text
Joining of an identified new hire recorded as a managed process
└── anchored on the employment start (day one as the process clock)
    └── a tracked, owner-assigned set of setup/orientation tasks
        └── tracked to completion around the start date
```

Four properties:

1. **Joining-as-process**: a per-new-hire onboarding case/workflow exists as a managed object, initiated from a hiring event (offer accepted / hire recorded), not just a record.
2. **Start-date anchor**: task timing is organized relative to the first day of employment — before it (pre-boarding), on it, and in the early tenure after it.
3. **Owner-assigned task set**: the work is decomposed into tasks assigned to specific people/functions (HR, manager, IT, other teams) **and to the new hire personally**.
4. **Completion tracking with oversight**: the process has observable state (open/completed/overdue) that the organization oversees, so steps are not missed.

Remove any one: without 1 it's just an HRIS new-hire record; without 2 it's generic task management; without 3 it's a static printed checklist; without 4 it's an email thread. Historical check (§24-style): a paper-era onboarding pack (signed contract in a file, first-day schedule, desk and keys arranged by the supervisor, orientation by HR) satisfies 1–4; a legacy HRIS new-hire checklist satisfies 1–4; therefore portals, e-signature, mobile apps, SMS reach, I-9/E-Verify, tax wizards, 30-60-90 plans, and AI assistance are not definitional — they are modern implementations layered on the same core.

### L1 — Common Mature Structure (evidence layer B across the sample)

- Reusable onboarding templates/workflows, conditioned on employment type, role, department, location, or geography
- Recurring task categories:
  - employee record/data setup (attributes from the contract: dates, supervisor, schedule, compensation-adjacent fields)
  - document generation, e-signature, collection, and storage (contracts, confidentiality agreements, policy acknowledgements)
  - region-specific compliance forms (US: I-9/E-Verify, federal/state tax withholding, payment setup; EU-style: tax ID, social security, health insurance, student enrollment confirmation)
  - IT accounts and equipment provisioning (as assigned tasks: email account, tool accounts, hardware choice/order, access checks)
  - workplace/workspace preparation (desk, keys/badges)
  - welcome communications (new-hire invitation with account creation; company-wide welcome announcement; team introduction)
  - orientation content (first-day information, safety briefing, handbooks)
  - early check-ins/feedback meetings, buddy/welcome contact
  - training kickoff (as embedded or adjacent workflows)
- Deadline-based scheduling relative to the start date, with reminders and automated chasing
- A new-hire-facing journey surface: account creation, profile completion, document upload/signature, confirmations — usable before day one, often without a corporate email or login
- Cross-functional fan-out with scoped access (task performers can see the data their task needs; group-assigned tasks complete when any member finishes)
- Oversight surface: all onboarding cases in flight, per-hire progress, overdue items
- Integration posture: new-hire data in from the ATS/HRIS/payroll system of record; signed documents and completed data back to it

### L2 — Variant / Optional Structure

- Packaging: HRIS-embedded module (most common) vs standalone journey platform between ATS and HRIS vs suite product for frontline/industry segments vs enterprise "experience/orchestration layer" above the HR+IT stack
- Frontline/deskless reach: SMS/WhatsApp delivery, no-login journeys, no corporate email required
- Regional compliance packs: US (I-9, E-Verify, W-4-style withholding, state variations) vs EU-style (tax ID, social security, health insurance, works documents); healthcare credential/license tracking
- Engagement/retention extensions: pulse checks, predictive indicators, structured 90-day retention programs
- Enablement/ramp extensions: 30-60-90 day plans, role-based enablement, drip-fed LMS content and knowledge assessment
- Crossboarding (internal moves), reboarding, M&A mass-boarding on the same machinery
- AI assistance: conversational onboarding assistants, SMS agents, agent-generated ramp plans (current market wave, not definitional)
- Native integration depth: automatic data sync and document write-back vs manual entry; orchestration claims toward IT provisioning

### L3 — Vendor-specific (research notes only)

- Personio: steps/groups/templates machinery; permission-override on step assignment; locked mandatory sections in the email-invitation builder; employment-type templates (working students: enrollment confirmation + attendance email); Automations-area widgets; the German/EU attribute set (tax ID, social security, health insurance) in its best-practice template
- GoCo: "Hiring Workflows" naming; Hiring + Onboarding Wizard split (admin hiring portion vs new-hire onboarding portion); per-task "Required/Optional/Hidden" customization; "Reset & Publish" to apply template edits to active instances; "Existing Employee Hiring Workflow" for implementation migrations; invite by email or SMS with dynamic variables; E-Verify/Checkr marketplace integrations
- Click Boarding: "slots between your ATS and HRIS" positioning; tax wizard; MS Teams delivery of onboarding; predictive engagement indicators; crossboarding/reboarding/M&A pillars
- HR Cloud: "Maya" SMS AI agent for frontline new hires (no app/login); "onboarding layer above payroll" positioning with payroll staying system of record; modular Onboard Suite/Compliance/Maya packaging; credential-expiration tracking for healthcare
- Enboarder: AI Journey Builder; embedded AI assistants and stakeholder-coordinating AI agents; auto-generated 30-60-90 ramp plans; WhatsApp delivery; regional login instances; "system of action" framing
- All retention-percentage / hours-saved / time-reduction figures on vendor pages are marketing claims, not operational facts; none are reproduced in the final document.

## Vendor-specific Findings

See L3 above. Notable single-source items kept out of the canonical document: Personio's permission-override mechanics for step assignees; GoCo's Reset & Publish instance-reset behavior and required/optional/hidden per-field controls; Click Boarding's MS Teams delivery and predictive indicators; HR Cloud's SMS agent; Enboarder's agentic ramp-plan generation.

## Boundary Findings

1. **vs ATS**: the ATS owns candidate → offer; onboarding begins at the hiring event. The seam is explicit in the sample: Personio assigns onboarding templates "when a candidate profile is converted to an employee profile"; Click Boarding positions itself as "slots between your ATS and HRIS"; HR Cloud's FAQ defines onboarding as starting "from offer acceptance". Remove the hiring-event trigger and post-offer task machinery → what remains is a recruiting tool.
2. **vs HRIS (Human Resource Information System)**: the HRIS holds the employee record; onboarding is a process layer that runs on it. The complication is packaging: in the sampled HRIS products (Personio, GoCo) onboarding is natively embedded, while standalone/journey/suite implementations sync with the HRIS as the record. Structural test: remove the orchestrated pre-start task process → what remains is a new-hire record; remove the record and the onboarding case has nothing to anchor on and no destination for its outputs.
3. **vs Employee Offboarding Platform (sibling leaf)**: mirror symmetry confirmed across all five sampled products — every vendor ships onboarding and offboarding as one product on one employee record (Personio On-/Offboarding settings; GoCo workflows + termination guides; Click Boarding pre/on/off pillars; HR Cloud Onboard/Offboard modules; Enboarder onboarding/offboarding/transition journeys). The machinery (templates, owner-assigned steps, deadlines, employee-facing journeys, oversight) is shared; the direction and the anchor differ (start date vs last working day). This strengthens the earlier joint-review flag: candidate shared "employee transition journey" structure with two primary directions.
4. **vs Corporate LMS / Employee Learning Platform**: training appears inside onboarding as a task category (embedded training workflow in GoCo; safety briefing in Personio's template; drip-fed LMS content in Enboarder). The learning platform owns courseware, curricula, and completion records; the onboarding platform owns the joining process. Remove the process/case machinery and pre-start anchoring → what remains is a learning tool.
5. **vs IT provisioning / IAM joiner automation**: in every sampled implementation, account creation and equipment setup appear as tasks assigned to IT/manager (Personio: IT-team checkbox steps; HR Cloud: task-and-reminder framing). Enboarder claims integration-level orchestration toward IT systems (vendor claim, marketing-level). The onboarding platform coordinates the decision and accountability; identity/endpoint systems execute. Remove the employment/joining context and task fan-out → what remains is joiner-leaver automation.
6. **vs Customer Onboarding Platform (§07 sibling)**: identical name, different subject. The customer-side Type orchestrates a customer's adoption of a product/service (accounts, usage, success milestones); this Type orchestrates a person's entry into employment (compliance documents, payroll setup, workplace, team). No shared structure beyond the generic journey/checklist pattern; the directory's §07 vs §09 placement is correct.
7. **vs Employee Experience Platform**: EX platforms consolidate multiple workforce-experience domains (communications, listening, recognition, service) on one employee-facing surface. Onboarding platforms are lifecycle-moment specialists; their employee-facing surfaces exist for the joining window (and sibling transitions), not for everyday experience delivery. Some vendors drift toward EX positioning (Enboarder's experience-first framing, HR Cloud's engagement suite), but the sampled core structures remain onboarding/transition processes.
8. **vs Payroll / Benefits Administration**: onboarding collects tax-withholding, payment, and benefits-election data as steps (GoCo documents this explicitly in the wizard), but pay execution and benefit enrollment administration remain with the owning systems (native in suite products like GoCo; explicitly delegated in HR Cloud's "payroll remains the system of record" stance). Onboarding is the collection-and-coordination moment, not the system of record.
9. **Packaging observation (taxonomy)**: no sampled vendor markets onboarding as a pure-play standalone point product — it always ships inside an HRIS, a journey platform, a suite, or an orchestration layer. The Type is structurally real (the same core model appears across very different packagings) but has no pure-play market anchor; same pattern as the offboarding leaf.

## Uncertainties

- Enterprise HCM (Workday, SAP SuccessFactors, Oracle) and HR-ESM (ServiceNow) onboarding structures could not be verified — help surfaces are JS apps/login walls (consistent with the sibling leaf's findings). Claims about those ecosystems are kept general in the final document.
- Whether any product executes IT provisioning natively (vs delegating to IT or triggering via integrations) is not verifiable from the reachable evidence; Enboarder's orchestration claims are marketing-level.
- Exact start-date-relative scheduling semantics (e.g., "N days before start" rules) are documented only implicitly (Personio: per-step deadlines; Click Boarding/HR Cloud/Enboarder: stage framing). No numeric timing rules are asserted anywhere.
- The extent of benefits-enrollment handling inside onboarding varies by packaging (native in an HRIS suite vs synced for a layer product); not researched deeply.
- AI-assistant/agent capabilities are currently marketing-forward across the sample; operational behavior could not be verified from help documentation for most vendors.

## Final Synthesis

An Employee Onboarding Platform is the process layer for the beginning of an employment relationship. Its defining core is small: a per-new-hire process record created at the hiring event, anchored on the employment start date, that decomposes the joining work into owner-assigned, deadline-tracked tasks — assigned to HR, the manager, IT, other functions, and the new hire personally — and tracks them to completion under HR oversight, before day one and through the early tenure. Around that core, mature products add the same furniture: reusable templates conditioned on worker type and role; the recurring task categories (record setup, documents and e-signature, region-specific compliance forms, IT accounts and equipment, workplace, welcome and orientation, early check-ins, training kickoff); a new-hire-facing journey usable before the first day (portal or no-login mobile); reminders and escalation; an in-flight oversight dashboard; and integration boundaries — the ATS hands over the hire, the HRIS/payroll stays the system of record, IT systems execute provisioning. The market packages this structure as an HRIS module, a journey platform between ATS and HRIS, a frontline-focused suite product, or an enterprise orchestration layer; the Type is defined by the structure, not the packaging. Onboarding and offboarding are directional mirrors of one machinery — a symmetry the market itself confirms by shipping them as one product.
