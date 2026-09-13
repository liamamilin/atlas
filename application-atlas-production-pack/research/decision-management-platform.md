# Research Notes — Decision Management Platform

Leaf: Decision Management Platform (§10 Enterprise Operations & Administration)
Slug: decision-management-platform
Research date: 2026-09-08
Model: opencode-go/omen-alpha

Joint-review obligation carried from the business-rules-management-system pass (2026-09-07, STATUS.md Boundary Issues): "business-rules-management-system vs decision-management-platform — umbrella-vs-core overlap … candidate outcomes are umbrella+core two-leaf structure (recommended) or alias consolidation. Recommend joint review when decision-management-platform is processed." Discharged below (Boundary Findings #1).

---

## Research Goal

Understand what a Decision Management Platform (DMP) is as an Application Type, from real products: what the central managed artifact is ("the decision"), how decisions are composed (rules, predictive models, strategies), how they are governed and executed, whether decision measurement/improvement is definitional, and where the Type's boundary sits — especially against Business Rules Management System (BRMS, processed sibling), Business Process Management Platform (processed), Credit Decisioning Platform (processed), and Machine Learning Platform / MLOps.

## Initial Boundary (hypothesis before research)

A DMP is an enterprise platform where recurring operational business decisions are managed as first-class, versioned, governed assets: a decision composes executable logic — business rules plus predictive/analytics models — and executes at runtime against transaction/case data, returning outcomes to operational systems, with decision outcomes measured to improve the decision assets continuously.

Nearest types and expected seams:

- BRMS — managed artifact is the rule asset; DMP additionally treats models/strategies/analytics as co-equal managed artifacts (BRMS pass's proposed distinction; to be confirmed).
- BPM Platform — managed artifact is the process model with long-running instances and human tasks.
- Credit Decisioning Platform — credit-domain-specific descendant (bureau data, adverse-action reasons, lending workflows); DMP is domain-generic.
- Machine Learning Platform / MLOps — managed artifact is the model; in a DMP models are inputs to decisions.
- Fraud Detection / AML / Clinical Decision Support — domain solutions; may embed or pair with decision platforms.

## Research Questions

1. What is the central managed artifact, and is "the decision" a named, manipulable, versioned object in real products?
2. What composes a decision — rules, models, code, strategies — and how do the pieces relate?
3. What does the runtime execution loop look like (invocation, evaluation, outcome, trace)?
4. What does the decision change loop look like (authoring → testing → simulation → experimentation → deployment → monitoring → revision)? Is champion/challenger definitional?
5. Is decision outcome measurement/analytics a structural pillar of every sampled product?
6. Who uses the platform (roles), and in which industries?
7. Boundary: DMP vs BRMS (discharge the joint-review flag), vs credit decisioning, vs ML platform, vs BPM.
8. Historical check: would pre-ML-era decision systems (1990s credit strategy management: rules + scorecards + champion/challenger + strategy tracking) satisfy the core?

## Representative Products

Selection principles: market representation across the "decision management/decisioning" naming space; different product philosophies (analytics-suite pole, independent pure-play pole, BRMS-lineage pole, insurance-vertical pole); different customer tiers; documentation reachability.

| Product | Pole / philosophy | Customer tier | Evidence quality |
|---|---|---|---|
| **SAS Intelligent Decisioning** (SAS Viya) | analytics-suite pole; decisions as composed objects beside a full model-management stack | large enterprise (banking, insurance, retail, gov) | Tier 1–2: product page + features list + vendor blog (all fetched) |
| **Sparkling Logic SMARTS** | independent pure-play; analyst-first "data-powered decision manager" | mid-market → enterprise | Tier 1–2: product overview + 3 capability pages (fetched) |
| **InRule Decision Platform** | BRMS-lineage repositioned as "decision platform"; .NET heritage | mid-market → enterprise | Tier 1: official docs glossary (fetched) |
| **Sapiens Decision** | insurance-vertical pole; legacy-code extraction + decision modeling + Decision-as-a-Service | large enterprise (insurance, banking, mortgage) | Tier 2: product page + home page (fetched) |

Boundary-context vendors (not full samples): IBM Operational Decision Manager (BRMS pass — its own page calls it a decision management platform; carried over), FICO Decision Management Suite (the EDM archetype — unreachable, see Source-access Limitation), Pega Customer Decision Hub (unreachable), Provenir/Experian (credit-adjacent pole — covered from the credit-decisioning pass).

## Sources

Fetched 2026-09-08 unless noted:

1. SAS — Intelligent Decisioning product page — https://www.sas.com/en_us/software/intelligent-decisioning.html (fetched OK)
2. SAS — Intelligent Decisioning features list — https://www.sas.com/en_us/software/intelligent-decisioning/features-list.html (fetched OK)
3. SAS Voices blog — "What's in a decision? Four components needed to operationalize your analytics" — https://blogs.sas.com/content/sascom/2025/08/21/whats-in-a-decision-four-components-needed-to-operationalize-your-analytics/ (fetched OK)
4. Sparkling Logic — SMARTS product overview — https://www.sparklinglogic.com/product/ (fetched OK)
5. Sparkling Logic — SMARTS Decision Analytics — https://www.sparklinglogic.com/smarts-decision-analytics/ (fetched OK)
6. Sparkling Logic — SMARTS AI & ModelOps — https://www.sparklinglogic.com/smarts-ai-modelops/ (fetched OK)
7. Sparkling Logic — SMARTS Lifecycle Management — https://www.sparklinglogic.com/smarts-lifecycle-management/ (fetched OK)
8. Sparkling Logic homepage — https://sparklinglogic.com/ (fetched OK)
9. InRule — Decisioning Glossary (official docs) — https://docs.inrule.com/docs/inrule-decisioning-glossary (fetched OK)
10. Sapiens Decision — product page — https://sapiensdecision.com/product (fetched OK)
11. Sapiens Decision — home page — https://sapiensdecision.com/ (fetched OK)

Carried over from sibling passes (not re-fetched): research/business-rules-management-system.md (IBM ODM product page fetched 2026-09-07; Corticon; SMARTS rules/lifecycle pages; InRule docs), research/credit-decisioning-platform.md (FICO unreachable there too; Provenir/Taktile domain-generic observation), applications/business-rules-management-system.md, applications/credit-decisioning-platform.md.

### Source-access Limitation

- **FICO (fico.com)** — transport errors on both attempted URLs (2 failures). The EDM/decision-management archetype vendor (Decision Management Suite, Blaze Advisor heritage) is therefore evidenced only indirectly (through the credit-decisioning pass's boundary notes and the BRMS pass). No FICO-specific structure is asserted anywhere.
- **Pega (pega.com, docs.pega.com)** — 403 on both attempts (2 failures). Pega's "decisioning / next-best-action / adaptive models" pole is noted as market context from prior knowledge only where explicitly flagged as unverified; no Pega-specific claim is made.
- **Provenir** — /product/ 404; not retried (credit pole already covered by the processed credit-decisioning pass).
- Precise vendor marketing figures (SAS: "7,000 transactions per second", "5–10 milliseconds") observed on the SAS features page are recorded here as vendor claims only and are deliberately NOT carried into the final document.

## Product Observations

### SAS Intelligent Decisioning

Evidence layer A unless noted.

- Self-definition: "cloud-based software that combines AI, machine learning, and business rules to automate thousands of operational decisions every day… delivers the right action in real time" (product page).
- Vendor concept decomposition (blog): enterprise decisioning = "automated, repeatable, rules-based decisions powered by data and analytics, combined with business processes, protocols and policies"; a decision integrates four pieces — data, models, governance, business rules — in one environment (blog; layer A vendor-framing).
- **Decision builder**: low-code drag-and-drop UI to "assemble decisions using business rules, custom code and analytics"; decisions defined by "browsing centralized data, model and business rule repositories and selecting from existing assets"; conditional branching logic (Yes/No, Equal, Range, Like) with outputs from any preceding step; built-in version control for entire decision flows; where-used reports (features list).
- **Rules management inside the platform**: "Integrated business rule management platform", rule version management, common rule repository for reuse, lookup tables — a complete BRMS core inside the decisioning product (features list).
- **Models as first-class inputs**: deep linking from decision flow to model repository in SAS Model Manager; SAS models + Python + open-source models executed natively; governance workflows applied to models through Model Manager (features list). Model Manager is a separate Viya product — the DMP composes, does not own, the full model lifecycle.
- **Decision testing**: test cases from multiple sources with data mapping; scenario tests with expected results; "autogenerated validation test… resembles the chosen deployment destination"; common environment for testing, change management, auditing, validation (features list).
- **Governance workflows**: approval pathways from a single location; graphical representation of the decisioning life cycle and parties; comments/labels documenting each stage; audit history of decisioning workflows; publish decisions to Git for DevOps integration (features list).
- **Decision analysis / traceability**: "explicit and detailed rule-fire analysis"; graphical analysis of decision paths for development and production; trace information persisted in production for audit; decision variables persisted for "decision improvement" (features list).
- **Performance monitoring automation**: performance reports/notifications; "Automatically retrain analytical models when they decay"; "Swap champion with challenger models based on thresholds"; end-to-end model management automation (features list).
- **Strategy improvement** (named feature group): "Perform champion/challenger model comparisons"; simulation options; lineage/impact analysis of components; response history; "Strategy performance monitoring and reporting with SAS Visual Analytics" (features list).
- **Deployment**: real-time REST (SAS Container Runtime OCI containers; micro analytic service), batch (cloud analytic services), in-database, in-stream/IoT (features list).
- Users (FAQ): "data scientists, business analysts, risk teams and IT teams"; industries: banking, insurance, retail, telecom, government (FAQ).
- Customer stories on the page: credit decision automation (Nexent Bank, VietCredit, S-Bank), supply-chain/IoT anomaly decisions (Georgia-Pacific) — cross-domain breadth (layer A page-level).
- Analyst category: "Gartner® Magic Quadrant™ for Decision Intelligence Platforms, 2026 — Leader" (product page; layer A for category naming).

### Sparkling Logic SMARTS

Evidence layer A unless noted.

- Self-definition: "all-in-one business rules and decision management platform designed for business analysts to quickly automate and continuously improve complex operational decisions"; tagline "More than a rules engine" (product overview). Homepage testimonial frames it as "the best decision management platform… rules engine of choice" (layer A page-level).
- Product pillars as structured navigation: Rules Authoring; Low-Code No-Code; AI & ModelOps; Decision Analytics; Lifecycle Management; Technical Architecture; AI Assistant (site-wide nav; A).
- **Rules authoring**: author/test rules against data without code; DMN-standard decision modeling ("Model decisions (using DMN standard) as you gather requirements"); decision flows (product page + carried-over rules-authoring pass context).
- **AI & ModelOps**: "Operationalize data science models" — import Python models; import ONNX/PMML from external platforms (SAS, SPSS, R); invoke external model services; build models in-platform (BluePen: data explorer, technique selection, interactive decision trees, fairness metrics e.g. disparate impact, explainability e.g. SHAP); "Manage model and decision lifecycle in one place"; monitor model performance, drift alerts, automate retraining and replacement (AI & ModelOps page).
- **Decision Analytics**: "Monitor and measure decision outcomes through customizable dashboards, simulations, and alerts"; "Build fully-integrated dashboards to measure decision quality"; "Run simulations, shadow and champion/challenger experiments" (screenshot caption: "60-20-20 split among Champion, Aggressive, and Conservative strategies"); "Monitor decisions and models in real-time and trigger alerts"; KPIs monitored in testing and live environments (Decision Analytics page).
- **Lifecycle management**: decision governance across environments; control who can view/edit/test/deploy decision logic; versioning and release management; "read-only" releases for QA; one-click rollback; configurable lifecycle workflows ("Orchestrations" automating user interactions, decision logic, decision-management and deployment tasks); discussion boards, activity stream, task review of "the new underwriting strategy" (Lifecycle Management page).
- Use cases (product page footer): "modernize your loan origination system, rating engine, or product configurator"; blog series covers pricing engines, insurance rating, fraud, state-aid management, component distribution — cross-industry breadth (layer A page-level).
- Equifax customer story: SMARTS as the engine of Equifax's "interconnect decision management platform" for 6+ years (homepage; A page-level).
- Explainability is a named theme (blog series title "Explainability in Decision Management"; AI Assistant "Generate explanations for decision logic").

### InRule Decision Platform

Evidence layer A (official documentation).

- Platform definition (glossary): "Decision Platform refers to the tools and services we offer to author, manage, store, and execute automated decisions. It includes irAuthor and Author Studio for building rule applications, irCatalog for storing and versioning them, and irVerify for testing. At runtime, the platform uses Decision Services and the Rule Execution API… the full lifecycle of decision logic from authoring through deployment and execution."
- **Decision as a named object**: "Decision — A named entry point for running logic. A decision has inputs, executes rules, and returns outputs." Decision Flow — "A visual model for describing the sequence of logic in a decision." Decision API — REST execution of decisions and rule sets (glossary).
- **Rule application** as the packaged asset: "a package that contains the logic, data structures, and configuration needed to evaluate business decisions… entities, fields, rule sets, rules, notifications, actions"; stored in irCatalog with versioning; CI/CD promotion through dev/test/prod (glossary).
- **Rule semantics**: rule sets with fire modes (auto-optimized, auto-sequential, auto single pass, explicit) and execution types — full conflict/ordering machinery (glossary; consistent with BRMS pass's rule-semantics finding).
- **Decision analytics as a platform component**: "InRule Metrics — the component of the platform that provides analytics or measurement capabilities for decision logic, for example, tracking executions, outcomes, and performance of rule applications over time… KPIs that can be tracked during rule execution"; Rule Execution Log records "rule firings, field changes, and notifications" (glossary).
- **Model surface**: docs navigation includes an "ML Studio" section (model training/integration surface) — present but NOT examined in depth this pass (thin evidence; layer A for existence only).
- Endpoints to external systems (databases, email, queues, web services) as the integration mechanism (glossary).
- Observation: a BRMS-lineage product whose managed artifact vocabulary is "decisions" and which ships a named decision-measurement component — supports the seam hypothesis that the DMP = rule core + decision-asset framing + measurement layer.

### Sapiens Decision

Evidence layer A (product pages) with layer-B marketing caution.

- Self-definition: "End-to-end business logic management capabilities from legacy code extraction to decision modeling with no code tools, and deployment through Decision-as-a-Service" (product page).
- Three-stage structure: **Extract** (Automated Logic Extraction — AI extracts business logic from legacy code into "technology independent decision models"), **Model** (Decision Manager — "analysts to validate, model, test, and govern logic, before generating performant code"; no-code visual modeling workbench "powered by The Decision Model"; in-line testing; business glossary; enterprise governance with approval workflows and traceability), **Deploy** (Decision Execution — hot deployment, "Decision-as-a-Service with OpenAPI", "full traceability from model to code and back again", "Analytics on business logic usage and traceability") (product page).
- Value framing: "Translating policy to code quickly and accurately"; "manage same-day rule changes using intuitive no-code tools" (home page).
- Industries: insurance, banking & capital markets, mortgage; logo wall of large carriers/banks (home page).
- Analyst quote on home page: "Decision Management solves the challenge of operationalizing AI and Machine Learning" (Aite-Novarica analyst, quoted on the vendor's page — layer A for the vendor's positioning, layer B for the claim).
- Analyst category: "Named as a Visionary in the Gartner Magic Quadrant™: Decision Intelligence Platforms" (home page, inaugural MQ — A page-level).
- Marketing performance figures (5–30x speed, 70–90% efficiency) — vendor claims, not carried.

### Carried-over context (sibling passes)

- **BRMS pass (2026-09-07)**: established that IBM ODM's own product page calls it a decision management platform; Sparkling Logic SMARTS calls itself a decision management platform; InRule calls itself a decision platform; and "every 'decision platform' sampled still contains a complete BRMS core (authoring/repository/engine)". Its STATUS boundary entry proposed: BRMS managed artifact = rule asset; DMP additionally treats predictive models/strategies/decision analytics as co-equal managed artifacts. Recommended umbrella+core two-leaf outcome.
- **Credit Decisioning pass (processed)**: Boundary finding — "vs Business Rules Management System / Decision Management Platform: those are domain-generic decision automation (Taktile and Provenir both serve non-credit decisions — insurance, AML, onboarding). The credit instance is defined by credit data integration, credit-decision outputs with adverse-action reasons, and lending-workflow governance. Test: remove the credit domain → generic decision platform." Also documented FICO as the classic enterprise rules/decision heritage and fico.com as unreachable.
- **BPM pass (2026-09-07)**: BPM's central managed artifact = governed versioned engine-executed end-to-end process model with instance state/history; decision/rules layers are standard capabilities inside BPM suites (the seam is which artifact is primary).

## Cross-product Comparison

| Structure | SAS Intelligent Decisioning | Sparkling Logic SMARTS | InRule Decision Platform | Sapiens Decision |
|---|---|---|---|---|
| Decision as named, versioned, manipulable asset | ✓ decision flows, version control, where-used | ✓ decision flows/assets, versioning, releases | ✓ "decision = named entry point"; rule applications versioned | ✓ decision models (The Decision Model), versioned governance |
| Business rules as core logic form | ✓ integrated rule management | ✓ rules authoring pillar | ✓ core | ✓ business logic/rules + glossary |
| Predictive models integrated into decisions | ✓ SAS/Python/open-source, model repository deep-link | ✓ Python/ONNX/PMML/external services; in-platform models | ✓ ML Studio present (thin evidence) | ✓ AI/ML integration named at deploy stage |
| Governed versioned lifecycle independent of app releases | ✓ governance workflows, Git publish | ✓ lifecycle pillar, roles, releases, rollback | ✓ irCatalog + CI/CD | ✓ approval workflows, traceability |
| Testing / simulation before deployment | ✓ test cases, validation tests | ✓ simulations, shadow runs | ✓ irVerify | ✓ in-line testing |
| Champion/challenger or live experimentation | ✓ champion/challenger comparisons + threshold-based champion swap | ✓ simulations, shadow, champion/challenger experiments | not observed in examined pages | not observed in examined pages |
| Decision outcome measurement / analytics | ✓ "Strategy improvement" group; strategy performance monitoring | ✓ Decision Analytics pillar (decision-quality dashboards) | ✓ InRule Metrics (executions/outcomes/KPIs) | ✓ analytics on business logic usage |
| Explainability / execution traceability | ✓ rule-fire analysis, persisted production traces | ✓ explainability theme, audit | ✓ rule execution log | ✓ full traceability model↔code |
| Runtime posture | REST/container, batch, in-database, in-stream | cloud-native runtime (architecture page) | Decision API/SDK/JS runtime | Decision-as-a-Service (OpenAPI) |
| Industry breadth | credit, fraud, retail, supply chain/IoT, gov | pricing, rating, loan origination, underwriting, public sector | mid-market enterprise, .NET estate | insurance, banking, mortgage |
| Analyst-category naming | Gartner MQ Decision Intelligence Platforms (Leader) | — | — | Gartner MQ Decision Intelligence Platforms (Visionary) |

Reading of the matrix:

- **4/4**: decision as managed versioned asset; rules as core logic form; governed lifecycle; testing/simulation; outcome measurement; traceability. (InRule's model-integration cell is thin but present.)
- **2/4** (both analytics-first products): champion/challenger experimentation — common, not definitional.
- InRule shows the gradient: it is a BRMS whose platform vocabulary and component set have grown the decision-object framing plus a metrics component — evidence that BRMS and DMP are core-and-umbrella, not disjoint markets.

## Canonical Model

### L0 — Defining Invariant (minimal; remove any leg → different Type)

1. **The decision as a managed asset composed of decision logic.** The central artifact is a named, versioned decision definition that composes executable logic from multiple technique types — business rules (universal core form) and predictive/analytics models as co-equal, first-class inputs (remove the model leg → BRMS; remove the managed-asset leg → an engine/library).
2. **A governed decision lifecycle independent of application releases.** Decision assets are authored, tested, approved, promoted and versioned through their own change management; consuming applications are not re-released when decisions change (remove → hard-coded logic; the "management" leg).
3. **Runtime decision execution for operational systems.** Decisions execute against the facts of individual transactions/cases and return actionable outcomes to invoking applications (API/service/embedded) (remove → design-time modeling or analytics tooling with no operational loop).
4. **The decision measurement loop.** Executed decision outcomes are captured and analyzed (decision performance/quality monitoring), and decision assets are revised on that basis — the closed improvement loop that makes it "decision management" rather than a decision engine (remove → a rules/decision engine with no improvement loop).

Jointly-held: the four legs are load-bearing. (1) alone = model/repo tooling; (1)+(3) without (2)+(4) = decision engine; (2)+(3) without (1)'s composition and (4) = BRMS; (4) without (2)+(3) = analytics/monitoring without operational decisions.

Historical/market-sample check (§24-style): 1990s–2000s credit strategy management systems (policy rules + scorecards + strategy trees + champion/challenger testing + strategy performance tracking, executed per application) satisfy all four legs without any modern cloud/AI machinery — the analytics-vendor lineage confirms legs are not era-bound. Bare expert-system shells / rule-engine libraries fail legs 2 and 4 (components, not platforms) — consistent with the BRMS pass's treatment of engines as building blocks. Legacy policy-to-code platforms (Sapiens's own framing) satisfy the legs with rules-only logic plus a model-integration surface — the leg is the co-equal treatment of models, not their mandatory use in every deployment.

### L1 — Common Mature Structure (very common; not defining)

- Visual decision authoring: decision flows/orchestration canvases, decision tables, business-language rules, DMN-style decision models; low-code/no-code posture for analysts.
- Testing & simulation suites as promotion quality gates; validation environments resembling production deployment.
- Champion/challenger and shadow experimentation on live traffic; simulations on historical data.
- Decision analytics dashboards: decision volumes, outcomes, KPIs, decision-quality measures, real-time metrics and alerts.
- Model lifecycle adjacency: model import (Python/ONNX/PMML), external model services, drift monitoring, retrain/swap automation — often via a companion model-management product.
- Explainability and traceability: rule-fire/decision-path traces, persisted production traces, audit histories.
- Data orchestration: bindings to enterprise data sources, lookup tables, external service invocation from decision logic.
- Environment promotion machinery: repositories, read-only releases, one-click rollback, CI/CD/Git publishing.
- Governance roles: who may view/edit/test/approve/deploy decision assets.

### L2 — Variant / Optional Structure

- Packaging spectrum: module of an analytics suite (SAS Viya) ↔ independent pure-play platform (SMARTS) ↔ BRMS-lineage platform (InRule) ↔ vertical-tuned platform with legacy-extraction services (Sapiens for insurance).
- Industry tuning: credit/origination, insurance rating/underwriting, fraud, pricing, eligibility, supply-chain/IoT anomaly decisions.
- Deployment posture: SaaS/cloud-native containers, managed servers, embedded SDK/JS runtimes, batch, in-database, in-stream/edge.
- Experimentation depth: none / simulation-only / full champion-challenger arbitration.
- Authoring philosophy: analyst-first no-code vs developer-first code-form logic.
- Decision-model standard: proprietary models (The Decision Model) vs DMN support.
- Optimization modules (mathematical optimization inside decisions): present in the archetype vendor's suite per market context — unverified this pass (source unreachable).
- Adaptive/real-time learning decisioning (next-best-action pole): market context — unverified (source unreachable).
- GenAI assistance for authoring/explanation (SMARTS AI Assistant) — era-current, single-product observed.

### L3 — Vendor-specific (kept out of the final document)

- SAS: Decision Builder, SAS Container Runtime, micro analytic service (MAS), CAS batch, SAS Model Manager linkage, Power Platform connector, published tps/latency figures.
- Sparkling Logic: SMARTS "Washington" release, BluePen (fairness/explainability model builder), RedPen, Orchestrations, activity streams/to-dos, Equifax interconnect engine story, 60-20-20 champion/challenger split example.
- InRule: irAuthor, Author Studio, irCatalog, irVerify, irSDK, irScript, fire modes (auto-optimized/auto-sequential/auto single-pass/explicit), Rule Execution API lineage, InRule Metrics, ML Studio.
- Sapiens: Automated Logic Extraction (ALE), Decision Manager (DM), Decision Execution (DE), The Decision Model, POJO code generation, "Logic Unleashed" framing.
- Carried over: IBM Decision Center/Decision Server; FICO Blaze Advisor/Decision Modeler/Optimizer naming (from sibling passes; FICO itself unreachable).

## Boundary Findings

1. **vs Business Rules Management System — JOINT REVIEW DISCHARGED (from this side).** Confirmed from the DMP sample: every sampled decision platform contains a complete rule-management core (SAS "integrated business rule management platform"; SMARTS self-described "business rules and decision management platform"; InRule is BRMS-lineage; Sapiens manages business logic/rules with glossary+traceability). The observable seam matches the BRMS pass's proposal: **the managed artifact**. In a BRMS the central managed asset is the *rule* (condition→action unit); in a DMP the central managed asset is the *decision* — a versioned composition of rules, models, and other logic — and the platform additionally treats predictive models as co-equal assets and closes the loop with decision-outcome measurement (L0 leg 4). Removal tests both ways: remove model composition + measurement loop from a DMP → a BRMS remains; add a decision-composition layer + models + outcome measurement to a BRMS → a DMP. **Ratified outcome: umbrella+core two-leaf structure** (the BRMS pass's recommended option): both leaves stand; BRMS = rules-centric core Type; DMP = broader decision-lifecycle Type whose change loop runs through measurement. Products sit on a real gradient (InRule between the poles); neither leaf is an alias of the other. Alias consolidation is rejected because pure-play DMPs (SMARTS; SAS Intelligent Decisioning as packaged) exist and are marketed primarily on the decision/analytics layer, not the rule layer.
2. **vs Credit Decisioning Platform (§08, processed).** Confirms that pass's seam from this side: credit decisioning is a domain-specific descendant whose managed artifacts are credit applications and credit decisions with adverse-action machinery, bureau data integration, and lending-workflow governance; the DMP is domain-generic (SAS cross-domain use cases; SMARTS pricing/rating/origination; Equifax uses SMARTS *as* the engine inside a credit-adjacent platform). Test: remove the credit domain machinery → generic decision platform. Consistent both directions.
3. **vs Business Process Management Platform (§10, processed).** Artifact seam: BPM's central managed artifact is the governed end-to-end *process model* executed as long-running instances with human task allocation; the DMP's artifact is the *decision*, executed in short evaluation invocations. BPM suites embed rules/decision layers (BRMS/BPM passes both observed); the seam is which artifact is primary. No change to either leaf.
4. **vs Machine Learning Platform / MLOps (§13).** The ML platform's managed artifact is the model (training, registry, deployment, monitoring); the DMP's managed artifact is the decision that *consumes* models. SAS demonstrates the pairing (Model Manager is a separate Viya product; Intelligent Decisioning composes model outputs into decisions); SMARTS's AI & ModelOps pillar exists to operationalize models *into* decisions. Products in the DMP sample do not train models from scratch as their purpose.
5. **vs Approval Workflow Platform / Workflow Management (§10).** Human-decision routing vs automated decision evaluation: approval platforms record attributable human approve/reject decisions in defined paths; the DMP produces automated outcomes from logic. An approval threshold implemented as a rule is DMP output consumed by a workflow (consistent with BRMS doc).
6. **vs domain decision engines (fraud detection, AML, clinical decision support, underwriting workbenches).** Domain platforms' managed artifacts are domain records (transactions, alerts, patients, risk items); they may embed or pair with a DMP. The DMP's managed artifact is the generic decision asset serving many applications and use cases.
7. **Naming drift (recorded for taxonomy maintainers).** The analyst category is being renamed "Decision Intelligence Platforms" (Gartner inaugural MQ, 2026; SAS Leader, Sapiens Visionary page-claims). The directory leaf name "Decision Management Platform" corresponds to the same market (vendors' own terms: decision management platform, decision platform, decisioning platform, decision automation). No taxonomy change proposed; leaf name retained.

## Uncertainties

1. FICO Decision Management Suite (the archetype) could not be fetched; its suite composition (rules + modeler + optimizer + central analytics) is market context from sibling passes and general knowledge, not direct evidence. The L0 does not depend on it (4/4 sampled products carry the core), but the "optimization module" variant is unverified.
2. Pega's next-best-action/adaptive-models decisioning pole is unverified; whether adaptive learning should be an L2 variant or a separate Type is therefore left open (no claim made).
3. InRule's model-integration depth (ML Studio) is evidenced only by docs navigation; the model leg of the L0 rests on SAS + SMARTS (strong) + Sapiens (page-level) + InRule (existence-only).
4. Champion/challenger is 2/4 in the sample (both analytics-first products); held L1. Its historical centrality to credit strategy management supports "signature capability", but single-source caution prevents promotion to the defining core.
5. Whether an organization using a DMP purely for rules-based logic (no models deployed) is "still using a DMP" is a deployment-level question; the L0 captures the platform's structure (models are first-class assets), not every deployment's usage.

## Final Synthesis

The Decision Management Platform is the decision-lifecycle Type of the enterprise decision-automation family. Its defining core is four jointly-held structures: (1) the decision as a governed, versioned asset that composes decision logic — business rules plus predictive models as first-class inputs; (2) a decision lifecycle that changes decisions without application releases; (3) runtime execution of decisions against individual transactions/cases returning outcomes to operational systems; (4) a measurement loop that captures decision outcomes and feeds them back into revising the decision assets. Everything else commonly seen — visual authoring studios, testing/simulation suites, champion/challenger experimentation, analytics dashboards, model-drift automation, explainability traces, DMN, GenAI assistance — is standard capability or variant. The Type sits above the BRMS (whose managed artifact is the rule asset) as the umbrella in which rules are one technique among several; it is domain-generic, with credit decisioning, fraud, pricing, and rating engines as domain-specific descendants or downstream deployments. The joint-review flag with business-rules-management-system is discharged: keep-both, umbrella+core, ratified with the seam held on the managed artifact + measurement loop.
