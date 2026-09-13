# Research Notes — Pension Administration Platform

## Research Goal

Understand what a Pension Administration Platform actually is as an Application Type: the core objects it maintains, the lifecycle it administers, the workflows administrators and members perform, the rules that govern behavior, and the boundaries against neighboring Types (Insurance Policy Administration System, Benefits Administration Platform, Payroll System, Actuarial Modeling Platform, Retirement Planning Application, Fund Administration / Transfer Agency).

## Initial Boundary

Working hypothesis at start:

- Core: administration of occupational/retirement pension schemes — member registry with service/contribution history, rule-based benefit entitlement calculation, payment of benefits (retirement income, lump sums, transfers, death benefits), member self-service, employer data flows.
- Users: pension administrators / case handlers at pension funds, master trusts, third-party administrators (TPAs), insurers, in-house scheme teams; members (self-service); employers (data submission).
- Likely confusions:
  - vs Insurance Policy Administration System (structurally similar long-horizon record + payment pattern)
  - vs Benefits Administration Platform (employer-side, short-cycle enrollment)
  - vs Payroll System (employer-side wage computation; contributions flow out of payroll into the scheme)
  - vs Actuarial Modeling Platform (scheme-level liability valuation vs member-level administration)
  - vs Retirement Planning Application (consumer planning vs administration)
  - vs Fund Administration / Transfer Agency (fund-side vs scheme-side)

Known prior context from sibling research: `actuarial-modeling-platform` research notes already record the boundary "admin = member/benefit records and processes; actuarial modeling = valuation of the pension liability". This research must stay consistent with that.

## Research Questions

1. What are the central objects (scheme, member, accrual record, entitlement, case, payment)?
2. What is the member lifecycle the platform administers (join → accrual → leave/defer → retire → payment → death/dependants)?
3. How does benefit calculation work operationally (scheme rules, service/salary/contribution history, effective dating)?
4. How do contributions and employer data flow in, and how are they reconciled?
5. What payment operations exist (recurring pension payroll, tax handling, bank files, one-off settlements, overpayments)?
6. What roles and surfaces exist (admin workbench, member portal, employer portal, batch operations)?
7. Which rules genuinely govern system behavior (vesting, eligibility, indexation, tax, statutory reporting)?
8. What exceptions matter (overpayment, back-service corrections, trace transfers, deceased members, data migration)?
9. Where is the boundary against each neighboring Type — what would have to be removed for the product to become the neighbor?

## Representative Products

Selected for market representativeness, structural diversity (UK software+BPO / US institutional / US public-sector / Nordic), and different product philosophies:

| Product | Vendor | Market position | Evidence layer achieved |
|---|---|---|---|
| Aquila (Heywood Pension Technologies, formerly Aquila Heywood) | Heywood Pension Technologies | Largest independent UK pension administration software; DB/DC schemes, master trusts, TPAs; software + BPO | none — source unreachable |
| V3LOX | Vitech Systems Group | US/UK institutional pension & benefits administration (public sector, multiemployer, corporate, insurance) | none — source unreachable |
| PensionTrust | FIS | Long-established US public-sector pension fund administration (defined-benefit focus) | none — source unreachable |
| Etract | Etract AB | Nordic pension administration platform used by pension companies | none — source unreachable |

Additional market anchor considered but not fetched: TCS BaNCS for Pensions (global, insurance-grade pensions administration).

## Sources

### Source Access Record (2026-09-06)

The research environment could not reach any research-relevant source. Every fetch attempt failed (timeout, transport error, or 403). Attempts made:

| URL | Result |
|---|---|
| https://www.aquilaheywood.com/ | timeout ×2 |
| https://vitech.com/products/ , https://vitech.com , https://www.vitech.com | transport error ×3 |
| https://www.etract.se/en/ , https://www.etract.se | transport error ×2 |
| https://heywoodpensiontechnologies.com , https://www.heywoodpensiontechnologies.com/ | transport error ×2 |
| https://www.tcwcs.com/bancs-pensions | transport error |
| https://www.fisglobal.com/products/pensiontrust , https://www.fisglobal.com/ | timeout ×2 |
| https://www.tcs.com/what-we-do/products-platforms/bancs | 403 |
| https://en.wikipedia.org/wiki/Pension | timeout ×2 |
| https://duckduckgo.com/html/?q=... | timeout |
| https://example.com | **success** (control test — network partially available, egress heavily restricted) |

Conclusion: official operational documentation (Tier 1) and official product pages (Tier 2) were **not obtainable** on the research date. No Tier 3 external sources were reachable either.

### Evidence Consequence

Per the evidence rules:

- No Layer-A (directly observed) findings exist for any product. **No product-specific feature, module, limit, default, or workflow claim is made anywhere in this research or the final document.**
- The canonical model below is a **Layer-C canonical inference**: a domain-level model of what pension administration requires as an activity, written at deliberately reduced precision.
- No precise operational facts (numeric limits, time windows, default settings, exact state names, exact tax rules) are stated. All such detail is deliberately absent.
- The final document carries a sourcing-limitation note in its Sources section and uses calibrated wording throughout ("typically", "commonly", "in this market").
- Representative products are named as **market anchors only** (their identity and market position is general market knowledge), never as evidence for specific capabilities.

## Product Observations

**None available.** All four sampled products' official documentation was unreachable. Per the source-access limitation rule, no product-specific observations were recorded rather than filling them from model memory.

What follows instead is the domain model that any pension administration activity requires, written at canonical level. It is the basis for the final document, with the explicit caveat that it was not verified against any specific product's documentation on the research date.

### Domain Model Observations (canonical, unverified against product docs)

**Objects the activity requires:**

- **Scheme / plan** — the governing container. A pension scheme (UK occupational scheme, US public or corporate plan, Nordic/Dutch pension fund, DC recordkeeping plan) defines the rules under which members participate: eligibility, accrual, vesting, indexation, survivor benefits, payment forms. Multiple schemes can be administered on one platform; multiple sponsoring employers can participate in one scheme.
- **Member** — an identified person whose participation in a scheme is tracked. Membership is long-horizon (decades), often outliving active employment (deferred/leaver status).
- **Accrual record** — the member's history inside the scheme: service history, pensionable salary history (DB), contribution history (DC), and derived entitlement. This is the platform's central data asset; corrections must be possible retroactively with effective dates.
- **Benefit entitlement** — what the member is entitled to, computed from the accrual record under scheme rules at a point in time or at a life event. In DB: formula-based (service × accrual rate × salary, revalued/indexed). In DC: the accumulated contribution account (often with unitized investment holdings).
- **Life event / case** — administrative work is event-driven: join, contribution cycle, absence, leaving, transfer, retirement, death. Each event triggers processing against the member's record; mature platforms track these as cases with owners, tasks, and status.
- **Benefit payment** — the output obligation: recurring retirement income (pension payroll: gross calculation, tax, bank payment files, payslips, annual tax statements) and one-off settlements (lump sums, transfers out, death benefits).
- **Dependants / beneficiaries** — survivor benefits require tracking people related to the member's entitlement.
- **Employer participation** — sponsoring employers submit contribution/service data and are billed in some scheme types; employer-side data quality is a standing operational problem.
- **Correspondence / documents** — statements, calculation letters, election forms, payment notifications; generation and retention are core.

**Lifecycle the activity requires:**

```text
Scheme membership established (join / auto-enrolment / transfer in)
→ accrual maintained (periodic employer data: contributions, service, salary)
→ life event (leave / retire / transfer / die)
→ entitlement calculated under scheme rules
→ options presented and elected (payment form, transfer, deferral)
→ benefit set up and paid (recurring payroll and/or one-off settlement)
→ ongoing maintenance (indexation, statements, corrections, tax)
→ death → survivor/dependant benefits
```

**Rules that govern the activity:**

- Scheme rules (trust deed/rules/statute) are the supreme law inside the platform; the platform encodes them as configuration.
- Effective dating and retro-calculation: records span decades; rule changes and data corrections must recompute history.
- Payment accuracy: overpayments create recoverable debts; underpayments create complaints and regulatory exposure.
- Tax treatment of pension payments is jurisdiction-specific and mandatory in the payment run.
- Long retention, full audit trail, member data protection.
- Transfer safeguards: value calculation and coordination with receiving schemes.

**Surfaces the activity requires:**

- Administrator workbench (member record view, case queues, calculation screens, payment runs, correspondence).
- Member self-service (entitlement view, statements, personal data, retirement modelling) — modern, not defining.
- Employer data exchange (submissions, validation, reconciliation) — modern form is a portal; historical form was file exchange.
- Batch/operations surfaces (scheduled runs: contributions processing, indexation, pension payroll, statement generation).

## Cross-product Comparison

**Could not be executed.** No product documentation was reachable, so no cross-product comparison table of observed capabilities can be produced. The comparison dimensions that would have been used:

- scheme types supported (DB / DC / hybrid)
- operating model served (in-house / TPA-bureau / master trust)
- regional regime depth (UK / US public / US corporate / Nordic)
- case-management depth
- payment-run depth (pension payroll, tax)
- member/employer portal depth
- DC investment accounting depth
- deployment posture (SaaS / hosted / on-prem)

These dimensions are recorded as **unverified**. The final document therefore describes the Type's common structure in calibrated language without attributing specifics to any product.

## Canonical Abstraction

### L0 — Defining Invariant (deliberately minimal)

A Pension Administration Platform is recognizable as such if and only if it maintains:

1. **Scheme-governed member registry** — identified members whose participation is defined by the rules of one or more pension schemes/plans (not by a commercial insurance contract, not by an employment contract).
2. **Long-horizon accrual record** — per member, the service and/or contribution history from which entitlement derives, maintained over decades and correctable retroactively.
3. **Rule-based benefit calculation at life events** — computing what a member is entitled to (now or at a future date) from their accrual record under the scheme's rules.
4. **Benefit payment administration** — putting the benefit in the member's hands: recurring retirement-income payments and/or one-off settlements (lump sums, transfers, death benefits).

Test: remove the scheme governance → generic HR/person record system. Remove the accrual→entitlement link → contact registry. Remove calculation → static record store. Remove payment administration → a records/reporting system, not pension administration. All four are needed.

### Historical / market-sample check (§24)

- 1980s–90s mainframe pension administration systems (US public plans, UK scheme bureaus): had member registry, service history, benefit calculation, pension payroll — **fit L0**. They lacked portals, workflow objects, configurable rules engines, investment tracking — confirming those are not L0.
- DB-only systems (no investment accounting): fit L0 — confirming DC investment tracking is not L0.
- DC recordkeeping platforms (US 401(k)-style): plan-governed participant accounts, contribution accrual, distribution/vesting calculation, payment administration — **fit L0**. The Type therefore spans DB administration and DC recordkeeping.
- Nordic/Dutch/Canadian occupational pension systems: same core under different regimes — fit L0.
- Insurance-run group pension books: scheme/plan-governed membership still present — fit L0; the commercial-contract pole is where the boundary with policy administration begins.

Conclusion: L0 holds across eras, regions, and scheme types. The definition does not overfit the modern SaaS portal era.

### L1 — Common Mature Structure

Very common in current products but not required to recognize the Type:

- member self-service portal (entitlement view, statements, personal data updates, retirement modelling)
- employer data exchange with validation and reconciliation (portal or file-based)
- case/event management with workflow, task assignment, and status tracking
- pension payroll processing (recurring runs: gross-to-net, tax, bank files, payslips, annual tax statements)
- indexation / increase processing per scheme rules
- death & dependant processing (survivor benefits)
- transfer / trace processing (value calculation, receiving-scheme coordination)
- overpayment detection and recovery
- annual benefit statements and member communications (document generation)
- record correction with retro-effective dating (back-service adjustments)
- statutory/regulatory reporting and audit trail
- role-based administration with delegated access
- retirement forecasting / modelling tools for members
- data migration and scheme-conversion tooling (common when platforms take over schemes)
- integrations: payroll/HR (employer data), investment custodians/fund managers (DC unit prices), banks (payment files), tax authorities, document/letter services

### L2 — Variant / Optional Structure

- scheme type: DB / DC / hybrid; DB-centric administration vs DC recordkeeping (unitized accounting, investment elections, fund switching)
- operating model: in-house scheme team vs TPA/bureau (software + BPO) vs master-trust operator
- customer scale: single-employer scheme vs multi-employer/master trust vs public-sector plan vs insurance-run book
- regional regime: UK occupational (incl. auto-enrolment, PPF context), US ERISA corporate, US public-sector DB, Nordic occupational, Dutch pension funds, Canadian registered plans
- regulatory overlays: funding/valuation regimes, member-protection schemes, auto-enrolment duties
- DC investment-choice depth (self-select funds, unitized vs pooled accounting)
- buy-out / bulk annuity / pension-risk-transfer processing
- deployment: vendor-hosted SaaS vs hosted legacy vs on-prem mainframe
- bundling: with actuarial services, investment administration, or broader HCM/benefits suites

### L3 — Vendor-specific Structure

Not researched (sources unreachable). No vendor-specific findings are recorded. Product names (Aquila, V3LOX, PensionTrust, Etract, BaNCS) are anchors only.

## Vendor-specific Findings

None recorded — no product documentation was reachable. Deliberately left empty rather than filled from model memory.

## Rejected Findings

- **"Pension administration = DB only"** — rejected. DC recordkeeping fits the same L0 (plan-governed accounts, contribution accrual, distribution calculation, payment).
- **"Pension administration = member portal + modern web"** — rejected by the historical check; mainframe-era systems fit L0 without any portal.
- **"Pension administration includes investment management"** — rejected. Investment administration is a separate function; DC platforms track unit holdings as part of the entitlement record, but managing investments is not the Type's defining activity.
- **"Pension administration = insurance policy administration"** — rejected. Governance basis differs: scheme/trust/statute with employer participation vs commercial contract sold by an insurer. See Boundary Findings.
- **"Pension administration includes actuarial valuation"** — rejected. Valuation of the scheme liability is a separate Type (consistent with the actuarial-modeling-platform research notes); admin platforms may exchange data with it.

## Boundary Findings

| Neighbor | Relationship | Distinction | "Remove what → becomes the neighbor" |
|---|---|---|---|
| Insurance Policy Administration System | structurally closest | policy admin centers on a commercial contract (policy) with premiums/coverage sold by an insurer; pension admin centers on scheme membership with trust/statutory rules, employer participation, and employment-based accrual | remove scheme/employer/statutory governance and employment-based accrual → policy administration |
| Benefits Administration Platform | adjacent (employer-side) | benefits admin handles the employer's short-cycle enrollment across many benefit types (elections); pension admin handles the scheme-side decades-long lifecycle including payment | remove the scheme-side accrual/payment lifecycle → benefits administration |
| Payroll System | adjacent (employer-side) | payroll computes and pays wages for active employment and forwards contributions; pension admin receives contributions and maintains the scheme-side record | remove the scheme-side entitlement and benefit payment → payroll |
| Actuarial Modeling Platform | complementary | actuarial platforms value the scheme liability (scheme-level projections); pension admin maintains member-level records and processes | remove member-level administration, keep scheme-level valuation → actuarial modeling |
| Retirement Planning Application | consumer-facing neighbor | planning apps project retirement outcomes for an individual; no administration of records or payments | remove administration (records, cases, payments) → retirement planning |
| Fund Administration / Transfer Agency | fund-side neighbor | fund admin maintains fund NAV and investor registers for investment funds; pension admin maintains scheme membership and entitlements (a scheme's investments may sit in fund-administered vehicles) | move from scheme-side entitlement to fund-side NAV/investor register → fund administration |
| Wealth Management Platform | individual-account neighbor | wealth platforms manage individual investment accounts without scheme governance or pension lifecycle | remove scheme governance and pension lifecycle → wealth management |

The most important boundary is with **Insurance Policy Administration System**: both are long-horizon, rule-governed, payment-producing record systems. The distinguishing axis is the **governance basis of the entitlement** (scheme/trust/statute + employer participation + employment-based accrual vs commercial contract + premium). Insurers operating buy-out/bulk-annuity books sit near this boundary; a pension admin platform may administer the scheme while a policy admin system administers the resulting annuity contracts.

## Uncertainties

1. **Product capability specifics** — entirely unverified; no product documentation was reachable. Everything product-specific is deliberately absent.
2. **Whether sampled vendors position pensions administration inside broader suites** (e.g., pensions + benefits + absence) — plausible from general market knowledge but unverified; not asserted anywhere.
3. **Depth of DC investment accounting** in each sampled product — unverified.
4. **Regional coverage claims** (which regimes each product serves) — unverified.
5. **Whether "Pension Administration Platform" and "retirement plan recordkeeping" should be separate directory leaves** — this research treats DC recordkeeping as a Variant within this Type (same L0); if the taxonomy later wants a separate leaf, that is a taxonomy decision to record, not make. Recorded as a possible Boundary Issue.
6. **Exact module composition and terminology** of real products (e.g., how vendors name "case", "event", "payroll run") — unverified; the final document uses conceptual terms with a note that exact labels vary.

## Final Synthesis

A Pension Administration Platform is the system of record and the operating system for pension schemes: it maintains scheme-governed member records with decades-long accrual histories, computes benefits under scheme rules at life events, and administers the payment of those benefits — recurring retirement income and one-off settlements — while coordinating employers, members, and regulators. Its defining core is small (scheme-governed member registry + accrual record + rule-based benefit calculation + benefit payment administration); portals, case management, pension payroll machinery, indexation, statements, and integrations are the common mature structure that makes it practical; scheme type (DB/DC), operating model (in-house/TPA/master trust), regional regime, and deployment are variants. The Type is structurally closest to insurance policy administration but is distinguished by the governance basis of the entitlement. Evidence for this synthesis is canonical-level only: no product documentation was reachable on the research date, so the final document is written with reduced assertion strength and no product-specific claims.
