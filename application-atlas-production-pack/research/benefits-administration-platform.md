# Research Notes — Benefits Administration Platform

Research date: 2026-09-06
Slug: `benefits-administration-platform`
Directory leaf: Benefits Administration Platform (§09 HR, Workforce & Talent)

---

## Research Goal

Determine what a **Benefits Administration Platform** actually is as an Application Type: the core objects it maintains, the lifecycle it administers, the workflows administrators and employees perform, the rules that govern behavior, and — critically — its boundaries against the dense neighboring cluster (Payroll System, HRIS/HCM, Pension Administration Platform, Insurance Policy Administration System, Employee Wellbeing Platform, Employee Onboarding Platform, Compensation Management Platform, Leave & Absence Management).

## Initial Boundary

Working hypothesis before research:

- An employer-side administrative layer that sits between the employer's benefit program design and the systems that execute it (insurance carriers, payroll).
- Core objects: benefit plans, eligibility rules, enrollment windows/events, employee elections, dependents/beneficiaries, employee cost contributions.
- The platform administers and transmits elections; it does not underwrite insurance, process claims, or pay employees.
- Likely confusion: (a) HCM suites where benefits is a module of the HRIS; (b) payroll systems that carry benefit deduction codes; (c) pension administration (scheme-side, decades-long); (d) wellbeing platforms (program participation vs plan enrollment).

## Research Questions

1. What is the central record? (election? enrollment? coverage?)
2. What triggers an enrollment or a change? (new hire, open enrollment, qualifying life events)
3. How do elections become effective — what leaves the system, to whom?
4. How are plans modeled: plan → coverage tiers → rates → employer/employee cost split → eligibility classes?
5. What eligibility rules exist (waiting periods, classes, dependent eligibility, verification)?
6. What compliance machinery is embedded (ACA in the US; what else)?
7. What are the admin-facing vs employee-facing surfaces?
8. How does the packaging vary: standalone pure-play platform vs HCM suite module vs SMB HRIS feature?
9. What happens at termination / coverage end / mid-year changes?
10. Where exactly is the boundary with payroll, HRIS, pension admin, wellbeing?

## Representative Products

Selection logic: different packaging philosophy + different customer tier + documentation accessibility.

| Product | Packaging | Segment | Why selected |
|---|---|---|---|
| PlanSource | standalone benefits administration pure-play | large employers (vendor states "1,000+ employees"), broker channel | the carrier-connectivity-first philosophy; richest compliance/service scope |
| Benefitfocus (Voya) | standalone benefits administration pure-play | enterprise employers; also serves health plans (carrier side) | second pure-play; explicitly enumerates employee-side and admin-side structure; serves both sides of the market |
| Paycor | HCM suite module (Benefits Administration bundle) | SMB/mid-market | the suite-module philosophy; conceptual article + product page both accessible |
| BerniePortal | all-in-one SMB HRIS supported by insurance brokers | small employers | the broker-embedded SMB variant; shows the minimal end of the spectrum |
| Workday | enterprise HCM suite module | large enterprise | suite-embedded enterprise variant; **positioning-level evidence only** (public docs lack a benefits slice) |

Considered and abandoned (per source-access rules; 1–2 failures each, not retried): BambooHR (site 403; help center is a JS-rendered Salesforce community), GoCo (transport errors ×2), bswift (403), Employee Navigator (403), Rippling (404 ×2 on guessed product URLs). SAP SuccessFactors benefits was not attempted (suite-embedded archetype already covered by the Workday note; consistent with sibling-pass findings that SuccessFactors docs are JS shells).

## Sources

Fetched 2026-09-06:

- PlanSource — Benefits Administration Buyer FAQ: https://plansource.com/products/benefits-administration/ (Tier 2)
- PlanSource — Platform & Services: https://plansource.com/platform-services/ (Tier 2)
- Benefitfocus — Benefits Administration (employer solutions): https://www.benefitfocus.com/employer-benefit-solutions/benefits-administration (Tier 2; includes product FAQ)
- Benefitfocus — root/overview: https://www.benefitfocus.com/ (Tier 2)
- Paycor — article "What Is Benefits Administration?": https://www.paycor.com/resource-center/articles/what-is-benefits-administration/ (Tier 2/3, conceptual)
- Paycor — Benefits Administration Software product page: https://www.paycor.com/hcm-software/benefits-administration-solutions/ (Tier 2)
- BerniePortal — root: https://www.bernieportal.com/ (Tier 2)
- Workday — Administrator Guide HCM landing: https://doc.workday.com/admin-guide/en-us/human-capital-management.html (Tier 1 slice; covers HRM/Employee Experience/Workforce Management/Talent Management only — **no benefits section publicly reachable**)

Unreachable (recorded as limitations): BambooHR, GoCo, bswift, Employee Navigator, Rippling, Workday benefits doc slice. All official content used is vendor-produced (product pages/FAQ/articles); no Tier-1 operational help center for any sampled product was fully reachable in this pass. Assertion strength is calibrated accordingly: structural claims are cross-product (Layer B), no precise operational numbers/limits are stated anywhere.

Sibling-pass cross-references (Layer B context): research/payroll-system.md (benefits admin = election source upstream of payroll), research/pension-administration-platform.md (employer-side short-cycle vs scheme-side decades-long), research/employee-wellbeing-platform.md (plan enrollment vs program participation; lifestyle spending accounts straddle), research/employee-onboarding-platform.md (onboarding collects elections as steps; benefits admin is the system of record).

---

## Product Observations

### PlanSource (evidence layer A, product positioning + FAQ + platform page)

- Positioning: purpose-built benefits administration for organizations with 1,000+ employees; multi-state, complex eligibility rules; serves employers, brokers/consultants, resellers, HCM partners, carriers.
- Own definition (FAQ): benefits administration software "helps employers manage employee benefits enrollment, eligibility, compliance, and ongoing changes in one centralized system… ensures benefits data stays accurate across payroll, carriers, and HR systems."
- Open enrollment: guided employee experiences, claims-based decision support, configurable workflows, real-time eligibility, AI-assisted communications; HR teams get "visibility into progress and exceptions."
- Compliance (product + service): ACA reporting, COBRA administration, dependent verification, eligibility tracking; QMCSO administration listed as a service.
- Extended services bundled around the platform: ACA administration (measurement, reporting, form distribution, federal and state mandates), carrier billing & payment (consolidate/automate carrier billing, reconciliation, payment), COBRA administration (notifications, elections, billing, compliance), consumer health account administration (HSA, FSA, HRA, LSA), custom communications, employee service center, advocacy services, QMCSO, total rewards statements, verification services (automated eligibility and dependent verification).
- Carrier connectivity as the differentiator: a carrier integration program connecting carriers via modern API integrations "which replace manual processes and weekly file feeds"; a Plan Configuration API that "automates plan setup and renewals directly from carrier systems"; real-time Enrollment APIs; Evidence of Insurability (EOI) integrations; provider directory search inside enrollment.
- Integrations: "leading HRIS, payroll, and workforce management platforms… accurate, real-time data flow across the HR ecosystem."
- AI (implementation/config, reporting, communications, dependent verification, virtual assistant, service-center insights) — marketing-level; structure only.
- Vendor-claimed metric (L3, not promoted): an EOI API quote — completion "from 27% to 87%".

### Benefitfocus (evidence layer A, product page + FAQ)

- Own definition (FAQ): benefits administration software "works by providing a centralized portal for benefits access for benefits administrators as well as employees. These systems automate the process of enrolling employees, managing benefits data, communicating and educating on plan details and managing integrations with benefit carriers, payroll and other third-party providers."
- Employee side (enumerated): personalized benefits portal; mobile-friendly access; new hire and life event support; plan comparison and claims-based decision support; contribution management; dependent and beneficiary management; year-round access and nudges to use benefits.
- Administrator side (enumerated): enrollment and participation management; employee and dependent administration; communications and content management; reporting and claims-based insights; data exchange support; case management; document management.
- Scope statement (FAQ): both "dedicated benefits administration companies and Human Capital Management solutions (HCMs) with benefits modules will cover the basics like initial benefits eligibility, annual enrollment and life change events" — direct confirmation of the shared baseline across the two packaging philosophies.
- Benefit types (FAQ): "health insurance, point solutions, voluntary benefits, retirement plans, and more"; a pre-vetted point-solution panel; voluntary benefits catalog.
- Implementation (FAQ): vendor-supported setup of all benefits "including electronic data interchange (EDI) builds, file integration and reconciliation."
- Integration (FAQ): with "payroll, HCM, HRIS and other benefits providers… to automate data sharing, help ensure accurate deductions."
- Surrounding solution areas (nav): Billing & Payroll, Data & Analytics, Service & Support (Benefits Contact Center), Compliance, Employee Engagement (decision support, incentives dashboard, mobile app, total rewards), Consumer Health Accounts, Communications.
- Distinctive: also operates on the **health plan (carrier) side** — eligibility & enrollment, billing & payments, data management & exchange, quoting & activation for insurers; ICHRA administration.

### Paycor (evidence layer A, product page + conceptual article)

- Product page framing: "Managing benefits plans, ACA eligibility, and workers' compensation is time consuming and complex."
- Benefits Administration bundle = Benefits Advisor + ACA Reporting + Workers' Compensation.
- Benefits Advisor: "Simplify open enrollment, receive automated alerts"; "automated workflows, robust EDI connections, detailed reporting, and open enrollment wizard"; an AI decision-support guide ("Ask Emma") offering real-time support, AI-powered insights, personalized recommendations.
- ACA Reporting: "manages all aspects of ACA tracking and reporting"; proactive notifications, comprehensive reporting, interactive dashboards.
- Workers' Compensation (adjacent module): pay-as-you-go, "automatic payroll deductions," "automatic data transfer to insurance carriers."
- Conceptual article (definitional support): benefits administration is "the process of creating, managing, and updating an organization's employee benefits program"; typically owned by HR; benefit menus span health insurance, retirement accounts, student-loan repayment, stock options, financial education, leave; compliance is the top challenge ("laws… change every year"); deadlines and reporting requirements tracked; open enrollment named as the process tools most support.
- Segment: SMB/mid-market HCM suite (payroll-native company).

### BerniePortal (evidence layer A, root page only — minimal)

- Positioning: "The HRIS Supported by the Broker You Already Trust"; "all-in-one HRIS, backed by their broker" for small employers.
- Benefits administration is one feature among an all-in-one HRIS set (ATS/onboarding/HR/payroll/benefits implied by feature-overview nav).
- Distribution philosophy: the insurance broker "stays in the loop throughout"; broker training center; broker partnership program.
- Customer quote: "Insurance renewal time is a breeze" — renewal season as the recurring admin event.
- KB/help portal exists but is a JS application; no article content fetchable. Claims kept minimal.

### Workday (evidence: positioning-level only)

- The public Administrator Guide for HCM exposes Human Resource Management, Employee Experience, Workforce Management, Talent Management — no Benefits section is publicly reachable (the benefits doc area is not in the public slice).
- Workday is included only to represent the enterprise HCM-suite packaging variant; no structural claims are made about it in this research or the final document beyond "suite-embedded benefits administration exists as a market variant" (supported by Benefitfocus FAQ's explicit mention of "HCM solutions with benefits modules" and PlanSource's HCM-partner positioning).

---

## Cross-product Comparison

| Dimension | PlanSource | Benefitfocus | Paycor | BerniePortal | Workday |
|---|---|---|---|---|---|
| Packaging | standalone pure-play | standalone pure-play | HCM suite bundle | all-in-one SMB HRIS feature | enterprise HCM suite module (not verified) |
| Segment | 1,000+ employees (vendor claim) | enterprise; also carrier side | SMB/mid-market | small employers | enterprise |
| Plan catalog as employer-defined offerings | Yes (FAQ: enrollment/eligibility/changes centralized) | Yes (FAQ: plan details managed/communicated) | Yes ("managing benefits plans") | Yes (feature scope) | presumed (unverified) |
| Eligibility administration | Yes ("real-time eligibility", verification services) | Yes ("initial benefits eligibility") | Yes ("ACA eligibility") | implied | presumed |
| Employee self-service enrollment | Yes (guided experiences, decision support) | Yes (personalized portal, plan comparison) | Yes (enrollment wizard) | Yes (self-service portal) | presumed |
| Enrollment windows/events | open enrollment + life events (guided flows) | "new hire and life event support" + annual enrollment | "open enrollment wizard" | renewal season (customer quote) | presumed |
| Life event change processing | Yes (configurable workflows) | Yes (explicitly enumerated) | Yes (automated workflows/alerts) | implied | presumed |
| Dependents & beneficiaries | dependent verification services | dependent and beneficiary management (explicit) | dependent administration (implied via bundle) | implied | presumed |
| Carrier data exchange | core differentiator: API program replacing "weekly file feeds"; EOI | EDI builds, file integration, reconciliation | "robust EDI connections"; workers' comp carrier data transfer | broker-mediated (not evidenced in detail) | presumed |
| Payroll linkage | HRIS/payroll integrations, "accurate… data flow" | integrations "help ensure accurate deductions" | same-suite payroll; workers' comp "automatic payroll deductions" | same-suite payroll | presumed |
| Billing/reconciliation with carriers | carrier billing & payment service | Billing & Payroll solution area | not evidenced | not evidenced | presumed |
| Compliance machinery | ACA, COBRA, QMCSO, dependent verification (services) | Compliance solution area; ACA named | ACA Reporting module | not evidenced | presumed |
| Consumer health accounts (FSA/HSA/HRA) | Yes (HSA/FSA/HRA/LSA service) | Yes (Consumer Health Accounts) | not evidenced | not evidenced | presumed |
| Decision support | claims-based decision support; AI assistant | plan comparison, claims-based decision support (SAVVI tool disclosed) | "Ask Emma" AI guide | not evidenced | presumed |
| Total rewards statements | Yes (service) | Yes (solution area) | not evidenced | not evidenced | presumed |
| Outsourced services (service center, billing, verification) | Yes (deep: full-scope outsourced services) | Yes (contact center, service & support) | not evidenced | broker plays this role | presumed |
| Total benefits scope | health, voluntary, point solutions, consumer accounts, lifestyle (LSA) | health, point solutions, voluntary, retirement | benefits plans + workers' comp focus | benefits + broker channel | presumed |

Evidence: every "Yes" above is Layer A (directly observed on the cited vendor page); "implied" = indirect; "presumed (unverified)" = market expectation only, kept out of all strong claims.

**Key structural convergence (Layer B):** three independently written vendor definitions (PlanSource, Benefitfocus, Paycor) all describe the same spine — *enrollment + eligibility + ongoing changes in one system, kept accurate across payroll, carriers, and HR systems*. Benefitfocus explicitly states the shared baseline across pure-plays and HCM modules: "initial benefits eligibility, annual enrollment and life change events."

---

## Canonical Model (concept layer)

```text
Employer benefit program (defined by the employer, per plan year)
├── Benefit plan catalog        — offerings (medical/dental/vision/life/disability/retirement/
│                                 voluntary/point solutions) each with rules
│     └── eligibility rules     — who may elect (employee classes, status, waiting periods)
│     └── coverage tiers        — employee / +spouse / +family etc.
│     └── rates & cost split    — premiums and employer/employee contribution scheme
├── Eligible population         — workforce (from HRIS/employment records) + their dependents
│     └── dependents / beneficiaries attached to the member
├── Enrollment events & windows — bounded periods in which elections may be made
│     └── new hire / open enrollment / qualifying life events
├── ELECTION RECORD (central object)
│     └── member × plan year × plan × coverage tier × covered dependents
│         × beneficiary × employee cost × effective dates; tracked lifecycle
├── Change administration       — life event → change window → documentation → updated elections
└── Effectuation handoff        — elections leave the system to become effective:
      ├── carriers/administrators (enrollment files/EDI/APIs) → coverage
      ├── payroll (deduction instructions) → paycheck
      └── billing reconciliation against carrier invoices
```

## Abstraction Levels

### Level 0 — Defining Invariant

The smallest structure without which the software is no longer a benefits administration platform:

1. **Employer-defined benefit plan catalog** — named offerings with eligibility rules and cost sharing, administered for a population (per plan year).
2. **Eligibility administration** — determining which members of the workforce (and their dependents) may elect which offerings.
3. **Employee benefit election as the central tracked record** — a member's binding choice (plan × coverage tier × covered dependents × employee cost × effective dates) with a tracked lifecycle.
4. **Bounded enrollment events/windows** — elections are possible only during defined events (hire, open enrollment, qualifying life events), not at arbitrary times.
5. **Effectuation handoff** — election outcomes are transmitted to the systems that make them effective (carrier enrollment and/or payroll deductions). The platform administers and transmits; it neither underwrites nor pays.

Historical/market-sample check (§24-style reasoning, recorded here): 1990s US cafeteria-plan/flexible-benefits administrators (plan menu + eligibility + elections + deduction handoff), UK flexible-benefits/salary-sacrifice platforms, and minimal SMB HRIS benefits tracking (records + exports to broker/payroll) all satisfy these five invariants without APIs, AI, compliance services, or marketplaces. The invariants survive the check.

### Level 1 — Common Mature Structure

Present across most sampled products (Layer B unless noted):

- dependent and beneficiary management
- qualifying-life-event change workflows (change window + documentation + updated elections)
- open enrollment campaign machinery (window configuration, communications, HR visibility into progress/exceptions)
- plan configuration depth: coverage tiers, rate tables, employer contribution schemes, eligibility classes
- standardized carrier data exchange (EDI file builds/integration; API-based feeds in the most mature implementations)
- payroll deduction linkage ("ensure accurate deductions"; deduction mapping)
- carrier billing reconciliation (pure-play platforms; as product areas/services)
- compliance machinery — in the US: ACA tracking/reporting (three of three direct samples); dependent verification (two); some add COBRA and QMCSO administration (single-source: PlanSource — kept weak)
- employee decision support (plan comparison; claims-based guidance; AI assistants — three of three direct samples)
- reporting: enrollment/participation status, cost reporting (three of three)
- communications/content management (two: PlanSource, Benefitfocus)
- consumer health account administration, FSA/HSA/HRA (two pure-plays: PlanSource, Benefitfocus)
- total rewards statements (two: PlanSource, Benefitfocus)
- employee service center / advocacy / benefits contact center (two: PlanSource, Benefitfocus)
- mobile access, year-round engagement/nudges (Benefitfocus explicit; PlanSource "consumer-grade experience")

### Level 2 — Variant / Optional Structure

- **Packaging**: standalone pure-play platform (PlanSource, Benefitfocus) ↔ HCM/HRIS suite module (Paycor; Workday-class enterprise suites) ↔ broker-embedded SMB HRIS feature (BerniePortal).
- **Regional/regulatory regime**: the researched sample is US-centric (ACA/COBRA-shaped compliance). Other markets shape the same skeleton differently (e.g., pension/retirement-centric packages, flexible benefits/salary sacrifice) — asserted only as variant, no direct evidence this pass.
- **Benefits scope**: core insured plans only → + voluntary benefits → + point-solution ecosystems → + consumer health accounts (FSA/HSA/HRA/LSA) → + retirement.
- **Service depth**: software-only vs software + outsourced services (ACA/COBRA/billing/verification/service center).
- **Marketplace posture**: pre-vetted voluntary/point-solution catalogs (Benefitfocus); carrier quoting/activation (Benefitfocus health-plan side).
- **Carrier-side deployment**: the same platform class also serves health plans (Benefitfocus) — a two-sided variant.
- **Decision-support sophistication**: static plan comparison → claims-based guidance → AI assistants.
- **Adjacent modules**: workers' compensation administration (Paycor), lifestyle spending accounts (PlanSource), ICHRA (Benefitfocus, carrier side).

### Level 3 — Vendor-specific (research notes only)

- PlanSource: "Boost" carrier integration program; Plan Configuration API (plan setup/renewals automated from carrier systems); real-time Enrollment APIs; in-flow EOI with provider directory search; agentic-AI implementation (plan-document ingestion, config pre-population, test generation, EDI template matching); EOI completion metric "27% → 87%"; positioning "1,000+ employees".
- Paycor: "Ask Emma" AI decision-support guide; Benefits Advisor / ACA Reporting / Workers' Compensation bundle naming; pay-as-you-go workers' comp with "automatic payroll deductions"; Paychex acquisition context.
- Benefitfocus: SAVVI-powered Personalized Decision Support (with disclosed ownership conflict-of-interest); "Care Panel" point-solution program; carrier-side solutions (eligibility & enrollment, quoting & activation, ICHRA administration); HITRUST/PCI certifications; "2.4% vs 6%" cost-trend marketing claim.
- BerniePortal: broker-in-the-loop distribution model (broker as support/training channel); broker training center.
- Workday: (nothing public to record).

## Vendor-specific Findings → Rejected from Canonical Core

- Carrier API programs vs weekly EDI feeds: implementation maturity of the *same* invariant (effectuation handoff) — not definitional.
- AI decision support / virtual assistants: modern additive layer; three products show it but in different forms; excluded from the defining core.
- Outsourced services (service centers, billing bureaus): a business-model variant of the pure-plays, not the Type.
- Health-plan-side (carrier-side) operation: a second market served by one vendor; not part of the employer-side Type definition.
- Workers' comp, lifestyle accounts, ICHRA: adjacent modules; product-specific placement.

## Boundary Findings

1. **vs Payroll System.** Payroll executes pay runs and carries deduction codes; it does not define plan menus, determine eligibility, run open enrollment, or transmit elections to carriers. Benefits admin produces elections + employee cost shares and hands them to payroll as instructions ("help ensure accurate deductions" — Benefitfocus; "automatic payroll deductions" — Paycor workers' comp module). Prior pass (research/payroll-system.md) records benefits administration as an election *source upstream* of payroll. **Test: remove the plan catalog, eligibility administration, and election lifecycle → what remains is payroll with deduction codes. Remove pay execution → what remains is benefits administration.**
2. **vs HRIS / HCM.** The HRIS owns the employment record (worker master) that the benefits platform consumes for eligibility. In suite products benefits is a module on the same population — the boundary is data-ownership posture, not feature presence. **Test: remove benefit plans/elections → HRIS; remove the general employment record (job, org, comp history) → benefits administration.**
3. **vs Pension Administration Platform.** Established in the pension pass: benefits administration is employer-side and short-cycle (annual enrollment and elections across many benefit types; handoff, no payment); pension administration is scheme-side and spans decades through accrual rules to payment of retirement income. **Test: remove the scheme-side decades-long accrual/payment lifecycle → benefits administration; add it and shift to the scheme's perspective → pension administration.**
4. **vs Insurance Policy Administration System.** Policy administration is carrier-side: policyholder records, underwriting, premium billing to policyholders, claims. Benefits administration is employer-side: which of *our employees* elected *which group plan*, at what cost split, fed to the carrier. **Test: move the perspective from the employer's workforce to the insurer's policyholders → insurance policy administration.**
5. **vs Employee Wellbeing Platform.** Established in the wellbeing pass: benefits administration administers *enrollment and eligibility in employer-funded plans* (insurance-like elections); wellbeing administers *participation in programs*. Funded wellness wallets / lifestyle spending accounts straddle the two. **Test: elections of funded coverage → benefits administration; participation and engagement in programs → wellbeing.**
6. **vs Employee Onboarding Platform.** Onboarding collects benefits-election data as a step in a wider wind-up process; the election system of record is the benefits platform (documented in the onboarding pass: GoCo native vs "payroll remains the system of record" delegation). **Test: remove the day-one task-fan-out structure and keep only the election machinery → benefits administration.**
7. **vs Compensation Management Platform.** Both configure "plans" and cost to the employer. Compensation administers *pay* structures (salary ranges, merit budgets, bonuses); benefits administers *elections of coverage* in kind. **Test: elections with covered dependents and carrier handoff → benefits; pay ranges and merit cycles → compensation.**
8. **vs Leave & Absence Management.** Leave events interact with benefits (unpaid leave can affect eligibility/coverage/billing) but the managed object is absence from work, not an election. Boundary is adjacency, not overlap.

No taxonomy conflict found: the leaf is a coherent, independently documentable Application Type; pure-play and suite-module packaging are variants of one Type (confirmed by Benefitfocus FAQ's explicit statement that both cover "initial benefits eligibility, annual enrollment and life change events").

## Uncertainties

1. **No Tier-1 operational help center was fully reachable** for any sampled product (help portals are JS apps or 403/404). All structure comes from vendor product pages/FAQs. Consequently: no precise operational facts (QLE change-window day counts, waiting-period rules, deduction timing, file formats, EDI transaction codes, deadline calendars) are asserted anywhere. The final document is calibrated to structure-level claims.
2. **Enterprise suite internals (Workday-class)**: unverified; the suite-embedded variant rests on positioning plus Benefitfocus/PlanSource statements about HCM modules. Kept weak.
3. **Regional breadth**: every directly evidenced product is US-market-shaped. UK/EU/APAC benefits-administration variants (salary sacrifice, flexible benefits, pension-heavy packages) are asserted only as variants from general market structure.
4. **SMB minimal end**: BerniePortal evidence is root-page-level only; the minimal feature set of SMB benefits tracking (how far "tracking" goes before it stops being administration) is under-evidenced. The final document phrases the low end generically.
5. **Retirement plans** inside benefits administration: Benefitfocus names retirement as a manageable benefit type; the depth (recordkeeping vs election-and-deduction handoff only) was not verifiable. Kept at "election and deduction handoff" level.
6. **Qualifying-life-event catalog**: confirmed as a mechanism (two products explicitly; a third implicitly) but the standard event list was not enumerable from official docs; the final document names only the events directly evidenced (birth/marriage-type events are NOT named — "life events" stays generic).

## Final Synthesis

A Benefits Administration Platform is the employer-side administrative layer for employer-sponsored benefits: it holds the employer's benefit plan catalog with its eligibility rules and cost-sharing scheme, determines who may elect what, captures employee elections during bounded enrollment events (hire, open enrollment, qualifying life events), tracks each election and its lifecycle (changes, coverage ends), and hands the outcomes to the systems that make them effective — carriers for coverage, payroll for deductions — with billing reconciliation and (in mature markets) compliance machinery around the cycle. The platform administers and transmits; carriers insure and payroll pays. Packaging ranges from standalone pure-play platforms (carrier-connectivity- and compliance-heavy, often with outsourced services) through HCM-suite modules (payroll- and HRIS-adjacent) to broker-supported SMB HRIS features (minimal, renewal-driven). The defining core is deliberately smaller than the modern feature set: plan catalog + eligibility + election record + bounded windows + effectuation handoff.
