# Research Notes — Health Plan Administration System

Research date: 2026-09-08
Slug: health-plan-administration-system
Leaf: Health Plan Administration System (§22 Healthcare & Life Sciences)

## Research Goal

Understand, from real products, what a health plan's core administration system is: what the central objects are (member, enrollment, eligibility, benefit plan, claim, provider, premium), how coverage is established and maintained, how benefit obligations are determined and settled, how the health-specific machinery (enrollment events, eligibility, provider-facing seams, government-program files) differs from the already-processed insurance policy administration family, and where the boundaries lie against the unprocessed §22 siblings (payer claims processing, provider network management, utilization management, payer care management) and the processed §08/§09 neighbors.

Standing instruction carried into this pass (from the insurance-policy-administration-system pass, recorded in STATUS.md Boundary Issues): health plan administration is structurally a health-insurance instantiation of the policy-administration family; define the center from the health-specific machinery (enrollment events, eligibility, provider-facing seams) and cross-reference rather than duplicate the contract-lifecycle core.

## Initial Boundary (pre-research hypothesis)

- Hypothesis: the health plan administration system is the payer-side system of record for the plan's enrolled population and benefit obligations — the health-instantiation counterpart of the carrier-side policy administration system, centered on members and eligibility rather than on the contract.
- Expected core: member/coverage record + enrollment & eligibility machinery + benefit plan configuration + benefit execution (claims adjudication) + premium administration.
- Likely confusions: Payer Claims Processing (§22 sibling — adjudication machinery), Benefits Administration Platform (§09 — employer side), Provider Network Management (§22 sibling), Utilization Management / Prior Authorization (§22 siblings), Payer Care Management (§22 sibling), Public Benefits Management (§24 — government agency side), Patient Portal (member-facing surface), Healthcare Revenue Cycle Management / Provider Claims Management (provider side of the same claim), Pension Administration Platform (§08 — member-registry structural neighbor).

## Research Questions

1. What is the central object set — member, subscriber/dependent, benefit plan/product, provider, claim, premium — and which object anchors the world?
2. How does enrollment work: intake channels (employer files, individual applications, government eligibility files), election/enrollment periods, validation, effective dating?
3. How is eligibility maintained and answered (real-time verification, who asks)?
4. How are benefit plans configured (coverage rules, cost sharing, network applicability, authorization rules) and how do changes propagate?
5. Is claims adjudication bundled into the core or connected — and where exactly is the seam with a separate claims-processing Type?
6. What is the provider-facing seam: provider master data, portals, remittance, network linkage?
7. How does premium administration work (individual vs group, subsidy/government payment files, reconciliation) and is it definitional?
8. What regulatory machinery is standard (standardized transactions, government file exchanges, encounter data, audit readiness) and is it definitional or regime-dependent?
9. Who operates the system, and what interfaces do staff and external users face?
10. What are the market segments/poles (commercial group, individual market, government programs, TPA/self-funded, provider-sponsored) and do they share the same core?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer/market poles. Note: the two dominant legacy core platforms (TriZetto QNXT/Facets) and the leading cloud challenger (HealthEdge) were not reachable; the reachable sample spans the modern CAPS pole, the modular-suite pole, the individual-market pole, the care-layer boundary anchor, and a services/category anchor.

| Product | Vendor | Philosophy / segment | Evidence reached |
|---|---|---|---|
| AxisCore (+ AxisConnect) | HealthAxis | Cloud-native CAPS for health plans and TPAs; bundling pole (adjudication + enrollment + provider + financial in one core) | Homepage, AxisCore page, platform-capabilities page (Tier 2), evidence layer A |
| MarketProminence + CareProminence suites | MHK (MedHOK, Hearst Health) | Modular payer suites; Medicare Advantage / Part D heavy; market-side and care-side suites around existing cores | Homepage, Enrollment & Member Maintenance page, Premium Billing page (Tier 2), layer A |
| ACA Marketplace Cloud / All-in-One | Softheon | Individual-market health plan operations (shopping, enrollment, billing, renewals); ACA/ICHRA/Medicare Advantage/Dental | Homepage + For Health Plans navigation (Tier 2), layer A |
| Unified Data Platform / Aerial-class solutions | Medecision | Payer-side care/UM/quality/risk platform — boundary anchor for the clinical-program layer (adjacent Type) | Homepage (Tier 2), layer A |
| Healthcare payer services ("Core Administration System modernization") | DXC Technology | Services vendor; confirms "Core Administration System (CAS)" as the payer-side market category; legacy-core reality | Healthcare industry page (Tier 2), layer A |

Unreachable (attempts recorded; no product-specific claims made from them):

- Cognizant TriZetto (QNXT, Facets) — cognizant.com URLs 404 ×2 (dominant legacy CAPS; market anchors only)
- HealthEdge (HealthRules Payor) — healthedge.com 403 ×2 (leading cloud-native core challenger)
- Epic (ASA / health plan administration inside EHR) — epic.com 403 ×2 (platform-native variant anchor)
- Conduent (payer/Medicaid) — transport errors ×2
- Gainwell Technologies (Medicaid MIS) — transport errors ×2
- medicaid.gov MMIS pages — 403 ×2 (official government anchor for the Medicaid variant)
- HMS, TCS Chroma, HM Health Solutions — transport error / 403 / timeout (single attempts, abandoned per effort budget)

## Sources

Fetched 2026-09-08:

- HealthAxis — homepage: https://healthaxis.com/
- HealthAxis — AxisCore product page: https://healthaxis.com/our-solutions/axis-core
- HealthAxis — platform capabilities: https://healthaxis.com/platform-capabilities
- MHK (MedHOK) — homepage: https://mhk.com/
- MHK — Enrollment & Member Maintenance: https://mhk.com/solutions/mhk-marketprominence/enrollment-member-maintenance/
- MHK — Premium Billing: https://mhk.com/solutions/mhk-marketprominence/premium-billing/
- Softheon — homepage: https://www.softheon.com/
- Medecision — homepage: https://www.medecision.com/
- DXC Technology — Healthcare industry page: https://www.dxc.com/us/en/industries/healthcare

Context sources (already-processed sibling/neighbor leaves, for boundary consistency):

- research/insurance-policy-administration-system.md (family note; EIS Census & Enrollment Intake; Sapiens health scope; group master contracts with member-level records)
- applications/benefits-administration-platform.md (employer-side seam: elections → effectuation handoff to carriers)
- applications/pension-administration-platform.md (member-registry structural neighbor)
- applications/electronic-health-record-ehr.md (clinical record — opposite side of the payer/provider divide)
- applications/insurance-agency-management.md, applications/insurance-claims-management.md (insurance family seams)

## Product Observations

### HealthAxis AxisCore (evidence layer: A — direct, product pages)

- Category self-identification: the contact form and navigation offer "Core Administrative Processing System (CAPS)" for both "(Health Plans)" and "(TPAs)"; AxisCore page headline: "AxisCore — The Modern CAPS for Health Plan Administration"; "A unified, cloud-native Core Administrative Processing System (CAPS) engineered to handle the massive scale of modern health plan administration."
- Core-definition sentence (the pass's most valuable single quote): "AxisCore™ is not just a database; it is a high-performance orchestration engine. It consolidates claims adjudication, enrollment, provider management, and financial coordination into a single, immutable source of truth." — a vendor-named four-pillar CAPS model: adjudication + enrollment + provider management + financial coordination on one member/benefit record.
- Audiences served: Health Plans, TPAs, Risk-Bearing Providers (ACO/IPA/Medical Group options in the contact form) — the same machinery marketed across payer and TPA seats.
- Platform capabilities page (18 named capabilities): Provider Portal ("Centralised access for providers to submit claims, verify eligibility, and manage authorisations"); Enrollment & Eligibility ("Streamlined member enrollment workflows with real-time eligibility verification across all plan types"); Claims Adjudication ("Automated, rules-driven claims adjudication"); Encounter Data Submission ("Accurate encounter data capture and submission support that ensures completeness and CMS audit readiness"); Appeals & Grievances ("End-to-end tracking with configurable workflows and regulatory compliance"); Customer Service Management ("Integrated case management and member service tools"); Integration Interfaces ("Open, standards-based interfaces"); Disability Examination; Configuration Management ("Flexible, no-code configuration tools to adapt benefit rules, plan designs, and workflows without IT dependency"); Provider & Member Data Management ("A unified data layer for accurate provider directories, member records, and benefit administrative systems"); Call Centre AI Voice Agents; Utilization Management; Member Portal & Appointment Scheduling; Patient Care Management; Premium Billing ("Automated billing and collections management with full reconciliation support and configurable billing cycles"); Pharmacy Benefits Management ("Formulary configuration, prior authorisation, and cost control"); Medical Reviews; Reporting & Analytics.
- Vendor posture/claims (recorded as claims, not asserted): serving plans since 1964 (TPA lineage); "$2B+ claims paid annually"; "10M+ claims processed"; "50+ health plans served"; "65+ benefits plans managed"; "96% efficiency straight out of the gate" vs "legacy CAPS hit its ceiling [at] 80%" straight-through-processing narrative; SOC 2 Type II; agentic-AI positioning (NOVA operations layer; nventr engineering partnership).
- Lineage note: TPA-rooted vendor — the same platform is positioned for plans and for TPAs administering employer (self-funded) business.

### MHK / MedHOK — MarketProminence + CareProminence (evidence layer: A)

- Positioning: "From the point of enrollment and across every moment of care, discover why the largest health plans, pharmacy benefit managers and managed care organizations trust MHK"; "MHK combines enterprise workflow technology with AI-driven orchestration to simplify operations, reduce costs, and drive better outcomes."
- Suite architecture (navigation): MarketProminence (market side) — Enrollment & Member Maintenance, Premium Billing, Financial Reconciliation, Web Portals; CareProminence (care side) — Utilization Management, Complaints Appeals & Grievances (CAG), Care Management, Population Health & Quality Management, Pharmacy Management; cross-cutting — SmartProminence Orchestrator, DataVisor (payer analytics), Interoperability ("FHIR-based APIs"), Web Portals.
- Observation: the market-side suite covers enrollment/member/billing/reconciliation/portals but names no claims-adjudication module — the modular posture: MHK coexists with separate claims cores ("Seamlessly share required data with subcontractors and internal systems"). Contrast with HealthAxis's bundled CAPS — two packaging poles within one Type.
- Enrollment & Member Maintenance page (Medicare-shaped): "Medicare enrollment software purpose-built to meet CMS requirements right out of the box"; "From application intake to ongoing member updates"; plan teams can "Process both electronic and paper applications with automatic data validation"; "Identify eligible election periods and verify member eligibility in real time"; "Submit and receive eligibility data directly from CMS and other regulatory sources"; "Manage changes such as address updates, premium adjustments and disenrollments"; "Seamlessly share required data with subcontractors and internal systems". CMS Submitter add-on: "automates daily submission and import of all required CMS files" (enrollment and non-enrollment files), with 24/7 monitoring; Online Enrollment Center (OEC) integration as an alternative to the Submitter. Vendor claim: "Automations move up to 95% of records through CMS compliant, pre-enrollment processing without user interaction."
- Premium Billing page: "automates complex billing tasks... for individual and group members—while maintaining full CMS compliance"; "Automate premium calculations and billing workflows"; "Manage complex remittance models across both member and group accounts"; "Integrate CMS payment files directly into member balances for real-time accuracy"; "full visibility into billing statuses and account changes"; Premium Portal member self-service: "View premium balances and account history", "Make one-time or recurring payments", "Update contact information and payment methods", "Submit change requests".
- Client evidence (testimonials): enrollment AVPs at regional plans; "The ability to report almost every field of data" as a compliance-reporting draw; self-configuration without vendor involvement; handle-time reductions (vendor-published claims).

### Softheon (evidence layer: A)

- Positioning: "Health Plan Operations Made Simple. Growth Made Possible"; "Shop, Quote, Enroll, Bill, Communicate - All in One Place"; "All-in-One Solution for Payers."
- For Health Plans: All-in-One Solution, Shopping & Enrollment, Billing & Payments, Member Renewals, Reporting & Analytics, Healthcare AI, Provider-Sponsored Plans ("payvider model").
- Markets served: ACA Marketplace (on-exchange), Off-Exchange/ICHRA, Medicare Advantage, Dental, Small Group — "Give your members the continuity of coverage they deserve."
- Individual-market machinery visible on page: shopping/quote/enroll (consumer election capture), billing & payments, member renewals (retention/churn reduction), government-agency angle ("Reduce fraud, waste, and abuse while ensuring compliance and expanding equitable coverage access").
- Compliance posture: "Stay aligned with CMS, IRS, and state regulations with confidence in a system trusted by regulators"; certification badges (FIPS 140-2, FISMA Moderate, HIPAA, NIST 800-53 Rev. 5, PCI DSS 4.0.1, SOC 1/2 Type 2).
- Vendor claims: 30M+ enrollments; $20B+ premiums processed; "1 in 3 ACA Plans Trust Softheon"; 2026 Best in KLAS for ACA Marketplace Cloud (vendor-cited).
- Observation: claims adjudication is NOT evidenced on the fetched page — the individual-market pole is enrollment/billing/engagement-heavy; consistent with the modular-posture reading and with individual-market plans' lower claims complexity.

### Medecision (evidence layer: A — boundary anchor)

- Positioning: "Purpose-built for health plans and providers... transforms fragmented data into actionable intelligence, powering event-driven workflows"; audiences: Commercial Health Plans, Government Health Plans, Third-Party Administrators, Providers.
- Solutions: Care Management, Utilization Management, Quality Management (HEDIS measures engine), Risk Management (HCC risk models, chart review), Pharmacy Management, Provider Enablement (provider portal, SMART on FHIR), Patient Engagement.
- Observation: NO enrollment, eligibility, premium billing, or claims adjudication on the payer solutions — this is the clinical-program layer that sits on top of / beside the administration core. Confirms the boundary against payer care management: same customers, different center. ("over 93 million lives" — vendor claim.)

### DXC Technology (evidence layer: A — category/services anchor)

- FAQ: "For payer organizations, DXC covers the spectrum of Core Administration System (CAS) modernization healthcare IT services from assessments to full application code transformation accelerated through AI." — independently confirms "Core Administration System (CAS)" as the payer-side market category name, sibling term to CAPS.
- Solution card: "Modernized Core Administration System — Modernize legacy Core Administration Systems using cloud-native technologies and Generative AI."
- Customer story: "Delta Dental's legacy core system—serving 36 million people—faced end-of-life obsolescence with no off-the-shelf replacement available... re-platformed to cloud-native architecture on Azure in 12 months" (vendor-claimed figures) — evidence of the long-lived legacy core reality and of "core" as the plan's irreplaceable system of record. Dental line shaping also visible (dental plans run the same core machinery).

### Context from the insurance-policy-administration-system pass (research notes, 2026-09-07)

- EIS PolicyCore ships "Census & Enrollment Intake" as a market-specific component "for benefits/health/L&A: automated digital enrollment and census tracking, validated, mapped, staged, passed to PolicyCore" — the policy-admin family's health-adjacent edge: census/enrollment intake feeding a contract core.
- Sapiens CoreSuite for Life & Pensions covers "individual and group life, wealth, health, and pensions products"; group master contracts with member-level records classified L2 in that pass.
- The family L0: master policy record (parties × coverage × premium × period) + governed effective-dated lifecycle. The health pass must show how the center differs (member/eligibility/benefit-execution vs contract lifecycle) while cross-referencing the family.

## Cross-product Comparison

| Dimension | HealthAxis AxisCore | MHK MarketProminence/CareProminence | Softheon | Medecision | DXC (services) |
|---|---|---|---|---|---|
| Category self-name | Core Administrative Processing System (CAPS) | payer suites (no CAPS claim on fetched pages) | health plan operations platform ("All-in-One Solution for Payers") | payer care/data platform | "Core Administration System (CAS)" (client's system) |
| Member/coverage record | yes (unified data layer: "member records") | yes (Enrollment & Member Maintenance) | yes (enrollments; member renewals) | no (consumes member data) | n/a (client systems) |
| Enrollment machinery | Enrollment & Eligibility capability; "all plan types" | deep: applications (electronic+paper), election periods, CMS exchanges, member maintenance | deep for individual market: shopping/quote/enroll, renewals, ICHRA/ACA/MA | no | modernization only |
| Real-time eligibility | named ("real-time eligibility verification") | named ("verify member eligibility in real time") | implied (enrollment/billing ops) | no | n/a |
| Benefit plan configuration | Configuration Management ("benefit rules, plan designs, workflows", no-code) | plan/product configuration evidenced indirectly (premium adjustments, compliance fields) | plan products per market (ACA/MA/dental) | no | n/a |
| Claims adjudication | bundled (named capability; "claims adjudication, enrollment, provider management, and financial coordination" in one core) | NOT named as own module (modular posture; shares data with internal systems/subcontractors) | not evidenced on fetched pages | no (UM only) | legacy CAS contain it (modernization target) |
| Provider seam | Provider Portal (claims submission, eligibility, authorizations); Provider & Member Data Management (directories) | indirect (subcontractor data sharing; payer portals suite) | not evidenced | Provider Enablement (provider portal, FHIR) | n/a |
| Premium billing | named capability ("billing and collections... full reconciliation... configurable billing cycles") | deep: individual + group accounts, remittance models, CMS payment files into balances | deep (Billing & Payments; $20B+ premiums claim) | no | n/a |
| Government machinery | Encounter Data Submission (CMS audit readiness) | CMS Submitter, OEC, election periods, CMS compliance "out of the box" (MA/Part D shape) | CMS/IRS/state alignment; exchange/ICHRA machinery | government health plans audience | government payer modernization |
| UM / care / quality | UM + Patient Care Management capabilities (bundled-lite) | full CareProminence suites (UM, CM, quality, pharmacy) | no | full platform (the center) | n/a |
| Appeals & grievances | named capability ("regulatory compliance built in") | full CAG suite | no | integrated in UM ("integrated appeals and grievances") | n/a |
| Packaging pole | bundled CAPS | modular suites around existing cores | market-module cloud (ACA pole) | clinical-layer platform | services over legacy CAS |

Convergence across the reachable sample:

- Member + enrollment + eligibility as the standing record (HealthAxis, MHK, Softheon; DXC implies via "core").
- Real-time eligibility verification as a named, first-class function (HealthAxis, MHK).
- Benefit rules / plan designs as configurable objects (HealthAxis explicit no-code; MHK/Softheon plan-shaped products).
- Premium billing where premiums exist (HealthAxis, MHK — individual AND group accounts; Softheon).
- Government-program machinery as a regime-shaped layer, deepest in the Medicare-shaped product (MHK), present as encounter/audit posture at HealthAxis, as CMS/IRS/state posture at Softheon.
- Claims adjudication bundled in the full-core posture (HealthAxis) but NOT necessarily present in modular suites (MHK market-side, Softheon pages) — adjudication is the CAPS bundle's component, not the Type's invariant.
- Clinical layers (UM/care/quality) appear as either bundled-lite capabilities (HealthAxis), full separate suites (MHK CareProminence), or the entire neighboring platform (Medecision) — separable from administration.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately minimal)

```text
Member & coverage of record
  (the plan's enrolled population — subscribers with dependents under group
   master contracts, or individuals direct — each carrying effective-dated
   coverage under the plan's benefit products)
  └── Enrollment & eligibility administration
      (coverage established/changed/ended through recorded enrollment events →
       eligibility determined and continuously maintained → current eligibility
       answerable in real time to internal and external askers)
      └── Benefit plan configuration
          (each plan product held as an operative rulebook: covered services,
           cost-sharing structure, network applicability, authorization rules,
           effective periods)
          └── Benefit execution & settlement
              (for care received, the plan's obligation is determined by
               applying the rulebook to the service and settled by payment —
               performed in-system, or orchestrated through a connected
               claims engine)
```

Four jointly-held invariants:

1. **Member & coverage of record** — the identified person (subscriber or member) with effective-dated coverage segments under the plan's products; the member, not the contract document, anchors the world (group master contracts are real, but member-level coverage administration is the operative center — the family note's health-specific shift).
2. **Enrollment & eligibility administration** — membership is not static: it is established, changed, and ended through recorded events (applications/elections, employer eligibility files, government eligibility files; life events, address/premium changes, disenrollments), with eligibility determinations maintained as effective-dated segments and current eligibility continuously answerable in real time. Without it: a static roster.
3. **Benefit plan configuration** — the plan's products exist in the system as operative rulebooks (what is covered, at what member cost, within which network, under what authorization rules, effective when) from which execution and member communication derive. Without it: membership administration with no benefit semantics.
4. **Benefit execution & settlement** — the reason the Type is "administration of a health plan" and not an eligibility registry: care received by members generates claims/encounters against which the plan determines what it owes (eligibility + benefit-rule application, cost sharing, network rules, authorization status) and settles (provider payment/remittance, member liability). The determination-and-settlement leg is invariant; whether the adjudication engine is bundled or connected is a packaging variant.

Jointly-held is load-bearing:

- 1+2 without 3+4 → an enrollment/eligibility registry (file handler + verifier), not plan administration.
- 3+4 without 1+2 → a claims engine (payer claims processing machinery) with no membership of record.
- 1+3 without 2 → snapshot roster + rulebook; no enrollment machinery, so no administration over time.
- 1+2+3 without 4 → membership and rulebook but no benefit semantics ever executed — not a plan's operating system.
- 2+3+4 without 1 → transaction processing with no member population of record.

Premium administration is deliberately NOT in L0: Medicare Advantage plans collect premiums from CMS rather than members; Medicaid managed-care plans and TPAs administering self-funded employers may collect no member premium at all — the four invariants hold in all of these. Where premiums exist, billing is standard mature structure (L1).

Historical check (per workflow §24-style reasoning): a paper-era health plan (subscriber ledger, group enrollment lists, benefit certificates as the rulebook, manual claim examination and payment) satisfies all four invariants — no EDI, no CMS files, no portals, no cloud. A non-US statutory fund (member registry, insurance-status eligibility, statutory benefit catalog, provider bill review/payment) also satisfies an abstracted reading, though the US-shaped sample limits confidence (see Uncertainties). The definition is not over-fitted to the modern cloud CAPS.

### L1 — Common Mature Structure (standard capabilities)

- Premium billing & receivables (individual and group invoicing, remittance models, subsidy/government payment files integrated into balances, reconciliation, delinquency handling)
- Provider data & settlement seam (provider master data, directories, provider portal for claim submission / eligibility verification / authorization management, remittance outputs)
- Claims-operations machinery depth (intake, editing, repricing, coordination of benefits, adjustments, payment-integrity hooks) — where adjudication is bundled
- Utilization-management / prior-authorization linkage (authorizations as adjudication inputs; UM suites often separate products)
- Appeals & grievances handling with regulatory rigor (deepest in government-program products)
- Member servicing (member portal — balances, payments, changes; ID cards and welcome materials; correspondence templates; customer-service case management)
- Regulatory transaction & reporting machinery (standardized enrollment/claim/eligibility/payment transactions; automated government file submission/import; encounter data submission; audit readiness)
- Financial reconciliation (premiums/payments/government files against balances)
- Document generation (plan materials, explanation documents, letters)
- Configuration tooling (no-code benefit rules, plan designs, workflows), roles & permissions, audit trails
- Reporting & analytics; open/standards-based integration APIs (FHIR-class interoperability)
- Pharmacy benefit linkage (formulary configuration, PBM integration, pharmacy prior authorization)

### L2 — Variant / Optional Structure

- Government-program machinery depth: Medicare Advantage / Part D shape (election periods, CMS file exchanges, CMS payment files, encounter data, audit posture); Medicaid managed-care / state-run MMIS instantiation; quality/rating programs
- Individual-market machinery: marketplace/exchange shopping-quote-enroll, subsidies/tax-credit alignment (IRS), ICHRA, open-enrollment campaigns, retention/renewal machinery
- Commercial group machinery: employer eligibility/census feeds, group master contracts, group billing
- TPA / self-funded (ASO) posture: no premiums; employer-funded; TPA fee income outside the system's benefit semantics
- Line shaping: dental, vision, behavioral, pharmacy carve-ins/carve-outs
- Provider-sponsored plans (payvider): plans operated by provider organizations
- EHR-platform-native deployment (administration inside an EHR vendor's ecosystem — Epic ASA class; unreachable this pass, anchor only)
- Regional/regime variants beyond the US-shaped sample (low evidence)
- Clinical-suite bundling depth (care management, quality, risk adjustment — adjacent Types bundled at MHK/HealthAxis, separate at Medecision)
- Payment integrity / fraud-waste-abuse modules
- Delivery posture: software license vs BPO/BPaaS (vendor runs the operation)

### L3 — Vendor-specific (research notes only)

- HealthAxis: AxisCore/AxisConnect naming; NOVA agentic operations layer; nventr AI partnership; "immutable source of truth" phrasing; 96%-STP marketing claim; Disability Examination capability; Call Centre AI Voice Agents; TPA-since-1964 lineage; SOC 2 Type II emphasis.
- MHK: MarketProminence/CareProminence/SmartProminence/DataVisor branding; CMS Submitter add-on; Online Enrollment Center (OEC); "up to 95% pre-enrollment automation" claim; Premium Portal specifics; Hearst Health network; NCQA/HEDIS/PQA certification stack.
- Softheon: ACA Marketplace Cloud KLAS rating; 30M+ enrollments / $20B+ premiums / "1 in 3 ACA plans" claims; FIPS/FISMA/NIST/PCI badge wall; payvider model page; "continuity of coverage" framing.
- Medecision: Unified Data Platform; AgentFoundry (agentic AI); "93M lives" claim; Frost & Sullivan / Black Book citations; excell consulting.
- DXC: CAS modernization service line; Delta Dental 36M-life legacy re-platform case (Azure, 12-month, savings figures — vendor claims); Medical Coding ML.
- Unreachable anchors (no claims from them): TriZetto QNXT/Facets (Cognizant), HealthEdge HealthRules Payor, Epic ASA, Conduent, Gainwell, HMS, TCS Chroma, HM Health Solutions.

## Rejected Findings (not promoted to core)

- "Claims adjudication machinery defines the Type" — rejected as the sole center: adjudication is bundled in the full-CAPS posture (HealthAxis) but absent/named-nowhere in modular suites (MHK market-side pages, Softheon pages). The invariant is the obligation-determination-and-settlement leg, not the engine. Machinery detail belongs to the payer-claims-processing seam.
- "Premium billing is definitional" — rejected: MA plans (CMS-paid), Medicaid MCOs and self-funded TPAs operate the core without member premiums. L1.
- "Government/CMS file machinery is definitional" — rejected: regime machinery; paper-era and non-US plans satisfy the core without it. L1/L2.
- "UM/care management/quality is part of the admin core" — rejected: separable suites (MHK CareProminence) and an entire adjacent platform (Medecision) prove separation; bundled capability at best.
- "Provider network contracting/credentialing is the core" — rejected: the provider master and settlement seam are L1; full contracting/credentialing/adequacy machinery belongs to provider-network-management territory.
- "Member portal = the Type" — rejected: a surface (L1), like provider portal.
- Marketing figures (96% STP, 95% automation, 30M enrollments, $20B premiums, 36M lives, savings/release numbers) — excluded from the final document; vendor claims only.

## Boundary Findings

- **vs Insurance Policy Administration System (§08, processed — family note discharged from this side)**: the policy pass recorded health plan administration as "structurally a health-insurance instantiation of the policy-administration family" and asked this pass to center health-specific machinery. Done: the center here is the member population and benefit execution (enrollment events, eligibility segments, benefit rulebooks, obligation settlement), not the contract-lifecycle core (issue → endorse → renew → cancel as effective-dated transactions on a policy). Both hold effective-dated governed records; the family resemblance is real, but the operative center differs (member-level eligibility administration under group master contracts vs contract-level amendment machinery). Keep-both, cross-referenced.
- **vs Payer Claims Processing (§22, unprocessed — flag)**: the heaviest overlap in the directory. In the full-CAPS posture, adjudication is a bundled component of the administration core (HealthAxis). Working seam proposed for that pass: health plan administration = the system of record for members, eligibility, benefit plans, premiums, and the plan's obligations (the "who is covered, under what rules, what has the plan owed and paid" record); payer claims processing = the claims-operations machinery (intake → edit → adjudicate → pay → adjust), whether embedded in a CAPS or shipped standalone. Candidate keep-both with the "system of record vs processing machinery" test; the bundled-vs-modern packaging reality must be acknowledged there.
- **vs Benefits Administration Platform (§09, processed)**: employer-side vs payer-side confirmed. The benefits pass recorded the "effectuation handoff to carriers (enrollment files/EDI/API)" — that handoff is this Type's enrollment intake surface (employer files, member elections). Two sides of one seam; keep-both.
- **vs Provider Network Management (§22, unprocessed — flag)**: provider contracting, credentialing, fee schedules, network adequacy vs the administration core's provider master and settlement seam. Sampled products carry provider data and portals inside the CAPS; network machinery is a candidate separate Type. Flag for that pass.
- **vs Utilization Management / Prior Authorization Platform (§22, unprocessed — flag)**: clinical-review machinery vs administrative record. Authorization status appears as an adjudication input inside CAPS products (HealthAxis provider portal "manage authorisations"; Softheon pharmacy prior authorization); UM suites ship separately (MHK CareProminence, Medecision). Flag for those passes.
- **vs Payer Care Management (§22, unprocessed — flag)**: Medecision and MHK CareProminence evidence the clinical-program layer as a distinct center (care plans, quality measures, risk models) with no enrollment/premium/claims of record. Keep-both expected; flag for that pass.
- **vs Healthcare Revenue Cycle Management / Provider Claims Management (§22)**: provider-side billing and claim submission vs payer-side obligation determination and settlement — opposite ends of the same claim. No confusion once the seat is named.
- **vs Patient Portal (§22)**: member portal is a servicing surface of this Type (L1), not a separate administration Type; Patient Portal leaf is the generic patient-facing surface (provider-anchored).
- **vs Public Benefits Management (§24, unprocessed)**: government-agency-side benefit programs; health plan administration remains insurance-side even for government programs (MA plans, Medicaid MCOs). The state-run MMIS is the government-operated variant of machinery similar to this Type — boundary note for both passes.
- **vs Pension Administration Platform (§08, processed)**: member-registry structural neighbor (long-horizon governed membership, rule-based entitlement, payment runs). Distinguishing axis: pension entitlement accrues from scheme participation (service/contributions); health coverage is event-driven enrollment under benefit products with per-service obligation determination. Cross-referenced in both directions.
- **vs Customer Service Platform (§07)**: member-services case management is a component (L1); the Type's center is the coverage/benefit record, not the service conversation.

## Uncertainties

- The two dominant legacy CAPS platforms (TriZetto QNXT/Facets) and the leading cloud challenger (HealthEdge HealthRules Payor) were unreachable (404/403) — the pass's main evidence gap; the canonical model rests on the reachable five (HealthAxis, MHK, Softheon, Medecision, DXC) plus the policy-pass family context. No product-specific claims are made from unreachable vendors.
- Epic ASA (EHR-native health plan administration) unreachable — the platform-native variant is described at L2 as an anchor only.
- Cost-sharing machinery depth (deductible/OOP-accumulator mechanics) was not detailed on any reachable page; benefit configuration is written conceptually ("cost-sharing structure, periodic thresholds, accumulated amounts") with moderate wording — no precise mechanics asserted.
- Medicaid MMIS official definition (medicaid.gov) unreachable — the state-run variant is described at low precision from product-side evidence only.
- Non-US / statutory-fund fit is inferred abstraction, not product observation — the sample is US-shaped (consistent with the §22 directory's US payer vocabulary).
- "Real-time" eligibility verification is vendor language (HealthAxis, MHK); actual response-time guarantees were not evidenced and are not asserted.
- Whether MHK's absence of a named adjudication module reflects a strict modular posture or unstated bundling could not be confirmed beyond the fetched pages.

## Final Synthesis

The Health Plan Administration System is the payer-side operating system of record for a health plan. Its world has four jointly-held structures: the member & coverage of record (an enrolled population carrying effective-dated coverage under the plan's products); enrollment & eligibility administration (coverage established/changed/ended through recorded events, eligibility continuously maintained and answerable in real time); benefit plan configuration (each product held as an operative rulebook of coverage, cost sharing, network applicability, and authorization rules); and benefit execution & settlement (the plan's obligation for care received is determined by applying the rulebook and settled by payment — in-system or through a connected claims engine). Around that core, mature products add premium billing (where premiums exist), provider and member portals, claims-operations depth, UM linkage, appeals & grievances, regulatory transaction machinery, reconciliation, document generation, analytics, and clinical-suite adjacency. The Type's market names are core administrative processing system (CAPS) and core administration system (CAS); its packaging poles are the bundled full core and modular suites around separate claims cores; its segment poles are commercial group, individual market, government programs, and TPA/self-funded. The boundaries that matter: member/benefit center vs contract-lifecycle center (insurance policy administration), system of record vs claims machinery (payer claims processing), payer side vs employer side (benefits administration), administration core vs clinical programs (payer care management, utilization management), and payer settlement vs provider billing (revenue cycle).
