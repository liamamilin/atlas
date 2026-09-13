# Research Notes — Synthetic Data Platform

Research date: **2026-09-09** · Leaf: §13 Data, Analytics & AI Systems · Slug: `synthetic-data-platform`

## Research Goal

Understand what a Synthetic Data Platform actually is as an Application Type: what objects exist inside it, what its core production loop is, how quality/privacy are handled, how the "learned-from-real-data" and "designed-from-rules" poles relate, and where its boundaries run against Data Labeling, Test-Data/Environment Management, Data Quality, anonymization tooling, mock-data generators, and synthetic-media (imagery) platforms.

## Initial Boundary

- Hypothesis: a platform that generates artificial-but-realistic datasets so work can proceed where real data cannot be used (privacy/compliance, data access, test coverage, ML training).
- Likely neighbors: Data Labeling Platform, Database Dev/Test Environment Manager, Data Quality Platform, Data Catalog/Data Exchange, Machine Learning Platform, AI Model Evaluation Platform.
- Key tension noticed up front: some market products "train a model on real data" (statistical/learned pole), others explicitly never touch production data and generate from designed rules (deterministic pole). Both are marketed as synthetic data platforms. The definition must span both without collapsing into either.

## Research Questions

1. What are the core objects? (generator/model, source data, metadata/spec, synthetic dataset, evaluation report, connectors)
2. What is the canonical workflow? (connect/define → build generator → generate → evaluate → deliver)
3. How is the generator realized? (deep generative models, classical statistics, deterministic rule engines, LLM-based)
4. How is output quality measured? (fidelity metrics, diagnostics, validity/integrity checks, privacy assessment)
5. What delivery surfaces exist? (web app, SDK/API, writeback to databases/environments)
6. Who are the users and what jobs dominate? (ML training vs test data vs privacy-safe sharing)
7. Where are the boundaries vs labeling, TDM/environment managers, data quality, masking, mock-data generators, and synthetic imagery?

## Representative Products

| Product | Pole / philosophy | Customer level | Sources reached |
|---|---|---|---|
| MOSTLY AI | AI-generated (sample-based) synthetic data, privacy/GDPR-led enterprise platform + Apache-2 SDK | Enterprise (banks, telecom) + individual SDK | mostly.ai root, /synthetic-data-basics (Layer A) |
| Tonic.ai (Structural / Textual / Fabricate) | Dev/test-data-centric: de-identification + subsetting + synthesis; Fabricate = from-scratch synthesis | Engineering teams, enterprises; self-hosted or cloud | docs.tonic.ai (Layer A, Tier 1) |
| SDV (DataCebo) | Open-source Python library; statistical synthesizers; research lineage (MIT DAI Lab 2016) | Individual data scientists → enterprise tier | docs.sdv.dev (Layer A, Tier 1) |
| GenRocket | Design-driven, deterministic test-data generation; "No production data touched. Ever." | Global 2000 enterprise, GSI-delivered | genrocket.com (Layer A, Tier 2) |
| Gretel | Developer API-first synthetic data | Developer/startup→enterprise | gretel.ai redirects to NVIDIA (acquisition); docs.gretel.ai unreachable (×2 transport errors) — **not sampled**, market fact only |

Rejection note: Hazy (transport error ×1), yData docs (JS shell, no content) — abandoned per network rules. No claims made about them.

## Sources

- https://mostly.ai/ and https://mostly.ai/synthetic-data-basics — fetched 2026-09-09
- https://docs.tonic.ai/ , /app/readme.md , /app/readme-1/tonic-workflows.md — fetched 2026-09-09
- https://docs.sdv.dev/sdv/ , /get-started.md , /evaluation/diagnostic.md — fetched 2026-09-09
- https://www.genrocket.com/ — fetched 2026-09-09
- https://www.gretel.ai/ — redirects to NVIDIA product page (title "Synthetic Data Generation for Agentic AI | Use Case | NVIDIA"); docs.gretel.ai unreachable — recorded as market-consolidation evidence only

## Product Observations

### MOSTLY AI (evidence layer A unless noted)

- Homepage self-positioning: "The MOSTLY AI Data Intelligence Platform" — four data categories: **Real-World Data** (AI assistant over production data), **Mock Data** (rule-based, "no real sample required", "low realism"), **Synthetic Data** ("high-fidelity, privacy-safe datasets that mimic real data"), **Simulated Data** (edge cases / what-if scenarios).
- Synthetic Data SDK (Apache v2): `mostly.train(data=...)` → **Generator** object → `g.reports()` → `mostly.probe(g, size=…)` → seeded generation `probe(g, seed=[{'age': 65, 'gender': 'male'}])` → `g.export_to_file()`. Generators exportable and uploadable to the platform. "Your data never leaves your environment."
- Basics page taxonomy (their own, Tier 1-adjacent): **AI-Generated (sample-based)** — trained on real datasets, preserves statistical properties; **Mock Data (rule-based)** — templates/rules/randomness, low realism; **AI-Generated Mock (LLM-based)** — prompt-driven, "lacks statistical grounding".
- Workflow named as **Train → Generate → Protect → Validate**. "Protect: no one-to-one links to real subjects; re-identification risks are eliminated by privacy protection features." "Validate: automated QA checks utility and similarity; prevent overfitting and leakage."
- "Each created Generator by MOSTLY AI comes with an automated Model Insight Report."
- Positioning vs masking/pseudonymization: synthetic data "created entirely from scratch… no one-to-one relationships between synthetic records and real individuals"; pseudonymized data "is still personal data" (GDPR framing, EU vendor).
- Use cases enumerated: AI training, analytics, testing & QA, demos/prototypes, explainable-AI stress testing. Customer stories: Swiss Post (synthetic customer base), Erste (UAT data), JPMorgan sandbox, Databricks clean rooms.
- Enterprise deployment: Kubernetes/OpenShift, run on your compute. Newer platform framing: "Data for Everyone", agentic data science (2025+ merger note: "powered by Syntho").

### Tonic.ai (evidence layer A, Tier 1)

- Three products in one company: **Structural** ("De-identify, subset, and synthesize structured and semi-structured data"), **Textual** ("De-identify, redact, and synthesize unstructured data, free-text, and files"), **Fabricate** ("Synthesize relational data, free-text, and mock APIs from scratch").
- Structural user guide: "creates safe, realistic datasets to use in staging environments or for local development… used by engineers, data analysts, or security experts."
- Data flow: source database (PII/PHI) → transforms sensitive values → writes to destination (database, storage location, container repository).
- Core objects (Tier 1): **Workspace** ("contains the data connections and data generation configuration"), **Data connectors** ("read from and write to a specific type of data source"), **Privacy Hub** ("current protection status based on the sensitivity scan and workspace configuration"), **Database View** (configure transformations per table/column), **Generators** ("A generator is assigned to a column and performs a data transformation" — note: per-column transformer, different vocabulary from SDV/Mostly's whole-model "generator"), **Subsetting**, generation **jobs**, **schema changes** review.
- Workflow (Tier 1): (1) create workspace with source+destination connections; (2) analyze **sensitivity scan** results ("identifies columns that contain sensitive data… need to be protected by a generator"); (3) configure: **table modes** ("controls the number of rows and columns that are copied"), column sensitivity flags, column generators ("replaces the source value with a different value… scramble the characters or assign a random value of the same type"); (4) run **data generation job**, track progress, view results.
- Also: Structural Agent (AI chat), Structural API, self-hosted instance management, user access management.

### SDV / DataCebo (evidence layer A, Tier 1)

- "The Synthetic Data Vault (SDV) is a Python library designed to be your one-stop shop for creating tabular synthetic data." Created at MIT's Data to AI Lab 2016; DataCebo founded 2020; "the largest ecosystem for synthetic data generation & evaluation."
- Key features: **Train your own generative AI model** ("single table, sequential, or multi-table (relational)"; "designed to work on-prem, with standard CPUs"); **Evaluate & visualize** ("measure the statistical quality… diagnose problems… compare synthetic with real"); **Customize** ("add constraints, adjust preprocessing, selecting anonymization options").
- Workflow (Tier 1): **Data Integration** (connect DB or load file; create **metadata object** describing the data) → **Modeling** (create a **synthesizer**, learn patterns; "The patterns are saved in a synthesizer object… a model that contains a condensed representation of your data") → **Sampling** ("generate realistic synthetic data on-demand. Or supply instructions to your synthesizer to create specific types of data"; export to file or database) → **Evaluation** ("comparing it against the real data… basic diagnostic stats… statistical quality… visualize differences").
- Synthesizer family named: Gaussian Copula ("fast, customizable, transparent"), CTGAN ("GAN-based… high fidelity"), PAR ("sequences"), HMA ("multi tables… connected tables in a database").
- Customizations: "Custom Processing & Anonymization"; "Constraint-Augmented Generation — input business rules into your synthesizer using constraints. This ensures high-quality, valid synthetic data, 100% of the time."
- Diagnostic Report (Tier 1): Data Validity (PK uniqueness/non-null, min/max boundary adherence, category adherence, regex-format IDs, datetime formats), Structure (same column names), Relationship Validity (multi-table: cardinality ranges, referential integrity). "We expect the score to be a perfect, 100%." Plus quality report and visualization utilities; SDV Enterprise upsell for scale/quality/deployment.

### GenRocket (evidence layer A, Tier 2 marketing — product-structural claims only)

- Self-positioning: "The Future of Test Data Management & Generation"; "Transform from legacy TDM to Design-Driven Synthetic Data… **No production data touched. Ever.**"
- "Design-Driven Synthetic Data means you don't copy data—you design it. Define the structure, rules, and scenarios you need, and generate high-quality data instantly, without relying on production systems."
- Explicit philosophy contrast: "**Deterministic — Highest quality data, not Probabilistic**"; 750+ data generators; 125+ data formats; US patent (#9,552,266 B2) "for systems and methods for data generation" incl. "test data generation with referential integrity".
- Capability areas named: Data Masking ("Sensitive (PII) data is never looked at or stored — it's synthetically replaced"), Data Subsetting, Data Orchestration ("subsets and synthetic data sets orchestrated to one or many test environments in parallel, on demand"), Data Profiling ("16 methods to automate data modelling using metadata"), TDM Self-Service (G-Portal requests, G-Questionnaire permutations), AI/ML Training Data ("production data for training ML can be biased, contain sensitive data or not available"), Pipeline/CI-CD integration ("right data, at the right time, in the right place"), Platform Management, accelerators (X12 EDI healthcare, banking, COTS/Salesforce).
- Users implied: QA/dev/test teams at enterprise scale, delivered via global system integrators.

### Gretel (market fact only — not sampled)

- gretel.ai redirects to NVIDIA ("Synthetic Data Generation for Agentic AI | Use Case | NVIDIA"); docs.gretel.ai unreachable (transport error ×2). Recorded as market consolidation; no product-internal claims made.

## Cross-product Comparison

| Structure | Mostly AI | Tonic Structural/Fabricate | SDV | GenRocket | Verdict |
|---|---|---|---|---|---|
| Persistent reusable **generator** (whole-model object) | Yes — "Generator", train→probe→export | Fabricate/generation configs; per-column "generator" vocabulary | Yes — "synthesizer object", saveable | Yes — designed generator families (750+) | **All four** — core (name/vocabulary varies) |
| Realism basis: trained on real data | Yes (sample-based core) | Structural: real source transformed; Fabricate: from scratch | Yes (training data required) | No ("No production data touched. Ever.") — designed rules/scenarios from schema/metadata | **Basis is dual**: learned OR designed |
| On-demand controlled generation (volume/format/seed) | probe(size), seed-conditioned | generation jobs, table modes control rows/cols | sample on-demand, "supply instructions" | instant generation, any volume/format, scenario-driven | **All four** — core |
| Structured artifact schema | tabular (+text claims) | relational DBs, semi-structured | single/sequential/multi-table | 125+ formats, EDI, mainframe | **All four** — core |
| Evaluation/assurance layer | Model Insight Report; Validate step; privacy protection | Privacy Hub protection status; sensitivity scan | Diagnostic + Quality reports (validity/structure/relationships) | deterministic validity + referential integrity by design | **All four**, form varies strongly — core-adjacent common layer |
| Sensitive-data detection | privacy protection framing | sensitivity scan (PII/PHI) | anonymization options | masking (synthetic replacement, "never looked at") | Common (not universal in form) |
| Transformation-without-generation co-capability | positioned against masking | yes — core de-identification/subsetting | constraints/preprocessing, not masking | yes — masking/subsetting as modules | Common co-capability |
| Conditional/seeded/scenario generation | seed conditioning | table modes | "supply instructions" | scenarios/test-case objectives | Common |
| Source connectors + destination writeback | platform connectors, export | explicit connectors + destinations | load/export file/DB | orchestration to environments | Common |
| Web app + SDK/API/CLI | platform + SDK | web + API + Agent chat | Python library (web absent in community) | portal + integrations | Common; GUI not universal |
| Multi-table/relational integrity | complex tabular/textual | relational focus | HMA + referential-integrity checks | patent-claimed referential integrity | Common |
| Multi-user collaboration/org layer | platform teams | workspaces + user access | absent in OSS library | G-Portal/GMUS self-service | Common in platform-form products |

## Abstraction (four layers)

### L0 — Defining Invariant (minimal)

A data-manufacturing application whose defining core is exactly three jointly-held structures:

1. **The generator as the held unit of record** — a persistent, named, reusable definition of how to produce data: either a model learned from a source dataset or a designed configuration of schema + rules + scenarios. It survives sessions, is re-executable, and is the object users build, inspect, and manage. (Remove → ad-hoc scripts, not a platform.)
2. **Controlled on-demand manufacture of artificial datasets** — executing the generator produces structured datasets whose shape, volume, and format the user controls, commonly with conditioning/seeding/scenarios; the records are artificial rather than copies. (Remove → a stored model file, no manufacturing loop.)
3. **A declared realism basis** — the generator is grounded in a source of truth the output preserves or respects: the statistical structure of real source data, or a designed specification (schema, business rules, integrity constraints, referential integrity). (Remove → ungrounded random fake-data filler, below the Type.)

Jointly-held load-bearing: (1) alone = a model artifact; (2) without (1) = scripts; (3) without (1)+(2) = a spec document; (1)+(3) without (2) = modeling research, not a platform.

### L1 — Common Mature Structure

- Evaluation/assurance layer over generated output (fidelity/quality reports, diagnostic validity/structure/relationship checks, privacy protection status) — present in all four sampled in different forms
- Sensitive-data detection (PII/PHI scanning) and handling
- Transformation-without-generation co-capabilities (masking, de-identification, subsetting of real data)
- Conditional / seeded / scenario-driven generation
- Connectors: source ingestion + destination delivery (databases, files, storage, environments)
- Multi-table / relational support with referential integrity machinery
- Multi-surface access (web application, SDK/API/CLI) and workspace/organization/user-access layer in platform-form products
- Modality extensions beyond tabular: sequential/time-series, free text, unstructured files, mock APIs

### L2 — Variant / Optional Structure

- Generation substrate: deep generative nets (GAN/AR-class) vs classical statistical models (copula-family) vs deterministic rule engines vs LLM prompt-driven mock generation
- Primary job emphasis: privacy-safe sharing & analytics vs dev/test data provisioning vs AI/ML training data
- Deterministic vs probabilistic output philosophy (explicitly opposed positions in-sample)
- Deployment: SaaS, self-hosted instance, on-prem compute, local library
- Privacy techniques: differential-privacy options, privacy reports, GDPR positioning
- Data-modality breadth (tabular-only vs +text vs +files)
- Enterprise machinery: RBAC/SSO, audit, clean-room sharing, self-service portals, CI/CD integration

### L3 — Vendor-specific (Research Notes only)

- Tonic: Workspace / Privacy Hub / Database View / table modes / Structural Agent; Structural-Textual-Fabricate product split
- Mostly AI: TabularARGN architecture naming, Model Insight Report, probe/seed API, "powered by Syntho" merger framing, Gartner quotations
- SDV: "synthesizer" naming, GaussianCopula/CTGAN/PAR/HMA specifics, MIT DAI Lab 2016 / DataCebo 2020 lineage, SDV Enterprise tier
- GenRocket: G-Portal / G-Questionnaire / G-Repository / GMUS / G-Families naming, "750+ generators / 125+ formats / 2.5M rows per minute" figures, US patent number
- Gretel→NVIDIA acquisition (market fact)

## Boundary Findings

- **vs Data Labeling Platform** — labeling produces annotations over REAL data items held by the platform; synthetic data platforms manufacture artificial records. Different unit of work; clean seam. (Labeling pass recorded its own seam: managed data-item population + labeling state.)
- **vs Database Dev/Test Environment Manager** — that Type derives/provisions non-production environments from a source database (copies, virtual clones); a synthetic data platform manufactures data. Adjacent in the dev/test job; Tonic and GenRocket straddle via subsetting/masking modules, but environment provisioning is not this Type's core. Seam: the environment vs the dataset.
- **vs Data Quality Platform** — data quality measures existing real data; the synthetic platform's evaluation layer judges GENERATED data against its basis. Different subject; evaluation-inside-generation is not data quality tooling.
- **vs masking/anonymization-only tools** — transformation without generation (pseudonymize/mask real rows) is adjacent; Mostly's own docs argue the distinction (pseudonymized data remains personal data; synthetic has no 1:1 links). The generation leg is definitional; masking is a common co-capability, not the identity.
- **vs mock/fake-data generators** (random filler with no grounding) — below the Type per the realism-basis leg; note the market blur: Mostly's taxonomy puts rule-based mock below synthetic, while Tonic Fabricate ("from scratch") and GenRocket (design-driven) remain synthetic-data platforms because they ground generation in schema/rules/integrity machinery rather than pure randomness.
- **vs synthetic imagery / CV sensor-simulation platforms** (scene-rendering training data for computer vision — Datagen/Parallel Domain class, not sampled) — a different production model (3D scene simulation/rendering vs dataset manufacturing). Mostly's own docs split structured vs unstructured synthetic data. Likely a separate Type; **flagged for taxonomy review**.
- **"去掉什么就变成另一个 Type" tests** — remove generation (keep masking/subsetting/provisioning) → test-data management / dev-test-environment territory; remove the held generator (keep evaluation) → data-quality/evaluation tooling; remove the realism basis → mock-data filler; move the object of record from generated data to annotated real data → Data Labeling.

## Historical / Market-Sample Check (§24)

- 1990s–2000s test-data generators (schema+rules → files/tables with referential integrity, TDM suites) satisfy all three L0 legs with no AI/cloud/web — historical check **passed**.
- Statistical-disclosure synthetic microdata (parametric/imputation lineage, statistical agencies since the 1990s) satisfies all three legs — **passed**.
- Modern learned-generation products (SDV/Mostly class) satisfy — **passed**.
- Therefore L0 must NOT be phrased as "generative AI trained on real data" (GenRocket explicitly rejects that pole yet is marketed as a synthetic data platform) and must not require a web GUI (SDV community is a library) or cloud deployment.

## Uncertainties

- Gretel's current product shape post-acquisition unverified (docs unreachable) — no claims made.
- Hazy, yData, Synthesized unreachable in this pass — enterprise-statistical-fidelity pole covered only by Mostly AI evidence.
- Whether the market will split "synthetic imagery/CV data" into its own Type — unresolved; flagged.
- LLM-based mock generation ("AI-generated mock") as a converging third pole — observed only through Mostly's taxonomy page; strength kept low.
- Exact privacy techniques (differential privacy parameters etc.) not researched to numeric precision — deliberately omitted per evidence rules.

## Final Synthesis

The Synthetic Data Platform is a **data-manufacturing** application: it holds a reusable **generator** — either a model trained on real data or a designed rule/scenario configuration — and executes it on demand to manufacture artificial datasets that preserve a declared realism basis (the statistics of a real source, or a designed schema with validity/integrity rules). Users control volume, shape, format, and often conditioning; the output is consumed where real data cannot be used: privacy-safe sharing and analytics, dev/test environments, and AI/ML training. Every sampled product wraps the loop with an assurance layer — quality/fidelity reports, validity and referential-integrity diagnostics, and privacy protection status — and most add transformation co-capabilities (masking, subsetting) beside generation. The Type is defined by the generator-manufacture-grounding triad, not by any particular model family, GUI, deployment, or the "trained on real data" framing that dominates current marketing.
