# Sports Performance Analytics

## Overview

A **Sports Performance Analytics** application is the staff-facing analysis application over measured sports performance. It holds a population of identified athletes as the subjects of analysis, binds quantified performance measurements to them, computes sport-native metrics from that data, compares results across athletes, groups, sessions, and time, and surfaces the findings as dashboards, reports, and player profiles that coaches and performance staff use to make decisions about training, load, availability, tactics, and development.

The defining core is small:

```text
Analyzed performance population (identified athletes; teams/sessions/competitions as contexts)
└── Performance measurement corpus (quantified data bound to that population, accumulating over time)
    └── Analysis → insight loop (metrics → comparison → dashboards/reports → staff decisions)
```

Everything commonly associated with modern products — wearable device pipelines, live session monitoring, AI risk models, video linkage, athlete-facing apps — is widespread in current products but is not what makes the product a performance analytics application. A spreadsheet-era workbook holding a squad's session measurements, computed weekly comparisons, and printed reports for coaches satisfies the same definition.

The Type is defined as much by what it does **not** own as by what it owns: it does not plan or assign training work (that is an Athlete Management System), does not administer testing protocols (that is a Fitness Assessment Application), does not edit or review video (Sports Video Analysis), and does not own medical episode records (Athlete Injury / Availability Management). It reads from all of these worlds and turns their data into insight.

## Users & Context

The primary users are the **analysis consumers and producers inside an organized sports program** — professional clubs, collegiate athletics departments, national federations and institutes, high-performance centers, tactical/defense units:

- **sport scientists / performance analysts** — configure metrics, build dashboards, run comparisons, and interpret trends; the deepest daily users
- **strength & conditioning / performance staff** — read load, readiness, and testing views to adjust how athletes are trained
- **coaches** — consume simplified views (daily status, player profiles, opposition summaries) to make selection and session decisions
- **medical staff** (where medical data flows in) — read injury-burden and availability analyses, while clinical detail stays behind a privacy wall
- **administrators / analysts** — manage data sources, integrations, and reporting standards across teams or departments

The athletes whose data is analyzed are the **subjects** of the system, not its operators; in some products they also get a read-facing view of their own numbers.

The work context is the training ground and the desk: live session monitoring on tablets or sideline devices during training and matches, and desk-based dashboard work before and after sessions. The rhythm is daily (who trained, how much, how they responded), weekly (microcycle comparisons), and seasonal (longitudinal development).

## Core Model

### The Defining Core

Three structures, held together. If any one is removed, the product is no longer recognizable as sports performance analytics:

- **The analyzed performance population.** Athletes exist as identified records — the "who" of every number — commonly organized into teams, squads, or groups, with sessions, drills, matches, and competitions as the contexts in which performance happens. Without this population the product is a generic charting tool over anonymous data.
- **The performance measurement corpus.** Quantified observations of athletic performance bound to that population and accumulating over time: physical load from wearables, testing results, athlete-reported wellness, match and event data, or manually entered numbers. The analytics application may collect this data itself (some vendors ship the devices), ingest it from integrated sources, or accept both. Without the corpus there is nothing to analyze.
- **The analysis → insight loop.** The system computes sport-native metrics from the corpus — load indicators, physical outputs, possession-value models, injury-burden rates — and supports comparison across athletes, groups, sessions or matches, and time: trends, benchmarks, norms, drill-downs from team to individual. The output is surfaced as dashboards, reports, and profiles consumed by staff for decisions. Without this loop the product is a data archive or a device data store.

The metrics and objects are **sport-native**: the system knows what a session, a drill, a match, a position, and a squad are, and its metric vocabulary is built for performance questions (how much work, how hard, how it compares, who is at risk). This is what separates the Type from a generic dashboard or business-intelligence tool, which could chart the same numbers but understands none of their meaning.

### Standard Capabilities

Mature products commonly carry most of the following. They make the analytics practical; they do not define the Type:

- **Configurable dashboards** — user-built or template views assembled from widget libraries (tables, line/bar charts, event tables, pitch or tactical views)
- **Role-based views** — different dashboards for coaches, scientists, medical staff, and analysts; day-to-day users get ready-made views, advanced users build their own
- **Team → group → individual drill-down** — squad-level trends that open into a single athlete's profile
- **Longitudinal analysis** — daily → weekly (microcycle) → season → multi-season trends per athlete and per squad
- **Benchmarks and thresholds** — comparisons against norms, position peers, or configured limits, with flags when values cross them
- **Export and sharing** — reports exported, printed, or shared to stakeholders outside the tool
- **Live session monitoring** — real-time views of group and individual effort during training or matches, beside post-session analysis
- **Multi-source ingestion** — device feeds, file imports, third-party integrations, and APIs feeding one corpus
- **Data-quality surfaces** — duplicate detection, missing-data and coverage checks, common where many sources are aggregated
- **Video linkage** — data insights attached to the corresponding video clips, where a video product is available
- **Athlete-facing views** — read-only apps showing athletes their own numbers (present in some products, not all)

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:            Analyzed population
Implementations:    club/squad rosters synced from wider platforms · multi-team
                    hierarchies for federations and departments · league-wide
                    player databases · match-squad and competition contexts

Concept:            Measurement corpus
Implementations:    vendor's own wearable devices · integrated third-party devices
                    and testing tools · vendor-collected match event/tracking data ·
                    manual entry and file imports

Concept:            Metric layer
Implementations:    configurable parameter/metric vocabularies · vendor-defined
                    load metrics · possession-value and expected-outcome models ·
                    exposure-adjusted injury rates

Concept:            Insight surfaces
Implementations:    widget-based dashboard builders · fixed role-based dashboard
                    families · live sideline apps · report generators ·
                    API/file delivery of computed data
```

A reader who has only seen one implementation — say, a GPS-vest monitoring dashboard — should still be able to recognize a match-event analytics platform or an enterprise reporting layer as the same Type from the core model.

## How It Works

### Establish the analyzed population

```text
Create or connect the organization (club, department, program)
→ import or sync athletes into teams/squads/groups
→ define who can see and build what (roles)
```

### Build the measurement corpus

```text
Connect data sources: devices, integrations, imports, manual entry
→ capture sessions and matches (live monitoring where offered)
→ data lands against athletes and session/match contexts
→ the corpus accumulates across days, seasons, and years
```

In wearable-first products the loop starts at the device: units are issued and collected, data is downloaded or uploaded automatically, and each session is processed into per-athlete measurements. In aggregation-first products the corpus is assembled from whatever systems the organization already runs. In match-data products the corpus arrives as collected event and tracking data for completed matches.

### Analyze and compare

```text
Open a dashboard (daily status, squad load, testing, match analysis)
→ compare across athletes, groups, sessions, matches, and time
→ drill from team trends into an individual profile
→ check values against benchmarks, norms, or thresholds
→ flag athletes or patterns that need attention
```

### Surface and decide

```text
Share or export reports to coaches and stakeholders
→ staff interpret the insight in their decision context
→ decisions follow: adjust training, manage load, change availability,
  refine tactics, evaluate players
→ the next session's data flows back into the corpus
```

The loop — measure → compute → compare → surface → decide — is the defining workflow. It repeats daily and compounds season over season.

### Maintain the corpus

Where many sources feed one analysis layer, data quality becomes part of the work: duplicate athlete records, missing measurements, and inconsistent session or game records are surfaced for review, because every downstream metric inherits their defects.

### Core vs Common vs Optional

**Defining core** — without these, not sports performance analytics:

- analyzed performance population
- performance measurement corpus bound to that population
- analysis → insight loop (sport-native metrics, comparison, decision-facing surfaces)

**Standard capabilities** — present in most modern products:

- configurable dashboards; role-based views; drill-down and individual profiles
- longitudinal analysis; benchmarks and thresholds; export/share
- multi-source ingestion; live session monitoring (in device-led products)

**Common variants / optional** — depends on segment, tier, and posture:

- video linkage; athlete-facing read views; data-quality tooling
- AI/ML layers (injury-risk models, generated player summaries)
- consumer/individual tier products beside team products
- API/file delivery of computed data for clubs' own tools

## Interfaces

The following surfaces are described in conceptual terms. Exact layouts and names vary by product.

### Squad dashboard / daily status

The staff's primary entry surface.

- per-athlete and squad-level indicators (load, readiness, availability, flags), current-session or current-week context
- primary actions: scan for outliers, drill into an athlete, export or share the view

### Individual performance profile

The longitudinal view of one athlete.

- measurement history across sessions and seasons, comparisons against squad or position benchmarks, current status
- primary actions: review trends, compare against peers or norms, export the profile

### Analysis / dashboard builder

Where analysts construct the views.

- widget libraries (tables, charts, event tables, pitch views), metric selectors, filters (time ranges, groups, event types), saved templates
- primary actions: create and edit dashboards, save templates, configure metrics

### Live session monitor

The sideline surface during training or matches (in products that offer it).

- real-time group and individual effort, session progress, alerts on configured limits
- primary actions: monitor effort, adjust session parameters, flag athletes in real time

### Report / export surface

- scheduled or on-demand reports, printable and shareable outputs, data exports
- primary actions: generate, share, print, export

### Data management / integrations

- connected devices and third-party sources, import queues, mapping of data to athletes and sessions
- primary actions: connect sources, import files, resolve mapping and quality issues

### Admin / settings

- roster and org structure, roles and permissions, metric configuration, integration credentials

### Athlete view (optional)

- a read-facing app or portal where an athlete sees their own measurements and trends

## Important Rules / Behaviors

### The analytics app informs decisions; it does not assign work

The system's output ends in human decisions. It does not plan, assign, or track training as managed work — that is the neighboring Athlete Management System's loop. In organizations that run both, the analytics layer feeds the staff who then act in the management system. This division is visible in the market: vendors that sell both ship them as separate products or separately licensed solutions.

### Comparability requires consistent measurement

Comparisons across athletes and time are only meaningful when the underlying measurements were collected the same way — same devices, same protocols, same processing. This is why products emphasize data accuracy and validated collection, and why a change of device or method is treated as a break in the record rather than a seamless continuation.

### The metric layer is derived, not entered

Most of what staff see is computed from raw capture. When raw capture is missing or wrong, the derived metrics inherit the defect — which is why aggregation-heavy products expose data-quality views (duplicates, missing data, coverage) as a first-class surface.

### Role-based visibility, with a medical privacy wall where medical data is analyzed

Access follows role and group. Where medical data flows into the analysis layer, a structural boundary separates restricted clinical detail from coach-facing summaries: performance and coaching staff see availability and burden, not medical narrative.

### Live and post-session are two modes of one corpus

Live monitoring during a session and post-session analysis read the same measurement model; live views trade depth for immediacy. Products differ in how much analysis happens in the moment versus after download, but the corpus is one continuous record either way.

### The corpus is longitudinal and durable

The record persists across sessions and seasons; its value compounds with history. Longitudinal comparison — this season against last, this athlete against their own baseline — is a core payoff, not an afterthought.

## Variants

The Type is realized in several recognizable shapes:

- **Wearable-first athlete monitoring** — the vendor ships the measurement devices and the analysis platform together; live session monitoring is strong; the corpus is dominated by physical load data (e.g., GPS/LPS/heart-rate tracking platforms for elite and pro teams, with scaled-down tiers for smaller organizations and youth)
- **Platform-agnostic aggregation layer** — the analytics layer sits on top of whatever systems the organization already runs, unifying device feeds, medical records, testing, and scheduling data into role-based dashboards; often one module of a wider suite
- **Match/event-data analytics** — the corpus is collected match event and tracking data; analysis centers on match output, opposition, and player evaluation; commonly delivered as a platform plus APIs and data files
- **Physiology-first monitoring** — the corpus centers on internal-load measures (heart-rate-derived metrics) for squad training management
- **Tier variants** — elite/pro platforms, collegiate deployments, high-school and youth products, tactical/defense programs; the same core at different scale and compliance postures
- **Delivery variants** — SaaS analysis platform; embedded analytics inside a management suite; data-plus-API delivery into clubs' own tools

A variant remains a **Variant** unless it changes users, core objects, workflow, or rules so much that the core model no longer applies — as happens when the center of gravity moves to opposition/tactical match content (Tactical Analysis territory) or to recruitment evaluation of external players (Sports Scouting territory).

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Athlete Management System | sibling, frequently bundled | the AMS owns the programming loop (plan → assign → deliver → track → adjust) and the managed roster; analytics owns the measurement corpus and insight loop and assigns nothing. AMS products embed reporting; analytics-first products do not run programs |
| Fitness Assessment Application | upstream input | the assessment app owns the structured testing event (protocol, administration, interpretation); analytics consumes test results as one stream among many |
| Athlete Injury / Availability Management | upstream input | owns the medical episode record and clearance decisions; analytics reads availability and burden from it behind a privacy wall |
| Sports Video Analysis | complementary | video editing, tagging, and review are the center there; here video is a linked context for data insights |
| Tactical Analysis Platform | adjacent, drift seam | centers on opposition/tactical content of matches; performance analytics centers on athlete/team performance measurement. Match-event analytics products drift toward this Type when opposition content becomes the center |
| Sports Scouting Platform | adjacent, drift seam | centers on recruitment evaluation of external players; player-evaluation modules inside analytics products drift toward it |
| Race Timing System | different object | produces official competition results for events; analytics consumes performance measurements for preparation decisions |
| Wearable Fitness Platform | different user model | centers the individual consumer's self-tracked data; this Type is staff-facing analysis over an organizational population |
| Dashboard Platform / BI | generic neighbor | could chart the same numbers but lacks the sport-native data model (athletes, sessions, matches, load, positions) and the performance-decision loop |

The most important boundary is with the **Athlete Management System**: the two Types share the athlete population and often the same vendors. The structural difference is what the system manages as work — the AMS manages preparation (programming, delivery, adjustment); performance analytics manages measurement and insight. Remove the programming loop from an AMS and the remainder drifts toward this Type; add one to this Type and it becomes an AMS.

## Representative Products

- Catapult (Vector / OpenField, Athlete Monitoring) — wearable-first load analytics with its own device line; elite professional teams down to high-school tiers
- Hudl Signal — cloud athlete-monitoring analytics with automated data processing and video-analysis integration; professional clubs and universities
- STATSports (Sonra / Apex) — wearable-first live and post-session monitoring for elite and professional teams, with an individual tier
- Kitman Labs (My iP) — enterprise reporting and visualization layer unifying performance, medical, and development data inside a wider platform; elite clubs, collegiate, leagues, defense
- Hudl Statsbomb — match event-data analytics platform for match analysis, opposition scouting, and player evaluation in professional football

The defining core was checked across the wearable-first, aggregation-layer, and match-data postures, and against spreadsheet-era and early-desktop equivalents, so the definition does not depend on any one data-source fashion, customer tier, or era.

## Sources

Research date: **2026-09-09**

- Catapult — Athlete Monitoring: https://www.catapult.com/solutions/athlete-monitoring
- Catapult Support (help center): https://support.catapultsports.com/hc/en-us — including the Vector OpenField Software category, the Console Dashboards & Visual Analytics section and article, and the Athlete Monitoring fundamentals section
- Hudl Signal: https://www.hudl.com/en_gb/products/signal
- Hudl Statsbomb: https://www.hudl.com/en_gb/products/statsbomb and https://www.hudl.com/en_gb/products/statsbomb/platform
- Kitman Labs — iP: Intelligence Platform: https://www.kitmanlabs.com/platform/ and My iP: https://www.kitmanlabs.com/platform/sports-analytics-reporting/
- STATSports — Sonra: https://statsports.com/sonra
- CoachMePlus (boundary reference): https://coachmeplus.com/

> Sourcing limitation: one intended sample (a physiology-first team analytics vendor) was unreachable — its site is a JavaScript-only application — and was dropped rather than reconstructed from memory. STATSports and CoachMePlus were observed at official product-page level only, so capabilities attributed to them are stated at that strength. Vendor-published numeric claims (event counts, integration counts, metric counts) were treated as marketing figures and are not stated as facts in this document. Precise metric formulas, thresholds, and plan-specific limits were not verified at documentation level and are deliberately not asserted.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary review against the neighboring sports-software Types are recorded in the paired Research Notes.
