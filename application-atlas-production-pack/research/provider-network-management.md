# Research Notes — Provider Network Management

Research date: **2026-09-09**. All fetches from the research environment; failures abandoned after 1–2 attempts per the network rule.

## Research Goal

Understand what a **Provider Network Management** application is as an Application Type: what objects exist inside it (providers, credentialing files, contracts, fee schedules, networks, directories), who operates it (which seat of the payer–provider relationship), how a provider moves from recruitment to participation to termination, what rules govern the network, and where the Type's boundary sits — especially against the two §22 siblings that pre-hung flags for this pass (**health-plan-administration-system**, **payer-claims-processing**), plus provider-side credentialing and member-facing directories.

## Initial Boundary (hypothesis before research)

- PNM is **payer-side** software: the health plan's system for managing its contracted network of healthcare providers.
- Expected center: provider data + credentialing + contracting + network adequacy + provider directory.
- Nearest neighbors: Health Plan Administration System (payer system of record — carries a provider master), Payer Claims Processing (consumes network status), provider-side credentialing (medical staff office / provider groups), provider directories (member-facing surface), Provider Claims Management (provider-side billing).
- Unknowns: whether credentialing is definitional or common; whether adequacy/directory machinery is definitional; whether a payer-suite module variant is materially different; how network status reaches claims adjudication.

## Pre-hung flags to discharge (from prior passes)

1. **health-plan-administration-system (processed 2026-09-08)**: "provider contracting, credentialing, fee schedules, network adequacy vs the administration core's provider master and settlement seam… network machinery is a candidate separate Type. Flag for that pass." Also its rejected finding: "Provider network contracting/credentialing is the core" — rejected there because the provider master and settlement seam are L1 in HPAS; full contracting/credentialing/adequacy machinery belongs to PNM territory.
2. **payer-claims-processing (processed 2026-09-08)**: "vs provider-network-management — provider master + settlement seam here vs contracting/credentialing/fee-schedule machinery there (consistent with the HPAS pass's flag)."

Both discharged below (Boundary Findings #1, #2).

## Research Questions

1. What is a "provider" in this context — individual, group, facility? How is the provider record structured?
2. What exactly is credentialing in the payer context (application, primary source verification, committee approval, re-credentialing)? Can its execution be delegated?
3. What is the contracting machinery (contracts, amendments, fee schedules, effective dates, termination)?
4. What is network adequacy and who monitors it (time/distance standards, specialty coverage)?
5. What is provider directory management and what drives its accuracy rules?
6. How does network participation status reach downstream operations (claims, member services)?
7. Who uses the system, in which roles?
8. Where are the boundaries: vs HPAS, vs payer claims processing, vs provider-side credentialing, vs member-facing directories?

## Representative Products

| Product | Seat / posture | Why sampled |
|---|---|---|
| **Andros** (andros.co) | payer-side full-lifecycle PNM (CVO services + platform) | the most explicit "provider network management" self-description in the sample; covers credentialing, contracting, PDM, network design, committee management |
| **Medallion** (medallion.co) | credentialing/enrollment operations platform serving payers AND provider orgs | the credentialing/enrollment machinery pole; also evidences the provider-side mirror (payer contract management, privileging) for boundary work |
| **Kyruus Health** (kyruushealth.com) | care-access platform for payers (provider data + directory/search) | the directory/member-facing pole; shows where PNM drifts into member engagement |
| **DataSpring, powered by CAQH** (dataspring.com) | industry data infrastructure (provider-sourced data cooperative) | the industry-utility pole: shared credentialing application, PSV, sanctions monitoring, directory attestation, adequacy data |
| **Availity** (availity.com) | payer-provider network + Provider Lifecycle Solutions | the network-scale PDM/attestation/intake pole; explicit "provider lifecycle management" definition |

Selection rationale: market representation across the payer-side PNM landscape, different product philosophies (full-lifecycle services+platform vs operations platform vs care-access vs data cooperative vs connectivity network), different customer tiers (national payers, regional plans, provider groups, digital health), and coverage of both seats for boundary work.

## Sources

Fetched successfully (Tier 1/2 official pages):

- Andros — root (credentialing/CVO), /network-lifecycle-platform/, /strategic-network-design/ — 2026-09-09
- Medallion — root, /solutions/payer-contract-management — 2026-09-09
- Kyruus Health — root (kyruus.com redirects to kyruushealth.com), /health-plans/ — 2026-09-09
- DataSpring (formerly CAQH) — root, /solutions/provider-data/credentialing-suite, /solutions/provider-data/directory-management — 2026-09-09
- Availity — root, /provider-lifecycle-solutions/ — 2026-09-09

Attempted and unreachable (abandoned per network rule; no claims made from them):

- Quest Analytics — www.questanalytics.com 403 ×2 (root + /network-adequacy/). The adequacy-analytics leader is therefore a market anchor only.
- NCQA — ncqa.org credentialing program page 403.
- CMS — cms.gov network-adequacy resource page 403.
- TriZetto QNXT / HealthEdge HealthRules Payer — unreachable in the prior HPAS and payer-claims passes (carried limitation); the payer-suite embedded-module variant rests on the HPAS pass's observation that sampled CAPS products carry provider data/portals inside the core.

Regulatory grounding note: credentialing standards (NCQA/URAC), directory accuracy rules, and adequacy standards are evidenced **from vendor compliance claims** (NCQA-certified CVO, NCQA-compliant sanctions monitoring, URAC accreditation, "state and federal regulatory compliance") rather than primary regulatory text. All regulatory statements in the outputs are kept at concept level.

## Product A — Andros (payer-side full-lifecycle PNM)

### Key observations (evidence layer A unless noted)

- Self-description (footer, every page): "Offering comprehensive, end-to-end healthcare provider network management services, including **recruitment and contracting, credentialing, and provider data management**." — the Type name appears verbatim in the vendor's own framing.
- Network Solutions lines: Credentialing (CVO), Strategic Network Design, Provider Network Development, Compliance Services, Committee Management, Medicare Advantage network building, "Contract with a Payor" (provider-side service — see Boundary Findings).
- **CVO credentialing workflow** (root page): provider-approved application process (API/batch/provider-filed intake; "two out of three of our application processes don't require any provider input") → automated primary source verification (data-matching algorithms; flags "malpractice, licensure, or sanctions issues") → trained professional oversight (staff contact providers/facilities, quality checks to NCQA standards) → credentialing report/profile ("specialty, languages, malpractice information, credentialing status and much more"; delivered as PDF, web portal, or API) → **Network Approval Management** ("level providers, identify risk to the committee… facilitate committee meetings and administration").
- Credentials: "Fully NCQA-Certified CVO" (strictest level), URAC-accredited Credentials Verification Organization, SOC 2 Type 2. Scale claims: "Built 200+ networks in all 50 states", "Perform 300k credentials annually" (marketing figures — L3 only).
- **Network Lifecycle platform page**: "A network lifecycle is a comprehensive, connected framework that supports every stage of the provider network journey. From **recruitment to credentialing to contracting, monitoring, and optimization**." Legacy-vs-modern table rows: credentialing (paper-based → automated), **network adequacy** ("periodic, geography-focused evaluations" → "continuous, data-driven, population-specific"), compliance (retrospective → audit-ready).
- **PDM positioning** (same page): "PDM is about the 'truth' of provider data — capturing, cleaning, validating, and maintaining it over time. The network lifecycle is about how that data flows and is used — across the entire network lifecycle (contracting, credentialing, onboarding, monitoring, and network performance)… **PDM is one component that powers the network lifecycle**." PDM data named: "provider credentials, specialties, locations, affiliations, and availability."
- **Strategic Network Design** (service page): "creating provider networks that meet **adequacy and access standards**." Phase One: "defining the specialty makeup, determining the best beneficiary file to use, and setting **time and distance parameters**." Phase Two: feasibility under conversion scenarios. Phase Three: recruitment strategy with scenario modeling. "We help healthcare payers… Ensure compliance with regulatory standards."
- Ghost networks blog listed ("Exposing The Phantom Threat To Member Access") — directory accuracy failure mode named by the vendor.

## Product B — Medallion (credentialing/enrollment operations platform)

### Key observations

- Solutions list: Provider data management, CredAlliance™, Provider enrollment, CVO credentialing, Roster management, Delegated credentialing, Payer contract management, Privileging, Cross-state licensing, Monitoring. "Who we help": Provider groups, **Payers**, Health systems, RCM organizations, Digital health — both seats served.
- **FAQ definitions** (vendor's own teaching content):
  - "Credentialing in healthcare is the process of verifying a provider's qualifications — education, training, licensure, and work history — before they're authorized to treat patients or bill insurance. Health systems, medical groups, and health plans use credentialing to ensure clinical quality, meet regulatory standards (NCQA, The Joint Commission), and **maintain payer contracts**."
  - "Provider credentialing… covers primary source verification of licenses, certifications, malpractice history, and education — and must be repeated on a regular **re-credentialing cycle, typically every two to three years**."
  - "Enrollment is the separate process of **contracting with payers** — Medicare, Medicaid, and commercial health plans — so a provider can bill for services rendered."
  - Documents needed: state medical license, DEA certificate, malpractice insurance, board certification, education/training records, CV, work history, "a completed CAQH profile."
- **Dashboards** (product UI screenshots): credentialing requests by status ("124 in progress, 63 ready, 171 in committee"), recredentials nearing expiration, sanctions audit log, "NPDB verification: 12 need attention…", "Medicare opt-out verification", "Total verifications by month across NPDB, OIG and SAM"; enrollment dashboards "Completed enrollments by payer (283)… across Medicare, Optum, Humana and Medicaid".
- **Delegated credentialing**: "Scale credentialing network-wide, without adding headcount" — the payer delegates credentialing execution to provider groups/CVOs.
- **Monitoring**: "Stay ahead of compliance standards with automated alerts" — sanctions/exclusion surveillance as a standing workflow.
- **Payer contract management** (provider-side mirror): "Turn payer contracts into a searchable, negotiation-ready system of record." AI extracts "effective dates, renewal windows, timely filing limits, payer contacts, and exclusions"; **implied rate calculation**: "Most contracts don't list a dollar rate — they reference a fee schedule, often as a percentage of Medicare… Medallion identifies that reference and calculates the implied per-code rate, accounting for provider type and code." Contracts rolled up "by payer and by group" across TINs/clinic brands. Example contract: "Behavioral health provider agreement with Contoso Health, effective 06/01/2026, covering Commercial Health and Medical Rental Network product categories in California… Initial three-year term, renewing annually." — evidences that participation terms are **product- and geography-scoped** and that fee schedules are the rate substrate.
- CredAlliance™: "Cutting $1.2B in redundant credentialing costs for payers" (press claim — L3).

## Product C — Kyruus Health (care-access platform for payers)

### Key observations

- Positioning: "The Leading Care Access Platform"; serves Health Systems & Hospitals, Medical Groups, and **Health Plans** (incl. Government Plans).
- For payers: "Provider Data Solutions — Provider data management and attestation"; "Search — Conversational-AI supported directory and navigation"; Guide, Cost, Reviews, Rewards, Price Transparency, Interoperability Services.
- Member-facing value framing: "Empower your members to find, evaluate, and select the best **in-network** care options based on detailed provider information, personalized cost estimates, appointment availability"; "Harness the power of our network of 500k+ providers nationwide to ensure **provider profile accuracy and enrich directories** with the data members want."
- Trust statistic: "77% of consumers say that inaccurate provider information on their health plan's website erodes their level of trust" (vendor survey claim — L3 number, but the *directory accuracy → member trust* causal framing is A-layer positioning).
- Geisinger case study: provider-payer data integration to enhance the digital provider directory (photos, languages spoken — "information not typically available in health plan directories").
- Scale claims: 100 health plan brands, 74M members served, 500k connected providers (L3).
- **Boundary signal**: Kyruus carries NO credentialing workflow and NO contracting machinery — its payer-side center is provider data + the member-facing directory/search experience. It is the drift pole toward member engagement / care access.

## Product D — DataSpring, powered by CAQH (industry data infrastructure)

### Key observations

- Rebrand context: "DataSpring, powered by CAQH… the trusted data connector at the core of healthcare." Provider Data solutions: Provider Data Management, Credentialing Suite (Primary Source Verification, Sanctions Monitoring), Directory Management. Member Data (COB, Medicaid) — out of PNM scope.
- **Credentialing Suite**: "More than 2.5 million providers actively enter and verify their information in the Provider Data Portal. With a **single credentialing application — accepted or supported in all 50 states** — DataSpring eliminates redundant processes… Providers and group administrators enter data once and it is shared with all plans they designate." 4.8M provider records across 757 specialties; 1.8M attested profiles monthly; 80% participating U.S. clinicians (vendor claims — L3 numbers, A-layer mechanism).
- **Primary Source Verification**: "validates credentialing information with data from **licensing boards, medical schools, government registries and other authoritative sources**."
- **Sanctions Monitoring**: "Sanctioned providers are flagged daily… meets NCQA requirements for monitoring license actions, sanctions, and Medicare/Medicaid exclusions"; 700+ sources monitored (L3 number).
- **Directory Management**: "Drawing on professional and practice information already entered and verified by providers… improves health plan directories"; "applies advanced analytics to data entered, updated and **confirmed by physician practices**… supports state and federal regulatory compliance." "1.8M+ confirmed provider profiles… 2.5M+ providers who have confirmed their data within the past 120 days. 53 health plans participating" (L3 numbers). Delegated groups: "administrators are able to centrally manage non-sensitive directory information and make changes to locations, phone numbers and other information once and push it to all providers."
- Directory data breadth: "health equity, race, ethnicity, language"; "telehealth services offered by providers, including the type of service and platform used."
- **Network adequacy**: "Plans can access detailed data to **assess, understand and manage provider networks**." — adequacy as a data product feeding the plan's own adequacy analysis.
- Case study: "Health Plan Achieves 84% Directory Accuracy for Medicare Advantage Plans… making 1.2 million phone calls to every office to confirm the clinician was practicing at that location" (L3 numbers; A-layer evidence that directory verification is a plan-side operational burden).
- Issue brief title: "Payer and Provider Contracting: Why a Critical Process is Stuck in the Past" — contracting as a recognized industry process spanning both seats.

## Product E — Availity (payer-provider network + Provider Lifecycle Solutions)

### Key observations

- **Provider Lifecycle Solutions** page — the sample's clearest canonical definition: "Provider lifecycle management is the process of managing the information and workflows that support a provider's relationship with a health plan. It includes the steps required to collect, validate, update, and use provider information across **credentialing, onboarding, network participation, directory management, claims, authorizations, and other payer operations**."
- "Accurate provider data supports payer operations across the enterprise. It affects **provider directories, claims adjudication, prior authorization, utilization management, network management, member access to care, and credentialing intake**." — network status as an input consumed by claims/UM; PNM as upstream producer.
- PDM + directory attestation: "collect provider information and maintain a complete, **attested**, and up-to-date provider record… validated through a provider-friendly attestation experience." Reach: "70% of U.S. providers… more than 400 provider data elements" (L3 numbers).
- **Credentialing Intake**: "Applications can be prepopulated with available provider data… captures required information and attachments up front, checks for completeness, and **routes completed application to the payer's credentialing team, verification partner, or preferred CVO for final validation**." — intake vs verification vs committee separation; delegation to CVO as a first-class routing target.
- FAQ: "What is directory attestation? … confirming that provider information is accurate, current, and ready for use in payer directories."
- Ghost networks: blog "Medicaid 'Ghost Networks' and the WSJ: What We Can Fix Now" — the failure mode named again, independently.
- Scale claims: 85% of U.S. providers on the network, 13B transactions annually (L3).

## Cross-product Comparison

| Dimension | Andros | Medallion | Kyruus Health | DataSpring (CAQH) | Availity | Strength |
|---|---|---|---|---|---|---|
| Provider as persistent identified record (clinician/group/facility; identity, qualifications, locations, practice attributes) | ✓ (profile: specialty, languages, malpractice, credentialing status) | ✓ (roster management; provider records) | ✓ (provider profiles; 500k network) | ✓ (4.8M records, 757 specialties) | ✓ (400+ data elements) | **Core (A, 5/5)** |
| Credentialing gate: application → primary source verification → committee/approval → status | ✓ (CVO workflow + committee management) | ✓ (CVO credentialing; dashboards "in committee") | ✗ (not in product) | ✓ (credentialing suite + PSV; committee not named — plans decide) | ✓ (intake → routes to credentialing team/CVO for "final validation") | **Core (A, 4/5)** |
| Re-credentialing / ongoing maintenance cycle | ✓ (monitoring services) | ✓ ("recredentials nearing expiration"; cycle named) | ✗ | ✓ (continuous attestation; sanctions daily) | ✓ (keep data "current over time") | **Core (A, 4/5)** |
| Contracting / participation terms (contracts, effective dates, fee schedules) | ✓ ("recruitment and contracting"; network development "recruit, contract") | ✓ (payer contract management — **provider-side mirror**; fee-schedule mechanics named) | ✗ | △ (issue brief on payer-provider contracting; no payer-side contract tool observed) | △ ("network participation" named in lifecycle; no contract tool observed) | **Core (A, 2/5 direct + B corroboration)** — see note |
| Effective-dated, product-scoped participation status consumed downstream | ✓ (network per product; MA network building) | ✓ (contract example: product categories + state + term) | ✓ ("in-network care options" in directory) | ✓ (directory = participating providers; adequacy data) | ✓ (status feeds claims/UM/directory) | **Core (A/B, 5/5)** |
| Network adequacy machinery (time/distance, specialty coverage, access standards) | ✓ (strategic network design: time/distance parameters, specialty makeup, beneficiary file) | ✗ | ✗ | ✓ (adequacy data product) | △ ("network management" named; no adequacy tool observed) | Common (A, 2/5 direct; Quest Analytics unreachable) |
| Provider directory management (attestation, accuracy, publication) | △ (directory accuracy in lifecycle framing; ghost-networks blog) | ✗ | ✓ (directory/search is the center) | ✓ (directory management solution) | ✓ (directory attestation) | Common (A, 3/5 + 1 partial) |
| Sanctions/exclusion monitoring (NPDB/OIG/SAM-class) | ✓ (flags malpractice/licensure/sanctions; compliance services) | ✓ (NPDB, OIG, SAM dashboards) | ✗ | ✓ (700+ sources, daily, NCQA-compliant) | ✗ (not observed) | Common (A, 3/5) |
| Delegated credentialing / CVO execution as first-class pattern | ✓ (Andros IS a CVO) | ✓ (delegated credentialing solution) | ✗ | ✓ (group administrators manage for providers) | ✓ (routes to "verification partner or preferred CVO") | Common (A, 4/5) |
| Member-facing directory/search experience | ✗ | ✗ | ✓ (the center) | ✗ | ✗ | Optional (A, 1/5) — drift pole |
| Provider-side mirror (contract management, privileging, enrollment from the provider seat) | △ ("Contract with a Payor" service) | ✓ (payer contract management, privileging) | ✗ (provider-side PDM exists for health systems) | △ (clinician-facing portal) | △ (provider-side portal exists in the wider platform) | Variant — same machinery, opposite seat |
| Government-program machinery (Medicare Advantage / Medicaid specifics) | ✓ (MA network building line) | ✓ (Medicare/Medicaid enrollment dashboards) | △ (Government Plans segment) | ✓ (MA directory accuracy case; Medicaid solutions) | △ (Medicaid ghost networks blog) | Variant (regime machinery) |

**Contracting note**: direct payer-side contracting-tool evidence is strongest at Andros ("recruitment and contracting" as a named PNM service; network development "Easily recruit, contract, and manage top talent"). Medallion evidences the contract/fee-schedule *data model* in detail but from the provider seat. DataSpring and Availity name contracting as an industry process / lifecycle stage without shipping a payer-side contract tool on the fetched pages. The participation-terms leg is therefore held as Core with the contract *relationship* (effective-dated, product-scoped, fee-schedule-based) as the invariant and the contract-*administration tooling depth* as a variant axis.

## Canonical Abstraction

### L0 — Defining Invariant (deliberately small)

Three jointly-held structures. Remove any one and the product stops being provider network management:

1. **The provider as the network-participant record of record.** A persistent, individually identified record for each healthcare provider in the plan's world — individual clinician, group/practice, or facility — carrying identity, qualifications, locations, and practice attributes (specialty, languages, contact). It is the anchor to which credentialing, contracting, participation, and directory data attach. Remove → generic contact/CRM.
2. **The participation relationship under managed terms.** An effective-dated in-network status binding the provider to a specific network/product of the plan, established through contracting (agreement with reimbursement terms — commonly fee-schedule-based) and scoped by product line and geography; this is the status that downstream operations (claims adjudication, member directories, provider services) consume. Remove → provider data management or a bare provider list.
3. **The admission-and-maintenance lifecycle.** The controlled path into and through participation: application → credentialing (primary-source verification of qualifications, committee/authority approval) → contracting → effective participation → re-credentialing, data maintenance, and monitoring → termination/deactivation. Execution may be delegated (CVO, delegated group) but the gate and its records are the plan's. Remove → static roster; the "management" is gone.

Jointly-held is load-bearing: (1) alone = provider CRM; (2) without (1)+(3) = a rate table with nobody attached; (3) without (2) = credentialing operations with no network consequence; (1)+(3) without (2) = credentialing platform; (1)+(2) without (3) = contract repository + roster with no admission gate.

### L1 — Common Mature Structure

- **Provider data management as a discipline** — deduplication, golden record, data quality, attestation loops (Andros PDM framing; Availity PDM; DataSpring portal; Kyruus PDM).
- **Network adequacy monitoring** — time/distance parameters, specialty makeup, access standards, feasibility/recruitment modeling (Andros design service; DataSpring adequacy data; Quest Analytics as unreachable market anchor). Regulatory-driven in the US; near-universal in modern US products but not definitional (paper-era payers managed networks without adequacy analytics).
- **Provider directory management** — attestation, accuracy verification, publication to member-facing surfaces (DataSpring, Availity, Kyruus; Andros lifecycle framing). Regulatory drivers make it near-universal in the US; still L1 because a PNM without directory publication machinery remains recognizable.
- **Sanctions/exclusion monitoring** — NPDB/OIG/SAM-class surveillance feeding alerts (Medallion, DataSpring, Andros).
- **Delegation management** — CVO/delegated-group execution with the plan retaining accountability (all four credentialing-carrying products).
- **Roster/data exchange** — provider rosters to/from partners, groups, downstream systems (Medallion roster management; DataSpring group push; Availity network transmission).
- **Committee/approval workflows** — credentialing committee queues, level-of-risk review (Andros committee management; Medallion "in committee" states).
- **Analytics** — network performance, credentialing turnaround, directory accuracy metrics (dashboards across sample).

### L2 — Variant / Optional Structure

- **Seat posture** — payer-side (the Type's center) vs provider-side mirror (Medallion payer contract management, privileging; Andros "Contract with a Payor" service): the same contract/credentialing machinery exists on the provider seat, serving negotiation and enrollment instead of network administration.
- **Regime machinery** — Medicare Advantage network building, Medicaid-specific flows, state-specific licensing (Andros MA line; Medallion cross-state licensing; DataSpring Medicaid solutions).
- **Product/portfolio scoping depth** — participation scoped per product line and state (Medallion contract example) vs simpler single-network plans.
- **Modern data breadth** — telehealth attributes, health equity/REL data, photos, languages in directories (DataSpring, Kyruus).
- **Automation era machinery** — AI term extraction, AI agents for payer follow-ups, automated PSV matching (Medallion, Andros, DataSpring).
- **Member-facing experience bundling** — search, cost estimates, scheduling attached to the directory (Kyruus) — drift toward the care-access platform.

### L3 — Vendor-specific (Research Notes only)

- Andros Arc™ / Arc Workflow / Network Lifecycle branding; CredSimple lineage (login domain); "300k credentials annually", "200+ networks", "ROI of 300%"; URAC accreditation ID.
- Medallion CredAlliance™; "$1.2B redundant credentialing costs"; "2 days median onboarding"; "99.9% file accuracy"; FirstLayerAI corporate name; performance-backed guarantees.
- Kyruus: 500k connected providers, 100 health plan brands, 74M members; RevSpring acquisition banner; Geisinger case study.
- DataSpring: 7.4M provider records, 1.8M monthly attested profiles, 53 participating plans, 84% directory accuracy case, 1.2M verification calls, 700+ sanctions sources, $775M savings claim; ProView portal; CORE operating rules.
- Availity: 70%/85% provider reach, 400+ data elements, 13B transactions, Abrasion Index, CMS-0057-F/0053-F suites.

## Rejected Findings (not promoted to core)

- **"PNM = provider data management"** — rejected: PDM is a component (Andros: "PDM is one component that powers the network lifecycle"; Availity: PDM inside the lifecycle). PDM alone has no participation gate and no network consequence.
- **"PNM = credentialing"** — rejected: credentialing is the admission gate (L0 leg 3) but credentialing operations without participation terms and network consequence is the credentialing-platform pole (Medallion's provider-side posture), not network management.
- **"Directory management is the core"** — rejected: the directory is the outward-facing publication surface (L1). Kyruus, which centers the directory/search experience, carries no credentialing or contracting — evidence that directory-centricity alone is a different center (care access).
- **"Network adequacy is definitional"** — rejected: strong common-mature machinery (regulatory-driven in the US) but the paper-era and minimal-pole payer manages a network without adequacy analytics; held L1.
- **"Member engagement / cost transparency belongs to PNM"** — rejected: adjacent bundling (Kyruus Cost/Guide/Rewards); not network administration.
- **"Claims adjudication or premium billing is part of PNM"** — rejected: no sampled PNM product adjudicates claims or bills premiums; both are consumed/adjacent (HPAS, payer claims processing).
- Marketing figures (300k credentials, $1.2B, 84%, 700+ sources, 400+ elements, 70%/85% reach, 13B transactions) — excluded from the final document; vendor claims only.

## Boundary Findings

1. **vs Health Plan Administration System (§22, processed) — FLAG DISCHARGED from this side; keep-both RATIFIED.** The HPAS pass proposed the seam: HPAS = the payer's system of record (member/coverage/eligibility/benefit/premium/obligation; its provider master + settlement seam is L1 there), PNM = the contracting/credentialing/fee-schedule/adequacy machinery. Corroborated from this side: (a) all five sampled products center the **provider population**, and none carries member enrollment, premium billing, or benefit-rulebook machinery of record; (b) the PNM products are independently deployable and marketed as standalone (Andros services+platform, Medallion platform, DataSpring solutions, Availity solutions) rather than as CAPS modules; (c) the direction of data flow is PNM → payer core: Availity names claims adjudication and UM as *consumers* of provider data, and the HPAS pass itself observed provider data/portals inside CAPS as L1. The provider record is a **shared object across an integration seam** (the CAPS provider master for settlement; the PNM record for participation lifecycle), not evidence of one Type. Cross-referenced in both documents.
2. **vs Payer Claims Processing (§22, processed) — FLAG DISCHARGED from this side; keep-both RATIFIED.** Claims machinery consumes network status as an adjudication input; PNM produces and maintains it through the participation lifecycle. No sampled PNM product performs intake → adjudicate → pay → adjust. The seam is producer-vs-consumer of the participation status, consistent with the PCP pass's own framing ("provider master + settlement seam here vs contracting/credentialing/fee-schedule machinery there").
3. **vs Provider-side credentialing / enrollment (no separate §22 leaf; capability + adjacent products)**: the same credentialing machinery exists on the provider seat — medical staff credentialing/privileging (health systems), payer enrollment (provider groups wanting to bill payers). Medallion literally serves both seats with one platform; its payer-contract-management product is the provider-side mirror of PNM's contracting leg. The distinguishing question is **whose network is being administered**: the payer's network (PNM) vs the practitioner's ability to practice and bill (provider-side). Recorded as a Variant axis, not a separate Type here.
4. **vs Provider Data Management (capability, not a directory leaf)**: PDM is L1 machinery inside PNM (Andros and Availity both position PDM as a component of the lifecycle). A PDM-only product without participation machinery is a data platform, not PNM. No taxonomy change proposed.
5. **vs member-facing provider directories / care-access platforms**: the directory is PNM's publication surface; the member-facing search/scheduling/cost experience built on top of it (Kyruus Connect for Payers) is the care-access drift pole. When member engagement becomes the center and credentialing/contracting disappear, the product has left this Type.
6. **vs Utilization Management / Prior Authorization Platform (§22 siblings)**: different machinery (clinical review of services vs administration of network participation); overlap is limited to shared provider records. No flag.
7. **vs Provider Claims Management / RCM (§22, processed)**: provider-side billing and claim submission vs payer-side network administration — opposite seats; no confusion once the seat is named.
8. **Ghost networks as a named cross-vendor failure mode**: directory entries for providers who are not actually available or participating (Andros blog; Availity blog on Medicaid ghost networks; DataSpring's verification-call case study is the operational response). Held as domain behavior evidence, not a structural finding.

## Historical / Market-Sample Check

- **Paper-era payer**: provider index files (cards/ledgers), credential files with verification letters and committee minutes, contract files with rate schedules, printed member directories. All three L0 legs satisfied with no software, no NPI, no NCQA, no adequacy analytics. ✓
- **Older software generation**: 1990s payer provider-master tables inside claims/administration systems + separate credentialing spreadsheets + contract files + annually printed directories. ✓ (consistent with the HPAS pass's observation that provider data lives inside CAPS as L1)
- **Regional / non-US payers**: provider contracting and qualification verification exist universally; the US-specific institutions (NCQA credentialing standards, directory accuracy regulation, adequacy standards, NPI) are regime machinery held at L2. A statutory-sickness-fund with contracted physician registers satisfies the core. ✓ (inferred abstraction — sample is US-shaped; recorded in Uncertainties)
- The definition names no NPI, no NCQA/URAC, no directory regulation, no adequacy metrics, no cloud/AI/deployment shape. ✓

## Uncertainties

- **Quest Analytics unreachable (403 ×2)** — the adequacy-analytics leader could not be observed; adequacy machinery is written from Andros/DataSpring/Availity evidence at moderate strength. No precise adequacy metrics (distance thresholds, ratio standards) are asserted.
- **Payer-suite embedded modules unreachable** (TriZetto QNXT, HealthEdge HealthRules Payer — carried limitation from the HPAS and payer-claims passes): the "PNM as CAPS module" variant rests on the HPAS pass's observation that sampled CAPS products carry provider data/portals inside the core; module-level structure unverified.
- **NCQA/CMS regulatory text unreachable (403)** — credentialing standards, directory accuracy rules, and adequacy standards are described at concept level from vendor compliance claims only; no specific standard numbers, cycle lengths beyond Medallion's own "typically every two to three years" (vendor statement, kept attributed), or regulatory citations are asserted.
- **Payer-side fee-schedule configuration depth** — direct payer-side tooling evidence is Andros' contracting services; the fee-schedule data model is evidenced in detail from the provider-side mirror (Medallion). Payer-side rate-configuration depth is inferred and kept at moderate strength.
- **Committee decisioning inside DataSpring** — the credentialing suite page shows PSV and monitoring but not committee workflows (plans decide); committee machinery is evidenced at Andros/Medallion. Held accordingly.
- **Non-US fit is inferred abstraction**, not product observation — the sample is US-shaped, consistent with the §22 directory's US payer vocabulary.

## Final Synthesis

Provider Network Management is the **payer-side management application for the plan's contracted provider network**. Its world has three jointly-held structures: the provider as the network-participant record of record (clinician, group, or facility — identity, qualifications, locations, practice attributes); the participation relationship under managed terms (effective-dated, product- and geography-scoped in-network status established by contract with fee-schedule-based reimbursement terms — the status claims adjudication and member directories consume); and the admission-and-maintenance lifecycle (application → credentialing with primary-source verification and committee approval → contracting → effective participation → re-credentialing, attestation, monitoring → termination), with execution delegable to CVOs and delegated groups while the gate and its records remain the plan's. Around that core, mature products add provider data management as a discipline, network adequacy monitoring, provider directory management with attestation, sanctions/exclusion monitoring, delegation oversight, roster exchange, committee workflows, and analytics. Variants span seat posture (payer center vs provider-side mirror), regime machinery (Medicare Advantage, Medicaid, state licensing), data breadth (telehealth, REL), automation era machinery, and member-facing bundling (the care-access drift pole). The boundaries that matter: payer system of record vs network machinery (health plan administration), producer vs consumer of participation status (payer claims processing), payer network administration vs provider-side practice/billing qualification (credentialing/enrollment mirror), and network administration vs member-facing care access (directory/search platforms).
