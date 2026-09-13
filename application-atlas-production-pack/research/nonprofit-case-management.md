# Research Notes — Nonprofit Case Management

Research date: 2026-09-08
Slug: `nonprofit-case-management`
Directory leaf: "Nonprofit Case Management" (§25 Nonprofit, Membership & Religious Organizations)

## Research Goal

Understand Nonprofit Case Management as an Application Type: what records exist inside it (clients/participants, cases, programs, services, notes, referrals), how a person who needs help moves from intake through service delivery to case closure, which roles participate (caseworker, supervisor, program manager, admin), which rules govern behavior (confidentiality, documentation, funder accountability), and where the boundary lies against Beneficiary Management, Social Services / Public Sector Case Management, Child Welfare Management, Nonprofit CRM / Donor Management, Nonprofit Program Management, and Monitoring & Evaluation platforms.

This pass also carries three joint-review obligations recorded by earlier passes:

1. **beneficiary-management (§25, processed)** — flagged that the products implementing beneficiary management all market themselves as "case management" (Apricot "case management at scale", ActivityInfo case-management use case, CommCare case-management platform) and held the boundary on a center-of-gravity test (population registry + what was delivered vs. a bounded casework episode driven by an accountable caseworker to closure). This pass must ratify or reject that boundary from the case-management side.
2. **child-welfare-management (§24, processed)** — flagged that nonprofit case management "shares the casework spine for private delivery agencies" and recommended joint review.
3. **monitoring-evaluation-platform (§25, processed)** — recorded a secondary vendor-drawn seam to nonprofit case management.

## Initial Boundary (hypothesis before research)

- Core hypothesis: software used by private/mission-driven service organizations (nonprofits, charities, community-based organizations) to manage **casework**: a person seeking help enters via intake, is assessed for eligibility/needs, is enrolled in one of the organization's programs/services, and a **case** (episode of service) is opened under an accountable caseworker, who documents contacts and services, makes referrals, and eventually closes the case with a recorded outcome. Funders (grantmakers, government contracts) require documentation and outcome reporting, which shapes the record heavily.
- The operator is an organization, not the state: programs and eligibility are **organization-defined**, and the accountability audience is **funders/grantmakers** rather than statute.
- Likely confusions:
  - Beneficiary Management (§25 sibling; registry vs episode center)
  - Social Services Case Management / Public Sector Case Management (§24 siblings, unprocessed; same spine, government operator/mandate)
  - Child Welfare Management (§24, processed; statutory protection loop)
  - Nonprofit CRM / Donor Management System (money in vs services out)
  - Nonprofit Program Management (§25 sibling, unprocessed; initiatives vs people)
  - Monitoring & Evaluation Platform (§25, processed; results frameworks vs case-level delivery)
  - HR Case Management, Legal Case Management, ITSM incident/ticket — the word "case" in other domains
  - Behavioral health EHR / clinical documentation (clinical pole of the same market)

## Research Questions

1. What is the unit of record — the person, the case, or the enrollment? Which object is the center?
2. How does a person enter (intake, self-registration, referral) and what does entry produce?
3. What is the case lifecycle: intake → assessment → plan → service delivery → referral → review → closure/exit? Who owns it?
4. How do programs and services appear (program enrollment, service transactions, attendance)?
5. What documentation machinery exists (case notes, forms, assessments, documents) and how is it attributed?
6. What funder/grant/compliance reporting machinery exists and how does it shape the record?
7. What access-control machinery is structural (roles, field/record-level visibility, audit, GDPR-style erasure)?
8. What referral machinery exists (internal, external/network) and how does it connect to the case?
9. What client-facing surfaces exist (portals, online forms, messaging, self-booking)?
10. What varies by market segment (behavioral health, homelessness/HMIS, victim services, youth, UK charity vs US human services), customer tier, and product posture?
11. Boundary: what distinguishes this Type from beneficiary management, from social-services case management, from child welfare, from donor CRM, from program management, from M&E?
12. Historical check: would paper-era charity casework still satisfy the definition?

## Representative Products

Selected for market representativeness, documentation accessibility, different product philosophies, and different customer tiers / geographies:

| Product | Philosophy | Segment / tier |
|---|---|---|
| **Apricot (Bonterra / Social Solutions)** | packaged "case management at scale" for nonprofits; funder-compliance emphasis; tiered SaaS | US human-services nonprofits; mid-market to enterprise |
| **Casebook (Casebook PBC)** | modern configurable person-centric SaaS ("designed by case managers for case managers"); spans nonprofit and public sector | US community organizations, schools, public agencies, tribal |
| **CaseWorthy (incl. ClientTrack lineage)** | enterprise multi-program human-services platform; person-centric "whole-person care" + outcome reporting | 1,000+ nonprofits and local/state governments (vendor claim); homelessness/HMIS, workforce, aging, behavioral health verticals |
| **Lamplight Database Systems** | tailored "case management CRM" for small/medium UK charities; light registry + casework + outcome measures | UK charity sector (children & families, homelessness, women's support, refugees, mental health) |

Rejected / not used samples (recorded limitations):

- **Foothold Technology (AWARDS, "human services EHR" posture)** — footholdtechnology.com 403 ×2 (root + /products/awards), abandoned per network rules. The EHR-posture pole is instead covered by CaseWorthy's care-delivery/claims language and the behavioral-health vertical discussion.
- **Penelope (Athena Software)** — Apricot's official FAQ states Social Solutions offered "Apricot, ETO, and Penelope," i.e., same vendor family as Apricot; excluded under the same-vendor sampling rule.
- **extendedReach, Salesforce Nonprofit Cloud case management** — known 403/blocked from sibling passes; not retried.

Cross-references used (Layer A from sibling passes, not re-fetched): CommCare, ActivityInfo, CiviCRM/CiviCase observations recorded in `research/beneficiary-management.md`; Casebook child-welfare observations in `research/child-welfare-management.md`.

## Sources

Fetched 2026-09-08:

- Apricot (Bonterra) — https://www.bonterratech.com/product/apricot (product page incl. official feature FAQ, tiers, Que AI, Impact Hub)
- Casebook — https://www.casebook.net/platform-overview/ and https://www.casebook.net/case-management-solution/ (platform + case-management pages incl. feature FAQ)
- CaseWorthy — https://eccovia.com/product/clienttrack/ (served CaseWorthy content after the Feb 2025 Eccovia/ClientTrack acquisition; homepage + FAQ)
- Lamplight — https://www.lamplightdb.co.uk/ (root) and https://www.lamplightdb.co.uk/system-features/ (features page)

Access limitations (assertion strength calibrated accordingly):

- **No Tier-1 operational help-center documentation was reachable for any sampled product.** Bonterra support/help was 403 in the sibling pass and was not retried here; Casebook's KB (gohub.casebook.net) was not fetched; CaseWorthy support center not fetched; Lamplight's newer hub domain (lamplighthub.co.uk) transport-errored once — the legacy domain (lamplightdb.co.uk) served instead. All direct evidence is Tier 2 official product pages and official FAQs.
- Consequently **no precise operational facts** are asserted anywhere: no numeric limits, no exact case-status vocabularies, no default values, no timing rules. Status names and structures are described conceptually.
- CaseWorthy pages are marketing-dense; structural claims were taken only where the vendor states capabilities concretely (FAQ feature list, intake→care delivery→reporting framing, apBuilder configurability).
- The Eccovia/ClientTrack → CaseWorthy acquisition (Feb 2025, stated on the fetched page) means ClientTrack-specific structures could not be verified independently; claims are recorded as CaseWorthy claims.

## Product A — Apricot (Bonterra)

### Key observations (evidence layer A, Tier 2 product page + official FAQ)

- Self-description: "Case management software for nonprofits… Strengthen community outcomes, simplify workflows, and showcase your successes." Parent platform: "Bonterra Impact Management platform brings together industry-leading case management software… and robust impact measurement capabilities."
- Official feature list (FAQ): "Apricot forms the basis of our case management solution and provides users with the following features":
  - "Case management: including tools for managing **caseloads, exits and enrollments**, schedules, and **network and internal referrals**."
  - "Forms and records: including a form designer, secure document folder, templates, and smart entry fields."
  - "Reporting tools: such as **compliance reporting**, aggregate reports, and an inventory dashboard."
  - "Workflow management features include email triggers, workflow management, automated rules, and alert notifications."
  - "Security and administration controls: such as **role-based permissions**, complex passwords and inactivity checks, multi-factor authentication, and single sign-on tools." (field-level controls named elsewhere on the page: "role-based permissions, field-level controls, and built-in compliance templates")
  - "Participant engagement features include secure online forms, direct messaging, and a **streamlined intake process**."
  - "Attendance, inventory, and bulk data entry tools, such as batch record creation, attendance tracking, and inventory management."
  - "Imports and integrations: including an import tool, automated imports, and API access."
- Flow framing: "unifies participant and program data into one platform… **From intake to reporting**."
- Funder machinery: "Quantify and communicate your program outcomes…"; "Deliver clear, **funder-ready impact reports**"; "Use **Data Standards** in Apricot to align metrics across programs and organizations"; AI "data integrity review — identify missing fields, duplicates, and inconsistencies before reporting deadlines."
- AI (Que): participant snapshot, note capture (spoken/written → structured case notes), early-intervention signals ("disengagement patterns or missed milestones based on your program criteria"), Que Data Studio.
- Tiers: Essentials / Pro / Enterprise; sibling products ETO and Apricot for Government ("compliance-ready cases").
- History (FAQ): "Founded in 2000, Social Solutions was a leading case management software provider for nonprofit organizations and public sector agencies… offered Social Solutions Apricot, ETO, and Penelope."
- Vocabulary: "participants", "caseloads", "enrollments", "exits", "intake", "referrals", "programs".

## Product B — Casebook

### Key observations (evidence layer A, Tier 2 platform + case-management pages)

- Self-description: "Configurable Human Services Software — Organize and manage **services, clients, and case data** with a human services solution configured to your nonprofit or public sector organization's needs."
- Case-management page: "Effortlessly **manage, track, and organize all your cases and clients** from one centralized hub"; "makes it easier for nonprofit, private sector, and public organizations to fulfill their missions and deliver better client outcomes."
- Named features: **Enhanced Case Notes** ("Record important interactions and **service deliveries** with our platform's Notebook feature"); **Customizable Forms** ("draft, build, and review your organization's many forms… multistage creation process"); **Service Planning** ("Collaboratively develop, monitor, and adapt **individualized service plans**… provider services"); **Scheduling & Notifications**; **Workflows & Messaging** ("task assignments, real-time collaboration"); **Service Directory and Tracking** ("View a list of **services each client is involved in, the service providers, enrollment dates, and notes**… changes and outcomes over time"); **Built-in & Custom Reports** (drag-and-drop data picker); data-quality dashboard; integrations (API, Google/Outlook/Zapier, email-into-case).
- Model statement (FAQ): "designed by case managers for case managers… we have a **person-centric model** that collects everything in an organized manner."
- Reporting framing: "Be ready to **pull the reports that funders and controlling agencies require** of you… your organization's health and compliance."
- Security: AWS hosting, encryption, HIPAA compliance, SOC-II audit; "built in restrictions that will **limit users access to records they're not supposed to see**."
- Client quotes: "Tracking cases, services and providing the monthly data for supervisors and **grant requirements**"; "store all client data, emails are linked to our cases"; "a secure place to store all of my client files."
- Configurability: "preset with about 80 percent of what your organization would need out of the box, enabling you to configure the rest."
- Program areas: child welfare, youth & family, foster care, victim services, crime diversion & reentry, workforce & employment; solutions span community services, schools, public safety social work, public sector agencies, tribal. (Cross-reference: the child-welfare pass documented the statutory depth on the same platform — packaging overlap, one product family serving both.)

## Product C — CaseWorthy

### Key observations (evidence layer A, Tier 2 homepage + FAQ; fetched via former ClientTrack URL)

- Self-description: "Purpose-Built Platform for Human Services… a purpose-built, mission-critical software platform for **case & program management** to enable coordinated **whole-person care** and **outcome reporting** across the spectrum of human services."
- Scale claims (marketing, recorded as such): "1,000+ nonprofit organizations, local and state governments"; "15M+ Individual & Family Cases Supported"; "300M+ Case Notes Recorded"; "4B+ Services Delivered"; "$22.3B+ in Claims Processed"; "700K+ Community Workers, Providers & Locations Supported."
- Process framing (three named stages): "Intake That Accelerates Services — capture critical data, **determine eligibility in real time**, and connect clients to services" → "Care Delivery That Drives Measurable Outcomes — design **intelligent care plans**, coordinate services seamlessly, and continuously monitor progress" → "Reporting That Secures Funding and Proves Impact — **audit-ready reporting**, defensible outcome data, stronger funding position."
- FAQ feature list: "customizable workflows, secure data management with encryption and **role-based access**, automated notifications and reminders, advanced reporting and analytics, mobile access, **client and partner portals, document management, and comprehensive case notes**. Many features are configurable through **apBuilder**, so organizations can adapt **workflows, forms, and assessments** to match their own processes, without code."
- Person-centric positioning: "Move from Program-Centric to Person-Centric… a **360° view of every client**… Reduce duplicate intakes, conflicting records, and fragmented service delivery."
- FAQ definition of the category: "Case management software is a digital solution that helps organizations **track, manage, and streamline client interactions and case workflows**… enables social service providers, nonprofits, and government agencies to deliver more coordinated, effective support."
- Verticals: aging, behavioral health, IDD, education, employment & career, family services, homelessness & HMIS, government, veterans, survivor services.
- AI: Cara ("generate case summaries… AI-driven classification and predictive analysis").
- Lineage: Eccovia (ClientTrack) became part of CaseWorthy in February 2025 (stated on the fetched page).

## Product D — Lamplight

### Key observations (evidence layer A, Tier 2 root + system-features pages)

- Self-description: "Charities thrive with lamplight… Meet your new **case management CRM**." "We support charities, not for profits and CICs who need a tailored, powerful CRM database to **track their service delivery**." (Note the UK convention of branding case management as "CRM".)
- Record model (system-features page):
  - "Unlimited profile data — Add **profiles for anyone you work with – service users, staff, volunteers, funders, and partners**. Built-in **duplicate checking**… Customise fields by profile type… **View all case notes for each person in one place**."
  - "Group and one-to-one session recording — One-to-one counselling, group support sessions, open drop-ins or wider forums can all be **logged into your system**. Update the register manually… or let people book themselves online or use QR codes to log attendance."
  - "Referral tracking — Track **incoming, outgoing, and internal referrals**. Clients or partner agencies can refer via your website… Report on referral volumes and **link them to case records** to see the whole picture."
  - "Personal and team diaries… Manage tasks for you and your team, **linked directly to your service users and activities**."
  - "Outcome tracking — Use any outcome measure… Core 10, Core 34, PHQ6, GAD7, WEMWBS… licensed options like Triangle Outcome Stars and MyCAW."
  - "Easy, clear reporting — Create reports on any record type… Break down by ward, borough, service, or demographic information… export to Excel."
  - "You're in control — comprehensive system admin… Set your colour scheme, **customise terminology**, and highlight key information."
  - "Grows with you — modular system… enhanced auditing or a **Safeguarding dashboard**."
- Security/GDPR: ISO27001-certified; "user-specific access levels… two-factor authentication… even restrict login times"; GDPR archiving of profiles, permanent deletion "from both system and backups."
- Customer quotes: "the first thing we go to at the start of each day… a good point of reference, the reporting is great and **past details can support with new cases coming on board**" (Justice First); "with the volume of work, we are now recording" (Waveney DV&A Forum); outcome measurement "with the people we support when they first start with us and now" (Restitute).
- Vocabulary: "service users" (UK), "cases", "case notes", "referrals", "outcome measures".
- Tier: small/medium charity; pricing quoted "£20–£40 per team member, per month" (vendor-quoted, recorded as vendor claim only).

## Cross-product Comparison

| Dimension | Apricot | Casebook | CaseWorthy | Lamplight | Strength |
|---|---|---|---|---|---|
| Served-person record | "participant and program data unified"; participant engagement | person-centric model; client files | "360° view of every client"; individual & family cases | profiles for service users (+ staff/volunteers/funders/partners) | A across all 4 |
| Served-person naming | participant | client | client | service user | naming varies; concept stable |
| Episode machinery | caseloads, exits and enrollments; intake→reporting | cases; "manage, track, organize all your cases and clients" | "15M+ individual & family cases"; intake→care delivery→reporting | case records; "new cases coming on board" | A across all 4 |
| Episode owner | caseloads (case-carrying staff) | "designed by case managers for case managers" | community workers/providers | staff profiles; team diaries/tasks | A across all 4 |
| Documentation | form designer, smart entry fields, secure document folder | Notebook (case notes; "interactions and service deliveries"), multistage forms | "300M+ case notes recorded"; document management; comprehensive case notes | case notes per person; session recording (1:1, group, drop-ins); registers/attendance | A across all 4 |
| Entry / eligibility | streamlined intake; smart fields; secure online forms | intake forms; eligibility assessment forms | "intake that accelerates services… determine eligibility in real time"; assessments via apBuilder | website referrals; customized fields/terminology | A across all 4 |
| Program / service binding | enrollments and exits; programs | service directory & tracking (enrollment dates, providers, outcomes over time) | case & program management; multi-program in one platform | services; activities | A across all 4 |
| Planning | (workflow automation emphasis) | individualized service plans | intelligent care plans; monitor progress | tasks linked to service users | A in 3; lighter in Lamplight |
| Referrals | network and internal referrals (named) | service directory; email-into-case | coordinated care; partner portals | incoming/outgoing/internal referrals, linked to case records | A across all 4 |
| Outcome measurement | funder-ready impact reports; Data Standards | reports "funders and controlling agencies require"; data picker | outcome reporting; audit-ready; funding position | outcome measures (Core 10/PHQ6/GAD7/Outcome Stars) at start & end | A across all 4 |
| Confidentiality / access | role-based permissions + field-level controls; MFA/SSO | access restrictions limiting records users can see; HIPAA/SOC-II | encryption, role-based access | user-specific access levels, 2FA, GDPR archiving/permanent deletion, ISO27001 | A across all 4 |
| Workflow / task machinery | email triggers, automated rules, alerts | workflows & messaging; task assignment; scheduling & notifications | automated notifications; digital workflows | diaries; tasks linked to service users and activities | A across all 4 |
| Duplicate / data quality | AI data-integrity review (missing fields, duplicates) | data-quality dashboard | "reduce duplicate intakes" | built-in duplicate checking | A across all 4 |
| Attendance / group delivery | attendance tracking | attendance viewing (school page) | "4B+ services delivered" | session registers; drop-ins; QR attendance | A across all 4 |
| Participant self-service | secure online forms; direct messaging | client-facing portal (foster page) | client and partner portals | website referral forms; self-booking (publishing module) | B (common, partial in sample) |
| Configurability | form designer; templates; Data Standards | ~80% out-of-box, configurable rest | apBuilder (workflows/forms/assessments without code) | custom fields per profile type; customise terminology | A across all 4 |
| AI | Que (snapshot, notes, signals, data studio) | (not on fetched pages) | Cara (case summaries) | (none) | product-specific, emerging |
| Posture | packaged tiered SaaS (Essentials/Pro/Enterprise) | configurable SaaS | enterprise platform + data lakehouse | tailored small-org system, modular | structural difference (postures, not structures) |

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

Smallest structure without which the software stops being recognizable as Nonprofit Case Management — three jointly-held structures:

1. **Client records** — persistent identified records for the people the organization serves (client / participant / service user), typically with household or family context. Without it there is no casework — the product is a generic contact database (donor-CRM territory).
2. **Bounded casework episode under an accountable caseworker** — a **case** opened for a client, typically bound to one of the organization's defined programs/services, carrying a tracked lifecycle from intake through active service to a recorded exit/closure, and assigned to a named caseworker who is accountable for moving it. Without it the product is a served-population registry (Beneficiary Management) or a plain CRM.
3. **Documented casework record accumulating on the episode** — dated, attributed entries (case notes, session/service delivery records, assessments, attached forms/documents) that build up on the case and form the client's service history; this documentation is what makes the episode accountable to supervisors, funders, and auditors. Without it the case is an empty shell and the product is a task tracker.

Jointly-held is load-bearing:

- 1 alone = contact database / donor CRM
- 2 without 3 = empty case shells (ticket-like, no accountability content)
- 3 without 2 = an unstructured activity log / notes app
- 2+3 without 1 = anonymous task log with no person continuity
- 1+3 without 2 = client CRM with an activity log — the pre-casework posture (charity contact database with notes)

Deliberately **not** in L0 (each fails the "remove it and the Type still stands" test or is only common):

- **Funder/compliance reporting** — universal in the sample (all four report upward) and the sector's economic motive, but a casework episode with notes and closure is still recognizable case management without reporting machinery (minimal product configurations; historical paper case files). Reporting is L1.
- **Eligibility/needs assessment machinery** — universal in modern products, but historical and minimal-case forms of the Type (a case opened from a request, worked, documented, closed) satisfy the Type. L1.
- **Referrals** — named by all four, but a single-organization casework system without referral exchange is still the Type. L1.
- **Program enrollment as a separate object** — the episode is opened *under* a program/service; a separate enrollment record structure is a common implementation, not an invariant.
- **Statutory mandate, court/legal machinery, placement/permanency** — these belong to Child Welfare Management and Social Services Case Management. Their absence is characteristic of the private/mission-driven operator posture.
- **Clinical machinery** (diagnoses, treatment plans, claims billing) — behavioral-health pole only.
- **Portals, self-service, AI, offline mobile, outcome-measure instruments** — common or optional.

### L1 — Common Mature Structure

Present across the researched sample; expected in mature products but not definitional:

- configurable intake forms and eligibility/needs assessments (form designers, smart fields, real-time eligibility)
- program/service enrollment binding the client to the organization's offerings, with tracked enrollments and exits per program
- referral machinery — internal (between workers/programs) and external/network (between organizations) — linked to the case record
- service/goal planning on the case (individualized service plans / care plans)
- outcome measurement — instruments (often licensed, e.g., standardized scales) administered at start/end, plus aggregates
- funder/accountability reporting: compliance reports, aggregate reports, dashboards, shared data standards, audit-ready exports
- confidentiality machinery: role-based permissions, field/record-level visibility restrictions, audit logging; GDPR-style archiving/deletion in the UK context
- workflow/task machinery: task assignment, alerts/notifications, email triggers, scheduling/appointments, deadlines
- duplicate checking / data-quality tooling
- attendance tracking for group sessions/drop-ins; registers
- document storage under permissions
- participant self-service: online forms, portals, messaging, website referrals/self-booking
- imports/APIs and integrations
- search, saved views, bulk data tools

### L2 — Variant / Optional Structure

- **Vocabulary**: client / participant / service user / beneficiary — segment- and region-specific naming of the same concept (US products: client/participant; UK: service user; humanitarian: beneficiary).
- **Product posture poles**: packaged tiered SaaS flagship; configurable person-centric platform; enterprise multi-program platform with data-warehouse/analytics layer; small-org tailored modular system.
- **Vertical flavors** (each adjusts the record and rules around the same spine):
  - behavioral health / mental health: clinical documentation, standardized clinical measures, claims/billing straddling toward health EHR
  - homelessness / housing: coordinated-entry and HMIS data-standard postures
  - domestic violence / victim services: heightened confidentiality
  - workforce & employment, education/school social work, aging, IDD, veterans, criminal-justice reentry, refugee/migrant support
- **Operator straddle**: the same products sell to government agencies (Apricot for Government, CaseWorthy government vertical, Casebook public-sector solutions) — packaging overlap with §24 social-services/public-sector case management, not Type collapse.
- **AI assistance**: case summarization, note capture from speech, early-intervention signals, conversational data exploration (emerging; Apricot Que, CaseWorthy Cara).
- **Deployment**: cloud SaaS dominant; small-org and European deployments emphasize data-residency/GDPR tooling; on-premise/air-gapped documented only in the humanitarian sibling (ActivityInfo), not in this sample.

### L3 — Vendor-specific Structure

- Apricot: Que AI suite; Impact Hub analytics (built on Amazon Quick Suite); Data Standards library; Essentials/Pro/Enterprise tiers; ETO sibling brand; Apricot for Government; "40M+ lives touched" claim.
- Casebook: Annie E. Casey Foundation incubation; "first modern child welfare system granted a COTS waiver" claim; ~80% out-of-box claim; Notebook feature name; drag-and-drop data picker; AWS/HIPAA/SOC-II posture details; program-area packaging (child welfare, foster care, victim services, workforce, tribal…).
- CaseWorthy: apBuilder configurability; Cara AI copilot; data-lakehouse "CORE" foundation; ClientTrack lineage (Eccovia acquisition, Feb 2025); scale claims (15M+ cases, 300M+ case notes, 4B+ services, $22.3B+ claims).
- Lamplight: Outcome Stars partnership (Triangle); named outcome instruments (Core 10/34, PHQ6, GAD7, WEMWBS, MyCAW); publishing add-on module (website referrals, QR attendance); Safeguarding dashboard module; enhanced auditing module; ISO27001; £20–£40/user/month pricing claim.

## Vendor-specific / Rejected Findings

- **Rejected (as L0): "nonprofit case management = funder compliance reporting."** All four products report upward — it is the sector's economic engine — but the casework episode with documentation and closure is recognizable without reporting machinery (minimal configurations; historical paper case files). Reporting stays L1.
- **Rejected (as L0): "assessment/eligibility determination defines the Type."** Universal in modern products, but a case opened from a simple request, worked, documented, and closed still satisfies the Type historically.
- **Rejected (as L0): "clinical documentation defines the Type."** The behavioral-health pole adds diagnoses/plans/claims; the generic Type (Apricot for youth programs, Lamplight for befriending services) has none. Clinical depth is a vertical variant straddling toward health EHR.
- **Rejected: "nonprofit case management is just nonprofit CRM by another name."** Direction of flow differs structurally (services/goods delivered *to* people vs. money/gifts flowing *in*), and the episode/workflow/ownership machinery has no donor-CRM counterpart. Lamplight's "CRM" self-branding is a UK-vocabulary artifact — its documented record model (case notes, session recording, referrals linked to cases) is casework.
- **Rejected: "nonprofit case management = beneficiary management."** Center-of-gravity line (see Boundary Findings); the sibling pass's test is ratified, not contradicted.
- **Rejected: "the 'nonprofit' qualifier is the whole definition."** The casework spine is shared with government-operated social services; the operator/mandate context differs. Recorded as a boundary issue, not a collapse.
- **Not promoted (single-source):** Apricot's inventory management; Apricot Data Standards; Casebook's email-into-case; CaseWorthy's claims processing; Lamplight's QR attendance and safeguarding dashboard. Each is evidence for L2/L3 only.

## Boundary Findings

- **vs Beneficiary Management (§25 sibling, processed) — the primary joint-review obligation.** The beneficiary pass held: Beneficiary Management centers the **population registry** (who is served, what they need/qualify for, what was delivered, aggregated upward), while Nonprofit Case Management centers the **casework episode** (a bounded case driven through a workflow with an accountable caseworker and closure). Ratified from this side with first-hand evidence:
  - All four sampled products sell **episode machinery** as the front of the product: Apricot "caseloads, exits and enrollments"; Casebook "manage, track, and organize all your cases and clients" + "designed by case managers"; CaseWorthy "individual & family cases" + named casework stages; Lamplight "case records", "case notes", "new cases coming on board". None of the four foregrounds registration/distribution of a served population as the product's center — the registry is present but subordinate (client profiles, service tracking).
  - Conversely, the beneficiary pass's flagship products (ActivityInfo CVA pattern, CommCare app-built registries) demonstrably run registration + delivery + reporting **without** a full accountable-caseworker episode.
  - **Removal tests (both directions)**: strip the episode/caseworker/closure machinery, keep registry + enrollment + deliveries + population reporting → Beneficiary Management remains. Strip the population-registry center (keep caseloads of episodic casework) → Nonprofit Case Management remains. Verdict: **boundary HELD, keep-both; alias consolidation rejected.** Market vocabulary conflation is real (products marketed as "case management" implement registry-heavy patterns and vice versa) and is recorded as a standing vocabulary note, not a Type collapse.
- **vs Child Welfare Management (§24 sibling, processed) — second joint-review obligation.** Ratified: child welfare carries the **statutory protection loop** (mandated report intake with screening decisions, safety/risk assessment with legal force, out-of-home placement machinery, court-anchored permanency) and need-to-know confidentiality over an identified child. Nonprofit Case Management's defining core requires none of these; its cases are organization-defined services, and its accountability audience is funders, not statute. Casebook spans both from one platform (packaging overlap, not Type identity) — consistent with the child-welfare pass's own note. Verdict: **boundary HELD, keep-both.**
- **vs Social Services Case Management / Public Sector Case Management (§24 siblings, unprocessed) — new joint-review flag.** The casework-episode spine is the same; the differentiators are the **operator and mandate**: government statutory eligibility/entitlement vs. organization-defined programs and funder accountability. Same-product straddles (Apricot for Government, CaseWorthy government vertical, Casebook public-sector solutions) show this is a context line, not a feature line. Recommend joint review when those leaves are processed; likely outcome by the massage-practice/mobile-POS precedent: keep-both as seam-defined siblings with near-identical L0 and different operator context.
- **vs Nonprofit CRM / Donor Management System / Nonprofit Management Platform**: money in (gifts, memberships, campaigns, stewardship) vs. services out (eligibility, delivery, casework, outcomes). One product family can hold both (Bonterra sells donor products and Apricot; CiviCRM holds both as components per the sibling pass) — separable layers.
- **vs Nonprofit Program Management (§25 sibling, unprocessed)**: programs as initiatives/containers (plans, budgets, milestones) vs. the people and cases inside them. The enrollment binding means each Type references the other's central object; center-of-gravity differs. Light flag for the sibling's pass.
- **vs Monitoring & Evaluation Platform (§25 sibling, processed)**: M&E centers the planned-results framework + indicator actuals + accountability reporting loop (often with no person-level registry); case management's floor is the case-level service record. Vendor language bridges them ("outcome reporting", "impact measurement") — the vendor-drawn seam noted by the M&E pass is confirmed as a packaging/positioning seam, not a Type boundary problem.
- **vs Care Plan Management / Care Coordination (§22, health)**: both organize services/goals around a person, but health care plans are clinical/assessed-needs records without the funder-accountability framing; the behavioral-health vertical of this Type straddles.
- **vs HR Case Management / Legal Case Management / ITSM**: the word "case" is shared; the objects differ (employees/legal matters/incidents vs. people served by social programs). No structural overlap beyond the name.
- **"去掉什么就变成另一个 Type" 判据汇总**: remove the casework episode/caseworker/closure → Beneficiary Management (population registry); remove the client person model → generic workflow/ticketing tool; remove the documentation layer → task tracker; remove service-delivery semantics and keep donor gifts → donor CRM; move the operator to government with statutory eligibility → Social Services Case Management; add mandated-report screening + placement/permanency → Child Welfare Management; replace cases with results frameworks/indicators → Monitoring & Evaluation Platform.

## Historical / Market-Sample Check

- Paper-era charity casework (conceptual check): a client folder — intake form, assessment notes, caseworker's dated visit/contact notes, referral letters, service records, closure summary — satisfies all three legs at analog level: identified client record, bounded episode with an accountable worker, documented casework record ending in closure. No cloud, no funder dashboards, no outcome instruments required.
- Church/community-ministry assistance records (person + assistance episode + visitation notes) satisfy the core — matching the beneficiary pass's parallel church-registry check from the registry side.
- Pre-SaaS packaged systems (Social Solutions, founded 2000, per Apricot's own FAQ history; the pre-Bonterra generation named in the sibling pass) satisfy the core — packaged forms + caseloads + enrollments/exits + reporting without cloud/AI.
- Digitized paper case management (the Danish Refugee Council case study recorded in the sibling pass) satisfies without mobile/offline.
- Conclusion: the L0 does not over-fit to the current SaaS, funder-dashboard, AI-assisted market shape. The definition names no portals, outcome instruments, data standards, or AI.

## Uncertainties

1. **No Tier-1 operational documentation reachable for any sampled product** — all direct evidence is Tier 2 official product pages/FAQs. Case-status vocabularies, enrollment/case object relationships, and permission-granularity details per product could not be verified at help-center depth; the final document accordingly describes lifecycle and structures conceptually and asserts no precise operational facts.
2. The precise relationship between case, enrollment, and program objects inside products (e.g., one case per enrollment vs. case spanning enrollments) is not verified; products likely differ.
3. CaseWorthy evidence is marketing-dense and reflects a merged product line (Eccovia/ClientTrack folded in 2025); ClientTrack-specific structures could not be independently verified.
4. Lamplight's internal record model (how "case records" relate to profiles, referrals, and session records beyond the documented "referrals linked to case records" and "case notes per person") is only partially evidenced.
5. Relative market weight of the four posture poles, and the frequency of the behavioral-health (EHR-straddling) pole vs. the generic human-services pole, could not be quantified from accessible sources.
6. Penelope (same vendor family as Apricot per the FAQ) was excluded by the same-vendor rule; its counseling-oriented posture is therefore unverified and uncharacterized.

## Final Synthesis

Nonprofit Case Management is the casework system of record for mission-driven service organizations. Its world is organized around three jointly-held structures: identified client records for the people served; bounded casework episodes (cases) opened for clients under the organization's programs, assigned to accountable caseworkers, and carried through a tracked lifecycle to a recorded exit; and a documented casework record — dated, attributed notes, service records, assessments, and documents — accumulating on the case as the client's service history. Around this core, mature products add configurable intake and eligibility/needs assessment, program enrollment with tracked exits, referral machinery linked to cases, service/goal planning, outcome measurement, funder/accountability reporting, strict confidentiality machinery, workflow/task automation, duplicate checking, attendance tracking, and participant self-service. The sector's economic engine — funder reporting — is universal but not definitional. The Type is bounded by Beneficiary Management (registry center vs. episode center; boundary ratified, keep-both), Child Welfare Management (no statutory protection loop in the generic Type), Social/Public Sector Case Management (same spine, government operator/mandate; new joint-review flag), Nonprofit CRM (services out vs. money in), Nonprofit Program Management (initiatives vs. people), and Monitoring & Evaluation platforms (case-level delivery vs. results frameworks). Market vocabulary conflates "case management", "CRM", and "beneficiary management" labels; the structural center-of-gravity line, not the label, separates the Types.
