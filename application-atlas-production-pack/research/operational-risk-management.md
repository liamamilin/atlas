# Research Notes — Operational Risk Management (ORM)

Research date: 2026-09-10

## Research Goal

Understand what an Operational Risk Management application actually is as a software type: its central objects, workflows, roles, and the boundary against neighboring types — especially Enterprise Risk Management (whose research pass left a joint-review flag on this leaf), GRC Platform, Internal Controls Management, Incident Management, Operational Resilience, Third-Party Risk, and EHS/HSE software.

## Initial Boundary (hypothesis before research)

- ORM software is expected to be the operational-risk discipline's system of record: process-anchored risk records, RCSA (Risk and Control Self-Assessment) campaigns engaging first-line process owners, loss event capture with root-cause analysis, control linkage/testing, and KRI monitoring.
- Strongest association: financial services (Basel II definition of operational risk; FFIEC/OCC/NCUA supervision), but the discipline exists in non-financial firms too.
- Nearest confusions: ERM (shared building blocks, different center of gravity), GRC Platform (suite vs application), Internal Controls Management (controls-centered), Incident Management (IT/service restoration vs loss-event records), Operational Resilience (recovery/impact tolerances), EHS software (a different sense of "operational risk" — worker safety).
- Unknowns: whether loss events are definitional or only common; whether RCSA is definitional; how deep control testing goes; whether the Basel taxonomy is definitional (it should not be); whether non-financial ORM products share the same core.

## Research Questions

1. What is the central object, and what does an operational risk record carry?
2. How does RCSA work as a workflow (scoping, routing, first-line confirmation, second-line review/approval)?
3. Are loss events a first-class record type, and how do they link back to risks and controls?
4. How are controls modeled (library, mapping, testing cadence)?
5. How do KRIs/indicators work (thresholds, owners, cadence, alerting)?
6. What roles use the system (first-line process owners, second-line risk function, third-line audit, executives)?
7. Where is the boundary vs ERM / GRC Platform / Controls Management / Incident Management / Operational Resilience / EHS?
8. What varies by segment (banking vs non-financial, suite module vs standalone, community bank vs global bank)?
9. Historical check: would pre-Basel (pre-2004) or non-bank loss-register-style ORM still fit the definition?
10. Is "Operational Risk Management" used for other product worlds (polysemy check)?

## Representative Products

| Product | Positioning | Why selected |
|---|---|---|
| Archer (Enterprise & Operational Risk use case) | Enterprise GRC/IRM pioneer, Fortune 500 tier | Defines the combined ERM+ORM pattern; explicit ORM mechanics (RCSA campaign, loss events, indicators) |
| LogicGate Risk Cloud (Operational Risk Management solution) | Mid-market → enterprise no-code workflow GRC | Sells ORM as a distinct solution from ERM; RCSA scaling + KRI monitoring + issues/loss linkage |
| 360factors Predict360 | Financial-institution (bank/credit union) ORM, community/regional FI tier | Banking-regulatory ORM philosophy; vendor page documents the full ORM discipline, lifecycle, and FI-grade software capability set |
| Origami Risk (EHS Operational Risk Management) | RMIS/EHS heritage platform | Polysemy probe: shows a second, different product world using the same name (workplace-safety hazard management) |

Rejected/abandoned per network rules: ServiceNow IRM Operational Risk docs (timed out twice in the ERM pass — not retried), MetricStream ORM page (403 twice), SAI360 (404 on two URL guesses), Riskonnect (no dedicated ORM product page found; its ORM URL resolves to a webinar content page — consistent with the ERM pass's finding that Riskonnect sells ERM, not a separate ORM product).

## Sources

- Archer — https://www.archerirm.com/enterprise-operational-risk (Enterprise & Operational Risk use-case page). Fetched 2026-09-10. Layer A.
- LogicGate — https://www.logicgate.ai/solutions/operational-risk-management/ (ORM solution page; references the Operational Risk Management Application, Issues Management, Incident Management applications and the Operational Risk Management Suite). Fetched 2026-09-10. Layer A (product-page level).
- 360factors — https://www.360factors.com/products/operational-risk-management/ ("Operational Risk Management for Financial Institutions" — vendor educational page describing the ORM discipline, Basel taxonomy, five-step lifecycle, three lines of defense, and the FI-grade software capability set; Predict360 is the vendor's platform). Fetched 2026-09-10. Layer A (vendor educational/product-structure level; no deep help-center articles fetched).
- Origami Risk — https://www.origamirisk.com/solutions/ehs/operational-risk-management/ (EHS Operational Risk Management solution page). Fetched 2026-09-10. Layer A.
- Cross-reference: research/enterprise-risk-management.md (Archer/LogicGate/Riskonnect/LogicManager observations, 2026-09-06) for the ERM-side of the boundary.

Source-access limitation: deep help-center articles (Archer Community KB, LogicGate KB, ServiceNow docs, MetricStream) were not reachable from the research environment on 2026-09-10. All workflow claims below are calibrated to product-page/educational-page evidence; precise numeric limits, exact state names, and default settings are not asserted anywhere.

## Product Observations

### Archer — Enterprise & Operational Risk (archerirm.com)

Key observations (Layer A, product-page level):

- One combined "Enterprise & Operational Risk" use case; ORM is presented as one of three "closer look" panels alongside Enterprise risk management and Loss and indicator management.
- ORM panel mechanics: "Business and process managers open an RCSA that already holds their risks and controls. They confirm what still applies, reassess what changed, and add what is new. Your team reviews and approves, and Archer snapshots the result." → RCSA as a campaign workflow: scope by unit or process → generate an RCSA for each → route automatically → first-line confirms/reassesses/adds → risk team reviews and approves → snapshot.
- RCSA framing: "Assessments your owners will finish — Scope by unit or process, generate an RCSA for each, and route it automatically. The plant manager confirms what still applies instead of facing a blank form."
- Loss events: "Log occurrence, discovery, and loss dates, work the root cause and impact analysis, then link the event back to the risk and the control involved." Loss event intake reaches anyone in the company (provisioned users via the Loss Event application; employees outside via an Archer Engage form link).
- Indicators: "Set red and amber thresholds, numeric or qualitative, and Archer tasks the metric owner on the frequency you choose. Trends surface before a loss does."
- Risk record fields: "Capture impact, likelihood, owner, and status for each risk, then link the controls that mitigate it. The register shows coverage instead of a list of worries."
- Accountability: "Every risk, control, indicator, and loss event carries a named owner and a due date."
- Benefits list: enterprise risk register; linked control library; RCSA campaign workflow (scoped, routed, reviewed, approved); loss event intake and review (logged, analyzed, linked back to risk); key indicator monitoring (thresholds tracked, owners tasked each cycle); risk and loss dashboards.
- FAQ: frameworks — COSO for ERM, ISO 31000 for assessment method, NIST RMF, **Basel II for operational risk**; two-level taxonomy (enterprise risks + intermediate risks); custom rating scales a primary feature; BIA results from the Resilience solution roll into process-based RCSA.
- Suite context: ORM sits in a GRC platform alongside compliance, policy, audit, third-party, resilience, IT risk applications.

### LogicGate Risk Cloud — Operational Risk Management (logicgate.ai)

Key observations (Layer A, product-page level):

- ORM is a distinct solution from ERM (separate solution pages; both exist under "Risk Management"). Also an "Operational Risk Management Suite" and a preconfigured "Operational Risk Management Application".
- Headline capabilities: "Streamline and efficiently scale RCSAs"; "Automate key risk indicator (KRI) monitoring"; "Quantify GRC impact, revenue enabled, and risks mitigated".
- RCSA scaling: "Engage process owners without the hassle of growing licensing fees. Save risk teams' time with automated assessment scoping, assignment, and progress tracking." → first-line process owners as the assessment workforce.
- Process criticality: "Quantify and visualize risk across each business unit and process." → process/business-unit as the anchoring dimension.
- Loss/issues linkage: "Leverage the power of Spark AI to identify linkages across risks, issues, and loss events, then generate response plans in a single click." Built-in issue tracking; Issues Management and Incident Management as sibling applications.
- Role-based dashboards for cross-functional teams and executives; issue tracking built in.
- Suite context: ORM unites with "enterprise risk management, operational resilience, and regulatory compliance" as complementary programs.

### 360factors Predict360 — ORM for Financial Institutions (360factors.com)

Key observations (Layer A, vendor educational page describing the discipline and the FI-grade software capability set):

- Definition (Basel II origin, absorbed into FFIEC handbook): operational risk = "losses arising from inadequate or failed internal processes, people, and systems, or from external events."
- ORM is a **second-line function**: "It owns methodology, taxonomy, and aggregation, but does not execute day-to-day controls (the first line) or provide independent assurance (the third line, internal audit)."
- Seven Basel event-type categories (internal fraud; external fraud; employment practices & workplace safety; clients, products & business practices; damage to physical assets; business disruption & system failures; execution, delivery & process management) as the standard taxonomy reference in US banking.
- Five-step lifecycle with named outputs: **Identify** (process mapping, scenario workshops, loss data → risk register by Basel category, business unit, inherent severity) → **Assess** (RCSA: inherent and residual likelihood/severity, engages first-line process owners, ties risks to controls, second line challenges; typically annual with quarterly refresh on higher-risk processes) → **Monitor** (KRIs with thresholds triggering escalation; leading where possible) → **Control** (preventative/detective/corrective controls designed, documented, mapped, tested on a defined cadence; control library as bridge between register and audit posture) → **Report** (board-level quarterly view integrating loss data, KRI status, control test results, emerging risks; regulator reporting per FFIEC/OCC/NCUA cadences).
- Three lines of defense: first line (business unit risk owners execute controls, own residual risk), second line (operational risk function owns framework/methodology/challenge/aggregation), third line (internal audit assurance).
- FI-grade ORM software capabilities named: "A unified risk register; Configurable RCSA workflows; A mapped control library; KRI dashboards with threshold alerting; Loss event capture with investigation workflow; Scenario analysis tools; Board-ready reporting; A regulatory-change feed."
- ERM vs ORM (FAQ): "ORM is the second-line discipline that produces the operational-risk component of that [ERM] view. ERM covers credit, market, operational, liquidity, strategic, and reputational risk in a single board-level view."
- Regulatory anchors: FFIEC Operational Risk booklet, OCC Heightened Standards, NCUA SL 13-12, Basel SMA, BCBS Sound Practices; scenario analysis as a named tool; loss data scarcity as a driver of scenario-based methods.
- Suite context: Predict360 operational risk module "shares taxonomy and control library with the third-party risk, regulatory change, and audit modules."

### Origami Risk — EHS Operational Risk Management (origamirisk.com)

Key observations (Layer A — polysemy probe):

- "Operational Risk Management" here is an **EHS solution**: "Prevent incidents before they happen. Identify hazards, reduce risk, and maintain compliance… keep your workforce safe."
- Tool set: Job Safety Analysis (JSA), Lockout Tagout (LOTO) procedures, Permit to Work (nine configurable permit types), Asset Management, Risk Assessments ("assess and rank risks by severity and probability… trigger workflows based on thresholds"), Pre-Task Planning.
- Bridge language: "roll up insights to ERM dashboards to connect safety data to enterprise risk management strategy" — the EHS-ORM world explicitly feeds ERM, but its objects (hazards, job steps, permits, equipment isolation) are worker-safety objects, not Basel-style operational-loss objects.
- Conclusion: this is a different product world sharing the name. The DIRECTORY leaf sits in §11 (Legal, Risk, Compliance & Governance) next to ERM/GRC/TPRM, so the intended sense is the GRC/financial-services discipline; the EHS sense belongs to EHS/HSE Platform territory.

## Cross-product Comparison

| Structure / capability | Archer | LogicGate | 360factors (Predict360) | Origami Risk (EHS) | Evidence |
|---|---|---|---|---|---|
| Operational risk records anchored on business units / processes | ✔ "scope by unit or process" | ✔ "risk across each business unit and process" | ✔ register "by Basel category, business unit" | ✘ (hazards/jobs instead) | B — GRC-sense sample |
| RCSA as the assessment instrument (first-line owners assess risks + controls; second line reviews/approves) | ✔ scoped→routed→confirmed→reviewed→approved→snapshotted | ✔ "scale RCSAs… engage process owners… automated scoping, assignment, progress tracking" | ✔ RCSA with inherent/residual, first-line engagement, second-line challenge | ✘ (JSA/PTW instead) | B — GRC-sense sample |
| Loss event capture as a first-class record, linked back to risks and controls | ✔ occurrence/discovery/loss dates, root cause, link to risk + control | ✔ "linkages across risks, issues, and loss events" | ✔ "loss event capture with investigation workflow" | ✘ (incident reporting is safety-incident world) | B — GRC-sense sample |
| Control library mapped to risks | ✔ "linked control library… controls mapped to the risks they cover" | implied (RCSA ties risks to controls) | ✔ "a mapped control library" | ✘ | B |
| KRI monitoring with thresholds + owner tasking/alerts | ✔ red/amber thresholds, owner tasked per frequency | ✔ "automate KRI monitoring" | ✔ "KRI dashboards with threshold alerting" | ✘ | B |
| Control testing on a cadence | not named on page | Automated Control Testing is a platform feature (not ORM-page-specific) | ✔ "tested on a defined cadence" | ✘ | B-weak → Common |
| Scenario analysis | not named on page | not named on page | ✔ named tool + framework component | ✘ | A (one product) → Optional/Common in FI segment |
| Board/executive reporting | ✔ prebuilt dashboards for managers and the board | ✔ role-based dashboards for executives | ✔ board-ready reporting | ✘ | B |
| Basel taxonomy / FI regulatory anchoring | ✔ Basel II named in FAQ | Banking Solution suite exists | ✔ seven Basel categories, FFIEC/OCC/NCUA | ✘ | B (FI segment), not universal |
| Sold inside broader GRC/IRM suite | ✔ | ✔ | ✔ | ✔ (IRM platform) | B — all sampled |
| First-line/second-line role split | ✔ process managers confirm; risk team reviews/approves | ✔ process owners assess; risk teams save time | ✔ three lines of defense explicit | ✘ | B — GRC-sense sample |

## Canonical Model — Four-Layer Abstraction

### L0 — Defining Invariant (minimal)

1. **Process-anchored operational risk records.** The system manages a persistent population of risk records for risks arising from failed or inadequate internal processes, people, and systems, or from external events — each attached to the business unit / process / activity where the risk lives, with a named owner and a standardized severity rating. (Remove → a generic enterprise risk register with no operational anchor, i.e. ERM territory.)
2. **The risk-and-control self-assessment loop.** First-line process/business owners are engaged as assessors: an RCSA campaign scopes assessments by unit or process, routes them to the owners, who confirm/reassess existing risks and controls and add new ones; the second-line risk function reviews and approves the result. Risks are tied to the controls that mitigate them. (Remove → a second-line-only risk list with no front-line engagement — the assessment machinery that makes ORM operational.)
3. **Loss event capture linked back to risks and controls.** Actual operational loss/incident events are recorded as first-class records (occurrence/discovery/impact), investigated for root cause, and linked to the risk records and controls involved. (Remove → an assessment-only tool with no feedback from reality; the loss loop is the ORM signature that most distinguishes it from ERM.)

Removal tests: remove process anchoring → ERM; remove the RCSA loop → a static register nobody in the business feeds; remove loss events → RCSA-only tooling, losing the discipline's defining feedback loop. All three legs are jointly held: 1 alone = a risk list; 2 without 1 = assessments with nothing to anchor; 3 without 1+2 = an incident log with no risk program.

Historical check (pre-Basel, pre-2004, regional, spreadsheet-era): a loss register with root-cause notes, process-level risk inventories, paper/spreadsheet RCSAs routed to unit managers, and a control list mapped to risks satisfies L0 fully. KRIs, Basel categories, scenario analysis, GRC suites, and AI are not needed for recognizability → correctly excluded from L0. Non-financial operational risk programs (e.g., an industrial firm tracking process failures and losses with self-assessments) also fit.

### L1 — Common Mature Structure (cross-product common)

- KRI/indicator monitoring: indicators assigned to risks, measured on a cadence by named metric owners, with red/amber thresholds and alerting/escalation on breach.
- Control testing on a defined cadence (preventative/detective/corrective controls; test results feeding reporting).
- Inherent vs residual scoring on the same risk record; second-line challenge of first-line ratings.
- Risk appetite/tolerance thresholds translated into measurable limits; escalation paths.
- Scenario analysis workshops for severe/low-frequency risks (especially where loss data is scarce).
- Campaign rhythm: annual RCSA cycles with periodic refresh on higher-risk processes; snapshots showing how ratings moved between cycles.
- Issue/corrective-action management arising from assessments, losses, and control failures.
- Role model: first-line process/business owners (assess, execute controls), second-line operational risk function (taxonomy, methodology, campaigns, challenge, aggregation), third-line internal audit (assurance), executives/board (consume reports); user-attributed audit trail.
- Dashboards and reporting: risk and loss dashboards, heat maps, board-ready views.
- Intake forms reaching people outside the core user base (loss reporting by any employee).
- Organizational-entity scoping (business unit / location / process hierarchies).

### L2 — Variant / Optional Structure

- Banking/regulatory depth: Basel event-type taxonomy, regulator-facing reporting cadences, capital methodology (SMA), scenario analysis as a first-class method, examination-findings linkage. FI-grade platforms add regulatory-change feeds.
- Quantitative loss-exposure modeling / risk quantification as a separate capability or product line.
- Operational resilience adjacency: BIA results and impact tolerances feeding process-based RCSA (Archer); resilience as a sibling solution (LogicGate).
- Depth of GRC-suite embedding: policy, compliance, audit, TPRM, BCM, ESG as sibling applications vs standalone ORM tool.
- Industry overlays beyond banking: insurance (ORSA), healthcare, energy/utilities, manufacturing.
- AI assistance: linkage discovery across risks/issues/losses, first-pass assessment, response-plan generation (LogicGate Spark AI; Archer Evolv).
- Delivery & licensing: SaaS vs on-prem; unlimited end-user licensing for RCSA participation (LogicGate).

### L3 — Vendor-specific (research notes only)

- Archer: combined Enterprise & Operational Risk use case; two-level taxonomy recommendation; nightly snapshots; Risk and Control Matrix report; Engage forms for external intake; Basel II/COSO/ISO 31000/NIST RMF anchoring; Evolv Foundation plain-language record queries.
- LogicGate: Risk Cloud Applications/Workflows semantics; ORM Application + Issues Management + Incident Management packaging; Operational Risk Management Suite; Spark AI linkage/response-plan generation; Value Realization Tool; unlimited end-user RCSA licensing.
- 360factors: Predict360 module sharing taxonomy/control library across TPRM, regulatory change, audit; Ask Kaia AI compliance app; ABA/Crowe content libraries; FI-specific regulatory anchors (FFIEC/OCC/NCUA/SR 26-02).
- Origami Risk: EHS-ORM tool set (JSA, LOTO, PTW, pre-task planning) — a different product world under the same name.

## Vendor-specific Findings

(See L3; none promoted to the canonical model.)

## Rejected Findings

- "ORM = ERM with a different name": rejected. Same building blocks, different center of gravity — see Boundary Findings. Archer combines them in one use case; LogicGate sells them as separate solutions; 360factors explicitly positions ORM as the second-line discipline producing the operational-risk component of the ERM view.
- "Basel taxonomy is definitional": rejected. Basel categories are the standard reference in banking, but the defining structure (process-anchored risks + RCSA + loss events) predates and exceeds Basel; non-financial ORM programs fit without it.
- "KRIs are definitional": rejected — present in all three GRC-sense products at page level, but a loss register + RCSA program is recognizably ORM without them (historical check).
- "Control testing cadence is definitional": rejected — evidenced clearly in one product (360factors) and as a platform feature in another; treated as common mature structure.
- "The EHS sense (JSA/LOTO/PTW) is the same Type": rejected — different objects, users, and regulatory world; recorded as a polysemy/boundary finding.
- Precise claims (number of scale levels, exact refresh frequencies beyond vendor-stated examples, exact status names): rejected — no deep official help-center documentation was reachable; asserting them would exceed evidence.

## Boundary Findings

- **vs Enterprise Risk Management (joint-review flag from the ERM pass — DISCHARGED):** the two types share record types (risks, controls, RCSA, loss events) but differ in center of gravity. ORM is anchored on operational processes, first-line engagement, control failures, and loss events; ERM is anchored on the enterprise-wide register aggregated to leadership across all risk categories (strategic, financial, compliance, operational). Evidence: Archer markets them as one combined use case with RCSA as the operational mechanism inside the enterprise register; LogicGate sells them as separate solutions; 360factors states "ORM is the second-line discipline that produces the operational-risk component of that [ERM] view." Test: remove the enterprise cross-category roll-up → ORM; remove the process/loss anchoring and first-line assessment loop → ERM. Boundary is real but porous; in the market the two are often modules of one suite and one product can host both. Keep-both ratified: both leaves describe distinct centers of gravity with distinct primary objects (loss events and process-level controls vs enterprise roll-up).
- **vs Governance Risk & Compliance Platform:** GRC Platform is the broader suite (policies, compliance obligations, controls, audit, ethics). ORM is the operational-risk-centered application within it. In the current market ORM is nearly always a module/solution of such a platform.
- **vs Internal Controls Management:** controls management is anchored on the control library and its testing/compliance mapping (control-centric); ORM is anchored on risks and losses (risk-centric) with controls as the mitigation linkage. Control testing appears in both; the primary object differs.
- **vs Incident Management (IT/operational):** IT incident management restores service (detection→response→resolution); ORM loss events are risk-program records for root-cause and loss analysis feeding the risk register. An ORM platform may include an incident/issue application (LogicGate), but the defining loop is the risk/loss linkage, not service restoration.
- **vs Operational Resilience:** resilience manages disruption preparedness for important business services (impact tolerances, recovery, testing); ORM manages operational losses and control failures. They feed each other (Archer: BIA results roll into process-based RCSA) but the primary objects differ.
- **vs Third-party Risk Management:** TPRM scopes risk machinery to vendor/counterparty relationships and their lifecycle; ORM's population is the organization's own processes and people (vendor events may enter as loss events).
- **vs EHS/HSE Platform (polysemy):** "Operational Risk Management" is also used as a name for workplace-safety hazard management (JSA, LOTO, permit to work — Origami Risk). That world's objects are hazards, job steps, and permits, not Basel-style operational-loss records; it belongs to the EHS/HSE Platform Type. The §11 leaf is the GRC/financial-services sense. Recorded in STATUS Boundary Issues.
- **vs spreadsheet loss/RCSA registers:** the software-type boundary is the living linkage (risks↔controls↔losses), routed campaigns, threshold alerting, and audit-attributed history — what static spreadsheets cannot provide.

## Taxonomy note

DIRECTORY places Operational Risk Management under "Legal, Risk, Compliance & Governance" alongside ERM, GRC Platform, TPRM, etc. Research supports ORM as a valid standalone Type (distinct process/loss-centered core), delivered in the live market mostly as a module/solution of GRC/IRM platforms. The ERM pass's joint-review flag is discharged from this side: keep-both, with the center-of-gravity test documented above.

## Uncertainties

1. Exact risk-record and loss-event lifecycle states (draft/active/closed etc.) not verified from deep official docs — stated only as "statuses and workflows exist."
2. Whether control testing is universal in ORM products or belongs to Controls Management modules — evidence is weak (one product explicit, one platform feature); treated as common, not definitional.
3. ServiceNow IRM (a market leader in operational risk for non-FI enterprises) could not be fetched; its inclusion could shift emphasis (workflow-platform embedding, CMDB linkage) but not the L0 core.
4. Degree of scenario-analysis universality outside financial services — evidenced in the FI segment; treated as segment variant.
5. Non-financial GRC-sense ORM products (manufacturing, energy) were not directly sampled; their inclusion rests on the Origami bridge language and the general GRC-suite pattern — the L0 was deliberately kept segment-neutral to cover them.
6. Riskonnect appears not to sell a separate ORM product (its ORM URL resolves to content, and its solution list omits ORM) — consistent with the ERM pass; not independently confirmed.

## Final Synthesis

An Operational Risk Management application is the operational-risk discipline's system of record: the second-line function's workbench for managing the risks that live in the organization's day-to-day processes, people, and systems. Its world has three load-bearing structures. First, a process-anchored risk register: operational risk records — risks of failed processes, people, and systems, or external events — attached to the business units and processes where they live, owned by name, rated on the organization's scales. Second, the risk-and-control self-assessment loop: campaigns scoped by unit or process, routed to first-line process owners who confirm what still applies, reassess what changed, and add what is new, with the second-line risk function reviewing and approving — risks tied to the controls that mitigate them. Third, the loss-event loop: actual operational losses and incidents captured as first-class records, investigated for root cause, and linked back to the risks and controls involved, so ratings rest on evidence rather than memory. Around these run the common mature structures: KRI thresholds and alerts, control testing on cadence, appetite thresholds and escalation, corrective-issue management, snapshots and trend views, and board-ready reporting. The defining character is operational and first-line: the front of the business feeds the system through self-assessments and loss reports, and the risk function owns methodology, challenge, and aggregation. The type's nearest neighbor is ERM, which shares every building block but centers on the enterprise-wide roll-up of all risk categories to leadership; ORM centers on the process level and the loss feedback loop. In the current market ORM is nearly always a module or solution of a broader GRC/IRM platform, with the deepest segment form in banking under Basel/FFIEC-style frameworks. The name is also used for a different product world — workplace-safety hazard management (EHS) — which shares the words but not the objects.
