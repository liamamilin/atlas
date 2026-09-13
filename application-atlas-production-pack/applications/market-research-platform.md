# Market Research Platform

## Overview

A **Market Research Platform** is the research professional's end-to-end system for running studies. It manages each research study as a persistent record carried through a lifecycle — design the instrument, source and operate the sample, field, process the data, produce the deliverable — and it treats the people who answer as a managed input: sample is sourced through the platform (marketplaces, panels, supplier connections, synthetic respondents) or brought by the user, and in both cases flows through the platform's fieldwork machinery of feasibility, quotas, quality controls, and cost.

The defining core is small:

```text
The study as the managed unit of record
└── carried through design → field → analyze → report
    ├── respondent supply operated as a platform function
    └── research-grade processing and deliverable production
```

Three properties, held together. Remove the managed study and only a survey tool or a pile of ad-hoc analyses remains. Remove the operated sample supply and only a survey platform's publish-and-distribute fielding remains. Remove the processing-and-deliverable layer and only a data-collection pipe or a sample exchange remains. The scope is deliberately subject-agnostic — the population a study examines is whatever the research question demands: consumers, business decision-makers, healthcare professionals, employees, citizens.

Everything else commonly associated with the category — AI drafting and AI agents, synthetic respondents, advanced method toolkits, benchmark databases, learning loops, qualitative extensions, client portals — is widespread in current products but is not what makes the product a market research platform. The paper-era research agency (paper questionnaire, field department, hand tabulation, typed report) satisfies the same core without any of it.

## Users & Context

The primary users are people who run research as a discipline:

- **agency researchers** — design, field, process, and report studies for client organizations; the platform is their production system, often run at high study volume across many clients and countries
- **insights teams inside brands and organizations** — run the research program themselves: concept and product testing, brand and campaign tracking, market and audience studies
- **independent and self-serve researchers** — consultants, academics, and small teams who need methodologically sound studies without an agency, using self-serve tools with expert support on hand

Secondary consumers are the stakeholders who receive the outputs — marketing, product, and executive audiences reading dashboards, toplines, and decks — and, at agencies, the clients who log into live portals.

The typical context is a decision that needs evidence: a concept before launch, an ad before air, a price before listing, a market before entry, a brand's health over time. A second context is continuous: tracking studies that repeat on a schedule and compound value wave over wave. The platform's reason for existing as a category is that it industrializes this work — one system carries the study from question to deliverable, with the sample supply and the methodological machinery built in.

## Core Model

### The Study as the Unit of Record

The central object is the **study**: a bounded piece of research — a question, an instrument, a sample plan, the collected data, and the outputs — held as a persistent, identified record. The study is what gets named, designed, quality-checked, launched, monitored, closed, and reported. It accumulates its own history: versions, waves, fieldwork events, and deliverables. Around studies sits the **portfolio**: reusable templates, locked best-practice methodology, libraries of past studies, and cross-study knowledge that mature platforms treat as a first-class layer rather than a folder structure.

### The Sample Plan and the Fieldwork Operation

Who answers is a designed, operated input — not an afterthought:

- **sample sources** — the platform's own sample marketplace or panels, connected supplier networks, synthetic respondents (era-typical), or sample the user brings (client lists, own panels, email campaigns)
- **feasibility** — a live estimate of whether the targeted population exists in sufficient numbers, and at what cost, before the study is committed
- **quotas** — required counts per subgroup, so the achieved sample's makeup is controlled rather than incidental
- **fieldwork controls** — redirects between suppliers and the platform, completion tracking, live monitoring of quotas and pace, and mid-field adjustment
- **quality machinery** — detection and removal of speeders, bots, straight-liners, and duplicate or fraudulent respondents, with bad respondents replaced during fielding

This is the structural feature that most separates the Type from plain survey software: respondent supply is an operated platform function with procurement semantics (sources, cost, feasibility), not an optional distribution channel.

### The Instrument

The **instrument** is the structured set of questions the sample answers:

- question types: closed choice, scales, grids, ranking, open text, and rich media stimulus (images, audio, video) that concept, ad, and packaging tests depend on
- logic: routing and branching, complex quota-driven paths, loops, randomization
- authoring depth as a spectrum: visual drag-and-drop builders at one pole, full scripting (code-level control) at the professional pole
- method packaging: advanced research methods — conjoint analysis, maximum-difference scaling, pricing methods, monadic testing, concept and ad testing — delivered as ready-to-use tools or templates rather than as raw question types to assemble by hand
- multilingual support for multi-country studies

### The Data and the Processing Layer

As the study fields, **responses** accumulate and the platform's processing layer turns them into research outputs:

- automated data processing and cleaning — the platform's quality machinery runs continuously, so what the researcher sees is processed data, not raw intake
- tabulation: per-question results, crosstabs, pivot tables, respondent segments
- weighting and significance testing, so that samples can be corrected to a population frame and differences between groups or waves can be trusted
- open-text handling: theme coding and sentiment, increasingly AI-assisted
- method-specific models: preference simulators and share/revenue projections for conjoint-class studies, scores and diagnostics for ad and concept tests

### The Deliverable

The study ends in **deliverables** produced for stakeholders or clients:

- live dashboards that fill as data arrives and remain available after fielding
- toplines and summary reports; auto-generated presentations with native charts
- client portals — secure, live views for stakeholders during and after fielding
- exports: spreadsheets, slides, and statistical formats for further analysis

### One Structure, Many Implementations

The core model is conceptual. Products realize it differently, and the differences are the Type's main variant axes:

```text
Concept:   Respondent supply operated as a platform function
Realized as:   built-in sample marketplace · own or partner panels ·
               connected supplier networks · synthetic respondents ·
               bring-your-own lists and email campaigns

Concept:   The instrument
Realized as:   fully scripted professional builds · wizard-driven
               self-serve tools · pre-built study templates with the
               methodology baked in

Concept:   The deliverable
Realized as:   live dashboards · auto-generated decks · client portals ·
               exports to analysis tools
```

A reader who has only seen one realization — say, a self-serve conjoint tool with a sample marketplace — should still be able to recognize an agency-grade scripting suite as the same Type from the core model.

## How It Works

### The study lifecycle (the defining workflow)

```text
Design
  → choose or build the instrument (method tool, template,
    or scripted questionnaire; AI drafting increasingly assists)
  → define the sample plan (population, targeting, quotas,
    sample size; watch feasibility and cost update)
  → quality-check the build (logic, links, routing)
Field
  → launch (immediately or scheduled; often a soft launch first)
  → sample flows in from the chosen sources
  → monitor live: quotas, pace, quality; adjust mid-field
  → filter and replace bad respondents continuously
Analyze
  → process and clean the data
  → tabulate, weight, test significance; run method models
  → read results through crosstabs, segments, dashboards
Report
  → assemble deliverables (topline, dashboard, deck)
  → publish to stakeholders or clients (portals, exports)
  → close the study; retain it in the portfolio
```

Two rules shape this loop. First, the sample plan is a commitment: feasibility and pricing are known before launch, and fielding consumes budget as respondents arrive. Second, fielding is actively operated — the researcher watches quotas and quality live and intervenes (adjusting quotas, sources, or pacing) while the study runs, rather than publishing a link and waiting.

### The tracking loop

```text
fix the instrument and sample definition
→ field on a schedule (waves)
→ compare each wave against prior waves
→ maintain a trended record (brand health, campaign impact)
```

Tracking reuses a stable instrument so change over time is measurable; mature products support this with locked templates, wave management, and trended reporting. Multi-country studies extend the same loop across markets with translated instruments and per-market quotas.

### Capability tiers

**Defining core** — without these, not this Type:

- the study as a managed record carried through design → field → analyze → report
- respondent supply operated as a platform function (sources, feasibility, quotas, quality, cost)
- research-grade processing and deliverable production

**Standard capabilities** — present in essentially all mature products:

- instrument authoring with research-grade depth (question types, logic, quotas, media, multilingual)
- method libraries (conjoint, MaxDiff, pricing methods, monadic and concept/ad testing)
- fieldwork operations (pre-launch QA, live monitoring, mid-field adjustment, wave deployment)
- data-quality machinery (fraud/bot detection, speeder filtering, replacement)
- tabulation, weighting, significance testing, open-text analysis
- dashboards, toplines, decks, and exports (client portals with live stakeholder views at the agency-facing pole)
- study-portfolio layer (templates, research libraries, cross-study knowledge)
- human research support alongside the tool

**Optional / variant** — depends on product philosophy and segment:

- AI drafting, AI analysis, AI agents at process stages
- synthetic respondents and synthetic/human mixed designs
- multi-mode fielding (phone/CATI, offline)
- qualitative extensions (digital diaries, online focus groups, communities, video responses)
- panel management (operating a standing panel as an asset)
- benchmark databases and automated learning loops
- full-service project delivery (the vendor runs the study)

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Study dashboard / project list

The entry surface listing studies and their state. Typical information: study names, status (design / fielding / closed / reported), key metrics, recency. Primary actions: create a study (from template, method tool, or blank), open a study, search the portfolio.

### Study builder

Where the instrument is designed. Typical information: ordered question list, question settings, media attachments, logic map. Primary actions: add/edit questions, set routing and quotas, randomize, apply a method template, preview as a respondent, run automated QA checks. At the professional pole this surface includes code-level scripting; at the automation pole it may be reduced to configuring a pre-built study template.

### Sample & audience setup

Where who-answers is defined. Typical information: target population and targeting criteria, quotas per subgroup, sample size, feasibility and cost estimates, sample source selection. Primary actions: choose sources (marketplace/panels/suppliers/own lists), set quotas, review feasibility, confirm the sample plan.

### Fieldwork monitor

The operations surface while the study is live. Typical information: completions against quotas, pace, drop-off, quality flags, source performance. Primary actions: adjust quotas, pause or boost sources, review flagged respondents, extend or close fielding.

### Analysis / results

The processing surface. Typical information: per-question results, crosstabs, segments, significance indicators, weighted totals, open-text themes, method outputs (simulators, scores). Primary actions: filter, split, create segments, weight, build charts, run method models.

### Reporting & delivery

The stakeholder-facing surface. Typical information: dashboards, toplines, presentation decks, share links. Primary actions: assemble reports, generate decks, publish client portals, export to spreadsheets/slides/statistical formats.

### Admin & collaboration

Team management, roles and permissions, billing and sample budgets, integrations and APIs (to CRMs, panel providers, and analysis tools).

## Important Rules / Behaviors

### The sample plan is a commitment with a budget

Feasibility and cost are established before launch; fielding spends money as respondents complete. Changing the sample plan mid-field is an operational act with cost consequences, which is why platforms surface feasibility and pricing during design rather than after.

### Fielding is actively operated, not published and forgotten

The researcher monitors quotas, pace, and quality live and intervenes while the study runs — adjusting sources, rebalancing quotas, replacing failed respondents. This operational posture is what "fieldwork" means in this Type, and it is the main behavioral difference from publish-and-distribute survey tooling.

### Data quality is enforced continuously

Speeders, bots, straight-liners, duplicates, and fraudulent respondents are detected and removed — in some products replaced during fielding so the achieved sample still reaches its quotas — so the dataset the researcher analyzes is processed, not raw. Quality machinery runs whether or not the researcher watches.

### Mid-field instrument changes are controlled

Changing questions while respondents answer would corrupt comparability. Supported paths are operational (adjust quotas, sources, pacing, close or extend fielding); instrument edits are constrained once fielding has begun, with the strictness varying by product. Tracking studies go further: the instrument is locked across waves by design.

### Weighting and comparability are the researcher's discipline

Weighting schemes, significance testing, and wave-over-wave comparison are first-class machinery because the category's outputs are meant to support decisions — and because samples bought from multiple sources must be made comparable before their results are pooled or compared.

### Deliverables are stakeholder-facing artifacts

The study's output is produced for someone other than the researcher — a client, an executive, a product team. Live client portals, branded reports, and presentation-ready decks are standard machinery, not afterthoughts; at agencies the deliverable is the product being sold.

### Human research support is part of the product

Unlike most software categories, market research platforms typically pair the tool with access to research professionals — for study design review, methodological choices, and interpretation — up to full-service delivery where the vendor runs the study. The category's self-image is methodological rigor made accessible, and the human layer is a deliberate part of that.

## Variants

- **Agency-grade professional suite** — full scripting control, multi-mode fielding, panel management, data visualization, and services aimed at research agencies and enterprise research teams running high study volumes.
- **Insight-automation pole** — pre-built study templates with methodology and benchmarks baked in, automated sample and reporting, "set-and-forget" operation aimed at brand insights teams; speed and consistency over scripting depth.
- **Self-serve method-and-sample pole** — advanced methods packaged as approachable tools with integrated sample buying and expert support; serves consultants, academics, small teams, and brand teams without agency budgets.
- **Suite-embedded research core** — the research capability living inside a broader experience-management or CX platform, sharing infrastructure with customer and employee programs.
- **Sample-posture variants** — built-in marketplace, own/managed panels, connected supplier networks, synthetic respondents, bring-your-own lists; most products support several at once.
- **Method-breadth variants** — quant-only toolkits vs multi-mode (phone/offline) machinery vs qualitative extensions (diaries, online focus groups, communities, video).
- **Service-depth variants** — DIY → assisted → full-service, where the vendor's researchers design and run the study on the platform.

A variant remains a variant unless it changes the users, core objects, workflow, or rules so much that the defining core no longer applies.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Survey Platform | closest tool-level sibling | survey platforms author and field instruments to respondents, with respondent supply as an optional commercial add-on and analysis depth as a variant axis. Here the study is a managed lifecycle record, respondent supply is an operated platform function, and processing reaches client-ready deliverables. Remove the operated fieldwork and study machinery → a survey platform remains. The market itself blurs the seam (suite products are claimed by both categories) |
| Research Panel Platform | adjacent supplier-side Type | the panel platform's managed object is the standing member population (recruit, profile, incentivize, maintain); here the managed object is the study, with sample bought or routed as fieldwork procurement. Panel-management modules inside MR suites are that Type's machinery at module grain. Remove the standing population from either side and they swap |
| Consumer Research Platform | closest sibling, commercially fuzzy | consumer research platforms are consumer-subject-scoped with audience access bundled as product for brand-side teams; this Type is subject-agnostic with sample procurement as an operated function for research practitioners. Several products self-label with both vocabularies — the seam is a gradient, kept as separate Types on the recorded test |
| Sample exchange / marketplace (market structure, no leaf) | upstream supply | exchanges route respondents programmatically from supplier networks to buyers, holding no study of record and no processing or deliverable layer. This Type integrates exchanges as sample sources. Remove the study lifecycle and processing → an exchange remains |
| Competitive Intelligence Platform | different data nature | CI runs a standing monitored loop over tracked entities from observed data; here structured studies are fielded to sampled populations. Competitors appear inside studies as stimulus, not as the tracked population |
| Social Listening Platform | different data nature | listening observes unsolicited public expression; this Type asks structured questions of sampled people. Asked vs observed; complementary in practice |
| Marketing Analytics Platform | different data source | marketing analytics measures the organization's own campaign and channel performance from observed behavioral data; this Type generates attitudinal data by asking and processes it with survey-statistics machinery |
| Voice of Customer Platform | relationship-scoped neighbor | VoC manages feedback from an existing customer relationship as a standing program; this Type studies arbitrary populations via procured sample. Own-customer studies are the bridge case |
| Employee Survey Platform | population-bound sibling | the same instrument machinery bound to the workforce population and employment lifecycle; here the population is whatever the research question demands. An employee study is one study among many here |
| A/B Testing Platform | different evidence source | experimentation measures revealed preference on live product traffic; this Type collects stated preference from sampled humans |

## Representative Products

- **Forsta (Research HX / Decipher)** — agency-grade professional suite: scripted survey engine, built-in sample marketplace with bring-your-own-sample, live fieldwork management, data visualization, panel management, and qual modules
- **Qualtrics (Market Research / Research Hub)** — research core inside an experience-management suite: unified market/product/UX/brand research, human and synthetic panels, study library with locked methodology
- **Conjointly** — self-serve method-and-sample platform: advanced methods packaged as tools, integrated sample marketplace with bring-your-own options, automated analysis and reports
- **Zappi** — insight-automation pole: pre-built ad/concept/pack study templates, automated sample and AI-generated reports, benchmark and learning-loop layers (self-labels "consumer insights platform" — the documented seam with the consumer-research Type)

The defining core was checked against older and differently positioned forms — the paper-era research agency, the 1990s–2000s MR software generation (authoring + data processing + tabulation with CATI sample management), regional MR software, and thin bundled-sample DIY products — to avoid over-fitting the definition to the current AI-era implementation.

## Sources

Research date: **2026-09-10**

Primary official sources:

- Forsta — Market research platform (Research HX): https://www.forsta.com/platform/market-research/
- Forsta — Advanced data collection (Decipher): https://www.forsta.com/platform/market-research/advanced-data-collection/
- Qualtrics — homepage: https://www.qualtrics.com/
- Qualtrics — Market Research Software: https://www.qualtrics.com/market-research/
- Conjointly — homepage: https://conjointly.com/
- Conjointly — How it works: https://conjointly.com/how-it-works/
- Zappi — homepage: https://www.zappi.io/ and platform page: https://www.zappi.io/web/platform
- Dynata — homepage (boundary context): https://www.dynata.com/
- Cint — boundary context reused from the Research Panel Platform pass (research/research-panel-platform.md, fetched 2026-09-07)

> Sourcing limitation: no vendor help-center or admin-console documentation was reachable from the research environment on 2026-09-10 (Qualtrics support/product-doc URLs returned 404 this pass and in the prior panel pass; Zappi's knowledge base is login-gated). All reached sources are official product/positioning pages, so operational mechanics are stated only at the level those pages support: no numeric limits, defaults, or console internals are asserted, and vendor-published figures (survey volumes, panel sizes, language counts, speed claims) are treated as marketing claims and excluded from this document. Zappi's and Qualtrics' contributions are positioning-level by consequence.

Detailed product-by-product observations, the cross-product comparison matrix, the full boundary analysis (including the discharged joint reviews with the Research Panel Platform and Consumer Research Platform passes), and the historical/market-sample check are recorded in the paired Research Notes.
