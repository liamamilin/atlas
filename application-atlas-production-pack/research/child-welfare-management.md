# Research Notes — Child Welfare Management

Research date: 2026-09-06
Slug: `child-welfare-management`
Directory leaf: "Child Welfare Management" (§24 Government, Public Sector & Civic)

## Research Goal

Understand what child welfare management software actually is as an Application Type: what records exist inside it (children, families, cases, placements), how a report of concern becomes a statutory casework episode and then a permanency outcome, which roles participate (caseworker, supervisor, intake, licensing, legal, provider), which rules govern behavior (confidentiality, mandates, court/legal status), and where the boundary lies against social services case management, public sector case management, court case management, and health-care care-management Types.

## Initial Boundary (hypothesis before research)

- Core hypothesis: a government (or contracted agency) casework system for child protection and welfare: intake of reports of suspected abuse/neglect → screening → safety/risk assessment → casework episode (in-home services or out-of-home placement) → permanency (reunification, adoption, guardianship) → closure, over identified child + family records under extreme confidentiality.
- US framing: state SACWIS/CCWIS systems of record; county agencies; commercial products either replace the state core (COTS waiver), supplement it, or sit on a platform.
- UK framing: local authority children's social care case management (children in need, child protection plans, looked-after children).
- Likely confusions: Social Services Case Management, Public Sector Case Management, Nonprofit Case Management, Court Case Management, Care Plan Management / Care Coordination (health), Beneficiary Management, child support enforcement (different domain), foster-care placement software (a slice of this Type).

## Research Questions

1. What are the core records? (child, caregiver, household/relationship, referral, case, assessment, placement, carer/home resource, provider, legal events)
2. How does a report of concern enter, and what does screening produce?
3. What do assessment/investigation structures look like (safety plans, assessments, findings)?
4. What is the case lifecycle and who owns it (caseworker, supervisor approval)?
5. How are placements managed (carer recruitment/licensing, matching, moves, permanency goals)?
6. How do legal/court processes appear in the record?
7. How do payments/finance and provider relationships appear?
8. What reporting/regulatory machinery exists (US federal reports, UK statutory returns)?
9. What confidentiality/permission machinery is structural?
10. Where is the boundary vs generic social-services/public-sector case management?
11. What varies by region (US vs UK), customer tier (state/county/private agency), and product posture?

## Representative Products

Selected for market representativeness, documentation accessibility, and different product philosophies / customer tiers / geographies:

| Product | Philosophy | Tier / Geography | Evidence access |
|---|---|---|---|
| Casebook (Casebook PBC) | modern configurable commercial SaaS core; CCWIS-ready with ACF COTS waiver; child welfare + foster care/adoption programs | US, state/county/private agencies | official product pages (child welfare, foster care & adoption, platform overview) — Layer A |
| Northwoods Traverse | agency-side casework/documentation layer for county child welfare; mobile/offline; bidirectional exchange with state systems | US county human services | official product pages (Traverse for Child Welfare, Modules) — Layer A |
| System C / Liquidlogic Children's Case Management | UK local authority children's social care statutory case management (CIN / child protection / looked-after children); family records + carer records + placement finance | UK local government | official product page + FAQ — Layer A |
| WellSky Protective Services (adult) | adjacent analog: same protective-services casework pattern for adult protective services — used only for boundary/family-pattern evidence, NOT a child welfare product | US state programs | official product page — Layer A (boundary-informing) |
| Salesforce (Public Sector / HHS) | platform/CRM posture for government case management — market anchor only; no child-welfare-specific operational claims drawn | cross-region | official industry page — Layer B (positioning only) |

Abandoned samples (recorded limitation): extendedReach (extendedreach.com root + support subdomain 403 ×2 — per network rules abandoned), Salesforce child-welfare-specific solution docs (industry pages generic; solution doc IDs not discoverable), Tyler Technologies, WellSky child-welfare-specific product (child welfare 404; vendor serves the domain via human-services platform).

## Sources

Fetched 2026-09-06:

- Casebook — https://www.casebook.net/ (platform overview)
- Casebook Child Welfare — https://www.casebook.net/casebook-child-welfare-software/
- Casebook Foster Care & Adoption — https://www.casebook.net/casebook-for-foster-care-and-adoption/
- Casebook platform overview — https://www.casebook.net/platform-overview/
- Northwoods — https://www.teamnorthwoods.com/ (root)
- Northwoods Traverse for Child Welfare — https://www.teamnorthwoods.com/traverse/traverse-program-areas/traverse-for-child-welfare/
- Northwoods Traverse Modules — https://www.teamnorthwoods.com/modules/
- System C — https://www.systemc.com/ (root; liquidlogic.co.uk redirects here)
- System C Liquidlogic Children's Case Management — https://www.systemc.com/local-government/liquidlogic-childrens-case-management/
- WellSky Protective Services (adult) — https://wellsky.com/solutions/community/protective-services/
- Salesforce Public Sector — https://www.salesforce.com/industries/public-sector/ (positioning only)

Not reachable (recorded limitation): extendedreach.com + support.extendedreach.com (403 ×2), wellsky.com/solutions/child-welfare/ (404), Salesforce child-welfare-specific docs (not discoverable via Bing; bing.com generic results; duckduckgo transport error), System C customer centre (login-gated), Casebook help KB at gohub.casebook.net (not fetched), help.teamnorthwoods.com (linked but not fetched).

## Product Observations

### Casebook (Casebook PBC) — Evidence Layer A (official product pages)

- Positioning: "configurable human services software … from intake through reporting" for government agencies, nonprofits, and social service providers; child welfare is a named program area alongside youth & family, foster care, victim services, workforce, tribal.
- Child welfare page: incubated by the Annie E. Casey Foundation; "the first modern Child Welfare system granted a COTS waiver by the Administration for Children and Families (ACF)".
- CCWIS and federal reporting-ready: "Casebook collects all data required for AFCARS, NYTD and NCANDS reporting, enabling administrators to prepare files for Federal submission easily."
- Central system of record; API-first; RESTful interoperability; bidirectional data exchange with partners; configurable reporting for internal/external stakeholders.
- Foster care & adoption page: "recruiting foster or adoptive parents to documenting, assessing, and tracking homes, children, and families"; digitized process including "a client-facing portal for intake, and customizable forms for eligibility assessment, licensing, placements and long-term tracking".
- Person profile: "attach files, view vital information, track progress and assess services, incidents and relationships for a full view of a person's history of involvement, profile notes, application status and more."
- Placement: "Place children with families based on your criteria. With custom forms, mapping and person-profile you can filter, assess and place with both the big-picture and important details in focus."
- Licensing tracking: customer quote "filter by status, who's done what and where they are in the license process"; "no-wrong-door point of entry solution to track calls, emails, attach documents, and report incidents related to foster homes and foster children and parents."
- Platform capabilities: form building (multistage custom forms), service planning (individualized service plans, provider services), scheduling & notifications, workflows & messaging (task assignment, real-time collaboration), enhanced case notes, service directory & tracking ("services each client is involved in, the service providers, enrollment dates, and notes … changes and outcomes over time"), built-in & custom reports (drag-and-drop data picker), data-quality dashboard.
- Security: AWS hosting, encryption, HIPAA compliance, SOC-II audit; "built in restrictions that will limit users access to records they're not supposed to see" — need-to-know access restriction explicitly named.
- Person-centric model: "we have a person-centric model that collects everything in an organized manner."

### Northwoods Traverse — Evidence Layer A (official product pages)

- Positioning: "cloud-based, AI-powered software for health and human services professionals", "built for caseworkers, by caseworkers"; child welfare is one of four program areas (with adult & aging, child support, economic assistance).
- Child welfare program areas supported: "child protective services; investigation, intake, and assessment; ongoing services and case management; foster care and kinship placement; adoption support; children's mental and behavioral health" (modules page). Child welfare page adds: adoption, assessment, kinship, intake, investigation, ongoing case management.
- What workers do with it: identify kin/family avenues; complete "releases and referrals in minutes"; understand "risks, strengths, and needs using current and historical data"; surface "medical reports, police records, and case history"; share documentation (consent/release forms) with families in real time; "receive quick approvals and supervisor input on safety and support plans"; finish "case notes, closings, and collect collateral info in the field"; "spend more time preparing for court, reunification, or adoption."
- Mandate compliance: "Meet investigation and home visit deadlines" (customer stat "97% of safety assessments on time" — product-specific, not generalized).
- Traverse Mobile: "complete forms; capture documents, audio, and video; and take photos automatically tagged with dates, times, and case and client connections … regardless of location or connectivity" (offline capable).
- Integration posture: "Traverse supports bidirectional data exchange and integrates with your state case management systems and existing tools" via iPaaS/APIs/connectors — i.e., the state child welfare system is the system of record and Traverse is the agency-side working layer. Product-page evidence that the US market has a state-core + agency-supplement split.
- Modules: Document Management (collect/complete/sign/share forms), Forms Management (auto-fill, exact-match of original hospital/school forms), Case Discovery 2.0 (AI timelines; summarize multiple documents/photos/audio/video; "identify key people, events, and safety concerns with AI insights"), Traverse Connect (portal: clients/providers upload documents from any device; forms for review/signature; verification), Workflow ("automatically route content to the right person based on type; assign due dates, flag items as high priority"), Traverse Reports (client/case/admin data; compliance reporting and audits), Family Mapping ("automatically identify people and connections from case files … improve kinship placement efforts"; "export and share family maps across the agency or in court"), Policy Assist (AI answers on policy/procedure).
- Security: AWS; "meets strict HIPAA and FedRAMP standards; data is encrypted in transit and at rest."
- Customers: US county agencies (Mesa County CO Department of Human Services, Scott County, Carver County, Jackson County OH, Morgan County OH).

### System C / Liquidlogic Children's Case Management — Evidence Layer A (official product page + FAQ)

- Positioning: "the UK's leading case management solution for children's social care"; "designed by practitioners, it manages case records for children in need, those under child protection plans, looked-after children, and care-experienced young people."
- Carer-side records: "facilitates the assessment and ongoing support of connected persons, foster carers, special guardians and adopters."
- Pathway maps: "intuitive pathway maps ensure compliance with regulations" — user-friendly maps that "help social workers visualise the journey of a child or carer through statutory processes."
- Customisable workflows: "management of cases across Child In Need, Child Protection, Children Looked After, and other key workflows."
- Family Working: "combines individual child records with the ease of single forms for siblings. Shared details are entered once, while unique needs are recorded separately … keeps individual records and provides a family view"; "Multi-agency chronology and Single View support coordinated care and effective triaging."
- Multi-agency collaboration: portals for information sharing "with external agencies, children, parents, and carers"; Delegation functionality ("real-time multi-agency contributions to assessments and forms … Local Authorities … delegate sections of an assessment or form to different users or teams"); Delegation Portal extends to external professionals "without the need to access the wider Children's Social Care Case Management system … access only to the specific form/questions they have been assigned"; "configurable privacy settings protect sensitive data."
- SingleView: "displays data from various sources … integrates information from the Children's Social Care System and third-party databases like Education, Youth Offending, Connexions, and Housing"; "permission-controlled access ensures appropriate data visibility."
- Finance: "an integrated finance solution that supports generating payments linked to social work activities, such as starting a placement and paying providers … budget monitoring and cost-benefit analysis."
- Early Help module: "case management for children and families who need support but do not meet social care thresholds, facilitating service requests, eCAF management, and referrals to and from social care."
- AI: FormFlow AI Assistant ("automates transcription, form population, and case note creation from practitioner-family conversations"; "government-certified").
- Customers: English local authorities (Kent, Durham, Cambridgeshire, East Sussex, Hull, Buckinghamshire, Swindon, Staffordshire, St Helens, Wiltshire).

### WellSky Protective Services (adult) — Evidence Layer A (boundary-informing only)

- Adult protective services (APS) software — the adult analog of the protective-services casework pattern. NOT a child welfare product; used only to establish the shared pattern family and the boundary.
- End-to-end process: "the initial report of an incident, screening, investigation, and data reporting"; optional modules "for care planning, service authorization and delivery, and financial management."
- Records: "client and perpetrator data from prior cases" surfaced during new intakes; "database of participants in previous intakes and investigations, as well as contact histories."
- Investigator safety: "Alert notes inform investigators of potential threats they may encounter on-site."
- Milestone machinery: dashboards "identify cases where milestones are in danger of being missed, there is insufficient documented activity, or cases appear to be stuck"; "schedule critical milestone dates to comply with state regulations … system alerts … timely completion of risk assessments and documentation."
- Federal reporting analog: NAMRS report export (Agency/Key Indicators/Case Components) — the adult analog of US child welfare's federal reporting burden.
- Mobile assessments "with or without the internet"; web intake form saves "an intake record … for further processing."

### Salesforce (Public Sector) — Evidence Layer B (positioning only)

- Government case management/CRM platform posture: "integrated view of case data, AI-powered automation, digital-first collaboration"; FedRAMP-authorized Government Cloud; HHS solutions exist ("Connect constituents with the care they need … human services outcomes"). No child-welfare-specific operational structures documented on reachable pages; no claims drawn beyond platform posture.

## Cross-product Comparison

| Aspect | Casebook | Northwoods Traverse | System C Liquidlogic (UK) |
|---|---|---|---|
| Protected person record | person-centric model (client/person profiles; full view of involvement history, relationships, incidents) | case files organized per child/client; Case Discovery identifies people/events from files | individual child records; Family Working keeps individual records + family view |
| Family/caregiver context | person profiles with relationships; foster/adoptive family records | Family Mapping (people/connections from case files; kinship placement) | Family Working (siblings, shared forms); family view; multi-agency chronology |
| Report/intake | no-wrong-door entry tracking calls/emails/documents/incidents (foster care page); client-facing portal for intake | intake program area; Traverse Connect portal intake | referrals to/from social care; Early Help service requests; (UK MASH-style intake implied, not documented) |
| Screening/assessment | configurable assessments/forms (eligibility assessment) | investigation/intake/assessment program area; safety plans; risk/strengths/needs from data | assessments with pathway maps; delegated multi-agency contributions to assessment forms |
| Case lifecycle & ownership | cases with case notes, tasks, workflows, reporting | ongoing case management; workflow routing, due dates, priority | statutory pathways: Child In Need → Child Protection → Looked After; manager authorisation tasks |
| Supervisor role | supervisor dashboards; team collaboration | "quick approvals and supervisor input on safety and support plans" | manager authorisation of shared forms |
| Placement & carers | foster/adoptive parent recruiting → eligibility/licensing forms → placements; "place children with families based on your criteria"; license-process tracking | foster care and kinship placement; adoption support | connected persons/foster carers/special guardians/adopters assessed and supported; placement events |
| Permanency | adoption program; long-term tracking | reunification/adoption as outcome time horizons | looked-after children → care-experienced young people (post-care continuity) |
| Legal/court | not documented on fetched pages | "preparing for court"; family maps shared "in court" | statutory processes via pathway maps (court specifics not documented on fetched page) |
| Services/providers | service directory & tracking (providers, enrollment dates, notes) | releases/referrals; Traverse Connect with outside providers | Early Help service requests; delegated contributions from external agencies |
| Finance | not documented beyond reporting | not documented | integrated finance: payments linked to social work activities ("starting a placement and paying providers"), budget monitoring |
| Regulatory/reporting | AFCARS/NYTD/NCANDS data collection; CCWIS posture | Traverse Reports for "compliance reporting and audits" | regulatory compliance via pathway maps (UK statutory returns not documented) |
| Confidentiality machinery | access restrictions limiting records users can see; HIPAA/SOC-II; AWS | HIPAA/FedRAMP; encrypted transit/at rest | permission-controlled visibility; configurable privacy settings; Delegation Portal scoped access |
| Multi-agency sharing | bidirectional exchange with partners | bidirectional exchange with state systems | portals, Delegation, SingleView (education/youth offending/housing) |
| Mobile/offline | mobile-ready | Traverse Mobile: offline; auto-tagged photos/audio/video | (not documented on fetched page) |
| AI | (current gen) | Case Discovery, Family Mapping, Policy Assist | FormFlow AI transcription → forms/notes |
| Deployment | SaaS (AWS), per-user pricing | SaaS (AWS) | local-authority deployment; suite with education/finance/adults modules |

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which the Type stops being recognizable:

```text
Identified child (protected person record)
└── Family / caregiver context (household & caregiver records linked to the child)
    └── Statutory referral / report of concern with a recorded screening decision
        └── Safety / risk assessment with recorded findings
        └── Casework episode under an accountable caseworker (tracked lifecycle)
            └── Out-of-home placement & permanency as first-class structures
                (when children cannot remain at home)
```

Plus one defining behavioral rule:

- **Need-to-know confidentiality over the whole record** — access to child welfare records is restricted to those with a role-based need; the product's permission model is structural, not cosmetic.

Six structural properties + one rule, each supported across the sample:

1. **Identified child as protected person record** — Casebook: person-centric model with involvement history; Liquidlogic: individual child records (explicitly per child even inside family forms); Traverse: per-child case files. Historical check: paper child-welfare case registers centered the same per-child record. Without an identified protected person, the product is not child welfare software.
2. **Family/caregiver context attached to the child** — every sample models the family around the child: Casebook person profiles with relationships; Traverse Family Mapping (people/connections); Liquidlogic Family Working (siblings share forms but keep individual records). Child welfare casework is family-based; a system that manages only the individual is generic case management.
3. **Statutory referral/report of concern with a screening decision** — the work enters as a report/concern about a child (Casebook no-wrong-door intake tracking calls/emails; Traverse intake program area; Liquidlogic referrals to/from social care + Early Help service requests). WellSky APS shows the same pattern in the adult analog (report → screening → investigation). The screening decision (accept/redirect/no-further-action) starts and legally anchors the casework episode.
4. **Safety/risk assessment with recorded findings** — Traverse safety plans and risk/strengths/needs analysis; Liquidlogic structured assessments on statutory pathways; Casebook eligibility/assessment forms. The assessment is what converts a report into a decision (substantiate, provide services, remove, close).
5. **Casework episode under an accountable caseworker with a tracked lifecycle** — all three carry case records with case notes, tasks/workflow routing, due dates, and supervisor approval (Traverse "supervisor input on safety and support plans"; Liquidlogic manager authorisation tasks; Casebook supervisor dashboards + collaboration). The case is the durable unit of statutory work between openings.
6. **Out-of-home placement & permanency as first-class structures** — Casebook: foster/adoptive home recruiting, licensing forms, placements, adoption; Traverse: foster care & kinship placement, adoption support, permanency; Liquidlogic: looked-after children pathway, carer assessment (foster carers/special guardians/adopters), placement-linked payments. Not every case uses placement, but a system that cannot carry placement, carer resources, and permanency goals is social services case management, not child welfare management.

**Defining rule: need-to-know confidentiality** — Casebook explicitly restricts records users may see; Liquidlogic uses permission-controlled visibility, scoped delegation, and configurable privacy settings; Northwoods runs HIPAA/FedRAMP government-grade controls. Child welfare records are among the most legally protected records in any jurisdiction; the permission model is part of what the product is.

Historical/regional check (market-sample check): pre-digital child welfare (paper case files, child protection registers, placement ledgers) exhibits all six properties without any modern machinery. UK local authority systems (Liquidlogic) satisfy the definition with entirely different statutory vocabulary (children in need / child protection plans / looked-after children) and no US federal reporting. US county deployments (Traverse) satisfy it as an agency-side layer without being the state system of record. Tribal/First Nations deployments (Casebook tribal program) fit. Therefore the defining core must NOT include: US federal reporting codes (AFCARS/NCANDS/NYTD), CCWIS/COTS-waiver posture, hotline phone numbers, court-module specifics, payment engines, or AI.

### L1 — Common Mature Structure

Present in most mature modern products, not required for the definition:

- Case notes / contact documentation as a narrative record over the case (all three).
- Structured, configurable forms and assessment instruments per program (form builders in Casebook and Traverse; Liquidlogic forms/pathways).
- Task/workflow routing with due dates, priorities, and supervisor review/approval gates (Traverse Workflow; Casebook workflows & messaging; Liquidlogic authorisation tasks).
- Service referral to external providers and service directory/tracking (Casebook service directory; Traverse releases/referrals + Traverse Connect; Liquidlogic Early Help referrals).
- Family/relationship mapping and kinship search (Traverse Family Mapping; Casebook mapping on person profiles).
- Mobile/offline field capture with media auto-attached to case and client (Traverse Mobile; Casebook mobile-ready).
- Client/family/provider portals for document exchange, forms, and e-signatures (Casebook client-facing portal; Traverse Connect; Liquidlogic portals for children/parents/carers).
- Multi-agency information sharing beyond the agency boundary, scoped by permissions (Liquidlogic Delegation + SingleView; Traverse state-system exchange; Casebook bidirectional exchange).
- Reporting/analytics: caseload, milestones, compliance, audit preparation (all three).
- Alert/notification machinery for deadlines, milestones, and worker safety (Traverse mandates; WellSky APS alert notes as pattern analog).
- Regulatory/federal reporting data capture (Casebook AFCARS/NYTD/NCANDS; Traverse compliance reports; UK statutory returns implied by pathway compliance but not documented).
- Integration/exchange with state or national systems and partner agencies (all three).
- Legal/court involvement tracking (court preparation, legal-status attributes) — strongly present (Traverse court prep) but documented unevenly; kept at L1, not L0.

### L2 — Variant / Optional Structure

Depends on region, customer tier, regulatory posture:

- **System-of-record posture** (US): state SACWIS/CCWIS core vs commercial COTS core under federal waiver (Casebook's ACF COTS waiver) vs agency-side supplement layer exchanging with the state system (Traverse).
- **Customer tier**: state agencies vs county agencies vs private/nonprofit delivery agencies (Casebook serves all three; Traverse county-focused).
- **Regional program vocabulary**: US (investigation/in-home/foster care/adoption) vs UK (children in need / child protection plans / looked-after children / care-experienced) — different labels for the same skeleton.
- **Placement-side depth**: carer recruitment/licensing/home-study machinery (Casebook, Liquidlogic carer records); kinship emphasis; adoption programs.
- **Finance/payments**: placement- and provider-linked payments and budget monitoring (Liquidlogic integrated finance); absent or deferred in others' fetched documentation.
- **Prevention tier**: early-help/pre-statutory case management below intervention thresholds (Liquidlogic Early Help module).
- **AI assistance**: conversation-to-form capture (Liquidlogic FormFlow), case-file analysis/timelines (Traverse Case Discovery), policy Q&A (Traverse Policy Assist), family-map generation.
- **Regulatory security postures**: HIPAA/FedRAMP (US), CJIS posture (Casebook publishes a CJIS page), government certification of AI (Liquidlogic).
- **Tribal/First Nations variants** (Casebook tribal program).
- **Suite composition**: standalone case management vs bundled with social-care finance, education case management, adult social care (System C suite).

### L3 — Vendor-specific (research notes only)

- Casebook: Annie E. Casey Foundation incubation; "first modern child welfare system with ACF COTS waiver" claim; "about 80% out of the box" configurability; drag-and-drop report builder; AWS us-east-1/ca-central-1 + nightly backups; 8am–8pm ET support; per-user pricing; CJIS page; gohub.casebook.net knowledge base.
- Northwoods: Traverse/Grove product naming (Grove = human-powered case-aide service); Case Discovery 2.0; Traverse Connect; Policy Assist; Family Mapping; marketing stats ("2 more productive hours a day", "around $50 per worker, daily" overtime/mileage, "97% of safety assessments on time", "45,000 caseworkers", "55.5 million+ content items"); Mesa County customer story; help.teamnorthwoods.com customer stories.
- System C/Liquidlogic: SingleView; Delegation/Delegation Portal; Family Working; FormFlow AI Assistant ("government-certified"); Early Help; eCAF; Social Care Finance; Education Case Management integration; "UK's number-one" claim; St Helens/Wiltshire/Swindon/Staffordshire customer stories; Connexions/Youth Offending/Housing integrations; CareFlow EPR sibling.
- WellSky: NAMRS export; "most widely used solution for adult protective services" claim; Web Intake Form; HSS Advisory Board.

## Vendor-specific Findings

See L3. None entered the canonical model. The US federal reporting triad (AFCARS/NCANDS/NYTD) and CCWIS posture are documented US regulatory layers (Casebook) and stay at L1/L2 — the UK sample runs the full Type without them.

## Rejected Findings

- "Child welfare management = federal reporting machinery" — rejected: AFCARS/NCANDS/NYTD are US-specific regulatory layers; the UK sample and historical samples satisfy the Type without them.
- "It is just case management for children" — rejected: what distinguishes the Type is the statutory protection loop (report → screen → assess → case) plus placement/permanency structures and the confidentiality regime; a plain case-management core without those is a different Type.
- "Placement operations are the Type" — rejected: placement is one defining structure inside the full statutory casework loop; foster-care placement software alone misses intake/assessment/permanency.
- "Adult protective services is the same Type" — rejected: same protective-services casework pattern family, different protected population and program law; WellSky APS used only as boundary/pattern evidence.
- "Foster-parent recruiting/marketplace features are defining" — rejected: placement-side capabilities (L1/L2).
- "AI assistance is defining" — rejected: current-generation, product-specific (L2).
- "Court case management is part of the Type" — rejected as structure: legal events/legal status attach to the child welfare case; the court docket is a separate Type (Court Case Management System).
- "Payments are defining" — rejected: only one sampled product documents integrated finance (Liquidlogic); common but not definitional.

## Boundary Findings

- **vs Social Services Case Management (§24 sibling, unprocessed)**: closest seam. Child welfare management is the statutory child-protection/permanency specialization: the protected person is a minor, reports trigger legally mandated screening/assessment, the case can end in state custody/placement, and permanency is a legally defined outcome. Test: remove the child-protection mandate, safety assessment, and placement/permanency structures → generic social services case management remains; add them → child welfare management. Joint-review flag recommended (sibling unprocessed).
- **vs Public Sector Case Management (§24 sibling, unprocessed)**: generic government casework (intake → route → work → close) lacks the child/family person model, safety assessment, placement resources, and permanency lifecycle. Test: does the system know what a placement is? If not, it is generic public sector case management.
- **vs Nonprofit Case Management (§25 sibling, unprocessed)**: private child welfare agencies deliver services using case management records; but Child Welfare Management carries the statutory loop (mandated intake, court-anchored decisions, placement authority) regardless of which organization operates the software. Products like Casebook span both from one platform — packaging overlap, not Type identity. Related: beneficiary-management pass flagged that market vocabulary conflates case management names.
- **vs Court Case Management System (§24)**: court systems manage dockets/hearings/filings for the judiciary; child welfare systems track legal status, court events, and court-preparation artifacts as attributes of the child's case. Test: remove hearings/dockets → child welfare remains; remove the child/family/placement model → court case management remains.
- **vs Care Plan Management / Care Coordination (§22, processed)**: both organize goals/services around a person, but health care plans are clinical/assessed-needs records without statutory screening, custody, or placement; care-plan pass already recorded "held vs Social Services Case Management" from the health side.
- **vs Child Support Enforcement** (not a §24 leaf, but the market ships it separately): Northwoods maintains Traverse for Child Support as a distinct program area (intake/case establishment, paternity, collections) from Traverse for Child Welfare — vendor evidence that child support (financial) and child welfare (safety/protection) are different Types despite similar names.
- **vs Adult Protective Services software**: adjacent analog sharing the report→screen→investigate→case pattern and federal reporting burden (NAMRS); different protected population and program. Vendors serve both from related product families (WellSky) — pattern-family adjacency, not the same Type.
- **vs Foster care agency management / placement software (e.g., extendedReach class)**: placement-side slice of this Type; when packaged alone (private foster agencies) it is a partial implementation, not a different Type.
- **vs Early Help / prevention case management**: Liquidlogic ships Early Help as a module of the same system — cases below statutory thresholds. Treated as a variant tier, not a separate Type, because it reuses the person/family/case spine.
- **Removal test for the Type itself**: remove screening/assessment machinery → intake-and-referral platform; remove placement/permanency → social services case management; remove the child-focused person model → generic case management; remove need-to-know confidentiality → not a lawful child welfare system in any sampled jurisdiction.

Taxonomy observation: the leaf name ("Child Welfare Management") is narrower than some market vocabulary ("child welfare information system", "children's social care case management") but matches the family of statutory child welfare/child protection casework systems. No conflicting directory leaf exists; no rename proposed.

## Uncertainties

- No Tier-1 help-center documentation was reachable for any sampled product (all evidence is official product pages/FAQs; Casebook KB and Northwoods help center exist but were not fetched; System C customer centre is login-gated). Consequently no precise operational claims were verified: no exact case-state vocabularies, no numeric limits, no default values, no timing rules are asserted in the final document.
- Court/legal module depth is documented only indirectly (Traverse court prep; Liquidlogic statutory pathway maps); the exact treatment of hearings/orders inside these products was not observed.
- UK statutory returns (DfE reporting) are implied by compliance framing but not documented on the fetched page.
- extendedReach (a major private-agency child welfare product) and Salesforce child-welfare solution docs were unreachable; the sample rests on three documented products plus one adjacent analog.
- The relative market weight of state-core vs agency-supplement vs commercial-core postures in the US could not be quantified from accessible sources.
- Intake/hotline machinery (centralized screening units) is inferred from program-area naming and the WellSky APS pattern; none of the fetched pages documents hotline operations in detail.

## Final Synthesis

Child welfare management software is the statutory casework system for protecting children. Its world is organized around an identified child and the family/caregiver context around that child. Work enters as a report of concern, is screened, and — where accepted — opens a casework episode under an accountable caseworker, structured by safety/risk assessments with recorded findings. The system carries, as first-class structures, the out-of-home placement machinery (carer/home resources, licensing, matching, placement events) and the permanency lifecycle (reunification, kinship/guardianship, adoption) that govern children who cannot remain at home. Everything sits under need-to-know confidentiality enforced by the product's permission model. Around this core, mature products add configurable forms/assessments, case notes, task/workflow routing with supervisor approval gates, service referrals and provider directories, family/kinship mapping, mobile-offline field capture, family/provider portals, scoped multi-agency sharing, reporting/audit machinery, regulatory reporting data capture, and integration with state or national systems. The defining core is jurisdiction-neutral: US (state/county, CCWIS posture or COTS core), UK local authority (children in need / child protection / looked-after children), tribal, and private-agency deployments all satisfy it with different vocabulary. The Type is bounded by social services case management (no statutory protection loop, no placement/permanency), generic public sector case management (no child/family/placement model), court case management (dockets vs case-attached legal status), and adult protective services (same pattern, different protected population).
