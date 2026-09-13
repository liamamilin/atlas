# Synthetic Data Platform

## Overview

A **Synthetic Data Platform** is a data-manufacturing application: it holds a reusable **generator** — a definition of how to produce data, realized either as a model trained on real data or as a designed configuration of schema, rules, and scenarios — and executes it on demand to produce **artificial datasets** that preserve a declared basis of realism: the statistical structure of a real source, or a designed specification with validity and integrity rules.

It solves a specific problem: much of the data work in an organization — training AI models, testing software, sharing datasets, exploring analytics — cannot legally, safely, or practically use real production data. The platform manufactures stand-in data that behaves like the real thing (same schema, same statistical shape, same integrity) without being the real thing.

The boundary: this is a manufacturing Type, not a measurement or annotation Type. It does not label real data (Data Labeling), does not provision database environments (Database Dev/Test Environment Manager), and does not audit the quality of existing data (Data Quality Platform). Its defining act is generating new artificial data from a held generator.

## Users & Context

Primary users are technical data practitioners, and the dominant context is enterprise and engineering work constrained by data sensitivity:

- **Data scientists / ML engineers** — need realistic training, validation, and test datasets for models, especially when real data is sensitive, biased, imbalanced, or inaccessible; commonly generate conditioned or rebalanced variants of a source dataset.
- **Developers / QA engineers** — need realistic data for staging environments, local development, and test cases, including edge cases and exception scenarios that production data never happens to contain.
- **Data engineers / platform teams** — configure connectors, run generation jobs, deliver outputs to databases, files, or test environments, and integrate generation into pipelines.
- **Privacy, security, and governance stakeholders** — assess whether generated output is safe to use and share, review protection status, and approve the replacement of sensitive data (personally identifiable information, protected health information) in non-production use.

Typical settings: regulated industries (banking, insurance, healthcare, telecom) moving data across trust boundaries; engineering organizations that have banned copies of production data in lower environments; data teams that need to widen access to data across teams or external partners without exposing real records.

## Core Model

The platform's world has five structures. The first three are the defining core; the last two make the platform operational in practice.

### The defining core

```text
Realism basis  (real source data  or  designed schema + rules + scenarios)
      ↓
Generator      (persistent, reusable, re-executable — the unit of record)
      ↓  executes on demand
Synthetic dataset  (controlled shape · volume · format · commonly conditioned)
      grounded by / judged against the realism basis
```

- **Realism basis.** What the generator is grounded in. Two realizations coexist across the market: a **learned basis** — the platform ingests a real dataset and a model learns its patterns, correlations, and distributions; and a **designed basis** — the user defines the schema, business rules, value distributions, and scenarios, and the generator produces data conforming to them, often without ever reading production data. Some products combine both (profile real metadata, then generate from design).
- **Generator.** The central held object: persistent, named, saveable, re-executable, and commonly exportable. When learned, it is a model containing a condensed representation of the source data. When designed, it is a configuration of generators and rules per field and relationship. This object — not any one generated dataset — is what users build, evaluate, refine, version, and reuse. Vocabulary varies by product ("generator", "synthesizer", generation configuration), and one product family even uses "generator" for per-column transformers; conceptually it is always the reusable data-producing definition.
- **Synthetic dataset.** The manufactured artifact: structured records matching a schema (tables with keys and relationships, sequences, documents, files). Records are artificial — no one-to-one correspondence with real individuals — while volume and format are user-controlled, from a handful of rows to production-scale. Users commonly steer generation with seeds, conditional instructions, or scenario definitions (e.g. "generate customers aged 65+ with claims").

### Standard operational structures

- **Evaluation layer.** Every mature product wraps the loop with assurance machinery: automated quality reports comparing synthetic against the basis, validity diagnostics (unique non-null primary keys, values within source ranges, categories matching the source, formats respected), referential-integrity checks across related tables, and privacy assessment of the generator itself — guarding against a model that memorized and would leak its training data. Designed-basis products guarantee validity by construction and verify integrity instead.
- **Connectors and delivery.** Source connectors to ingest real data (databases, files, cloud storage); destination delivery to write generated data where consumers work — databases, storage, test environments — plus file/SDK export.

## How It Works

The canonical loop has five movements. Learned-basis and designed-basis products travel it differently, but the loop is the same.

### 1. Establish the realism basis

```text
Learned basis:    connect to source → ingest/profile real data → sensitivity scan
Designed basis:   define schema → set rules, distributions, relationships, scenarios
Combined:         profile metadata/schema → derive generator design
```

On the learned path, a sensitivity scan typically identifies columns holding sensitive values that need protection during configuration.

### 2. Build the generator

```text
Learned:  choose model → train on source data → inspect quality report → adjust and retrain
Designed: configure per-field generators/rules → wire relationships/integrity → save
```

The generator is saved as a persistent object. Building it is iterative: train, evaluate, tune, retrain.

### 3. Generate on demand

```text
open/reuse a saved generator
→ set volume, format, output target
→ optionally condition generation (seed values, instructions, scenarios, subset rules)
→ run the generation job → synthetic dataset produced
```

Generation is repeatable and parameterized — the same generator can feed a 1,000-row demo or a production-scale staging load. Multi-table generation maintains keys and parent-child cardinality so the output remains a working relational dataset.

### 4. Evaluate and assure

```text
run quality report        (synthetic vs basis: statistical similarity, fidelity)
run validity diagnostics  (uniqueness, ranges, categories, formats — expected clean)
check relationships       (referential integrity, cardinality)
review privacy posture    (no memorization/leakage of real records; protection status)
```

Reports are attachable to the generator and become the artifact users review before trusting the data downstream.

### 5. Deliver

```text
export files / SDK output
→ write to destination database, storage, or environment
→ or integrate generation into CI/CD pipelines so tests receive data at run time
```

Alongside the generation loop, mature platforms commonly offer a **transformation co-flow**: mask, de-identify, or subset real data as it moves source → destination. This handles the cases where a faithful transformed copy is preferred over fully generated data. The co-flow is a capability, not the identity — the platform remains a synthetic data platform because it can manufacture data, not merely alter it.

## Interfaces

Surfaces are described conceptually; layouts and names vary by product.

### Web application (platform-form products)

- **Workspace / project view** — holds the data connections and generation configuration for one dataset or purpose; primary actions: create workspace, connect source and destination, invite collaborators.
- **Schema / column configuration view** — the table-and-column map where users mark sensitivity, assign rules or transformations per field, set table behaviors (how many rows flow through), and review detected schema drift when the source changes.
- **Protection / privacy dashboard** — current protection status of the configuration: which sensitive fields are covered, what remains exposed.
- **Generator / model management** — list of saved generators with their training source, version, and quality reports; primary actions: train, retrain, compare, export.
- **Generation jobs** — run history with progress, logs, and results; primary actions: run, schedule, inspect failures.
- **Quality report view** — side-by-side statistics of basis vs output, validity scores, relationship checks, privacy notes.

### SDK / API / CLI

Developer-first products expose the whole loop programmatically: train or load a generator, sample with size and seed parameters, run reports, export. Some products are effectively API-only or library-first, with the web app optional. An AI assistant/chat surface for configuration and data questions is appearing in newer platform releases.

### Self-service portal (test-data-oriented deployments)

A request-and-serve surface where development and test teams request the data they need (scenario, volume, format) and the platform provisions it on demand — often integrated directly into test automation and release pipelines so data arrives "at the right time, in the right place".

## Important Rules / Behaviors

- **Output is artificial, not copied.** For learned generation, the defining privacy claim is that generated records have no one-to-one link to real individuals. This is a design obligation on the generator: a model that memorizes its training data defeats the purpose, which is why privacy evaluation of the model is part of the standard loop. The strictness of privacy claims varies by product and technique; Treat overly strong claims ("fully anonymous") as vendor positioning rather than a structural guarantee.
- **Validity and integrity are enforced or diagnosed.** Primary keys stay unique and non-null; values respect source ranges and categories; dates and formatted identifiers respect formats; every foreign key in generated multi-table output references an existing parent row. Designed-basis products enforce this by construction; learned-basis products diagnose it and treat deviations as defects.
- **The basis is the contract.** Quality is always judged relative to the declared basis — statistical fidelity to the source data, or conformance to the designed rules. There is no absolute "correct" synthetic dataset; a generator can be faithful and still wrong for a purpose, which is why the basis choice and conditioning parameters are user decisions.
- **Generation is repeatable and parameterized.** The same saved generator, run twice with different parameters, produces different-but-equivalent datasets; the generator outlives any single run and is the thing users maintain.
- **Source schema drift matters.** When the underlying real schema changes, configurations must be reviewed and resolved — generated output is expected to track the structure of the basis.
- **Sensitive data handling.** On the learned path, sensitive columns are detected and must be protected by configuration before generation; on the transformation co-flow, sensitive values are replaced under rules; on the designed path, production data is often never read at all.

## Variants

Common market realizations of one Type:

- **Learned-basis enterprise platform** — trains generative models on real data (deep-learning and statistical model families), leads with privacy-safe sharing, analytics enablement, and AI training data; platform UI plus SDK; often deployable inside the customer's own environment so raw data never leaves.
- **Dev/test data platform** — organized around source→destination pipelines: sensitivity scanning, masking, subsetting, and synthesis over relational and semi-structured data; sells to engineering organizations; commonly self-hosted. A sibling product line generates relational data and mock APIs entirely from scratch.
- **Open-source statistical library** — the platform reduced to its modeling core: synthesizers for single-table, sequential, and multi-table data with sampling, constraints, and evaluation in code; commercial tiers add scale and enterprise deployment.
- **Design-driven deterministic generator** — never touches production data; builds generators from schema, rules, and scenarios; guarantees validity deterministically; optimized for test-data provisioning at enterprise scale with CI/CD integration and self-service portals; increasingly also sells the same machinery for AI/ML training data.
- **Developer API-first services** — synthetic data exposed as cloud APIs/SDKs for engineering teams (this segment has consolidated into larger AI-infrastructure vendors in recent years).

Cross-cutting variant axes: generation substrate (deep generative vs classical statistical vs deterministic rules vs LLM-prompted), primary job (privacy sharing vs test data vs ML training), modality breadth (tabular core; sequences, text, and unstructured files as extensions), deployment (SaaS / self-hosted / local library), and output philosophy (probabilistic vs deterministic).

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Data Labeling Platform | adjacent (ML data production) | organizes annotation of **real** data items by workers; the artificial-record population and generator are absent |
| Database Dev/Test Environment Manager | adjacent (dev/test job) | derives and provisions **environments** from a source database (clones, masked copies); a synthetic data platform manufactures **datasets** and may feed such environments |
| Data Quality Platform | adjacent (evaluation) | measures and remediates **existing real** data; a synthetic platform's reports judge **generated** data against its basis |
| Data Catalog / Data Exchange Platform | adjacent (sharing) | describes or brokers access to data that exists; a synthetic platform creates the data |
| Machine Learning Platform / MLOps Platform | consumer/producer neighbors | train, register, deploy, and monitor models; synthetic data is an **input** produced upstream, not the object the platform manufactures |
| AI Model Evaluation Platform | different subject | evaluates models, not datasets |
| Data Masking / anonymization tooling | capability overlap | transform real rows without generating new ones; within this Type masking is a co-capability beside the defining generation leg |

The sharpest boundary: remove generation from a synthetic data platform and what remains is test-data management and masking — a different Type. Add the annotation of real items and it becomes Data Labeling. Remove the realism basis (grounding in source statistics or designed rules) and the product degrades into an ungrounded fake-data filler, below this Type.

A note on scope: "synthetic data" is also used in the market for simulated imagery and sensor data for computer vision (generated by rendering 3D scenes rather than manufacturing structured records). That family shares the name but runs a different production model and is treated here as an adjacent market, not part of this Type's core.

## Representative Products

- **MOSTLY AI** — learned-basis enterprise synthetic data platform with an open-source SDK; privacy-led, European-market origin
- **Tonic.ai (Structural / Fabricate)** — dev/test-data platform spanning de-identification, subsetting, and synthesis of structured data, with a from-scratch generation line
- **SDV (DataCebo)** — open-source statistical synthesizer library descended from MIT research, with commercial enterprise tiers
- **GenRocket** — design-driven, deterministic test-data generation platform that generates without touching production data

The definition was checked against both opposed poles — learned/statistical products and design-driven/deterministic products — so it does not depend on the currently dominant "AI trained on real data" framing.

## Sources

Research date: **2026-09-09**

- MOSTLY AI — product site and "Synthetic Data Basics" documentation: https://mostly.ai/ , https://mostly.ai/synthetic-data-basics
- Tonic.ai — product documentation: https://docs.tonic.ai/ , https://docs.tonic.ai/app/readme.md , https://docs.tonic.ai/app/readme-1/tonic-workflows.md
- SDV / DataCebo — official documentation: https://docs.sdv.dev/sdv/ , https://docs.sdv.dev/sdv/get-started.md , https://docs.sdv.dev/sdv/evaluation/diagnostic.md
- GenRocket — product site: https://www.genrocket.com/

> Sourcing limitation: several additional market products could not be examined from the research environment on 2026-09-09 (one vendor's documentation was unreachable after repeated attempts, one redirected to its acquirer, one rendered no readable content). Conclusions therefore rest on the four products above, sampled across both opposed generation philosophies. Numeric claims (row rates, model sizes, privacy-technique parameters) are deliberately excluded; product-specific figures remain with the vendors' own pages.
