# A/B Testing Platform

## Overview

An **A/B Testing Platform** is a system for running controlled experiments on a live digital experience: it defines two or more versions of that experience, randomly assigns real users to each version, measures how a chosen goal performs in each group, and reports which version should become the experience.

The defining core is small:

```text
Experiment (a persistent, hypothesis-bearing record)
└── Variants (control + at least one alternative)
    └── Randomized assignment of real users to variants
        └── A measured goal compared across variants
            └── A decision: which variant should ship
```

Everything else commonly associated with the category — visual editors, Bayesian statistics, feature flags, heatmaps, idea pipelines, AI assistants — is widespread in current products but is not what makes the product an A/B testing platform. Older and simpler products (split-URL redirect testers, early website optimizers) satisfy the same core without any of those additions.

The platform answers a question no analytics tool can answer by observation alone: *did this change cause the improvement, or would it have happened anyway?* By randomly splitting users between an unchanged control and one or more treatments, it turns a correlation into a controlled comparison.

## Users & Context

Primary users:

- **Growth / CRO specialists and marketers** — test page layouts, copy, offers, and funnels on marketing sites and e-commerce properties; typically author variants in a visual editor without engineering help.
- **Product managers** — test feature designs, onboarding flows, and pricing/packaging presentations before committing to a rollout.
- **Data analysts** — define metrics, scrutinize results, and adjudicate whether an observed lift is trustworthy.

Supporting roles:

- **Engineers** — install the tracking snippet or SDK, expose parameters for server-side experiments, and keep event instrumentation correct.
- **Stakeholders / executives** — read results and sign off on ship/no-ship decisions.
- **Administrators** — manage permissions, governance, and account configuration.

Typical contexts: marketing websites and landing pages, e-commerce checkout and product pages, mobile apps, and software product features. The work is cyclical — a program of many experiments over time, not a one-off test — which is why mature products accumulate reusable libraries of metrics, audiences, and page definitions.

## Core Model

### The Defining Core

```text
Experiment
├── Variants (control + treatment(s))
├── Audience (who is eligible)
├── Allocation (what share of traffic enters, how it is split)
├── Goals (primary / secondary / guardrail) ← fed by Events
└── Result (per-variant comparison with statistical confidence)
     └── Decision (ship a variant / keep control / discard)
```

- **Experiment** — the central object: a named, persistent record that carries a hypothesis, its configuration, its run state, and its results. It exists before launch (draft), during the run, and after conclusion as an archived artifact. The experiment is the unit of planning, collaboration, and governance.
- **Variant** — one version of the experience being tested. Every experiment has a **control** (the current experience) and at least one **treatment** (the proposed alternative). An experiment with more than one treatment is an A/B/n test; testing combinations of multiple elements is a multivariate test.
- **Randomized assignment** — the platform decides which variant each eligible user sees, by chance, per a **randomization unit** (commonly the user; sometimes the device or session). Assignment is sticky: the same unit keeps seeing the same variant for the life of the experiment. This is the property that separates experimentation from rule-based targeting.
- **Goal / metric** — the measured outcome. A **primary metric** is the metric on which the win/lose call is made; **secondary metrics** watch for side effects; **guardrail metrics** protect business-critical numbers from regressing. Metrics are computed from **events** — behavioral signals such as clicks, page views, form submissions, purchases, or custom product events.
- **Result** — the per-variant comparison: the observed difference (lift) between treatment and control, together with a statistical statement of how trustworthy it is (confidence intervals and significance in frequentist products; probability-to-be-better and practical-equivalence in Bayesian products).
- **Decision** — the terminal output: declare a winner and roll it out, conclude there is no meaningful difference, or stop and discard. The decision is the reason the platform exists.

### Standard Capabilities of Mature Products

These appear across the researched sample and are expected in practice, though they do not define the Type:

- **Audience targeting** — conditions deciding who is eligible (device, location, traffic source, behavior, custom attributes), combinable with AND/OR logic.
- **Traffic allocation** — control over what percentage of eligible traffic enters the experiment and how it is divided among variants; commonly used to start small and ramp up.
- **Statistical engine** — significance testing, confidence intervals, or Bayesian probability reporting, often with corrections for multiple comparisons and sequential-evaluation methods.
- **Results page** — per-variant metric comparison with lift, confidence, and significance indicators; segment and dimension breakdowns; export.
- **Lifecycle management** — draft → running → paused → stopped/concluded → archived states, with scheduling of start and end.
- **QA / preview mode** — verify targeting, tracking, and variant rendering in real conditions before exposing real users.
- **Reusable libraries** — saved events/goals/metrics, audiences/segments, and page/URL definitions shared across experiments.
- **Experiments dashboard** — the list of experiments with status, and the entry point for creation.
- **Integrations** — passing experiment data to analytics tools, data warehouses, and collaboration systems.
- **Rollout mechanism** — pushing the winning variant to all users, or concluding back to control.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:            Variant authoring
Implementations:    visual editor on live pages, code editor (JS/CSS),
                    server-side parameters consumed by application code

Concept:            Randomization unit
Implementations:    user ID, device ID, session ID, custom ID

Concept:            Statistical backing
Implementations:    frequentist (p-values, confidence intervals,
                    sequential testing, variance reduction),
                    Bayesian (probability to be better, practical equivalence)

Concept:            Decision
Implementations:    winner rollout to production, parameter default change,
                    formal ship/no-ship record, archive
```

## How It Works

The canonical loop of an A/B testing platform:

```text
1. Formulate a hypothesis
2. Create the experiment and build variants
3. Define the audience and traffic allocation
4. Define goals from events
5. QA and preview
6. Start — randomized delivery begins
7. Monitor results
8. Conclude — decide the winner (or no difference)
9. Roll out or discard; archive the experiment
```

**1. Formulate a hypothesis.** The experimenter states what change will affect which audience and which metric. Mature products provide a hypothesis field on the experiment record, often with a fill-in template, because the hypothesis determines the primary metric.

**2. Build variants.** Depending on the product's philosophy, variants are authored in a **visual editor** (point-and-click changes to a live page: text, images, colors, layout, pop-ups), a **code editor** (JavaScript/CSS), or **server-side** (the experiment defines parameter values; application code reads the assigned value and renders accordingly). The control usually requires no authoring — it is the current experience.

**3. Define audience and allocation.** Targeting conditions decide who is eligible; allocation decides what share of that audience enters the experiment and how it is split across variants. Even splits are a common default; practitioners often start with a small share and ramp up after verifying stability.

**4. Define goals.** The primary metric — the one that will decide the experiment — is selected from a library of events and metrics (clicks, page views, transactions, custom product events). Secondary and guardrail metrics are added to watch for side effects. Some metric types must be instrumented before launch; others can be computed retroactively from already-collected data.

**5. QA and preview.** Before launch, the experimenter verifies in a preview/QA mode that targeting fires, tracking records, and each variant renders correctly. Mature products provide dedicated QA tooling for this because a broken experiment wastes traffic and pollutes results.

**6. Start.** The platform begins randomizing eligible users into variants. From this point the assignment is sticky: a user who sees the treatment keeps seeing it.

**7. Monitor.** The results page accumulates exposures and metric performance per variant. Early data is treated as diagnostic; mature products explicitly warn against making decisions before the experiment has enough data, and some provide sequential-testing methods that make interim checks statistically safe.

**8. Conclude.** When the primary metric reaches a trustworthy state — statistical significance at the planned sensitivity, or a decisive Bayesian probability — the experimenter declares an outcome: treatment wins, control holds, or no meaningful difference. Some products formalize this as an explicit decision action that also ships the winning parameters.

**9. Roll out or discard.** A winner is pushed to all users (instantly in client-side products, or as a default parameter change in server-side ones). A loser or inconclusive test is stopped; its record is archived as organizational learning.

### Capability Tiers

**Defining core** — without these, not an A/B testing platform:

- experiment as persistent record
- variants including a control
- randomized assignment of real users
- measured goal compared across variants
- decision output

**Standard capabilities** — present in most mature products:

- audience targeting, traffic allocation control
- primary/secondary/guardrail metrics
- statistical engine and results page
- lifecycle states, scheduling, QA/preview
- reusable libraries, dashboard, integrations, rollout

**Optional / variant** — depends on segment and philosophy:

- visual editor (client-side products) or server-side parameter model
- multivariate, split-URL, multipage, and A/A test types
- Bayesian vs frequentist methodology
- feature-flag integration, experiment isolation layers
- personalization mode, program-management pipelines, AI assistance, bundled behavioral analytics

## Interfaces

### Experiments dashboard

The entry surface: lists experiments with name, status, and key dates.

- typical information: experiment name, hypothesis excerpt, status, variants, traffic share, start date
- primary actions: create experiment, open one, filter/search, archive

### Experiment editor

The configuration surface for a single experiment, usually organized as steps or tabs.

- typical information: hypothesis, variant list, audience conditions, allocation percentages, goal selection, schedule
- primary actions: add/edit variants, set targeting, set allocation, attach metrics, schedule, launch

### Visual editor

The client-side variant authoring surface (in products that offer it): the live page rendered with an overlay for making changes.

- typical information: page content, selectable elements, change list per variant
- primary actions: edit text/images/styles, rearrange or hide elements, add widgets or code, record click goals

### Results / report page

The analysis surface.

- typical information: exposures per variant, per-metric lift, confidence intervals or win probabilities, significance indicators, segment breakdowns
- primary actions: switch metric views, filter by segment/dimension, adjust statistical settings, export, make the ship decision

### QA / preview mode

A verification surface used before launch.

- typical information: simulated variant rendering, firing events, targeting evaluation for the tester
- primary actions: force a variant, verify tracking, approve for launch

### Component libraries

Management surfaces for reusable objects: events/goals/metrics, audiences/segments, pages/URL conditions.

- primary actions: create, edit, reuse across experiments

## Important Rules / Behaviors

### Randomization is sticky

Once a user is assigned to a variant, they keep that variant for the life of the experiment. This consistency is what makes the comparison valid; products implement it with deterministic assignment keyed on the randomization unit.

### The primary metric governs the outcome

The win/lose call is made on the primary metric. In some products the primary goal is locked once the experiment starts, preventing post-hoc goal switching that would invalidate the test.

### Allocation changes are asymmetric

Increasing the share of traffic entering an experiment is generally safe; decreasing it mid-run can bias group composition and pollute results — products either warn against it or require a reset that re-randomizes users.

### Early results are diagnostic, not decision-grade

Peeking at unfinished experiments and stopping on the first significant reading inflates false positives. Mature products either warn explicitly, compute results on a fixed schedule, or offer sequential-testing methods that correct for interim looks.

### Statistical thresholds, not raw deltas, justify decisions

A treatment may show a higher conversion rate yet remain within noise. The platform's statistical layer — significance, confidence intervals, or win probability — is the arbiter, and products surface it prominently to prevent decisions on eyeballed differences.

### Experiments can interfere with each other

Concurrent experiments touching the same users can contaminate each other's results. Mature products provide isolation mechanisms (exclusive groups or layers) or at least visibility into overlapping experiments.

### Guardrails can stop a test automatically

Some products let critical metrics act as guardrails that pause a test or notify owners when the treatment regresses them — reflecting that a "winning" variant can still be unacceptable if it damages something else.

### Stopped experiments stop collecting, but history persists

Paused, stopped, and archived experiments behave differently in data collection, and their records are preserved as organizational memory — the experiment archive is itself a first-class asset of an experimentation program.

## Variants

Common forms of the Type:

- **Client-side web testing** — variants authored in a visual editor and delivered via a page snippet; the classic marketing/CRO form.
- **Server-side / feature experimentation** — variants expressed as parameter values consumed by application code via SDKs; favored by product and engineering teams; often integrated with feature flags.
- **Mobile app testing** — the same core against native app experiences, with SDK-based delivery.
- **Split URL / redirect testing** — variants are whole separate URLs; the oldest implementation pattern.
- **Multivariate testing** — multiple elements varied simultaneously to measure combinations.
- **A/A testing** — both groups get the same experience; used to validate the measurement pipeline itself.
- **Personalization mode** — the same delivery machinery with deterministic, segment-based assignment instead of randomization; present in several products as a sibling mode.
- **Program-management layer** — idea pipelines, hypothesis boards, and program dashboards wrapped around the testing engine in suite products.
- **Warehouse-native measurement** — results computed in the customer's own data warehouse rather than the vendor's store.

A variant remains a **Variant** unless it changes the defining core; all forms above keep variants, randomization, measured comparison, and decision intact.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Digital Experimentation Platform | closest sibling | shares the identical core (variants + randomization + measured comparison + decision); differs by center of gravity — engineering/product teams, server-side delivery, feature-flag and warehouse integration vs marketing/CRO teams, visual editor, web-page surface. The market itself blurs the two labels |
| Feature Flag Management Platform | adjacent, often bundled | flags control delivery (who gets what, on/off, gradual rollout); experiments measure effect. A flag without measurement is not an experiment |
| Conversion Rate Optimization Platform | practice-framed superset | CRO is the goal; A/B testing is the instrument. Market "CRO platforms" typically bundle testing with behavior analytics, personalization, and program management |
| Landing Page Optimization Platform | narrower variant | same core restricted to landing pages and acquisition campaigns |
| Marketing Analytics Platform | adjacent | analytics observes and reports; A/B testing intervenes by assigning users and establishes causal comparison. Results pages borrow analytics forms, but the defining act is the controlled comparison |
| Marketing Personalization Platform | adjacent, shared machinery | personalization assigns experiences deterministically by segment rule; A/B testing assigns randomly to compare. Products commonly ship both modes |
| Survey Platform | different evidence source | surveys collect stated preference (what users say); A/B testing measures revealed preference (what users do) under controlled comparison |
| Customer Data Platform | supporting infrastructure | supplies audience attributes and behavioral data that targeting and metrics consume |

The most important boundary is with **Digital Experimentation Platform**: research across the sample found one shared structure expressed in two philosophies (marketing/CRO-first vs engineering-first), with vendors themselves shipping both under one roof. The distinction is a gradient of audience, surface, and packaging — not a structural wall.

## Representative Products

- **Optimizely** — enterprise experimentation; ships client-side Web Experimentation and server-side Feature Experimentation as product lines
- **VWO** — CRO-oriented suite with a Bayesian statistics engine and visual-editor-first testing
- **AB Tasty** — mid-market experimentation and personalization with a guided step-based campaign flow
- **Statsig** — engineering-native experimentation platform with feature flags, server-side parameters, and warehouse-native options

The core model was checked against simpler and older patterns (split-URL redirect testing, early website optimizers) and against embedded A/B testing inside other products (email subject-line testing, ad creative testing) to avoid over-fitting the definition to the current marketing-suite pattern.

## Sources

Research date: **2026-09-06**

- Optimizely Support Help Center — Web Experimentation (category, key components, steps to create an experiment): https://support.optimizely.com/hc/en-us/categories/39024919539981
- VWO — product pages (root, Testing): https://www.vwo.com/ , https://vwo.com/testing/
- AB Tasty documentation — A/B test creation, campaign flow goals step, campaign types: https://docs.abtasty.com/
- Statsig documentation — experiments overview, create an experiment, read results, ending an experiment: https://docs.statsig.com/

> Sourcing limitation: VWO's help center was unreachable from the research environment (two failed attempts); VWO observations are positioning-level from official product pages, and claims about VWO internals are stated more weakly than claims about the other sampled products. Optimizely's main documentation portal is behind a login; its support help center was used instead. Precise statistical defaults and numeric limits are stated only where directly documented in fetched sources.

Detailed evidence, product-by-product observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
