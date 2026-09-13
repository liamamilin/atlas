# Research Notes — Value-based Care Platform

Research date: 2026-09-09
Leaf: Value-based Care Platform (DIRECTORY §22 Healthcare & Life Sciences)
Slug: value-based-care-platform

## Research Goal

Understand what a "Value-based Care Platform" actually is as an Application Type: what unit of record it holds, who operates it, what its core workflow is, and where its boundary sits against the neighboring §22 types (Population Health Management, Payer Care Management, Healthcare Revenue Cycle Management, Provider Network Management, Healthcare Quality Management, Utilization Management).

Two pre-hung flags must be discharged from sibling passes:

1. **payer-care-management (2026-09-08)**: "vs value-based-care-platform — payer↔provider contract/payment/quality-reporting machinery vs the plan's own member-facing care operations; co-deployed in vendor portfolios (ZeOmega 'value-based care reporting'; Inovalon 'Value-Based Care Management' products...)"
2. **population-health-management (2026-09-09)**: "value-based-care-platform — contract/payment/quality-reporting machinery vs the population management loop (PHM vendors sell VBC reporting as separate solutions/products: Azara VBC Reporting, Arcadia Contract IQ, Health Catalyst VBC Performance)"

## Initial Boundary (working hypothesis before research)

- Hypothesis: the Type is the *arrangement machinery* of value-based care — the payer↔provider payment arrangement as unit of record, performance measured against the arrangement's terms, and the money resolved under those terms.
- Likely confusions: PHM (population loop), payer care management (plan's clinical programs), RCM (claim-level billing), provider network management (network configuration), healthcare quality management (org quality governance), CLM (generic contract lifecycle).
- Unknowns: Is settlement computation definitional or optional? Is the Type US-CMS-specific or generic? Does one side of the market (provider vs payer) own it?

## Research Questions

1. What is the unit of record — contract? arrangement? program? What does it carry?
2. How does the platform measure performance (data sources, attribution, measures, benchmarks, risk adjustment)?
3. How does the money work (projection, tracking, settlement, adjudication, funds flow, reconciliation/audit)?
4. Who operates the platform — provider side, payer side, neutral, or both?
5. What interfaces exist (contract workspace, dashboards, worklists, financial views, data exchange)?
6. Where is the boundary vs PHM / payer care management / RCM / network management / quality management?
7. Historical check: does the definition hold for pre-"VBC-label" payment arrangements (1990s capitation, early-2000s pay-for-performance)?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer tiers:

| Product | Philosophy / pole | Customer tier |
|---|---|---|
| Arcadia (Contract IQ + VBC software) | provider-side data platform; contract creation/modeling as a distinct application; managed-services posture | health systems, CINs, ACOs |
| Health Catalyst (VBC Performance / VBC Intelligence) | provider-side analytics; transparent contract-level performance measurement | health systems |
| Azara Healthcare (VBC Reporting) | safety-net/FQHC tier; payer-provider data collaboration around VBC programs | community health centers, small ACOs, regional plans |
| Cedar Gate Technologies | payment-model-centric; bundles + capitation adjudication; both payer and provider sides; self-funded | payers, providers (ACO/CIN/IDN/IPA/MSO/FQHC), self-funded employers |
| Innovaccer (VBC suite + Contract Management) | data-activation platform with actuarial-intelligence contract layer; provider + payer | health systems, ACOs, regional plans |

Boundary observation (not a core sample member): ZeOmega (Jiva) — payer care management platform whose VBC reporting is a capability (Jiva Care Quality Navigator), used to confirm co-deployment behavior.

## Sources

All fetched 2026-09-09. Official product/solution pages (Tier 1/2). No help-center/user-guide documentation was reachable for any sampled product — sourcing limitation recorded below.

- Arcadia — Contract IQ: https://arcadia.io/contract-iq ; VBC software use case: https://arcadia.io/value-based-care-software ; platform: https://arcadia.io/platform
- Health Catalyst — VBC Performance: https://www.healthcatalyst.com/healthcare-analytics/population-health-value-based-care/value-based-care ; PHM & VBC overview: https://www.healthcatalyst.com/healthcare-analytics/population-health-value-based-care
- Azara Healthcare — VBC Reporting: https://www.azarahealthcare.com/vbc-reporting-with-payer-integration ; home: https://www.azarahealthcare.com/
- Cedar Gate — home/platform: https://www.cedargate.com/ ; VBC Analytics: https://www.cedargate.com/platform/analytics/value-based-care-analytics/
- Innovaccer — VBC suite: https://innovaccer.com/value-based-care ; Contract Management: https://innovaccer.com/products/contract-management ; home: https://innovaccer.com/
- ZeOmega — home: https://www.zeomega.com/

## Product Observations

Evidence layers: **A** = directly observed on the cited official page; **B** = cross-product commonality; **C** = canonical inference.

### Arcadia (Contract IQ + VBC software)

Key observations (Layer A):

- Contract IQ is positioned as "Healthcare contract management software **for providers**" that "simplifies value-based care (VBC) contract creation with seamless collaboration tools, an intuitive dashboard, and 'what if' scenario modeling to optimize performance."
- The stated challenge names the contract-type space: "various types of VBC contracts, including episodic or bundled payment models, capitation models, and more... Poorly optimized contract terms, fragmented data, and outdated network structures can make it difficult to maximize performance."
- Capabilities: "Collaborate with decision-makers in a unified interface; Predict revenue more accurately with forecasting and 'what if' tools; Automate manual processes like contract forecasting; Improve discoverability across teams and make data accessible to every stakeholder"; "Determine optimal contract types by population"; product screenshots show a **contract builder** and **contract modeling** surfaces; a demo is walked through by Arcadia's "Lead Actuary."
- VBC software use-case page: success requires "a thorough understanding of quality metrics, HCC risk scores, cost and utilization of care in your population, patient engagement and outreach strategies"; serves "CINs, ACOs, and healthcare systems who decide to take on risk"; "Since reimbursements are dependent on clinical outcomes, your organization can't afford to miss its value-based benchmarks"; "implement value-based payment models throughout your network."
- Money evidence: "Predict revenue more accurately with forecasting"; "Save up to $60K per month in third-party actuarial fees" (actuarial work absorbed into the product); KLAS client quote on the **audit and submission process**: "Things happen in the audit process that we catch through Arcadia's tool and their partnership that translate into real dollars"; "$10.7M Amount of shared MSSP savings generated by Arcadia customers"; "22% Higher MSSP bonuses."
- Data substrate: platform curates "clinical EHRs, claims, social determinants of health (SDoH), pharmacy records, ADTs, and other sources"; "Healthcare organizations use Arcadia to drive success under MSSP, NextGen, Medicaid, fee-for-service, and commercial value-based care contracts."
- Both-sides posture: provider customers "take on Medicare, Medicaid, and Commercial risk-based contracts"; payer customers "collaborate with provider networks to improve STARS / HEDIS performance and risk adjustment accuracy."
- Portfolio separation: Contract IQ is a distinct application beside Patient Registry, Care Manager, Network Modeler, Vista dashboards — the PHM/care loop and the contract machinery are separate products (corroborates the PHM pass's flag).

### Health Catalyst (VBC Performance)

Key observations (Layer A):

- Solution framing: "Maximize Results in Your Risk-Based Contracts — Achieve sustainable success in value-based care with transparent analytics and targeted action."
- Leadership questions name the unit of analysis: "Which **contracts**, populations, or interventions drive the biggest impact?"
- "Know Where to Focus: Find improvement areas across populations and contracts. Benchmark outcomes and financial performance. Prioritize high-ROI interventions."
- "Move Beyond Black Boxes: See how every calculation and model works. Understand **risk adjustment, groupers, and benchmarks**." — measurement machinery made transparent.
- "Turn Insights Into Results: Reduce avoidable utilization and cost. Improve coding and documentation accuracy. Close gaps in care to boost quality scores. **Capture more shared savings and incentives.**"
- "Build Resilience for Long-Term VBC Success: **Track contract performance over time.** Spot emerging risks early. **Adapt quickly to new contract types and measures.**"
- "Align Leaders and Teams: Unite finance, clinical, and operational stakeholders with shared goals and data" — role-tailored dashboards.
- Implementation phasing: "Phase 1: **Map current contract landscape.** Identify high-impact opportunities. Define metrics and goals."
- Related products: "VBC Intelligence — Clarity and action for value-based care performance"; "Value-Based Care Performance Suite."
- Portfolio separation: VBC Performance is one solution beside Population Health Management, Care Transformation, Patient Engagement, Network Management (corroborates the PHM pass's flag).

### Azara Healthcare (VBC Reporting)

Key observations (Layer A):

- Positioning: "The leading provider of data-driven analytics, quality measurement and reporting for the community health and physician practice market"; "Built for safety net providers" (FQHCs, PCAs, rural orgs) — the small-provider tier of the market.
- VBC Reporting: "Azara delivers timely, actionable clinical insights to care teams, facilitating **collaboration with health plans and other value-based care enablers**... work hand in hand with health plans on critical initiatives such as engaging **attributed members** in preventive care, improving clinical quality, **capturing risk adjustment factors**, and driving performance improvement... streamlining risk gap closure and the **sharing of supplemental data**... monitor, track, and improve quality, cost, and utilization outcomes."
- Payer data integration: "seamlessly integrates health-plan provided data, such as **rosters and claims from multiple plans**, within existing workflows"; "Plug-In Plan Care Gaps surfaces the status of care gaps as reported in the **Care Gap Reconciliation (CGR) Report** for a given patient, based on records found in the EHR and received from the Payer"; "Equip health plan teams with actionable clinical insights while also delivering plan data to providers directly at the point of care."
- Measure machinery: "a comprehensive library of over 600 measures – including over 50 certified HEDIS® measures, CMS eCQM measures used for MSSP, MCP, & PCF programs, and a broad range of other clinical quality measures."
- Performance grain: "granular insights into cost and utilization drivers throughout the network... at the **network, practice, and provider levels**."
- Money: FAQ — "Azara helps organizations identify where interventions can improve performance and **maximize shared savings**." (Improvement-oriented; no settlement computation documented.)
- Generic definition (vendor's own FAQ): "Value-Based Care is a healthcare delivery model that **rewards quality, outcomes, and cost efficiency rather than volume of services**. Success depends on data-driven insights, proactive care, and strong collaboration between providers and payers."
- Degraded-mode operation: "What should I do if I don't have access to payer data? Even without payer data, organizations can make progress using clinical and utilization data." — payer data is the common substrate, not a hard precondition.
- Trust machinery: NCQA Data Aggregator Validation — "Validated data flows... support the adoption of value-based contracting by making many of its core features more workable."

### Cedar Gate Technologies

Key observations (Layer A):

- Positioning: "the leading end-to-end technology platform enabling **payers, providers, and self-funded employers** to thrive in value-based care." Platform pillars: Data / Analytics / Care / Payment / Services.
- **Payment pillar** (the strongest settlement evidence in the sample): "Our composable payment technologies simplify the administration of complex payment models and reimbursement structures for value-based care. Sophisticated interface capabilities **seamlessly connect data with claims engines** to streamline adjudication, reporting, and payment processing."
  - Bundles Adjudication: "Optimize bundles definitions & program efficiency; Integrate seamlessly with claims systems; **Simplify bundling, pricing, unbundling & payments**; View bundles activity in customizable dashboards."
  - Capitation Adjudication: "**Simplify member attribution & PMPM payments**; Handle **multiple provider contracts** with ease; Plan for risk to maximize revenue & performance; **Streamline claims, funds flow, & reporting**"; module detail: "Manage constantly changing eligibility rolls... Easily administer multiple capitated payment agreements with various providers... Maintain oversight with automated checks and balances."
- **VBC Analytics**: What's included — "Financial Performance Analytics; Executive Analytics; **Bundle Definition Modeling**; Cohort Identification; Program Impact Tracking"; add-on modules — "**Contract Modeling**, Episode Classification Methodologies, Core HEDIS Measures, Hierarchical Condition Categories (HCC), Medicare Reference Pricing."
- The contract-lifecycle sentence (key for the unit of record): "Use our self-service tools to understand clinical and financial risks **before signing an agreement**. **Contract setup and management tools designed for VBC models support all contract types, including prospective bundles and capitation agreements. Once configured, examine member and provider performance according to contract rules.**"
- "Model any VBC contract to mitigate risk and **negotiate the best terms**"; "Examine financial metrics to **monitor funds flow in alternative payment models**"; "build cohorts based on **contract parameters**"; "Access a robust library of integrated scoring methodologies, like HCC, HEDIS, Hopkins ACGs, groupers, and preventables."
- Services pillar: Actuarial Consulting — "Forecast future spending based on historical trends; Get expert advice on VBC contracts & APMs; **Model & manage downside risk** for VBC programs"; Bundles Program Management — "Establish & negotiate optimal bundles agreements; Let us run all aspects of your bundles program."
- Market breadth: Payer (BCBS, national, payvider, regional), Provider (ACO, CIN, Delegated Services, FQHC, IDN, IPA, MSO, Payvider, Physician Practice), Self-Funded (brokers, employers, TPAs); lines of business Commercial / Medicaid / Medicare (ACO REACH, MA, MCP, MSSP, PACE, TEAM & Shadow Bundles); payment models: Alternative Payment Models (capitated payments, primary care attribution), Bundled Payments, Fee-for-Service.

### Innovaccer (VBC suite + Contract Management)

Key observations (Layer A):

- VBC suite framing: "Maximize Performance in Value Based Care — Improve patient outcomes and financial performance in value-based care models"; components: Population Health Analytics, Risk Adjustment, Quality Management, Care Management, **Contract Management**; "Optimize performance in value-based contracts with comprehensive financial analytics and monitoring."
- Contract Management: "Optimize your value-based contracts with powerful **financial modeling, performance tracking, and scenario analysis** tools. **Maximize shared savings and minimize downside risk.**"
- Contract Management product page: "Transform Financial Performance with **Actuarial Intelligence** — Build predictable revenue models, strengthen contract negotiations, and maximize financial performance in value-based care"; "Design VBC Contracts With Precision: Design optimal risk-bearing contracts and predict financial outcomes through world-class actuarial expertise and analytics"; "Protect your margins by utilizing benchmarking data and predictive analytics to identify **optimal contract terms and network configurations**"; "Achieve faster ROI in value-based arrangements through precise cost/utilization forecasting and proactive performance monitoring."
- FAQ: "Our actuarial experts build sophisticated financial models for **projecting performance, profitability, and risk in value-based care arrangements**. This includes MLR projections, premium revenue forecasting, utilization trends"; "We serve three core markets: providers managing value-based care programs (like Rise Health's ACO REACH program), regional health plans (such as CareFirst BCBS), and life sciences companies"; "episode-based cost and utilization benchmarks, provider performance management analytics, patient acuity models."
- Data substrate: Data Activation Platform integrating claims, EMRs, labs, pharmacy, SDoH; national dataset access (Medicare A/B/C/D, T-MSIS Medicaid all 50 states, commercial claims) "covering over 60 million lives."
- Scale evidence: Banner Health "managing 1.4M patients in value-based arrangements"; CommonSpirit "All-Payer Value-Based Claims Solution... actionable clinical, operational, and financial insights to regional Value Hubs"; "1.9M value-based lives managed in Innovaccer."
- Portfolio note (home page): "Perform in every contract, from full risk to fee-for-service"; solutions list includes "Contract Design and Management."

### ZeOmega (boundary observation)

Key observations (Layer A):

- Jiva is a payer care management / population health platform (Best in KLAS payer care management). VBC appears as a capability: "Jiva Care Quality (CQ) Navigator... centralizes HEDIS and CMS Stars quality program data, improves care gap closure rates, and **empowers value-based care reporting**."
- Health-systems blurb: "Exceed your value-based care benchmarks leveraging combined clinical and claims data"; Medicare Advantage blurb: "Built-in risk adjustment to drive consistent success in PMPM payment models and maximize Star ratings performance."
- Confirms the payer-care-management pass's co-deployment observation: a payer care-management platform carries VBC reporting as a module, not as its center.

## Cross-product Comparison

| Structure | Arcadia | Health Catalyst | Azara | Cedar Gate | Innovaccer |
|---|---|---|---|---|---|
| Arrangement as unit of record | Contract IQ: create/model/manage VBC contracts (bundled, capitation); "determine optimal contract types by population" | contract-level clarity; "map current contract landscape"; "track contract performance over time"; "adapt to new contract types" | VBC programs operated jointly with plans (program participation; payer integration) | "Contract setup and management tools... support all contract types, including prospective bundles and capitation agreements"; Bundle Definition Modeling; Contract Modeling add-on | "Design VBC Contracts With Precision"; financial modeling; scenario analysis; "optimal contract terms" |
| Multi-source data substrate | EHR + claims + SDoH + pharmacy + ADT lakehouse | unified data behind transparent analytics | EHR + plan rosters + claims + SDoH unified in DRVS | data lake from dozens of sources | Data Activation Platform (claims/EMR/labs/pharmacy/SDoH) |
| Attribution | implied (MSSP populations; risk contracts) | populations & contracts | "engaging attributed members" | "Simplify member attribution & PMPM payments"; "Primary Care Attribution" | patient risk assignment; "accurate patient risk assignment" case |
| Measure/quality machinery | quality metrics, HCC risk scores; MSSP audit/submission | risk adjustment, groupers, benchmarks | 600+ measures incl. HEDIS/eCQM (MSSP/MCP/PCF) | HEDIS, HCC, Hopkins ACGs, groupers, episode classification | Quality Management; HEDIS/Stars gap closure |
| Financial resolution | revenue forecasting, what-if, actuarial work absorbed, MSSP audit dollars | "capture more shared savings and incentives"; financial performance benchmarking | "maximize shared savings"; cost/utilization drivers | bundles + capitation **adjudication**; funds flow; PMPM payments | shared savings/downside risk; MLR projections; financial modeling |
| Market side | provider (+ payer analytics) | provider | provider/safety-net (plan collaboration) | payer + provider + self-funded | provider + payer |
| Posture | software + managed services (Best in KLAS VBC managed services) | software + expert services | software (+ clinical transformation team) | software + actuarial/program services | software + actuarial services |
| Performance grain | population/contract | contract/population | network/practice/provider | member/provider/contract | provider/network/contract |

Layer B (cross-product commonality, 5/5 unless noted):

- The **contract/arrangement** is a named, persistent object of work in every sampled product (Arcadia "VBC contracts", Health Catalyst "contracts", Cedar Gate "contract setup and management... all contract types", Innovaccer "value-based contracts", Azara VBC "programs" with plans).
- **Multi-source data aggregation** (claims + clinical + others) is the universal substrate.
- **Quality + cost measurement** against defined measures is universal (measure libraries, risk adjustment, groupers, benchmarks).
- The **financial dimension** of the arrangement is first-class in all five — from projection (Arcadia, Innovaccer) through tracking (all) to full payment adjudication (Cedar Gate only).
- **Attribution** (which members count toward which provider) is explicit at Azara and Cedar Gate, operational at Innovaccer (risk assignment), implied at Arcadia/Health Catalyst (Layer B at concept level).
- **Payer↔provider data exchange** (rosters/claims in; supplemental clinical data out; care-gap reconciliation) explicit at Azara, present in payer-facing postures of Cedar Gate/Innovaccer/Arcadia.
- **Scenario/what-if contract modeling** explicit at Arcadia, Cedar Gate, Innovaccer; improvement-targeting at Health Catalyst.
- **Managed-services/actuarial posture** present in all five at varying depth (Layer B; variant axis, not definitional).

## Canonical Abstraction

### Level 0 — Defining Invariant

Three jointly-held structures (Layer C, canonical inference from the cross-product comparison):

1. **The value-based arrangement as the unit of record.** A persistent identified payment arrangement between a paying party (payer / plan / employer) and a provider organization, covering a defined population over a performance period, carrying the payment model's financial terms (shared savings, risk corridor, capitation, bundled/episodic payment) and the quality/cost measures performance will be judged on. Remove → a contract repository or a population analytics tool; the Type's reason to exist dies.

2. **Arrangement-bound performance measurement.** The platform aggregates multi-source data (claims + clinical as the common core), applies attribution (which members/patients count toward which provider under the arrangement), computes the arrangement's quality and cost measures with risk adjustment and benchmarks, and tracks performance against the arrangement's own rules across the performance period. Remove → generic BI/quality reporting; the measurement is no longer bound to any arrangement.

3. **The arrangement's financial resolution.** The platform carries the arrangement's money content — projected and earned incentives, savings or losses, per-member or per-episode payment obligations — and computes/tracks/reconciles it against measured performance as the period unfolds, up to and (in some products) including payment administration and funds flow. Remove → performance reporting with no money loop; the "value" in value-based care is unoperated.

Jointly-held load-bearing tests:

- 1 alone = contract repository/spreadsheet
- 2 without 1+3 = population health analytics / quality reporting (PHM territory)
- 3 without 1+2 = claims adjudication / payment processing territory
- 1+2 without 3 = performance reporting, no money loop
- 1+3 without 2 = contract administration with nothing measured
- 2+3 without 1 = analytics plus a calculator with no arrangement of record

### Level 1 — Common Mature Structure

- Multi-source data aggregation/normalization (claims + EHR + SDoH + pharmacy) as substrate
- Attribution machinery (member/patient → provider under the arrangement; eligibility-roll sensitivity)
- Risk adjustment (HCC-class) and risk stratification
- Benchmarking (regional/national, peer comparison)
- Measure libraries (HEDIS-class, eCQM-class, custom quality sets; episode groupers)
- Care-gap worklists and quality-gap closure feeding action (link to care-management tooling)
- Dashboards with drill-down (contract → network → practice → provider) and executive reporting
- Scenario / what-if contract modeling for negotiation
- Payer↔provider data exchange (rosters, claims, care-gap reconciliation files, supplemental clinical data)

### Level 2 — Variant / Optional Structure

- Market side: provider-side (Arcadia, Health Catalyst, Azara), payer-side modules (ZeOmega), both-sides/neutral (Cedar Gate, Innovaccer)
- Payment-model families supported: shared savings (upside-only or with downside risk), capitation/PMPM, bundled/episodic, pay-for-performance bonus pools
- Regulatory program packaging: US CMS programs (MSSP, ACO REACH, MCP/PCF, TEAM, MA Stars) vs commercial/regional arrangements vs self-funded employer programs
- Posture: software-only vs software + managed services/actuarial consulting/program administration
- Bundled neighboring modules: care management, utilization management, network modeling, patient engagement (Cedar Gate bundles all; others sell separately)
- Customer segment: health systems/ACOs vs community health centers/safety net vs self-funded employers/TPAs

### Level 3 — Vendor-specific (Research Notes only)

- Arcadia: "$60K/month third-party actuarial fees" saving claim; "Best in KLAS 5×" VBC managed services; $10.7M shared MSSP savings figure
- Innovaccer: national Medicare/T-MSIS dataset access (60M lives); Humbi actuarial-intelligence sibling; Gravity/agent framing
- Azara: NCQA Data Aggregator Validation certification specifics; Care Gap Reconciliation (CGR) report; 600+ measure library figure
- Cedar Gate: "Shadow Bundles"; Hopkins ACGs; IQVIA ownership; ~60M covered lives figure
- ZeOmega: Jiva Care Quality (CQ) Navigator branding

## Anti-overfitting Notes

- **US CMS program machinery is NOT definitional.** MSSP/ACO REACH/Stars/HEDIS naming dominates the sample (US market), but Azara's own FAQ defines VBC generically ("rewards quality, outcomes, and cost efficiency rather than volume of services"), and Cedar Gate serves commercial, Medicaid, and self-funded lines with no CMS program required. The canonical definition names no program.
- **Multi-source cloud data lakes are NOT definitional** — they are the current substrate (Layer B), not the invariant. See historical check.
- **Managed services / actuarial consulting are NOT definitional** — a software-only product satisfies the core; services are a posture variant.
- **Full payment adjudication is NOT definitional** — only Cedar Gate documents bundles/capitation adjudication and funds flow; the others document projection/tracking/reconciliation support. The invariant is the arrangement's money content being computed/tracked/reconciled, not the payment run itself.
- **Attribution algorithm specifics are NOT definitional** — prospective vs retrospective assignment, update cadence, and roster mechanics vary and were not directly documented in fetched pages; held at concept level.

## Historical / Market-Sample Check (§24 discipline)

Would older, regional, or differently positioned products still fit the L0?

- **1990s US capitation management** (HMO/IPA per-member-per-month payments to physician groups with withholds and bonus pools, utilization budgets, encounter-based reconciliation): satisfies all three legs — arrangement (capitation agreement), measurement (utilization/cost against budget), financial resolution (withhold release, bonus distribution, PMPM reconciliation) — with no cloud, no HEDIS, no AI. ✓
- **Early-2000s pay-for-performance programs** (bonus pools paid against measured quality, e.g. regional payer programs): arrangement + measure-based evaluation + incentive settlement. ✓
- **UK GP fundholding (1990s)**: budget-holding arrangement with activity/cost reconciliation. Regional non-US fit. ✓
- **1980s DRG prospective payment**: a payment model, but realized almost entirely inside claims adjudication — no standing arrangement-level measurement loop; held as lineage, not the Type.

Conclusion: the Type's structure predates the "value-based care" label (2010s); the label is the current market name. The definition names no era machinery. Historical check **passed**.

## Boundary Findings

### vs Population Health Management — flag DISCHARGED (keep-both RATIFIED)

The PHM pass's flag ("contract/payment/quality-reporting machinery vs the population management loop") is confirmed from this side with fresh evidence:

- **Loop-center discriminator**: PHM = population-first loop (defined population → stratify → gap → act → measure at population scope). VBC platform = arrangement-first machinery (the contract/arrangement is the unit of record; measurement and money are bound to the arrangement's terms).
- **Portfolio separation directly observed at three vendors**: Azara sells "Value-Based Care Reporting" as a distinct solution beside DRVS (its PHM platform); Arcadia sells Contract IQ as a distinct application beside Patient Registry/Care Manager; Health Catalyst sells VBC Performance as a distinct solution beside Population Health Management. Vendors themselves draw the line.
- Bundling is common in both directions (Cedar Gate bundles care management with VBC payment tech), but the objects differ: PHM manages the population; VBC platform manages the arrangement and its money.
- Keep-both; cross-reference both documents.

### vs Payer Care Management — flag DISCHARGED (keep-both RATIFIED)

The payer-care-management pass's flag is confirmed:

- Payer care management = the plan's clinical-program operating layer (member as care subject, program portfolio, documented care-management loop). VBC platform = payer↔provider arrangement machinery (contract terms, performance against contract rules, financial resolution).
- Co-deployment confirmed: ZeOmega (payer care-management platform) carries "value-based care reporting" as a Jiva capability (CQ Navigator), not as its center. Inovalon's "Value-Based Care Management" product line (named by that pass) is consistent co-deployment evidence (inherited, not re-fetched this pass).
- Keep-both; cross-reference both documents.

### vs Healthcare Revenue Cycle Management (unprocessed sibling — flag HUNG)

- RCM = the provider's encounter→claim→payment billing loop (fee-for-service machinery). VBC platform = arrangement-level money (savings/losses/incentives, capitation, bundles).
- Seam evidence: Cedar Gate's payment tech "seamlessly connect[s] data with claims engines" — the claims engine remains claims machinery; the VBC payment layer is arrangement-shaped and sits beside/above it. Arcadia's MSSP audit/submission work is arrangement-level, not claim-level.
- Recommend joint review when healthcare-revenue-cycle-management is processed.

### vs Provider Network Management (processed 2026-09-09)

- PNM = the payer's contracting/credentialing/fee-schedule/adequacy machinery over its provider network. VBC platform = operating the payment arrangements with that network and measuring/settling performance under them.
- Portfolio separation observed: Arcadia ships Network Modeler as a separate application; Health Catalyst ships Network Management as a separate solution; Innovaccer's contract optimization references "network configurations" as an input. Adjacent, not the same Type.

### vs Healthcare Quality Management (unprocessed sibling — corroborates PHM pass's flag)

- Both consume quality measures. VBC measurement is arrangement-bound (measures defined by the contract, scored per contract rules, tied to money); quality management is organization-level quality-program governance. Distinct centers; keep separate.

### vs Utilization Management (processed 2026-09-09)

- UM = review machinery (prior auth/concurrent review/medical-necessity determinations). Appears in-sample only as a bundled module (Cedar Gate Care pillar) or sibling solution — never as the whole of this Type. Consistent with the utilization-management pass's own holding.

### vs Insurance Underwriting / Actuarial platforms (processed 2026-09-07)

- Actuarial modeling appears inside VBC platforms as scenario/what-if capability and as a services posture, but the VBC platform's center is the operating arrangement, not rate/underwriting decisions. Distinct.

### "Remove what to become another Type" judgments

- Remove the arrangement of record → population health analytics (PHM territory).
- Remove the measurement machinery → generic contract management (CLM territory).
- Remove the arrangement and keep claim-level money → revenue cycle / claims processing territory.
- Remove the money layer → quality reporting / PHM analytics territory.

## Uncertainties

1. **No help-center/user-guide documentation reached** for any sampled product (all evidence is official product/solution/marketing pages). Operational specifics — exact settlement workflows, reconciliation file formats, attribution update cadences, measure-submission mechanics — are unverified. Assertion strength reduced accordingly; no precise operational numbers are claimed in the final document beyond vendor-published figures.
2. **Settlement depth varies and the deep pole is thin in-sample**: only Cedar Gate documents full payment adjudication (bundles/capitation, funds flow). Whether mid-market VBC platforms routinely compute final settlement payments (vs supporting the payer's calculation) is unverified. The final document therefore frames financial resolution as a depth-varying capability with the arrangement's money content as the invariant.
3. **Attribution mechanics** (prospective vs retrospective, update cadence) not directly documented in fetched pages — held as a common capability at concept level only.
4. **ZeOmega's VBC reporting** observed only at capability level (video description + solution blurbs), not product documentation.
5. **Inovalon** "Value-Based Care Management" evidence is inherited from the payer-care-management pass (2026-09-08), not re-fetched; product line may have been reorganized since.
6. **Non-US market shape**: the sample is US-dominated. Regional analogs (e.g. UK/other single-payer incentive schemes) are asserted only at the historical-check level, not from product evidence.

## Final Synthesis

A Value-based Care Platform is the arrangement-and-performance machinery of payer–provider payment arrangements in which reimbursement depends on measured quality and cost performance. Its defining core is three jointly-held structures: (1) the value-based arrangement as the unit of record — parties, covered population, payment model, financial terms, measures, performance period; (2) arrangement-bound performance measurement — multi-source data aggregation, attribution, risk-adjusted quality/cost measure computation against the arrangement's own rules and benchmarks; (3) the arrangement's financial resolution — the money content (savings, losses, incentives, per-member or per-episode payments) projected, tracked, and reconciled against measured performance, with depth ranging from projection-and-reconciliation support to full payment adjudication and funds flow.

The Type is distinct from Population Health Management (population-first loop), Payer Care Management (plan's clinical programs), Revenue Cycle Management (claim-level billing), Provider Network Management (network configuration), and Healthcare Quality Management (org quality governance). Both pre-hung sibling flags are discharged: keep-both ratified on the arrangement-first vs population-first/program-first loop-center seam, corroborated by vendors' own portfolio separations (Azara VBC Reporting vs DRVS; Arcadia Contract IQ vs Registry/Care Manager; Health Catalyst VBC Performance vs PHM; ZeOmega VBC reporting as a Jiva capability).

Historical check passed: 1990s capitation/withhold management and early-2000s pay-for-performance satisfy the core with no modern machinery; the definition names no US program or era-specific implementation.
