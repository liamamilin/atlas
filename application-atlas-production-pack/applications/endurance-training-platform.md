# Endurance Training Platform

## Overview

An **Endurance Training Platform** is a system of record for the endurance training process. It holds the athlete's planned training schedule as the governing object, captures completed workouts against that plan, and accumulates the resulting training state over time — so that the next planning decision is informed by what training has actually happened, across one or several endurance sports (running, cycling, swimming, triathlon, rowing and related disciplines).

The defining structure is small:

```text
Athlete (+ optional Coach)
└── Training plan / calendar — the plan of record, persisting across the season
    └── Planned workout — prescribed before it is executed
        └── Completed workout — captured against the prescription
            └── Accumulated training state — load, fitness and trends over time
                └── feeds the next planning decision
```

Everything else commonly associated with these products — power and heart-rate metrics, structured interval files, trainer-platform sync, adaptive AI planning, wellness data, team social walls — is widespread in current products but is not what makes the product this Type. A coach mailing weekly plan sheets that an athlete answers with a completed training diary satisfies the same structure without any of those specifics.

When the center of gravity shifts to a single sport's activity record (the ride, the run, the swim as the unit of record), the product is drifting toward a sport-specific training application. When software itself performs the coach loop — composing and adapting training as its defining property — the product is drifting toward an AI fitness coach.

## Users & Context

The primary user is an **endurance athlete training toward goals** — recreational to elite — who trains on a schedule over weeks and months rather than exercising ad hoc. Typical reasons to open the platform:

- see today's prescribed workout and the state of the surrounding week
- record or sync a completed workout against what was planned
- check accumulated training state (fitness, load, progression) and upcoming target events
- adjust the plan when life intervenes — missed sessions, extra sessions, illness, travel

The second primary user is the **coach** (independent coach, coaching business, team or club coach), who prescribes on one or many athlete calendars, reviews completed training and feedback, and adjusts the program. Teams and clubs use the same machinery at group scale.

The work environment spans the whole training week: web and desktop for planning and deep analysis, mobile for daily glance-and-record, companion surfaces on watches, head units and indoor training equipment for executing prescribed workouts.

## Core Model

### The Defining Core

Three structures. If any one is removed, the product is no longer recognizable as an endurance training platform:

- **The planned training schedule as plan of record.** A dated, persistent calendar of prescribed workouts that exists *before* execution and accumulates across weeks and the season. Someone authors it — the athlete, a human coach, a template or marketplace plan, or an algorithm — but the author is not what defines the object. Without a governing plan the product becomes a workout tracker that logs the past.
- **The workout as a planned-vs-completed unit.** Each planned workout can be executed — indoors on a trainer, outdoors, guided or free — and its completion is captured by device/file sync or manual entry and held *against the prescription*. That the platform can always express "what was planned vs what was done" is the loop's hinge. Without it the product becomes a plan-delivery service or a disconnected log.
- **Accumulated training-state accounting.** Completed training aggregates over time into load, progression and state views — however computed or however much is delegated to the coach's judgment — and those views feed the next planning decision. The platform, not a spreadsheet beside it, carries the training state across the season. Without it the product becomes a one-shot plan generator.

### Standard Capabilities of Mature Products

These capabilities are common across mature products and make the core loop practical. They are not what makes the product an endurance training platform:

- **Thresholds and zones per sport** — personal threshold values (such as functional threshold power, lactate threshold heart rate, threshold pace) anchor intensity; zones derived from them drive both prescription and analysis. Changing a threshold re-derives the athlete's metrics.
- **Structured workout builder** — an editor that composes workouts as interval steps with targets (power, heart rate, pace, cadence), plus export/sync of those structured workouts to watches, head units and training platforms.
- **Two-way device and platform sync** — planned workouts pushed out to execution devices; completed activities pulled in automatically from watches, cycling computers and training platforms.
- **Performance modeling over the accumulated record** — fitness/fatigue/form-style charts, power-duration curves, weekly and seasonal summaries; the best-known formulation charts daily training stress as short-term fatigue, long-term fitness, and their difference as "form" for timing a peak.
- **Event targeting and periodization** — dated goal events with priorities; the season organized into phases (a base → build → specialize-style arc) that build fitness, sharpen it for the event's demands, then shed fatigue to peak.
- **Plan and workout libraries** — reusable workout libraries, saved full plans, and template or marketplace catalogs from coaches.
- **Coach attachment and feedback** — an athlete can be attached to a coach (or share access), the coach prescribes directly on the athlete's calendar, and both sides exchange comments, messages and attachments bound to specific workouts.
- **Roster management** — multi-athlete and multi-calendar views for coaching businesses, teams and clubs.
- **Wellness and recovery intake** — sleep, resting heart rate, HRV-class data from wearables, shown alongside the training record.

### One Structure, Many Implementations

The Core Model is written in conceptual terms. Implementations vary by product and era:

```text
Concept:            Plan of record
Implementations:    hand-built calendar, coach-prescribed calendar,
                    adopted template/marketplace plan, algorithm-generated plan

Concept:            Completion capture
Implementations:    automatic device/platform sync, structured-workout file
                    import (FIT/ZWO/ERG-class formats), manual entry,
                    guided indoor execution recorded by the platform itself

Concept:            Accumulated state
Implementations:    computed fitness/fatigue/form charts and power curves,
                    weekly/monthly summaries, coach-reviewed training diaries
```

A reader who has only seen an algorithmically adaptive, cycling-first product should still be able to recognize a coach-prescribed, paper-era or multi-sport program from the Core Model alone.

## How It Works

### Set up the athlete

```text
Create athlete profile
→ declare the sports trained
→ set personal thresholds per sport (power, heart rate, pace)
→ zones derive from thresholds
```

Thresholds are the anchor: per-sport metrics, zone targets and load accounting are computed relative to them. Mature products watch the completed record and suggest threshold updates when performances imply a change.

### Put a plan on the calendar

Four entry paths into the same plan-of-record:

```text
Build it:        season planner / plan builder around goal events and available time
Adopt it:        choose a template or marketplace plan and apply it to the calendar
Receive it:      an attached coach prescribes workouts directly onto the calendar
Generate it:     an algorithm composes and continually adapts the plan
```

Plans are periodized toward the athlete's dated, prioritized events: general base fitness first, more event-specific work next, then a taper that sheds fatigue faster than fitness so the athlete arrives at the event fresh. Plans and workouts can be copied, saved to libraries, and reused across athletes or seasons.

### The daily loop

```text
Open today's prescription on the calendar
→ execute it (guided indoor session, structured workout on a watch,
   or a free run/ride/swim)
→ completion syncs back automatically (or is entered manually)
→ the platform compares completed vs planned
→ the workout card shows compliance
```

The comparison is visible rather than implied: workouts are marked against planned duration, distance or training load, and unplanned sessions are recorded and folded into the record rather than ignored. Deviation is expected — the loop is designed to survive missed sessions, extra group rides, illness and travel, whether the response is a coach's comment, the athlete's own edit, or automatic re-planning.

### Analyze and adapt

```text
Per workout:  intensity, load, zones, intervals, curves
→ aggregated: weekly totals, fitness/fatigue/form trends, power curves, seasonal comparison
→ decision:   adjust upcoming workouts — by coach, athlete, or the system itself
```

Analysis closes back into planning. A coach reads the athlete's completed week and comments; a self-coached athlete drags upcoming sessions around; an adaptive system re-computes the plan from what actually happened. The record — not memory — carries the season.

### The coach loop

```text
Attach coach ↔ athlete (share or request access)
→ coach prescribes onto the athlete's calendar from libraries
→ athlete executes; completions sync in
→ coach reviews dashboards across the roster; comments per workout
→ program adjusted week by week
```

For teams and clubs the same machinery operates over group calendars, with team-level communication surfaces.

### Core vs Common vs Optional

**Defining core** — without these, not this Type:

- planned-first training calendar (plan of record)
- workout as planned-vs-completed unit
- accumulated training-state accounting
- multi-sport endurance scope

**Standard capabilities** — widespread in current products:

- thresholds + zones, structured workout builder + export
- two-way device/platform sync
- fitness/fatigue/form performance modeling
- event targeting with periodization
- plan/workout libraries and marketplaces
- coach attachment, feedback, roster management
- wellness/recovery data intake

**Variant / optional** — depends on product philosophy and customer:

- who adapts the plan (human coach / self-coached athlete / algorithm)
- dominant sport lens (cycling-first, triathlon-rooted, any-sport)
- native indoor execution (guided player, trainer control, virtual riding world) vs export-only
- team/club layer (social walls, attendance rosters)
- adjacent domains (strength training, nutrition, virtual racing)
- commercial posture (free community, athlete premium, coach-paid tiers) and extensibility (open API, custom charts)

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Training calendar

The platform's center.

- days and weeks holding planned workout cards, completed activities, metrics and events
- planned-vs-completed compliance visible on the cards; weekly summaries alongside
- primary actions: add/move/copy workouts, apply plans, add events and goals, open any workout

### Workout detail

Two depths in most products.

- quick view: summary metrics, planned description, execution guidance, pre/post comments
- expanded analysis: charted data streams, zone and interval breakdowns, map/curve views, attachments
- primary actions: inspect, comment, edit, attach files, download originals

### Plan builder / season planner

The plan-of-record authoring surface.

- goal events with dates and priorities, available training time, current state
- produced output: a periodized schedule laid onto the calendar, editable by drag or wizard
- primary actions: generate, recalculate, adjust blocks, save as template

### Analysis dashboard / performance chart

The accumulated-state surface.

- fitness/fatigue/form-style charts over the season, power-duration curves, weekly totals, configurable chart libraries
- primary actions: change ranges and sports, compare seasons, extract trends

### Athlete home

The daily-glance surface.

- time to the next priority event, today's prescription, current form/state, upcoming workouts, recent bests
- primary actions: open today's workout, view events and goals

### Workout builder

The structured-prescription editor.

- interval steps with targets per stream (power/HR/pace), save to library, export/sync to devices
- primary actions: compose, target, save, sync

### Coach console

The roster surface for coaches, teams and clubs.

- multi-athlete/multi-calendar views, per-athlete dashboards, communication inboxes, plan libraries
- primary actions: prescribe, review, comment, message, monitor

### Settings — zones, devices, connections

The configuration backbone.

- thresholds and zones per sport, connected devices and platforms, notification and unit preferences

## Important Rules / Behaviors

### The plan precedes the workout

Prescription comes first in the object model: a completed workout is recorded *against* a planned one. Unplanned training is captured too, but is visibly marked as unplanned — the distinction between the plan and what actually happened is a first-class, user-visible state.

### Compliance is explicit

The platform compares completed values with planned values and surfaces the result on the record (color or score). Exact thresholds for what counts as "on plan" vary by product.

### Thresholds anchor the metrics

Per-sport threshold values drive zone and load computation. When a threshold changes, derived metrics change with it; mature products detect likely threshold changes from performances and offer to apply them. Stale thresholds quietly distort every derived number — a known operational risk of the Type.

### The loop absorbs imperfection

Missed workouts, extra sessions, sickness and travel are recorded as deviations and folded back into planning rather than breaking the record. The adaptation response differs by product philosophy — coach judgment, athlete edit, or automatic re-planning — but the record itself is never silently rewritten.

### Adaptation authority is a philosophy, not a feature flag

Products differ on who moves the plan: a human coach, the athlete, or the system. Most products allow more than one authority at once (a coach adjusting an algorithm-generated plan, for instance).

### Capture has a fallback

Device and platform autosync is the default capture path, but manual entry and file upload preserve the loop when devices are absent — historically the original path, and still supported across the sample.

## Variants

- **Coach-first platforms** — the coach↔athlete relationship is the product's center of gravity; roster tools, plan libraries and coaching-business features dominate; athletes can also run self-coached (e.g. TrainingPeaks, Final Surge)
- **Self-serve adaptive platforms** — the algorithm is positioned as the athlete's coach; plan generation and adaptation are automatic; human-coach layers are absent or light (e.g. TrainerRoad)
- **Analytics-first community platforms** — deep analysis and open extensibility lead, with planning and coaching layers added around them; often free or community-funded (e.g. Intervals.icu)
- **Team/club platforms** — group calendars, social walls, attendance and communication machinery for teams and coaching businesses (e.g. Final Surge)
- **Sport-lens variants** — the same structure with a cycling, triathlon, or running-first emphasis, or any-sport generality; the dominant lens shapes the metric vocabulary but not the underlying model
- **Indoor-execution variants** — native guided workout players and trainer control, bundled virtual-riding worlds, or export-only postures that rely on external execution platforms
- **Adjacent-domain bundles** — strength training modules, nutrition and fueling machinery, virtual racing and spectator dashboards layered on the same record

A variant remains a variant unless it changes the unit of record: a product centered on the single-sport activity rather than the training plan belongs to a sport-specific Type, and a product whose defining property is software performing the coach loop belongs to AI fitness coaching.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Running / Cycling / Swimming Training Application | sport-specific siblings organized around the activity record (the run/ride/swim as unit of record, with the sport's own data semantics); here the workout-in-plan is the unit and sport activities are inputs to the training process |
| Workout Tracking Application | logs workouts after the fact with no governing plan-of-record and no season arc |
| Workout Programming Application | composes prescriptions but does not close the loop with captured completions, accumulated state and season periodization in endurance terms |
| AI Fitness Coach | software performing the coach loop is the defining property; here adaptation authority is a variant, and the managed training record is the center |
| Online Fitness Coaching / Personal Training Management | centers the coaching relationship or coaching business for general fitness; here the training-process record is the center and coach machinery is one layer within it |
| Wearable Fitness Platform | device-hub centered on general health/wellness data; here wearables are data sources feeding the training record |
| Fitness Progress Tracker | centers body-metric progress (weight, measurements) rather than the training process |
| Race Management Platform | organizer-side event operations; here events appear only as athlete-side targets the plan is built around |
| Nutrition Coaching Platform / Meal Planning | centers the nutrition process; nutrition appears here only as an adjacent module |

The most heavily traveled seam is with the sport-specific siblings (Running/Cycling/Swimming). The structural test: remove the planned-first calendar and accumulated training state — if what remains is still the product's center (the activity record with its sport semantics), it is a sport application; if what remains is a log, it is this Type's neighbor the workout tracker.

## Representative Products

- TrainingPeaks — coach↔athlete multi-sport training system of record; source of the industry's load-metric vocabulary
- TrainerRoad — self-serve adaptive training with structured-workout execution (cycling lens)
- Intervals.icu — free, community-built, analytics-first platform with open API
- Final Surge — coach/team-side platform for coaching businesses, teams and clubs

The Core Model was checked against the paper-era and coach-by-mail pattern (plan sheets + training diary + standing coach review) to avoid defining the Type by today's device-connected implementation.

## Sources

Research date: **2026-09-07**

- TrainingPeaks — product root https://www.trainingpeaks.com/ ; Athlete User Guide https://www.trainingpeaks.com/learn/trainingpeaks-athlete-user-guide/ ; education articles "What is TSS?" and "What is the Performance Management Chart?" (trainingpeaks.com/learn/articles/…); Help Center root https://help.trainingpeaks.com/hc/en-us
- TrainerRoad — product root https://www.trainerroad.com/ ; Cycling Training Plans https://www.trainerroad.com/cycling-training-plans/
- Intervals.icu — product root https://intervals.icu/ (feature pillars, integrations, pricing/community)
- Final Surge — product root https://www.finalsurge.com/ ; Features https://www.finalsurge.com/features ; For Coaches https://www.finalsurge.com/coaches

> Sourcing limitations: TrainingPeaks help-center category pages returned 403/timeouts (root and education articles were reachable); TrainerRoad's support site was unreachable (transport error); Intervals.icu feature subpages are JavaScript-rendered (captured via homepage and a fallback page). Assertions from those surfaces are kept at product-page strength, and precise operational details (numeric compliance thresholds, exact load formulas, plan-length constraints, pricing) are intentionally omitted from this document; they are recorded in the Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample breadth check are recorded in the paired Research Notes.
