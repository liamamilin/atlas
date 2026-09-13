# Consumer Research Platform

## Overview

A **Consumer Research Platform** is a brand-side research application for studying consumers directly. It supplies access to real consumer audiences, turns a research question into a structured study fielded to those audiences, and returns the answers as decision-ready insight — dashboards, crosstabs, reports, and increasingly conversational AI answers — for people making brand, marketing, and product decisions.

The defining core is small:

```text
The consumer as the studied subject
└── Structured study fielded to real consumers
    └── Platform-supplied access to consumer audiences
        └── Decision-oriented insight outputs
```

Four properties. Remove any one and the product stops being this Type:

- **The consumer as the studied subject** — the research is about people in their role as consumers: attitudes, behaviors, preferences, and perceptions of brands, categories, and products. Without this, the product is generic research or survey tooling.
- **Structured studies fielded to real consumers** — the platform converts a question into a structured instrument (typically a questionnaire) that sampled humans actually answer. Without this — if the data is only observed or scraped — the product is a listening or analytics tool, not a research platform.
- **Platform-supplied access to consumers** — reaching the consumers is part of the product itself: an owned panel, a panel network, or a continuously fielded syndicated dataset. The user never recruits respondents. Without this, the product is a survey authoring tool.
- **Decision-oriented insight outputs** — answers come back analyzed: charts, crosstabs, segments, statistical context, summaries, shareable stories. The product's deliverable is the answer, not a raw transcript or a raw data feed. Without this, the product is a sample marketplace.

Everything commonly associated with the category — AI drafting and AI analysts, advanced methods like conjoint and MaxDiff, trend-signal feeds, slide generators, proprietary mobile panel apps — is widespread in current products but is not part of the defining core. Older and differently positioned products (panel companies with DIY survey tools, syndicated-data pioneers, audience add-ons to survey tools) satisfy the core without any of those specifics.

## Users & Context

The primary users are teams inside consumer-facing (B2C) organizations who need evidence for decisions but are not necessarily trained researchers:

- **insights teams** — run and govern the research; increasingly use the platform to replace agency-commissioned studies for routine questions
- **brand and marketing teams** — track brand health, test campaigns and creative, profile their category's consumers
- **product teams** — validate concepts, features, packaging, and pricing with consumers before committing
- **agencies and media organizations** — profile audiences and back pitches and media plans with consumer data (a pronounced secondary audience, strongest for syndicated-data products)

The typical context is a decision under time pressure: a concept must be validated before launch, a campaign must be measured, a category question must be answered before a meeting. The platform's promise — and the reason it exists as a category — is that the brand can get a consumer answer in days rather than the weeks a commissioned agency study can take. A second context is continuous: brand and campaign tracking, where the same study repeats on a schedule and value compounds wave over wave.

## Core Model

### The Study as the Unit of Work

The central object is the **study**: a bounded piece of research — a question, an instrument, an audience, and the answers collected against them. In self-fielded products the user creates the study; in syndicated products the vendor fields studies continuously and the user's "study" is an audience definition plus queries over the resulting dataset. Either way, the study is what gets named, reviewed, launched, and reported.

### The Audience

The **audience** is the defined group of consumers who may answer. It is a first-class object with its own machinery:

- **targeting criteria** — country and language first, then demographic filters (age, gender, region, income, household characteristics, and other attributes whose availability varies by market)
- **quotas** — required percentages per group, so the sample's makeup is controlled rather than incidental
- **screening questions** — qualifying questions at the start of the instrument that screen respondents in or out on attributes the demographic filters cannot express (usage, ownership, specific behaviors)
- **feasibility** — a live estimate of how many respondents currently match the targeting, updated as filters are applied; feasibility gates the study before launch
- **sample size** — how many responses to collect, with pricing typically quoted against it
- **presets** — saved, reusable audience definitions, including representative presets (e.g., a nationally representative working-age sample)

### The Instrument

The **instrument** is the structured set of questions the audience answers:

- question types: single and multiple choice, grids/battery matrices, ranking, rating scales, open text
- media: images, audio, and video embedded in questions or shown as stimulus (concept and creative testing depend on this)
- logic: routing (branching paths based on answers) and display logic (show/hide individual questions), randomisation of questions and answer options
- structure: text cards between questions, question groups, multi-wave organization for repeated studies
- reuse: templates, team question libraries, translation for multi-market studies

### The Response Data and the Insight Layer

As the study fields, **responses** accumulate and the platform's **insight layer** turns them into answers:

- a live results dashboard that fills as data arrives — analysis starts before fielding completes
- charts and visualizations per question
- **crosstabs** — the workhorse: answers cross-analyzed by demographics, segments, or prior answers
- **segments and splits** — named subgroups (defined by targeting, answers, or uploaded customer data) compared against each other and against the total
- statistical context — significance testing so differences between groups or waves can be trusted
- open-text handling — theme extraction and sentiment analysis on free-text answers
- AI summaries and conversational analysis — plain-language questions answered from the study data (era-typical)
- storytelling and delivery — boards/stories that assemble charts into narratives, exports to spreadsheets, slides, and CSV, presentation-ready output

### One Structure, Many Implementations

The core model is conceptual. Products realize it differently, and the differences are the Type's main variant axis:

```text
Concept:   Platform-supplied consumer audience
Realized as:   proprietary panel app · panel network/partners ·
               continuously fielded syndicated dataset ·
               customer's own list (own-audience mode) · hybrids of these

Concept:   The study
Realized as:   user-fielded custom study · vendor-fielded syndicated
               dataset the user queries · scheduled tracking wave
```

A reader who has only seen one realization (say, a self-serve panel survey tool) should still be able to recognize a syndicated-data product as the same Type from the core model.

## How It Works

### The custom-study loop (the typical workflow)

```text
Frame the question
→ build the instrument (draft questions, media, logic;
  increasingly AI-drafted from a plain-language brief, then reviewed)
→ define the audience (country/language, demographic filters,
  quotas, screening questions; watch feasibility and price update)
→ review and launch (immediately or scheduled)
→ responses arrive; live dashboard fills
→ analyze (charts, crosstabs, segments, significance, AI summaries)
→ assemble and share the answer (boards, exports, presentations)
→ decide
```

Two rules shape this loop. First, the audience step is not an afterthought: feasibility feedback during setup tells the user whether the targeted consumers exist in sufficient numbers before any money is spent. Second, launching commonly locks the instrument — self-serve products typically treat launch (or purchase) as the point of no return for questionnaire edits, because changing questions mid-field would corrupt the data.

### The syndicated-query loop

```text
choose a dataset (and any compatible add-on datasets)
→ define an audience from the profiling points it contains
→ read answers through charts, crosstabs, and dashboards
→ ask conversational questions of the data (AI analyst)
→ share dashboards and slides
```

Here the vendor runs the fielding machinery continuously — large harmonized surveys, repeated in waves, recruited through panel partners — and the user's skill is in audience definition and comparison. The platform enforces comparability discipline: which datasets may be combined, which may not, and how totals must be rebased when mixing samples. Custom fielding exists in this pole too, usually as a service layer where the vendor's researchers design and run a bespoke study.

### The tracking loop

```text
fix the instrument and audience definition
→ field on a schedule (waves)
→ compare each wave against prior waves
→ maintain a trended record of brand/category health
```

Tracking is how the Type compounds value: brand trackers, campaign trackers, and product-launch trackers reuse a stable instrument so that change over time is measurable. Several products ship tracking as a distinct mode or product line.

### Capability tiers

**Defining core** — without these, not this Type:

- consumer as studied subject
- structured study fielded to real consumers
- platform-supplied consumer audience
- insight outputs for decisions

**Standard capabilities** — present in essentially all mature products:

- audience targeting (demographics, quotas, screening, feasibility)
- instrument builder (question types, media, logic, templates)
- live results dashboard with charts and crosstabs
- segments/splits and statistical significance
- exports and shareable output
- data-quality machinery (bot/fraud detection, attention and consistency checks, duplicate prevention)
- ongoing/tracking research
- human research support alongside the tool

**Optional / variant** — depends on product philosophy and segment:

- AI drafting, AI summaries, conversational analysts
- automated advanced methods (conjoint, MaxDiff, TURF, implicit association, pricing meters, driver analysis, segmentation)
- syndicated datasets and trended waves
- qualitative extensions (AI-moderated interviews, video responses, communities)
- market-trend signal feeds
- slide/deliverable generators
- data activation outward (audience activation to ad platforms, respondent-level data, APIs)

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Dashboard / home

The entry surface listing studies (and, in syndicated products, datasets). Typical information: study names, status (draft / fielding / complete), recency, key results. Primary actions: create a study, open a study, ask the AI assistant.

### Study editor

Where the instrument is built. Typical information: ordered question list (often with a structural "map" view showing routes and branches), question settings, media attachments. Primary actions: add/edit questions and text cards, set routing and display logic, randomise, preview as a respondent, share a draft for comments.

### Audience page

Where who-answers is defined. Typical information: country/language, demographic filters, quotas, feasibility/available-sample estimate, sample size, price. Primary actions: apply targeting, set quotas, add screening, load a preset audience, choose audience source (platform panel / own list / hybrid).

### Review & launch

Final gate before fielding. Typical information: summary of questions, logic, audience, schedule, cost. Primary actions: schedule or launch, confirm purchase.

### Results / analysis

The insight surface. Typical information: per-question charts, crosstabs, segment comparisons, significance indicators, open-text themes, AI summaries. Primary actions: filter, split, create segments, build charts, generate summaries, export.

### Story / board builder

Assembles charts and text into shareable narratives. Primary actions: add charts, arrange, annotate, present or export.

### AI assistant

A conversational surface over the platform's data — drafting surveys from a brief, answering plain-language questions from results or datasets, summarizing findings. Present in all sampled current products; depth varies.

### Admin & collaboration

Team management, roles and permissions, credits/billing (in credit-metered products), integrations/APIs.

## Important Rules / Behaviors

### The audience defines the validity of everything downstream

Targeting, quotas, and screening jointly determine who can answer; results are only as representative as the audience definition. Feasibility feedback during setup is the platform's way of forcing this conversation before launch — a niche target may be unreachable at the requested sample size, and the platform says so before money is spent.

### Launch is commonly a commitment point

In self-fielded products, once a study is launched (or purchased), the instrument is commonly locked against edits. Changes mid-field would make answers inconsistent; the supported paths are closing early, extending, or increasing sample — not rewriting questions.

### Analysis begins before fielding ends

Results dashboards fill live. Teams routinely read early data, and the platform's quality machinery (bot detection, attention checks, consistency tests, duplicate prevention, human review) runs continuously so that early reads are trustworthy. The user sees cleaned data, not raw intake.

### Comparability is enforced, not assumed

In tracking and syndicated contexts, the platform polices which comparisons are legitimate: which waves share an instrument, which datasets share a sample, when a total must be rebased before cross-dataset crosstabs are meaningful. Treating incompatible datasets as comparable is a documented error mode, and mature products surface the rules in-product.

### Respondent-facing surfaces carry consent and branding

Respondents see a privacy notice and consent step before the instrument; own-audience distribution commonly requires pseudonymised identifiers so responses can be linked to customer data without exposing personal information. Panel respondents are the platform's community, with incentives and engagement mechanics managed by the platform, not the user.

### Human research support is part of the product

Unlike most self-serve software categories, consumer research platforms typically pair the tool with access to research professionals — for study design review, bias checks, and interpretation. The category's self-image is "researcher in a box," and the human layer is a deliberate part of that.

## Variants

- **Self-serve panel pole** — proprietary consumer panel (often mobile-app-based with engagement mechanics), fast custom studies, simplicity for non-researchers; SMB through enterprise brand teams.
- **Syndicated-data pole** — vendor-fielded harmonized datasets queried in-platform; strongest among agencies, media, and brands needing audience profiling and market context rather than bespoke studies; custom research as a service layer.
- **Methodology-depth pole** — automated advanced-method toolkits (conjoint, MaxDiff, TURF, implicit association, pricing and driver methods) aimed at enterprise insights teams replacing agency-run studies.
- **Decision-engine pole** — the study core wrapped with trend-signal feeds, unified insight workspaces that mix survey data with documents, and instant deliverable generation.
- **Own-audience and hybrid modes** — distributing surveys to the brand's own customers or lists through the same instrument and analysis machinery, optionally combined with platform audiences in one study; the bridge toward customer-feedback use cases.
- **Qualitative extensions** — AI-moderated interviews, video responses, and research communities attached to the quantitative core.
- **Tracking products** — brand, campaign, ad, product-launch, and trend tracking as dedicated modes or product lines built on the same machinery.

A variant remains a variant unless it changes the users, core objects, workflow, or rules so much that the defining core no longer applies.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Research Panel Platform | adjacent supplier | the panel platform's managed object is the standing member population itself (recruit, profile, incentivize, maintain); here the population is supply infrastructure and the study-plus-insight is the product. Remove the study tooling from either side and they swap |
| Market Research Platform | closest sibling | market research platforms center the study lifecycle and sample buying across all research subjects for research professionals; consumer research platforms are consumer-subject-scoped with audience access bundled for brand-side teams. The seam is commercially fuzzy (several products self-label with both terms) and is flagged for joint review |
| Survey Platform | tool-level neighbor | survey platforms author and field instruments to arbitrary respondents without supplying a consumer audience or a consumer-insight analysis frame. Remove platform-supplied audience access from this Type and a survey platform is what remains |
| Voice of Customer Platform | relationship-scoped neighbor | VoC manages feedback from an existing customer relationship as an ongoing program; this Type studies market consumers via sampled audiences, who need not be customers. Own-audience surveys of customers are the bridge case |
| Social Listening Platform | different data nature | listening observes unsolicited public expression; this Type asks structured questions of sampled consumers. Complementary, not overlapping |
| Competitive Intelligence Platform | different subject | CI tracks competitors' moves; here competitors appear only as brands inside consumer studies. Signal-feed layers in some products drift toward CI but remain variant layers |
| Marketing Analytics Platform | different data source | marketing analytics measures campaign/channel performance from observed behavioral data; this Type generates attitudinal data by asking. They are frequently used together |
| A/B Testing Platform | different setting | experimentation platforms test variants on live product traffic with behavioral outcomes; this Type tests concepts, creative, and propositions with sampled consumers before or beyond the live product |

## Representative Products

- **Attest** — self-serve consumer research with integrated panels, own-audience and hybrid modes, AI co-pilot and AI-moderated interviews
- **GWI** — syndicated consumer datasets queried in-platform, with a conversational AI analyst and custom research services
- **Appinio** — proprietary mobile-first consumer panel with an AI-assisted survey platform and insight boards
- **quantilope** — automated advanced-method consumer intelligence platform with tracking products
- **Suzy** — consumer insights decision engine combining research, trend signals, and deliverable generation

The defining core was checked against older and differently positioned products (panel companies with DIY survey tools, syndicated-data pioneers, survey tools with audience add-ons) to avoid over-fitting the definition to the current AI-era implementation.

## Sources

Research date: **2026-09-07**

Primary official sources:

- Attest Help Center — https://help.askattest.com/en/ (incl. "Getting started with your first survey", "Selecting demographics for your survey", "Sending surveys to your own audience", and the Building surveys / Analysing results / Audience and targeting / Data Quality and methodology collections)
- Attest — https://www.attest.com/ (platform overview)
- GWI Help Center — https://help.globalwebindex.com/en/ (incl. "Using GWI data sets")
- GWI — https://www.gwi.com/ , https://www.gwi.com/platform , https://www.gwi.com/data
- Appinio — https://www.appinio.com/en/ , https://www.appinio.com/en/how-it-works/survey-platform , https://www.appinio.com/en/how-it-works/panel-app
- quantilope — https://www.quantilope.com/en
- Suzy — https://www.suzy.com/ , https://www.suzy.com/intelligence , https://www.suzy.com/insight

> Sourcing limitation: operational documentation for Suzy could not be reached from the research environment (its help center was unreachable; public pages are marketing-level), so Suzy-specific statements are kept at positioning level. Panel ownership and sourcing arrangements for some products are not publicly documented and are described only as "platform-supplied audience". Vendor-published scale figures (panel sizes, market counts, data volumes) are marketing claims and are deliberately not stated as operational facts in this document.

Detailed product-by-product observations, the cross-product comparison matrix, and the full boundary analysis are recorded in the paired Research Notes.
