# Research Notes — Beneficiary Management

## Research Goal

Understand "Beneficiary Management" as an Application Type in the nonprofit / NGO sector (DIRECTORY section 25, Nonprofit, Membership & Religious Organizations): what core objects exist, how beneficiaries enter / are served / leave, how services and aid are recorded, how the served population is reported upward, and where the boundary lies against Donor CRM, Nonprofit Case Management, Nonprofit Program Management, and Monitoring & Evaluation platforms.

## Initial Boundary

Working hypothesis before research:

- It is software for organizations that **serve people** (as opposed to raising money from them): registering beneficiaries, capturing needs/eligibility, linking people to programs, recording aid/service delivery, and reporting on the served population.
- Closest neighbors likely to be confused with:
  - Donor Management System / Nonprofit CRM (opposite flow: money in vs. aid out)
  - Nonprofit Case Management (sibling leaf; same people, possibly same products)
  - Nonprofit Program Management (programs/projects vs. people)
  - Monitoring & Evaluation Platform (indicators vs. people)
  - Social Services Case Management / Public Benefits (government section 24; statutory flavor)
  - **Homonym**: "beneficiary" in life insurance = designated payout recipient inside Policy Administration — a data field, not this Application Type.

## Research Questions

1. What is the unit of record — person, household, or case?
2. How does a beneficiary enter the system (intake / registration / enrollment) and how do they leave (exit / closure)?
3. How are needs, vulnerability, and eligibility captured and used?
4. How is assistance recorded (visits, attendance, distributions, payments, referrals)?
5. What program structures do products expose (programs, projects, services, activities)?
6. Who works in the system (field workers, caseworkers, program managers, M&E staff, admins), and on what surfaces (mobile vs. office console)?
7. How is the served population counted and reported to funders / donors?
8. How do products handle confidentiality (roles, field-level permissions, audit logs)?
9. Is "beneficiary management" a recognized standalone product category, or a layer inside case management / M&E / CRM products? (Determines whether this leaf is an independent Type or a Variant/Alias.)

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers:

| Product | Philosophy | Segment |
|---|---|---|
| **CommCare (Dimagi)** | no-code offline-first platform for building frontline data collection + case management apps | global health / humanitarian / development field programs |
| **ActivityInfo** | design-your-own relational database for MEAL + case management + cash & voucher assistance | humanitarian coordination, NGOs, UN agencies |
| **Apricot (Bonterra / Social Solutions)** | packaged case management for nonprofits with funder/compliance reporting | US human-services nonprofits and public agencies |
| **CiviCRM (CiviCase)** | open-source constituent CRM where case management is one component beside donations/membership/events | community organizations, advocacy, mixed donor+client orgs |

Rejected/attempted samples: RedRose (humanitarian beneficiary registration — site JS-only, no content reachable); Salesforce NPSP (developer docs blocked 403); not used for any claim.

## Sources

Fetched 2026-09-06:

- CommCare (Dimagi): https://www.dimagi.com/commcare ; https://www.dimagi.com/case-management/ (Tier 2 product pages)
- ActivityInfo: https://www.activityinfo.org/support/docs/index.html (Tier 1 docs index) ; https://www.activityinfo.org/about/case-management.html ; https://www.activityinfo.org/about/cash-voucher-assistance.html (Tier 2 use-case pages)
- Apricot: https://www.bonterratech.com/product/apricot (Tier 2 product page incl. feature FAQ)
- CiviCRM: https://docs.civicrm.org/user/en/latest/ (Tier 1 user guide index) ; https://docs.civicrm.org/user/en/latest/case-management/what-is-civicase/ (Tier 1 concept page)

Access limitations (assertion strength calibrated accordingly):

- CommCare public help wiki (dimagi.atlassian.net) not fetched; docs.commcarehq.org transport errors ×2 → abandoned per source-retry rule. CommCare claims rest on Tier 2 product pages.
- Apricot help center / operational documentation not reachable (bonterratech.com/products/... 403; /product/apricot served instead). Apricot feature claims rest on the vendor's own product-page feature list (Tier 2).
- Salesforce NPSP docs 403 → CRM-module philosophy evidenced via CiviCRM instead; no Salesforce-specific claims made.
- RedRose (humanitarian "beneficiary management" category) content not reachable → humanitarian registration/distribution flavor evidenced through ActivityInfo CVA material only.
- No precise operational numbers (record limits, exact permission matrices, exact status vocabularies) are claimed anywhere; none were verifiable at the reached documentation depth.

## Product A — CommCare (Dimagi)

### Key observations (evidence layer: A, Tier 2 product pages)

- Self-description: "a no-code platform for building offline **data collection** and **case management** apps… frontline health and social service programs in more than 130 countries use it to register clients, guide visits, and report results in real time."
- Case model: "Every client gets a longitudinal case record. Teams can assign and share cases, trigger follow-ups and referrals, and escalate what needs attention, with full case history at every visit."
- Named capabilities: longitudinal case records; case assignment & sharing; referrals & escalations; full case history; no-code app builder (cases, logic, multilingual forms, referrals); mobile / web / SMS surfaces; user roles & permissions; release management; bulk data tools; linked project spaces; live dashboards; reports & exports; data quality tools; APIs & integrations; messaging/SMS.
- Sector framing: community health, humanitarian response, agriculture…; use cases: service delivery, monitoring & evaluation, campaigns, **cash & voucher assistance**, research.
- Vocabulary: "clients", "cases"; customer quote uses "beneficiaries" ("a more robust and comprehensive solution to support our beneficiaries over time").
- Deployment posture: offline-first ("collect data, manage cases, and use job aids with no signal; everything syncs"); security/compliance surface (SOC 2, HIPAA, GDPR, AES-256, MFA/SSO/roles) prominent.

## Product B — ActivityInfo

### Key observations (evidence layer: A, Tier 2 use-case pages + Tier 1 docs structure)

- Case management use case: "Document every stage in the case management process from **intake to referral and case closure**." "Without writing code, create secure customizable databases accessible by selected users."
- Access control: "Invite users, assign user roles and cases"; "Assign cases to individual case workers"; "Grant or remove additional user permissions"; "Set rules with conditions for users to be able to view, add, edit or delete specific cases or fields"; "Use an audit log to review users' actions and records changes"; "Restore deleted data on your own"; location-based access; groups of case workers assigned to supervisors.
- Person-centric aggregation: "Gather all cases associated with an individual in one place."
- MEAL combination: "Combine Case management with MEAL and impact measurement… Measure and visualize impact by sharing Dashboards and Notebooks with donors and other key stakeholders."
- CVA use case: "Work with **beneficiary and market data**, track recurring payments, run surveys… and needs assessments"; "**Register and track beneficiaries and households**"; "Combine cash transfer data with case management capabilities for a complete picture of **each beneficiary**"; "Prevent duplicates and detect fraud with advanced form design settings and rules"; "Import and validate large volumes of harmonized data quickly"; "Invite users, assign roles, **cases or households**".
- Docs structure (Tier 1 index): database design / form design / permission design / report design / automations / data management / mobile data collection (online-offline) / user management / formulas; self-managed server (on-premise, air-gapped networks); SaaS hosted in EU.
- Field examples: UNRWA protection database, Danish Refugee Council digitizing a paper-based case management system (Rohingya response), Medicos del Mundo (case management + health emergencies + surveys + project tracking).
- Vocabulary: "beneficiaries", "households", "cases", "case workers".

## Product C — Apricot (Bonterra / Social Solutions)

### Key observations (evidence layer: A, Tier 2 product page incl. official FAQ)

- Self-description: "Case management software for nonprofits"; "unifies participant and program data into one platform… From **intake to reporting**."
- Official feature list (FAQ): 
  - "Case management: including tools for managing **caseloads, exits and enrollments**, schedules, and **network and internal referrals**."
  - "Forms and records: including a form designer, secure document folder, templates, and smart entry fields."
  - "Reporting tools: such as **compliance reporting**, aggregate reports, and an inventory dashboard."
  - "Workflow management features include email triggers, workflow management, automated rules, and alert notifications."
  - "Security and administration controls: such as **role-based permissions, field-level controls**… multi-factor authentication, and single sign-on."
  - "Participant engagement features include secure online forms, direct messaging, and a streamlined intake process."
  - "Attendance, inventory, and bulk data entry tools, such as batch record creation, attendance tracking, and inventory management."
  - "Imports and integrations: including an import tool, automated imports, and API access."
- Outcome/reporting framing: "Measure program impact… quantify and communicate your program outcomes"; "funder-ready impact reports"; "Data Standards in Apricot to align metrics across programs and organizations"; AI assistant (participant snapshot, note capture, early-intervention signals, data integrity review incl. "identify missing fields, duplicates, and inconsistencies before reporting deadlines").
- Product tiers: Essentials / Pro / Enterprise; sibling product "Apricot for Government"; sister product ETO (Evidence/Effects "ETO" = same vendor family).
- Vocabulary: "participants", "caseloads", "enrollments", "exits", "intake", "referrals", "programs".

## Product D — CiviCRM (CiviCase)

### Key observations (evidence layer: A, Tier 1 user guide)

- CRM substrate: "Contacts" are the center; components include Contributions (donations), Membership, Events, Campaigns, **Case management (CiviCase)**, Grants. Same contact pool can hold donors, members, event participants, and clients — tests the donor/beneficiary boundary within one product.
- CiviCase definition: "a tool for tracking and managing sequences of interactions between people in your organisation and contacts… In addition to tracking and managing your organisation's interactions with **clients or constituents**, CiviCase can also help you manage internal organisational interactions."
- Case = workflow of **Activities**: "track a specific workflow or set of procedures that must be followed and that involves a number of different organisational staff"; automated scheduling of follow-up activities (offset-based scheduling from case start); case statuses changed at decision points ("passed basic checks / failed basic checks / … / accepted").
- Case roles: example "Housing Support case" with Homeless Service Coordinator (creator/manager), Health Services Coordinator, Benefits Specialist; per-user case dashboards showing only assigned work ("thousands of applications… each saw a case dashboard showing only the work assigned to them").
- Registry mechanics: "Deduping and Merging" is a documented core workflow; custom fields; relationships (incl. household-style relationships); smart groups; logging of changes; permissions/access control documented in setup guide.
- Vocabulary: "contacts", "clients", "constituents", "cases", "activities".

## Cross-product Comparison

| Dimension | CommCare | ActivityInfo | Apricot | CiviCRM (CiviCase) | Strength |
|---|---|---|---|---|---|
| Unit of record | client (person) as case | beneficiary / household records | participant (person) | contact (person/org/household) | A across all 4 |
| Served-person naming | client(s), case | beneficiary, household | participant | contact, client, constituent | naming varies; concept stable |
| Entry into system | register clients (app built for it) | registration forms; bulk import of harmonized data | streamlined intake; secure online forms | contact creation + open case; dedupe/merge | A across all 4 |
| Needs / eligibility | assessment forms in app | needs assessments; form validation rules | intake process; assessment forms (smart fields) | custom fields + application-review workflow | A across all 4 |
| Program linkage | cases defined per app/program | records linked in designed relational database | programs; enrollments/exits | cases per procedure; campaigns | A across all 4 |
| Service/aid events | visits (guided forms), follow-ups | recurring payments (CVA); distribution-linked records | attendance tracking; service records; inventory | activities logged on case/contact | A across all 4 |
| Referrals | referrals & escalations | referral stage in case process | network and internal referrals | (activities/tasks) | A in 3; weaker in CiviCase |
| Worker assignment | case assignment & sharing | assign cases (or households) to case workers | caseloads | case roles; per-user dashboards | A across all 4 |
| Lifecycle / end state | case follow-up/close; escalation | case closure | exits and enrollments | case statuses incl. final | A across all 4 |
| Household modeling | per program design | first-class ("beneficiaries and households") | participant-centric (family implied) | household relationship type | partial; B (common, not universal) |
| Dedup / data quality | data quality tools; bulk tools | duplicate prevention via form rules; fraud detection | data integrity review (duplicates, missing fields) | deduping and merging | A across all 4 |
| Confidentiality | roles & permissions; compliance surface | conditional rules to view/add/edit/delete cases or fields; audit log | role-based + field-level controls; auditing | ACLs; change logging | A across all 4 |
| Funder / M&E reporting | dashboards; M&E use case | MEAL combination; dashboards/notebooks shared with donors; pivot tables | compliance + aggregate reporting; funder-ready dashboards; data standards | reports (CiviReport) | A across all 4 |
| Field / offline collection | offline-first mobile (defining) | mobile app online/offline | not emphasized | no | partial; B (segment-dependent) |
| Participant self-service | SMS/remote engagement | — | secure online forms; direct messaging | (public forms via website) | partial; B (optional) |
| Configurability | no-code app builder | design-your-own database/forms/permissions/reports | form designer; templates | custom fields; configurable case types | A across all 4 |
| Substrate | purpose-built platform | purpose-built platform | purpose-built SaaS | component of a CRM | structural difference |

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

Smallest structure without which the software stops being recognizable as Beneficiary Management:

1. **Beneficiary registry** — managed records of identified people (and/or households) that the organization serves. Without it there is nothing to manage.
2. **Program/service linkage** — an association between a beneficiary and a program/service the organization offers (enrollment, participation, case opening). Without it the records are just contacts.
3. **Recorded assistance events** — dated records of what was actually delivered to a beneficiary (visit, attendance, distribution, payment, referral, service session). Without it the software does not manage benefits, only people.
4. **Tracked participation state** — each beneficiary's involvement has an observable state over time (entered → active → ended/exited/closed), advanced by recorded events. Without it the registry is a static directory, not an operational system.

Deliberately **not** in L0: funder reporting (the sector's driving motive, but a registry with service records and no reporting is still recognizable); eligibility scoring; caseworker workflows; offline apps; household modeling; CRM integration.

### L1 — Common Mature Structure

Present across the researched sample; expected in mature products but not definitional:

- intake/registration forms with configurable per-program questions; needs/vulnerability/eligibility assessment
- duplicate prevention and merging (form-level rules, dedupe workflows, data-integrity review)
- configurable data model per program (custom fields / form designer / database designer)
- caseworker assignment: caseloads, case sharing, per-user work dashboards; household-level assignment in some products
- referrals — internal (between workers/programs) and network (between organizations)
- funder-facing aggregate reporting: compliance reports, indicators, dashboards, outcome measurement; data standards across programs
- access control beyond roles: conditional/field-level/record-level visibility; audit logs of who changed what; restore/deleted-data recovery
- attendance tracking; document storage; workflow automation (triggers, alerts, scheduled follow-ups)
- search, saved lists, bulk data tools, imports/APIs
- participant-facing self-service (online forms, messaging) — present in some
- offline/mobile field collection — defining for frontline-global segment, absent in office-console products

### L2 — Variant / Optional Structure

- **Vocabulary**: beneficiary / client / participant / constituent / contact — segment- and product-specific naming of the same concept.
- **Segment flavors**:
  - humanitarian/development field programs: offline-first, multi-country projects, CVA (targeting, recurring payments, fraud checks), large-volume harmonized imports, donor/MEAL reporting
  - US human services: packaged case management, funder compliance, data standards, attendance/inventory, participant engagement
  - community/faith-based, mixed donor+client: CRM substrate; beneficiary features as components
  - protection contexts (GBV, child protection): heightened confidentiality, pseudonymization/anonymized aggregates
- **Scale & deployment**: single agency SaaS ↔ national/multi-country rollouts (release management, linked project spaces); SaaS ↔ self-managed/on-premise/air-gapped.
- **Identity depth**: minimal self-reported identity ↔ verified ID ↔ anonymous service points (varies; not verified precisely in this sample).
- **AI assistance**: summarization of participant history, note capture, early-intervention signals, data-quality review (emerging, product-specific today).

### L3 — Vendor-specific Structure

- CommCare: application builder model (apps contain forms + case definitions), project spaces, case sharing semantics, free tier vs paid plans.
- ActivityInfo: database → form → sub-form design hierarchy, permission rules engine, self-managed server (air-gapped), MEAL notebooks, CALP Network membership.
- Apricot: Essentials/Pro/Enterprise tiers, Impact Hub (analytics on Amazon Quick Suite), Que AI assistant, Data Standards library, Apricot for Government.
- CiviCRM: CiviCase activity offsets scheduling, case roles/relationship-based roles, CiviGrant, CiviMail/CiviMember/CiviEvent component suite.

## Vendor-specific / Rejected Findings

- **Rejected (as L0): "beneficiary management = funder compliance reporting."** All four products report upward, but the reporting emphasis differs (ActivityInfo → MEAL indicators; Apricot → funder compliance; CommCare → program dashboards). Reporting is the sector motive, not the defining structure.
- **Rejected (as L0): "beneficiary management requires a case workflow with an assigned caseworker."** ActivityInfo's CVA pattern registers and tracks beneficiaries/households and recurring payments without a full casework episode. Casework is a dominant L1 structure, not the invariant.
- **Rejected (as L0): "beneficiary = household."** Household modeling is first-class in some products (ActivityInfo) and absent/optional elsewhere (CommCare case-per-person designs, CiviCRM optional household relationships). The person is the stable unit; household is common.
- **Rejected: "beneficiary management is just nonprofit CRM."** The flows differ structurally: donor CRM records money/goods flowing *in* (gifts, memberships, campaigns) with stewardship workflows; beneficiary management records services/aid flowing *out* to people with eligibility and delivery records. One product can hold both (CiviCRM components), which proves they are separable layers, not synonyms.
- **Rejected: "insurance beneficiary" homonym.** In life/health insurance, a beneficiary is a designated payout recipient — a field inside Policy Administration Systems, not an Application Type for serving people.
- **Not promoted (single-source):** Apricot's inventory management; CommCare's release management; ActivityInfo's air-gapped deployment; CiviCase's offset-scheduled activities. Each is product-specific evidence for an L2/L3 item only.

## Boundary Findings

- **vs Nonprofit Case Management (sibling leaf)** — the hardest boundary. Evidence: the three flagship products that would implement "beneficiary management" all *market themselves as case management* (Apricot: "case management at scale"; ActivityInfo: case management use case; CommCare: case management platform). The market vocabulary does not separate the two cleanly. Workable distinction by center of gravity:
  - Beneficiary Management centers the **population registry**: who is served, what they need/qualify for, what was delivered, how many were served — aggregation-first, person-anchored.
  - Nonprofit Case Management centers the **casework episode**: a bounded case driven through a workflow (intake → assessment → plan → actions → referral → closure) with an accountable caseworker and deadlines.
  - Test: remove the casework episode/workflow (keep registry + enrollment + deliveries + reporting) → still Beneficiary Management. Remove the population registry (keep only episodic casework) → Case Management.
  - Practical consequence: many real products straddle both; the Type boundary is a center-of-gravity line, not a product-boundary line. **Flagged for STATUS Boundary Issues.**
- **vs Donor Management System / Nonprofit CRM** — direction of the relationship: aid/services out (with eligibility + delivery + outcomes) vs. money in (with gifts + stewardship). CRM-substrate products prove coexistence of both populations on one contact base.
- **vs Nonprofit Program Management** — programs as containers/plans/budgets vs. the people receiving program services. Beneficiary management is people-centric; program management is initiative-centric.
- **vs Monitoring & Evaluation Platform** — M&E aggregates indicator results (often per program/site/period, sometimes with no person-level registry). Beneficiary management's floor is the person-level record. Products like ActivityInfo deliberately bridge both ("Combine Case management with MEAL").
- **vs Social Services Case Management / Public Benefits Management (section 24, government)** — same mechanics, different operator and mandate: statutory entitlement programs with government-defined eligibility vs. organization-defined programs. Sector placement, not core structure, is the differentiator.
- **vs Volunteer Management System** — volunteers contribute time; beneficiaries receive assistance; the same human can appear in both systems with different record semantics.
- **vs data collection tools (surveys/forms)** — a survey tool has no longitudinal person registry or participation state; a beneficiary system's records persist and accumulate events.
- **"去掉什么就变成另一个 Type" 判据汇总**: drop the beneficiary registry & program linkage → case management tool or generic CRM; drop the person-level records → M&E platform; drop service/aid events → contact database; drop the nonprofit context and add statutory eligibility machinery → government public-benefits system.

## Historical / Market-Sample Check

- Paper-based predecessors: the Danish Refugee Council case study describes digitizing a paper-based case management system; a digitized registry with enrollment + service records + closure still satisfies L0 — no cloud, no mobile, no offline sync required.
- Church/community registries: simple member-aid lists with visitation/assistance records fit L0 without any funder-reporting machinery.
- Older desktop-era human-services systems (pre-SaaS case management, e.g., the pre-Bonterra Social Solutions products named in Apricot's own FAQ history) fit L0 — packaged forms + caseloads + exits/enrollments + reporting.
- Government social-welfare legacy systems fit the same core with statutory wrapping.
- Conclusion: L0 does not over-fit to the current mobile-first, SaaS, funder-dashboard market shape.

## Uncertainties

1. **Type-status question (main)**: whether "Beneficiary Management" should remain an independent leaf or be folded into Nonprofit Case Management. Market terminology leans toward "case management" as the product-category name; "beneficiary management" is the natural name of the *registry layer* and is used as a category label mainly in humanitarian contexts. Recorded in STATUS Boundary Issues; not resolvable without a dedicated pass on Nonprofit Case Management / Nonprofit Program Management leaves.
2. Depth of permission granularity per product (field-level vs record-level vs conditional rules) could not be verified from operational help docs; only vendor summaries were reachable.
3. Household- vs person-level modeling frequency across the wider market is uncertain (sample leans person-with-household-option).
4. Precise identity-verification practices (ID checks, biometrics in humanitarian registration) were not evidenced in the reached sources and are therefore not characterized.
5. Salesforce NPSP module structure (commonly cited CRM-embedded approach) unverified — excluded from all claims.

## Final Synthesis

Beneficiary Management is the people-served counterpart of donor management: an organization-operated registry of the people (and households) it serves, bound to the organization's programs, accumulating dated records of assistance actually delivered, with tracked participation from entry to exit. Around this invariant, mature products add configurable intake/eligibility forms, deduplication, caseload/caseworker structures, referrals, strict access control with audit, and — the sector's reason for existing — aggregate reporting of services and outcomes to funders and coordinators. The market mostly sells this capability under the banner of "case management" or as part of MEAL/CRM platforms; the leaf is defensible as an independent Type only on the registry-vs-episode center-of-gravity distinction, which is flagged for taxonomy review.
