# Research Notes — Penetration Testing Management

Slug: penetration-testing-management
Research date: 2026-09-09
Methodology: v1.1 (update-v1/). Evidence layers: A = directly observed on an official source fetched in this pass; B = cross-product commonality across the sample; C = canonical inference from cross-product comparison and boundary reasoning.

---

## Research Goal

Understand what a Penetration Testing Management (PTM) application actually is as a software type: its core objects (engagement, scope, findings, report, retest), the engagement lifecycle, who operates it (pentest leads, testers, client-side security teams, remediation owners), what rules make an offensive test legitimate and safe (scope, authorization, rules of engagement), and where its boundary sits against Breach & Attack Simulation, Vulnerability Management, DAST/IAST, Attack Surface Management, bug-bounty/VDP platforms, Security Program Management, and professional-services automation.

## Initial Boundary

Working hypothesis before research:

1. Core use: organize offensive security testing as managed engagements — scoped, authorized, time-bounded tests executed by testers, producing recorded findings that are tracked through remediation verification and closed with a report.
2. Primary users: pentest leads / engagement managers, penetration testers (internal, provider, or vetted community), client-side security managers who request and consume tests, remediation owners.
3. Nearest neighbors: Breach & Attack Simulation (automated continuous control validation), Vulnerability Management (org-wide vuln lifecycle), DAST/IAST (testing tooling), Attack Surface Management (target discovery), bug bounty / VDP platforms (open continuous submission), Security Program Management / GRC (program layer), PSA (generic client-work management).
4. Likely boundary: PTM manages the human-led engagement lifecycle; BAS runs automated continuous simulations; VM owns the vulnerability record across all sources; DAST is tooling used inside engagements.
5. Unknowns: exact object model (pentest vs engagement vs project), finding-state taxonomies, how retest is modeled, whether "management" platforms exist independently of tester supply (marketplace vs own-team), how automated-pentest modules straddle.

Prior context from sibling passes (STATUS.md): the breach-attack-simulation pass drew the seam "PTM manages human-led, scoped, point-in-time engagements (rules of engagement, findings, retests); BAS is automated, continuous, and safe-by-design" and flagged a joint review for "automated pentesting" products (Pentera Surface/Core, Picus APV) straddling toward this leaf. The attack-surface-management and dast-iast passes both reference PTM as "organizes human engagements". This pass discharges those flags from the PTM side.

## Research Questions

- What is the unit of record — engagement, pentest, project, test? What does it carry?
- What does the engagement lifecycle look like (states, stages) and who moves it?
- What is a finding, what states does it traverse, and how does retest work?
- How is scoping done (assets, targets, parameters, environments, test period)?
- How is authorization / rules-of-engagement expressed (what testers may do, black/grey/white box, exclusions)?
- How are testers staffed (marketplace, vetted community, own team) and scheduled?
- What does the report contain and what report types exist (incl. attestation for compliance)?
- What surfaces exist for the client side (portal, communication, remediation tracking)?
- How do findings reach remediation (ticketing integrations)?
- Where is the line vs BAS ("automated pentesting"), VM, DAST, ASM, bug bounty, PSA?

## Representative Products

Selection rationale: market representativeness + different product philosophies (marketplace service vs managed crowdsourced vs internal-team tooling vs self-hosted open-source-heritage) + different customer tiers (enterprise buyers, consultancies/MSSPs, internal offensive teams) + documentation completeness.

| Product | Philosophy / position | Evidence level in this pass |
|---|---|---|
| Cobalt | Pentest as a Service (PtaaS) marketplace + a "Pentest Management Platform" (PMP) mode for customer-run in-house tests; the same platform serves both tester-supply models | A (official docs: pentest process, states, finding states, scoping, report contents, roles, methodologies, in-house mode) |
| Synack | Managed continuous pentesting with a vetted researcher community (Synack Red Team) + autonomous AI agent (Sara); PTaaS category self-naming; FedRAMP public-sector posture | A (official site: platform structure, products, solutions, customer quotes; positioning-level, no login-gated docs) |
| PlexTrac | Pentest reporting & management platform for internal offensive teams and service providers; full lifecycle from scheduling to remediation; expanding toward exposure management (acquired by Brinqa) | A (official platform overview + homepage; help center login-gated/401) |
| Dradis | Self-hosted pentest reporting & management; open-source Community Edition since 2007 (bundled in Kali) + commercial Pro; data-sovereignty pole; serves consultancies and internal teams | A (official product site + CE site) |

Rejected / unreachable: AttackForge (site JS-rendered empty; docs subdomain transport error ×1 — abandoned per network rule); Reconmap (domain now hosts an unrelated photo-geolocation product — the VAPT tool is gone from that URL); PlexTrac help center (401). No claims made about these.

## Sources

Official surfaces fetched 2026-09-09:

- Cobalt — Pentest Process: https://docs.cobalt.io/articles/pentest-process-BxpPkG77qd
- Cobalt — Pentest States: https://docs.cobalt.io/articles/pentest-states-KfXxlt4Re2
- Cobalt — Finding States: https://docs.cobalt.io/articles/finding-states-De6IE4W5Zw
- Cobalt — Engagements Overview: https://docs.cobalt.io/articles/engagements-overview-E2L8W0LxOt
- Cobalt — In House Pentests (Pentest Management Platform): https://docs.cobalt.io/articles/in-house-pentests-HYNuapVOyk
- Cobalt — Create a Pentest: https://docs.cobalt.io/articles/create-a-pentest-BQSirXEl9M
- Cobalt — Scope & Test Period: https://docs.cobalt.io/articles/scope-test-period-dvnBEgzJgm
- Cobalt — Contents of a Pentest Report: https://docs.cobalt.io/articles/contents-of-a-pentest-report-rkAVYIfSNL
- Cobalt — User Roles and Permissions: https://docs.cobalt.io/articles/user-roles-and-permissions-oCij6uRrUR
- Cobalt — Methodologies Overview: https://docs.cobalt.io/articles/cobalt-methodologies-overview-LTfYQiQvzV
- Cobalt — Blackout Period (DAST scanner module): https://docs.cobalt.io/articles/blackout-period-W5AScIJKtD
- Cobalt — docs index/sitemap: https://docs.cobalt.io/ , https://docs.cobalt.io/sitemap.xml
- PlexTrac — Platform Overview: https://plextrac.com/platform/overview/
- PlexTrac — Homepage: https://www.plextrac.com/
- Dradis — Product site (Pro): https://dradis.com/
- Dradis — Community Edition site: https://dradisframework.com/ce/
- Synack — Homepage / platform structure: https://www.synack.com/

Unreachable / degraded:

- PlexTrac Help Center — https://helpcenter.plextrac.com/ (empty render; /support/home 401) → PlexTrac claims stay at official marketing/product-page level; no operational-detail claims made from it.
- AttackForge — https://attackforge.com/ (JS-rendered empty), https://docs.attackforge.com/ (transport error) → abandoned; excluded from all claims.
- Reconmap — https://www.reconmap.org/ now serves an unrelated product → excluded.
- Synack product docs are behind login (login.synack.com); site-level claims only.

## Product Observations

### Cobalt (evidence layer A)

**Pentest lifecycle** (Pentest Process): six stages — Discover (prepare, map attack surface, account setup) → Plan (plan, scope, schedule; prepare test credentials; stakeholders alerted; "we'll assign pentesters based on your technology stack") → Test (pentesters test using methodologies; vulnerabilities shared in real time in Slack and the app; remediation can start during test) → Remediate (fix findings, submit for retest or accept risk; retesting included) → Report (Pentest Lead works on the report; downloadable, shareable with stakeholders) → Analyze (assess posture with dev/security teams, plan next pentest).

**Pentest states**: Draft → In Review (provider reviews submission) → Planned (accepted; pentesters assigned; dedicated Slack channel) → Live (testing underway; chat channel for questions/findings) → Paused (testing cannot continue; reason shared) → Remediation (results shared; fix or accept each finding; resubmit for retest) → Closed (all findings fixed-and-retested, accepted, or none found) / Cancelled (kept in records).

**Finding states**: Triaging (initial severity, under review/validation, not yet confirmed) → Pending Fix (validated, severity assigned by likelihood of occurrence and business impact; fix-and-retest or accept risk) → Ready for Retest → Fixed (retest could not reproduce) or back to Pending Fix; also Accepted Risk, Carried Over (open finding from a previous pentest on the same asset tracked on the current one), Declined (not a valid vulnerability), Out of Scope (found outside pentest scope), Duplicate; Draft state for in-house pentesters.

**Scoping** (Scope & Test Period): scoping parameters per asset type — Web (user roles, dynamic pages/routes), Mobile (operating systems), API (endpoints; GraphQL queries/mutations), External/Internal Network (IP addresses), Cloud (accounts/projects/resource groups, unique service instances, hostnames), Desktop (OS count), AI/LLM (tiered: prompt-injection / isolated LLM / RAG-enabled, with required documentation); combined asset types (Web+API, Web+API+External Network, Web+Mobile…). Scope complexity determines credits. Start date scheduling tied to PtaaS tier; end date confirmed after review; retest end date per contract tier.

**Assets**: "Assets are what we pentest" — persistent asset records (web, mobile, API, external/internal network, cloud, desktop, AI/LLM) with details and environments (Production / Staging / Development).

**Report contents**: Target, Test Period, Test Performed By (pentester profiles), Executive Summary (findings by severity, highlights), Scope of Work (target description + environment; in-scope methodologies tested to OWASP Top 10 / OWASP ASVS; checklist of tests performed; "Test Cases that Thwarted Exploitation Attempts"), Methodology (pre-engagement / penetration testing / post-engagement), Risk Factors (modified OWASP Risk Rating; impact × likelihood, 1–5 scales), Severity Definitions, Summary of Findings (graphs by type/severity; open ports and services), Recommendations, Post-Test Remediation (type/severity/state/resolution dates), Terms/disclaimer, Appendix A Finding Details (vulnerability type, description, affected URLs, proof of concept, severity, suggested fix). Report types: Automated Report (Agile), Customer Letter, Attestation Report, Attestation Letter, Full Report, Full Report + Finding Details.

**Roles**: customer side — Organization Owner (admin: assets, pentests, users, groups, security settings, integrations, credits ledger, insights), Organization Member (assets/pentests within group permissions), Pentest Team Member (per-pentest collaborator: view/edit pentest details, manage findings, collaborate in app + Slack, manage pentest users, view activity, manage Jira integration; no org-wide access unless also Owner/Member). Provider side — Pentester, Lead (manages team, 2+ testers), Coordinator (Agile or single-tester tests). In-House Pentester (customer-invited tester on the PMP). Cobalt Staff (administrative).

**In-House / PMP**: "With the Pentest Management Platform (PMP), you can launch and manage your in-house pentests with Cobalt. Set up a pentest, invite your own pentesters, and analyze pentest results in one place." Pentesters from the organization, a third-party company, or both; Cobalt pentesters not involved. Value props: visualize end-to-end pentest program, reduce administrative work, integrate findings into SDLC (Jira/API), standardize reporting with templates, track program improvements via ongoing test data/analytics. Two roles: Pentest Manager / In-House Pentester.

**Methodologies & rules of engagement**: methodologies fixed per test/asset type; OWASP Top 10 lists (web, API, mobile, AI/LLM, cloud) and OSSTMM for networks. Testing approaches: Black-box (no internal knowledge; "Testing will cease immediately and the Customer will be contacted if the pentester gains access to the application or network"), Grey-box (partial knowledge: credentials, API docs, architecture overview), White-box (full access: source, configs, test accounts). Out of scope: DoS/DDoS testing (downtime risk, indistinguishable from attack); third-party applications/libraries (test the integration, not the third-party product). Traffic discipline: all traffic from a controlled, identifiable IP range through VPNs that "can be stopped as needed in an emergency"; primarily manual techniques (light load) with brief automated spikes (peak figures vendor-stated).

**Adjacent modules** (straddle evidence): Autonomous pentests (create/launch/saved/review-closed-report articles; "Autonomous Web" methodology), DAST Scanner module (targets, scans, target authentication, blackout periods), Attack Surface Monitoring, Digital Risk Assessments and Secure Code Reviews as "Engagements" (special service types with flexible scheduling).

**Commercial model**: credits; scope complexity → credits; PtaaS tiers (Agile vs Comprehensive); co-branded reports for partners.

### Synack (evidence layer A — positioning level)

- Self-naming: "AI + Human Penetration Testing | PTaaS"; "Continuous Pentesting at Scale"; "Move from point-in-time testing toward continuous security validation without sacrificing human judgment or operational control."
- Platform triad: Sara AI Pentesting (autonomous red agent: "identifies, validates, and prioritizes vulnerabilities") + Synack Red Team ("over 1,500 of the world's most skilled and trusted security researchers" — vendor claim; vetted, skill-tagged profiles) + Synack Platform ("Access to on-demand researchers, vulnerability management, integration, and reporting").
- Platform tour framing: "Scope an asset, launch a test, review findings and build a continuous security validation program."
- Products: Penetration Testing (gray box: AI/LLM, API, Application, Cloud, Compliance pentesting), Attack Surface Management (separate product), Vulnerability Disclosure Program (separate product).
- Solutions: Continuous Penetration Testing, Third-Party Testing (third-party risk angle), "Beyond Bug Bounty", Vulnerability Management, Social Engineering Testing.
- Customer quotes (vendor-published): portal as "one-stop-shop approach to managing everything from test planning, to communication"; "Researcher Messaging and Jira Connector Improve Experience"; "At least 35 highly qualified penetration testers will test your site"; continuous testing cycles replacing point-in-time pentests (Allianz Direct).
- FedRAMP posture (public sector); MSSP partner packaging ("Human-led, AI-augmented pentesting packaged into your managed service portfolio").
- Vendor-stated marketing figures (32% lower costs, 22 days saved, 47% faster remediation, 99.98% noise filtered) — L3, excluded from final document.

### PlexTrac (evidence layer A — product-page level)

- Self-naming: "Penetration Test Reporting & Management Platform"; "pentest reporting and exposure assessment platform"; acquired by Brinqa ("Unified Exposure Management").
- Full lifecycle claim: "manage the entire penetration testing lifecycle—from engagement planning and testing procedures to reporting, remediation tracking, and validation"; "schedule testing engagements, track tester capacity, and execute repeatable testing methodologies using structured procedures mapped to frameworks like MITRE ATT&CK."
- Platform features: Schedule & Scope (Scheduler module; inbound scheduling requests; team workload capacity); Procedures & Runbooks (repeatable test plans; report against frameworks; ramp up new testers; purple-teaming runbooks); Data Ingestion (scanner/tool imports, dedup); AI authoring (auto-generate finding descriptions, remediation recommendations, narratives; reusable content library — vendor claims 25,000+ writeups); QA workflows (commenting, change-tracking, real-time collaboration); Client Portal (white-labeled; real-time findings view; historical data; remediation tracking); Workflow Automation (trigger events → Jira tickets / emails); Remediation & Retesting (ticketing integrations; built-in retest workflows); Exposure Management (finding-first vs asset-first lens over consolidated data).
- CTEM lifecycle mapping: Scoping (asset management, scheduler) → Discovery (manual testing in-platform: pentests, repeatable test plans, adversary emulation; integrated discovery tools) → Prioritization (configurable risk equations; Priorities module) → Validation (test and retest planning) → Mobilization (remediation workflows; Jira/ServiceNow with bi-directional updates at client/departmental level).
- Audiences: Enterprise teams (internal pentest reports) vs Service Providers/MSSPs (white-labeled client portal, expand service offerings); package ladders (Essential/Core/Premium) with feature tiers.
- Deployment: Secure Cloud, Private Hosted, Client Hosted.
- Customer quotes (vendor-published): consultancy use — "centralizes all our findings and progress in one console… clients to track vulnerabilities from one pentest to the next"; "shift from point-in-time testing to more continual engagements"; red-team and purple-team usage.

### Dradis (evidence layer A)

- Self-naming: "Self-Hosted Pentest Reporting & Management Platform"; solutions page "Manage Pentest Engagements — from scoping to re-test in one platform."
- Engagement container: the project holds scanner output, findings with evidence (code snippets, request fragments, screenshots), methodology as task checklists, notes, and the exported report. CE limitation: single project at a time; Pro: multiple concurrent projects ("manage all your pentests from one place" — Project Scheduler).
- Scoping: Contributor Questionnaires — "Your client answers scoping questions online. The answers are in Dradis before kickoff."
- Findings workflow: findings entered as-you-find in final form (library write-up + specifics); QA review states Draft / Ready for Review / Published that the export respects; PR-style inline comments and revision history; "Reporting day is not consolidation day."
- Consistency machinery: Issue Library (team-owned write-ups and ratings — "Same finding, same rating, whoever found it"); Methodologies (OWASP, PTES, OSCP, HIPAA, PCI or custom; methodology Kanban board with task assignment and evidence); Risk Calculators (CVSSv4, DREAD, MITRE ATT&CK, custom).
- Scanner ingestion: Rules Engine maps scanner output to library entries, dedups, drops non-reportables; 47+ integrations (Nessus, Burp, Nmap, Qualys, ZAP, OpenVAS, Nikto, Nexpose…); universal CSV importer; open-source plugins.
- Client-facing: Gateway / Interactive Results Portal — client reads findings in real time, asks testers in threads ("A suspected false positive is settled in the thread, not by email"); white-labeled, on the team's own domain; per-client history and trend (Business Intelligence).
- Remediation: built-in Remediation Tracker; ticketing integrations (Jira, ServiceNow, Azure DevOps) in Pro.
- Retest: "The re-test runs in the same project, or in a clone of it when months have passed."
- Reporting: template conversion service ("1,182+ templates converted since 2010" — vendor claim); one-click Word/Excel export; weekly-update exports during long engagements.
- Delivery philosophy: self-hosted only (on-prem, private cloud, air-gapped, own cloud tenant); "We never see your clients' findings"; data sovereignty, audit log, OTP MFA; CE (GPLv2, since 2007, bundled in Kali/BlackArch/ArchStrike) vs Pro editions (Assess / Remediate).
- Audiences: security consulting teams, corporate/internal security teams, enterprise.

## Cross-product Comparison

| Dimension | Cobalt | Synack | PlexTrac | Dradis |
|---|---|---|---|---|
| Unit of record | Pentest (with Assets as persistent targets) | Test / launch on a scoped asset (program-level) | Engagement (report as deliverable container) | Project (= one engagement) |
| Who staffs the test | Provider pentesters (Lead/Coordinator/Pentester) or customer's own (PMP in-house) | Vetted community (SRT) + autonomous agent (Sara) | Customer's own team (internal or MSSP testers) | Customer's own team (consultancy or internal) |
| Scoping | Structured scoping parameters per asset type + test period + credits | "Scope an asset, launch a test" | Scheduler + asset management; inbound scheduling requests | Contributor questionnaires answered by the client before kickoff |
| Methodology/coverage | Fixed methodologies per asset type (OWASP Top 10 family, OSSTMM); black/grey/white-box approaches | Gray-box service lines (app/API/cloud/AI-LLM/compliance) | Procedures & Runbooks mapped to frameworks (ATT&CK); repeatable test plans | Methodology checklists as tasks (OWASP/PTES/OSCP/HIPAA/PCI/custom); Kanban board |
| Finding record | States: Triaging → Pending Fix → Ready for Retest → Fixed / Accepted Risk / Carried Over / Declined / Out of Scope / Duplicate | Verified findings ("humans prove what matters"); noise filtering claim | Findings with evidence, severity, AI-assisted authoring; dedup across sources | Findings + evidence; library-based write-ups; QA states Draft/Ready for Review/Published |
| Retest | First-class: retest included; finding-level retest loop; retest end date | Continuous cycles; revalidation | Built-in retest workflows; validation phase | Re-test in same project or a clone |
| Report | Typed reports (Automated/Customer Letter/Attestation Report/Attestation Letter/Full) | Reporting in platform | Automated report generation; templates; reusable content; QA | One-click Word/Excel from templates; template conversion service |
| Client surface | Pentest Team Members + dedicated Slack channel; co-branded reports | Portal ("test planning to communication"); researcher messaging | White-labeled Client Portal with real-time findings + history | Gateway portal; client threads on findings; per-client trend |
| Remediation handoff | Jira/GitHub/GitLab/Azure DevOps tickets; remediate during test | Jira/ServiceNow connectors | Jira/ServiceNow workflows; trigger-based automation | Built-in tracker + Jira/ServiceNow/Azure DevOps |
| Program analytics | Insights page; program improvements via ongoing test data | Continuous validation program; per-client trend | Analytics dashboards; risk-reduction over time; Priorities module | Business Intelligence; per-client trend |
| Delivery | SaaS | SaaS (FedRAMP posture) | Cloud / private-hosted / client-hosted | Self-hosted only (incl. air-gapped); CE open-source |
| Commercial model | Credits + tiers (Agile/Comprehensive) | Contract/subscription (vendor-stated figures only) | Package ladders per audience | CE free; Pro per-user editions |
| Adjacent modules | Autonomous pentest, DAST scanner, ASM, digital risk assessment, secure code review | ASM, VDP, Sara AI | Exposure management/CTEM, priorities, assessments | Echo LLM assistant, rules engine, webhooks/API |

## Canonical Model

### L0 — Defining Invariant

The smallest structure without which the product stops being recognizable as Penetration Testing Management:

1. **The engagement as the unit of record** — a persistent, individually identified offensive-security test undertaking that carries its scope (targets/assets in and out of bounds), a bounded test window, its authorization context (who may test what, under which rules), and its assigned testers. Remove → a findings tracker or bug tracker with no test undertaking; a scheduling tool.
2. **Findings as the engagement's security output** — vulnerabilities discovered during the engagement recorded as structured, evidenced records (what, where, proof, severity, remediation guidance), attached to the engagement and reviewed before delivery. Remove → authorization paperwork with no security product; raw tester notes.
3. **The lifecycle through remediation verification** — the engagement advances through planned → executed → reported states, and its findings are tracked to resolution: fixed and retested (retest recorded against the same finding) or formally accepted as risk, before the engagement closes. Remove → one-shot report delivery; the "management" gone.

Tests: remove the engagement record and run techniques continuously → BAS; remove the offensive test and keep the vuln lifecycle → Vulnerability Management; remove the management layer and keep only testing tools → a pentest toolkit / DAST; remove security semantics and keep client-project delivery → PSA/project management; remove findings and keep scheduling + authorization → a booking tool.

Historical / market-sample check: the paper-era engagement — engagement letter with scope and rules, named testers, a findings list compiled during testing, a typed report, and a retest letter after fixes — satisfies all three legs with no software. Dradis CE (open-source, since 2007, bundled in Kali, single-project workflow) satisfies all three with no cloud, AI, marketplace, or continuous-testing machinery. The L0 therefore does not over-fit the current PTaaS/marketplace era. "Human testers" is held as the dominant realization (the engagement is staffed by assigned, accountable testers in all sampled products) rather than a named invariant; automated execution engines appear in-sample only as modules beside the engagement model (see L2/boundaries).

### L1 — Common Mature Structure

- Scoping machinery: persistent asset/target catalogs (web, mobile, API, network, cloud, desktop, AI/LLM), scoping parameters, environment designations (production/staging/development), test windows and scheduling.
- Methodology/coverage structures: methodology checklists or test plans mapped to industry frameworks (OWASP Top 10 family, OSSTMM, PTES, ATT&CK), attached to the engagement and worked as tasks; knowledge-level approaches (black/grey/white box).
- Findings quality machinery: triage/review states, deduplication, severity models (CVSS-family calculators or impact × likelihood), reusable findings/write-up libraries so the team's standard survives personnel changes.
- Report generation: templated reports (executive summary + technical detail + remediation guidance), attestation-style deliverables for compliance audiences, co-branded/white-labeled variants.
- Client/stakeholder surfaces: portals or channels where the client side sees findings (often in real time), communicates with testers, and tracks remediation.
- Remediation handoff: ticketing integrations (Jira/ServiceNow/GitHub/GitLab/Azure DevOps class) and/or built-in remediation tracking; retest workflows closing the loop.
- Tester staffing and capacity: assignment by skill/technology, scheduling, workload management; in provider models, vetted-tester pools and per-engagement communication channels.
- Program-level analytics: trends across engagements, per-asset or per-client history, risk-reduction over time.
- Integrations and automation: scanner-result ingestion, APIs/webhooks, notification channels.
- Role model: organization/program admin, engagement manager or lead, tester, client-side stakeholder, remediation owner; per-engagement access scoping.

### L2 — Variant / Optional Structure

- Tester supply: internal team; provider marketplace (PtaaS); managed vetted community; mixed (own + third-party). The same platform can carry several supply models (Cobalt PtaaS vs PMP).
- Cadence: point-in-time engagements vs continuous/rolling programs ("continuous penetration testing").
- Delivery: multi-tenant SaaS vs self-hosted/air-gapped (data-sovereignty pole); open-source core + commercial editions.
- Commercial model: credits per scope complexity, per-user subscriptions, enterprise contracts.
- Automated execution modules beside the human engagement model: autonomous/automated pentest modes, bundled DAST scanners — the "automated pentesting" straddle toward BAS/DAST territory.
- Suite expansion: attack surface management, vulnerability disclosure/bug-bounty programs, exposure-management/CTEM repositioning.
- Compliance packaging: attestation letters/reports mapped to frameworks (PCI-style testing requirements, SOC 2 evidence needs).
- Service-line breadth: web/mobile/API/network/cloud/AI-LLM pentesting, secure code review, digital risk assessment, social engineering, red-team/adversary-emulation engagements as managed service lines.
- Purple-team machinery: runbooks/procedures shared with defenders; detection-validation tie-ins.

### L3 — Vendor-specific (research notes only)

- Cobalt: credits model; Agile vs Comprehensive tiers; Lead/Coordinator role split; Pentest Management Platform (PMP); Carried Over finding state; dedicated per-pentest Slack channels; Autonomous Web methodology; DAST scanner with blackout periods; co-branded reports; vendor-stated figures (14-day standard test period, report in 2–3 business days, start-date lead times by tier, peak bandwidth/QPS tables).
- Synack: Synack Red Team (SRT) and researcher skill tags; Sara AI / "Autonomous Red Agent"; Acropolis recognition program; FedRAMP; MSSP packaging; vendor-stated figures (1,500+ researchers, 32%/22 days/35 hours/47%, 99.98% noise filter, "at least 35 testers").
- PlexTrac: Runbooks, Plex AI, Priorities module, Scheduler module, white-labeled client portal, package ladders (Essential/Core/Premium × Service Provider/Enterprise), Brinqa acquisition / "Unified Exposure Management", vendor-claimed 25,000+ writeups.
- Dradis: Gateway (results portal), Contributor Questionnaires, Rules Engine, Issue Library, Echo (LLM context engine), Mappings Manager, CE/Pro (Assess/Remediate) edition split, "1,182+ templates converted since 2010", "19 years / 1,182 teams / 81 countries" heritage claims.

## Boundary Findings

- **vs Breach & Attack Simulation** (discharges the BAS pass's joint-review flag from this side): BAS executes a maintained library of attack simulations continuously against the organization's own controls and records each control's response (prevented/detected/logged/missed). PTM manages scoped, authorized engagements staffed by testers that produce findings about the tested targets, tracked to remediation. The seam is engagement-management-with-findings vs continuous-automated-control-validation. Straddle: "automated pentesting" products (Pentera Surface/Core, Picus APV — covered in the BAS pass) and autonomous modules inside PTM platforms (Cobalt Autonomous Pentest, Synack Sara) run exploitation-led tests without a human tester; in-sample they appear as modules beside the engagement model, not as replacements for it. If a product's only structure is continuous automated attack execution with control-response grading, it is BAS/security-validation territory; if it organizes engagements with scope, authorization, testers, findings and retest, it is PTM even when some execution is automated.
- **vs Vulnerability Management**: VM owns the organization-wide vulnerability record and remediation lifecycle across all sources (scanners, pentests, bug bounty). PTM produces findings through authorized offensive engagements and hands them over (ticketing/API). PlexTrac straddles by packaging pentest reporting with vulnerability management and exposure management — packaging evidence that the two are adjacent, not identical; its own marketing splits "pentest reporting teams" from "vuln management teams".
- **vs DAST / IAST**: DAST/IAST are testing engines that exercise applications and emit vulnerability findings. A pentest engagement commonly uses such tools inside its execution; the engagement-management layer (scope, authorization, staffing, findings workflow, report, retest) is the Type. Cobalt ships a DAST scanner as a separate module beside its pentest lifecycle — module evidence for the seam.
- **vs Attack Surface Management**: ASM discovers and inventories externally exposed assets; PTM tests a scoped, authorized target set. Synack sells ASM as a separate product beside its pentesting platform; Cobalt likewise lists attack surface monitoring as a separate module. ASM output can feed PTM scope.
- **vs Bug bounty / vulnerability disclosure platforms** (no directory leaf): open, continuous, unscoped submission by arbitrary researchers vs scoped, authorized, staffed engagements. Synack sells a VDP as a separate product and positions pentesting "beyond bug bounty"; Cobalt's engagement is bounded by scope and test period. The authorization boundary is the seam.
- **vs Security Program Management / GRC**: program-level governance of security activities vs the engagement-level execution system. PTM's compliance outputs (attestation letters, framework-mapped reports) serve GRC but the managed object is the engagement, not the control framework.
- **vs Professional Services Automation / project management**: PSA manages billable client work generically (resourcing, time, billing). PTM consultancies could run on PSA, but the engagement's security-specific structure — scope/authorization, methodology coverage, findings with severity and retest — is the Type's object model. Dradis/PlexTrac serve consultancies without being PSA.
- **vs Cyber Incident Response**: findings are pre-incident vulnerabilities recorded under authorization; incidents are detected/declared events. Different object, different lifecycle.
- **"Remove what to become the other type" tests**: see L0 tests above.

## Uncertainties

- Synack's operational object model (exact engagement states, finding workflow) is behind login; claims about it stay at platform-tour level ("scope an asset, launch a test, review findings").
- PlexTrac's help center was unreachable (401); its engagement/finding state machinery is inferred from product-page feature descriptions only, not from operational docs. No precise state names asserted for PlexTrac in the final document.
- AttackForge and Reconmap could not be verified (unreachable / domain repurposed); the open-source pole is anchored by Dradis CE instead.
- Whether every PTM product carries a formal "authorization/rules-of-engagement" object (vs. handling authorization contractually outside the tool) was not verifiable across the sample; in-sample evidence shows scope + test period + rules expressed in-product (Cobalt) or via questionnaires (Dradis), but the L0 keeps authorization as part of the engagement's context rather than requiring a dedicated object.
- Exact severity scales vary (Cobalt: modified OWASP risk rating; Dradis: CVSSv4/DREAD/custom); the final document therefore treats severity models as machinery, not as a fixed scale.
- The market's naming is not settled: "pentest management", "PTaaS platform", "offensive security management", "pentest reporting & management" all appear; the directory leaf name (Penetration Testing Management) is retained.

## Final Synthesis

A Penetration Testing Management application is the system of record for offensive security testing as managed engagements. Its defining core is three jointly-held structures: the engagement (a persistent, identified, scoped and authorized test undertaking with a bounded window and assigned testers), findings (structured, evidenced vulnerability records produced by the engagement and reviewed before delivery), and the lifecycle through remediation verification (planned → executed → reported; each finding resolved by fix-and-retest or accepted risk before closure). Around that core, mature products add scoping machinery over persistent asset catalogs, methodology/coverage structures mapped to industry frameworks, findings-quality machinery (triage, dedup, severity models, reusable write-up libraries), templated and attestation-grade reporting, client-facing portals with real-time finding delivery, ticketing-based remediation handoff, tester staffing and scheduling, program analytics, and integrations. The Type varies along tester supply (internal team / provider marketplace / vetted community / mixed), cadence (point-in-time vs continuous programs), and delivery (SaaS vs self-hosted data-sovereignty poles). Its boundaries: BAS is continuous automated control validation without an engagement record; VM owns the org-wide vulnerability lifecycle that PTM feeds; DAST/IAST are engines used inside engagements; ASM discovers the targets; bug bounty/VDP is open unscoped submission; PSA is generic client-work management. Automated-pentest engines straddle toward BAS and appear in-sample only as modules beside the engagement model.
