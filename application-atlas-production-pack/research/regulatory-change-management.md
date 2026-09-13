# Research Notes — Regulatory Change Management

Research date: **2026-09-07**

## Research Goal

Understand what "Regulatory Change Management" software actually is as an Application Type: what the managed object is, who operates it, where regulatory content comes from, what the review/decision/response machinery looks like, how the audit trail is preserved, and where the Type's boundaries sit against neighboring Types (Compliance Management Platform, GRC Platform, Policy Management, Regulatory Reporting, Legislative Tracking, life-sciences RIM, regulatory news/intelligence services).

## Initial Boundary

Initial hypothesis (pre-research):

- **What it is:** software that tracks regulatory changes (new/amended/repealed rules from authorities), assesses their applicability/impact on the organization, and manages the resulting compliance response.
- **Who uses it:** compliance officers, regulatory affairs, risk, legal, EHS managers, financial-services compliance teams.
- **Nearest neighbors:** Compliance Management Platform (§11), Governance Risk & Compliance Platform (§11), Policy Management (§10), Regulatory Reporting Platform (§08), Legislative Tracking Platform (§24), Regulatory Information Management / RIM (§22), regulatory content/news services.
- **Prior recorded boundary note:** the financial-compliance-management pass (2026-09-06) recorded: "RCM centers on the change-tracking slice itself; there, change monitoring is an input feed that drives obligations, policies, and activities." This pass tests that from the RCM side.
- **Open questions:** Is vendor-curated regulatory content definitional or common? Is a content-only regulatory intelligence service the same Type? Does a GRC-suite module differ structurally from a standalone product?

## Research Questions

1. What exactly does the system track — what is the managed object?
2. Where does regulatory change content come from (vendor feed, horizon scanning, user entry)?
3. What does the applicability/impact determination look like, and is the decision itself a managed artifact?
4. What happens after a relevant change is confirmed — what is the response machinery (tasks, owners, deadlines)?
5. How is the change → decision → response chain preserved for auditors/regulators?
6. How does the Type connect to obligation registers, policies, controls, training?
7. What interfaces do users actually face?
8. What rules/states govern a change record (review decision categories, deadlines, amendment chains)?
9. What varies by domain (EHS vs financial services vs cross-industry) and by product posture (content-provider vs platform vs suite module)?
10. Where are the hard boundaries vs neighboring Types — what would you have to remove for the product to become that other Type?

## Representative Products

Selected for market representation, documentation quality, differing product philosophy (content-first vs platform-first vs suite-module vs program-tool) and different customer layers:

| Product | Posture | Domain | Customer layer |
|---|---|---|---|
| NAVEX One Regulatory Change Management | GRC/IRM suite module | cross-industry ethics & compliance | enterprise (13,000+ customers claimed) |
| CUBE RegPlatform | end-to-end regulatory-operations platform (ex-regulatory-content house; former Thomson Reuters Regulatory Intelligence web address now serves CUBE) | banking / financial services / insurance / corporates | global enterprise |
| Enhesa | content-provider-first regulatory intelligence platform | EHS, product compliance, chemicals, sustainability | global Fortune 500 (pharma, manufacturing, chemicals) |
| Ncontracts (Ncomply) | compliance-program suite tool with regulatory-change visibility | US banking / credit unions / mortgage / fintech | mid-market & community institutions (5,000+ claimed) |

## Sources

All fetched 2026-09-07:

- NAVEX — Regulatory Change Management product page: https://www.navex.com/en-us/platform/risk-governance/regulatory-change-management/ (plus NAVEX One platform page https://www.navex.com/en-us/platform/). Note: `/en-us/products/regulatory-change-management/` 404s; correct path found via products index.
- CUBE — RegPlatform product page: https://cube.global/products/regplatform (plus products index https://cube.global/products/). Note: `legal.thomsonreuters.com/en/products/regulatory-intelligence` redirected to CUBE during research.
- Enhesa — homepage + solution catalog: https://enhesa.com/ (incl. /solutions/ehs/compliance-intelligence, /solutions/ehs/regulatory-forecaster, /solutions/corporate-sustainability/requirements-center paths referenced from nav).
- Ncontracts — homepage + product navigation: https://www.ncontracts.com/ (Ncomply positioned under "Compliance Management"; direct /products/ncomply URL 404s).

Evidence layer used: official product/marketing pages (Tier 1–2). No client-gated help centers or datasheet PDFs were accessed. Numeric figures below are vendor-published marketing figures, quoted as such.

## Product Observations

### NAVEX One Regulatory Change Management

Evidence: Layer A (official product page, fetched 2026-09-07).

- Vendor's own definition of the process: "monitoring regulatory updates, understanding how they affect your organization and making the necessary changes to policies, controls, procedures, training or reporting."
- Three-stage product structure: **Centralized intelligence** (AI-enabled regulatory alerts filtered to the organization's jurisdictions/areas) → **Structured change execution** ("move relevant alerts into structured change plans with defined owners, next steps and deadlines") → **Audit-ready proof** ("connect each regulatory change to the assessments, actions, policies and controls that show how your team responded").
- Alert supply: "prioritized alerts from 8,000+ vetted regulatory bodies across 197 jurisdictions"; 20 curated data sectors; user selects industry verticals and risk categories; updates "clearly categorized by regulator, jurisdiction and stage of enforcement"; "follow related amendments and repeals without losing context."
- Review decision categories: "Review updates and determine whether they require monitoring, planned action or immediate response" — a tri-state decision. Impact documentation: "Document how the change affects specific business activities and risk measures."
- Response: "Launch structured change plans when action is required, including updates to policies, compliance training and communications"; "Establish defined timelines for completion or next review."
- Evidence trail: "Preserve documented impact decisions associated with the core regulatory change"; "Record response actions taken to address cited requirements and obligations"; "Link change plans to affected policies in NAVEX One Policy & Procedure Management"; "Generate reporting that reflects how specific regulatory updates were implemented."
- FAQ (vendor): "What does regulatory change management software do? — moves regulatory updates through a controlled review and action process. Teams confirm whether an update applies, document impact, assign responsibility and track deadlines… preserve the connection between the regulatory trigger and the response."
- FAQ: RCM vs regulatory compliance — "Regulatory compliance is the outcome… RCM is the process that keeps that outcome intact as rules evolve."
- FAQ: audit readiness — "retains the review decision, assigned owner, implementation timeline and related policy updates tied to each regulatory alert… a consistent historical timeline… without the risk of reconstructing events from scattered records."
- FAQ: cross-functional slowdown — "Legal may need to interpret the update, compliance may need to assess the impact and business teams may need to confirm what the change means in practice."
- FAQ: baseline being replaced — "Compliance officers typically monitor regulator websites, newsletters and horizon-scanning sources, but this becomes difficult to manage manually at scale."
- Suite posture: RCM sits inside NAVEX One; guidance flows into policy management workflows ("eliminating manual handoffs between systems"); AI agent (Nira) across the platform.

### CUBE RegPlatform

Evidence: Layer A (official product pages, fetched 2026-09-07).

- Positioning: "RegPlatform™ is where compliance and risk teams manage regulatory change from end to end. It turns a constant stream of global regulatory change into clear obligations, controls mapped to those obligations, and evidence you can stand behind. From the first sign of a rule change through to audit-ready proof."
- Named end-to-end journey (vendor's own stage names):
  1. **Detect** — "Horizon Scanning tracks regulatory change across every country, territory and published language, surfacing what is material to you in real time" (modules RegInsight, RegTrend).
  2. **Understand** — "Regulatory Inventory and Groups map each change to the entities, jurisdictions and business lines it affects, with the reasoning logged" (RegBook, RegGroup).
  3. **Translate** — "Obligations turns regulatory text into clear, owned obligations, interpreted consistently across Legal, Compliance and the business."
  4. **Validate** — "Mapping and Traceability links every obligation to the controls that cover it, showing coverage and gaps with full lineage" (Compliance Map, Control Mapping).
  5. **Act** — "Risk Control strengthens controls in line with your risk appetite, with clear ownership and peer benchmarking" (RegControl).
  6. **Explain** — "Reporting and Audit give you end-to-end, traceable evidence ready for the Board, auditors and regulators" (RegReport, RegOps).
  7. **Integrate** — "RegConnect delivers structured regulatory intelligence into the platforms you already run through a unified, versioned API, so nothing is re-keyed and every change stays traceable across systems."
- Cross-cutting: "Workflow & orchestration — threads tasks, ownership and approvals through every stage"; "Agentic AI coworkers — work alongside your team at every stage… outputs explainable and evidenced."
- Module list: Records Management, RegBook, RegConnect, RegDashboard, RegFlow, RegGroup, RegInsight, RegMap, RegProfile, RegReport, RegTrend.
- Audiences: banking, financial services, insurance, corporates, partners. Marketing claims "15 years of regulatory data", "peer-validated network intelligence" (peer benchmarking/network data — vendor concept).
- Provenance note: the Thomson Reuters regulatory-intelligence URL redirected to CUBE's site during this research (TR divested its Regulatory Intelligence business to CUBE — corporate history not verified in this pass; the redirect itself is directly observed).

### Enhesa

Evidence: Layer A (official homepage + solution catalog, fetched 2026-09-07).

- Positioning: "The AI-powered regulatory intelligence platform: see every compliance risk in one place, defend every decision, act faster."
- Four compliance domains: Environment, Health & Safety; Product Compliance; Chemicals; Corporate Sustainability.
- Content-first posture: expert-authored content (claimed 450+ jurisdictions, 65+ languages, 160+ in-house experts across 40+ countries, 35+ years), "plain language with the source attached."
- **Applicability**: "AI-powered Applicability — Turn a long list of requirements into the handful that apply to you. Our applicability screening agent cuts hours of manual assessment down to minutes, whilst leaving you in full control."
- **Forward view**: "Regulatory Forecaster — Prepare 12 to 36 months before a change takes effect. AI-powered horizon scanning across 400+ jurisdictions, with an Enhesa-authored impact ranking on every forecast."
- **Obligation register**: "Requirements Center — Give every obligation a named owner and a tracked status. Operative obligations extracted from in-force regulation across 26 domains, assigned across six business functions."
- **Change history behind obligations**: "EHS Legal Foundations — plain-language summaries of every in-force EHS regulation, with change notes and a jump to the exact citation." Compliance-department pitch: "Keep every requirement in one place, with its full history. Amendment records and source links behind each obligation, so you can show a regulator not just what applies today but how it got there."
- **Personalized relevance**: "Regulatory Daily Brief — learns what's relevant to you and your business and surfaces it before you have to go looking, with a plain-language reason why."
- Site-level compliance status ("Compliance Intelligence — find the requirements each site is missing… one corporate view of compliance status across every facility, on a single taxonomy of 400+ jurisdictions").
- Managed/expert services: "Analyst-supported regulatory monitoring, registers build and bespoke research." Enforcement Risk Insights (exposure scoring per requirement).
- AI distribution: "Enhesa MCP — integrate Enhesa's expert validated regulatory intelligence into Claude, ChatGPT, CoPilot or your own agents… grounded with source links and citations."
- Audience: "Half of the Global Fortune 500" (claimed); pharma, manufacturing, chemicals logos.

### Ncontracts (Ncomply)

Evidence: Layer A at product-page level (official homepage + navigation; deeper docs not accessed), fetched 2026-09-07.

- Ncomply is the "Compliance Management" product: "increases your compliance team's visibility to new and changing regulations, empowers them to be change agents, and consolidates much of the Compliance Management System functionality under one roof."
- Features listed: "Compliance AI Agent with Experts Built In" (Nquiry: "cited, auditable answers to complex compliance questions — in minutes, right inside your Ncomply"), "Tailored Regulatory Updates", "Effortless Requirements Builder", "Streamlined Policy Management", "Integrated Complaint Management."
- "Requirements Builder" indicates the update → requirement translation step (same conceptual move as CUBE's Translate and Enhesa's Requirements Center).
- Segment: US banks, credit unions, mortgage lenders, fintechs, wealth management; "5,000+ financial institutions" (vendor claim); case studies reference examiner-facing outcomes (NCUA exams, audit readiness).
- Content supply also exists as a public resource ("Regulatory News" section) — the vendor packages regulatory awareness into the compliance program rather than selling a standalone change tracker.

## Cross-product Comparison

| Dimension | NAVEX One RCM | CUBE RegPlatform | Enhesa | Ncontracts Ncomply |
|---|---|---|---|---|
| Managed object | regulatory alert/change → change plan | change → obligation → control chain | regulatory requirement/obligation w/ change notes | regulatory update → requirement |
| Content supply (A) | vendor-curated alerts, 8k+ sources / 197 jurisdictions / 20 sectors (vendor figures) | horizon scanning "every country, territory, published language" | expert-authored, 450+ jurisdictions (vendor figure) | tailored regulatory updates + expert analysts |
| Applicability judgment (A) | review decision: monitor / planned action / immediate response | mapped to entities/jurisdictions/business lines, "reasoning logged" | AI applicability screening, user confirms | tailored updates by segment/role |
| Response machinery (A) | change plans: owners, next steps, deadlines → policies/training | tasks, ownership, approvals threaded through stages | Requirements Center: named owner, tracked status | Requirements Builder + policy management |
| Downstream linkage (A) | policies (suite policy product), training, controls | controls with coverage/gap lineage | obligation register with amendment history | policy management module |
| Evidence posture (A) | audit-ready proof tied to each alert | end-to-end traceable evidence | "show a regulator… how it got there" | "cited, auditable" answers; examiner-facing |
| Domain | cross-industry ethics/compliance | banking/FS/insurance/corporates | EHS/product/chemicals/sustainability | US banking/credit unions |
| Posture | GRC suite module | end-to-end platform | content-provider-first platform | compliance-program suite tool |
| AI (era-common) | AI-enabled alerts + agent | agentic coworkers per stage | applicability/brief agents + MCP | cited-answer AI agent |

**Cross-product commonalities (Layer B):**

1. Every product centers on **tracked regulatory change as a record** with source attribution, jurisdiction and topic context — not on a generic task or document.
2. Every product makes the **applicability/relevance judgment an explicit managed artifact** (review decision categories, mapped entities/business lines with logged reasoning, screening with user confirmation, tailored delivery).
3. Every product provides **owned, deadline-tracked response machinery** (change plans, workflow/approvals, owned obligations, requirements builder).
4. Every product **links the change to downstream compliance artifacts** — obligations, policies, controls, training — rather than leaving actions free-floating.
5. Every product's headline value claim is **defensibility**: a preserved, retrievable chain from change to decision to response ("audit-ready proof", "evidence you can stand behind", "how it got there", "cited, auditable").
6. Vendor-supplied or vendor-curated **regulatory content** (alerts, horizon scanning, expert summaries) is present in all four — but each also explicitly positions it against the manual baseline (regulator websites, newsletters), indicating the content layer is substitutable in principle.
7. **Categorization machinery** (jurisdiction, regulator, topic/sector, enforcement stage) appears in all four.
8. **Amendment/repeal chains** — connecting later changes to earlier ones and to the living obligation — appear in at least NAVEX, Enhesa, CUBE (RegBook inventory).
9. **Forward-looking dates** (effective dates, horizon scanning/forecasts) appear in all four in some form.
10. **AI assistance** is universal in the current generation (era-common, not definitional).

**Divergences (posture, not structure):**

- Depth of **obligation → control → evidence lineage**: CUBE makes control mapping and gaps a first-class stage; NAVEX links to policies/controls within its suite; Enhesa stops at the owned-obligation register; Ncontracts stays at requirements + policy.
- **Who supplies the regulatory judgment**: content houses sell expert-authored interpretation (Enhesa, CUBE's heritage); suite/program tools lean on vendor expert teams or the customer's own staff.
- **Scope**: cross-industry (NAVEX), financial-services depth (CUBE), EHS/chemical/product (Enhesa), US banking program (Ncontracts).

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which the product is not recognizable as Regulatory Change Management:

1. **Tracked regulatory change record** — an identified change (new, amended, repealed, or forthcoming) to an external legal/regulatory requirement, held as a persistent record with source attribution and jurisdiction/topic context.
2. **Recorded applicability/impact decision** — an explicit, organization-scoped judgment per change: does it apply, to which parts of the organization, and does it warrant monitoring or action; the decision (including "monitor") is a managed, attributable artifact.
3. **Managed response machinery** — the decision drives owned, deadline-tracked actions (update obligations, policies, controls, procedures, training) tied back to the originating change.
4. **Preserved change → decision → response chain** — the linkage is retained as a retrievable evidence trail; this is what distinguishes management software from a news/alert feed plus a separate to-do list.

Removal test:

- Remove #1 → generic project/task management.
- Remove #2 → a regulatory news/alert content service.
- Remove #3 → a compliance reference library or manual; no management.
- Remove #4 → disconnected news feed + task list; the audit-defense purpose collapses.

Historical/market-sample check: pre-software compliance departments ran the same minimal loop — a regulatory-watch binder (bulletins from regulators, Fed/Register reading), a handwritten applicability note per change, a compliance calendar with assigned follow-ups, and an exam binder showing what was done. Paper-era and regional practice fits L0 without vendor feeds, AI, dashboards or control mapping. Vendor-curated content therefore belongs above L0. Historical check passes.

### L1 — Common Mature Structure

Present in most mature modern products (Layer B unless noted):

- vendor-curated regulatory content supply: alert feeds from regulator sources across jurisdictions, with sector/vertical filtering
- categorization by jurisdiction, regulator/authority, topic, and stage (proposed → in force → enforced)
- amendment/repeal chains connecting later changes to earlier records and to living obligations
- maintained obligation/requirement register derived from the change stream, with owned entries and status
- effective-date tracking and forward-looking horizon scanning/forecasting of upcoming changes
- change plans linking updates to policies, training, procedures and (in GRC-integrated products) controls
- management-facing reporting/dashboards; audit/regulator-facing evidence output
- AI assistance: alert filtering/summarization, applicability screening, cited Q&A (era-common)

### L2 — Variant / Optional Structure

- domain scope: cross-industry ethics & compliance; financial services; EHS/chemical/product compliance; sustainability; insurance
- product posture: content-provider-first platform; end-to-end regulatory-operations platform; GRC/IRM suite module; compliance-program tool with change tracking
- depth of obligation → control → evidence lineage (GRC-suite integration)
- managed/expert services layered on the platform (analyst monitoring, register building, helpdesks)
- integration posture: API into systems of record, embedding into LLM/agent ecosystems, suite-native handoffs
- scope of "regulatory" source: laws/regulations/rules from authorities; some adjacent products extend to industry standards/soft-law instruments
- segment/scale: global enterprise vs mid-market/community institutions
- AI depth: filtering/summarization → agentic coworkers → embedded cited-answer assistants

### L3 — Vendor-specific (research notes only)

- NAVEX: 8,000+ alert sources / 197 jurisdictions / 20 sectors figures; named linkage to its PolicyTech policy product; "Nira" AI agent; RCM Playbook resource.
- CUBE: Reg* module naming (RegBook, RegTrend, RegFlow, RegConnect, RegMap, RegProfile, RegOps…); "peer-validated network intelligence" concept; unified versioned API (RegConnect); 15-years-of-data claim.
- Enhesa: 450+ jurisdictions / 65+ languages / 160+ experts / 22,000 major changes in 2025 / 400,000 active requirements figures; Chemical Watch news desk; SDS Author/Manager tools; MCP distribution; Enforcement Risk Insights ROI scoring; "12 to 36 months" forecaster framing; six business functions / 26 domains taxonomy.
- Ncontracts: Nquiry named AI agent; "Experts Built In"; case-study claims (e.g., 33% compliance workload reduction at one credit union); 5,000+ institutions claim.

## Vendor-specific Findings

See L3 above. Additionally: NAVEX and Ncontracts both frame the Type against manual monitoring (regulator websites/newsletters) — useful vendor-validated evidence of the baseline being replaced. CUBE uniquely markets cross-customer "network intelligence" (peer benchmarking); Enhesa uniquely distributes its content into external LLM toolchains (MCP).

## Boundary Findings

1. **vs Compliance Management Platform (§11 sibling, unprocessed at this pass)** — the compliance-management sibling centers on the obligations/activities program of record (the standing state); RCM centers on the change event that alters that state. Evidence: financial-compliance-management pass recorded the same seam from the other side ("change monitoring is an input feed there; RCM centers the change-tracking slice"). Market bundles heavily: Ncontracts sells change visibility inside "Compliance Management"; NAVEX sells RCM as a separate module. Structural test: is the primary record the change event (RCM) or the obligation/activity program (CM)? Remove the change-event center and RCM collapses into Compliance Management.
2. **vs Governance Risk & Compliance Platform (§11 sibling, unprocessed)** — GRC is the umbrella platform spanning risk registers, controls, audits, incidents; RCM is the regulatory-watch slice, most often delivered as a module. Same test as ERM pass recorded for suite vs standalone posture.
3. **vs Policy Management (§10, processed)** — RCM triggers policy reviews and links change plans to policies; the policy corpus and its draft→approval→publication lifecycle is the other system's core. NAVEX explicitly sells the two as connected products. Remove the change-watch and RCM becomes policy management's upstream trigger only.
4. **vs Regulatory Reporting Platform (§08)** — producing filings/data submissions *to* regulators vs managing the internal response *to* regulatory change. Different terminal output.
5. **vs Legislative Tracking Platform (§24 sibling, unprocessed)** — legislative tracking monitors bills/legislation for external/advocacy/government-affairs purposes (inference from directory context; not directly researched this pass); RCM is organization-internal compliance response with owned actions. Remove the internal response machinery and RCM degrades toward a monitoring service.
6. **vs Regulatory Information Management / RIM (§22 sibling, unprocessed)** — life-sciences RIM manages regulatory submissions/dossiers/registrations for products; regulatory intelligence there concerns the product's own filings. Different center of gravity (inference; not researched).
7. **vs regulatory content/news services** — a feed of regulatory updates without applicability judgment and owned response is a content product (Enhesa's news desks, vendor regulatory-news resources). The response loop is the Type's spine: remove #2/#3 from L0 and the product is no longer management software. Enhesa/CUBE demonstrate content houses shipping the workflow; the reverse (workflow tools adding content) is also universal.
8. **vs EHS management / site compliance systems** — Enhesa's Compliance Intelligence (per-site compliance status) shades into EHS management; the change-tracking and obligation-register slice remains RCM's, the site-level inspection/audit/permit machinery belongs to EHS systems (boundary noted, not fully explored).

## Uncertainties

- Exact state taxonomies of a change record beyond NAVEX's tri-state review decision are vendor-specific; no cross-product state model is asserted. CUBE's seven stages are a vendor's journey framing, not an industry-standard state machine.
- Operational depth (fields, statuses, permission models, SLA timers) sits behind client-gated help centers for all four products; evidence is product-page level. No precise operational limits asserted anywhere.
- Whether customers can run the full loop with purely self-sourced changes (no vendor feed) is not directly documented by any sampled vendor; inferred as possible from the vendors' own framing of manual monitoring as the baseline. Kept out of the defining core accordingly.
- CUBE's corporate history (acquisition of Thomson Reuters Regulatory Intelligence) not verified; only the URL redirect observed.
- Legislative Tracking and RIM boundaries rest on directory context plus general market knowledge, not direct research — flagged for the future passes of those leaves.
- Whether "industry standards/soft law" (vs law/regulation) is in-scope for the Type varies; NAVEX markets regulation-specific coverage; standards frameworks appear elsewhere in GRC suites. Held as variant, not invariant.

## Final Synthesis

Regulatory Change Management is the compliance function's change-handling system of record. Its world contains one external input (changes to rules issued by authorities) and four managed structures: the tracked change record, the recorded applicability/impact decision, the owned response machinery, and the preserved chain connecting them. The defining core is deliberately minimal and content-agnostic: vendor-curated feeds, expert interpretation, control-mapping depth, AI agents, and domain-specific taxonomies are common mature structure or variants, not the invariant. The Type holds its own place in the taxonomy because its center of gravity — the change event and the defensible decision/response trail attached to it — is distinct from the obligation program (Compliance Management), the policy corpus (Policy Management), and filings production (Regulatory Reporting), even though the market ships it heavily bundled with all three.

Product-specific checks passed: the four sampled postures (suite module, end-to-end platform, content-first platform, program tool) all satisfy the L0 structure without modification; the historical/paper-era practice also satisfies it.
