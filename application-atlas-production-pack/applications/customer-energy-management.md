# Customer Energy Management

## Overview

A **Customer Energy Management** application is the software through which the user of energy — a household or a business customer — observes, understands, and acts on **their own premises' energy usage and cost**. It collects or receives the customer's energy data (meter readings, in-home monitoring, connected devices), turns it into cost and usage insight, and drives action: changing behavior, automating or controlling devices, choosing rate plans, and participating in utility programs.

Two realization poles share the same structure:

- **utility-provided customer tools** — energy insights and self-service experiences that an energy utility offers to its customers under the utility's brand, usually embedded in or connected to the utility's website and account;
- **customer-owned energy products** — applications that come with home energy monitors, connected plugs, solar/battery systems, or EV chargers, operated by the customer directly.

The defining core is deliberately smaller than the modern feature set. Real-time data, smart-meter feeds, device control, solar and battery integration, neighbor comparison, AI assistants, and bill payment are all widespread but none of them is what makes the software customer energy management. A utility portal showing monthly usage from monthly meter reads — and even the older tradition of mailed home energy reports comparing a household to its neighbors — sits on the same defining loop.

## Users & Context

The primary user is the **energy customer**: the person (or business) who pays for and uses the energy at a specific premises — a home, an apartment, a shop, a small facility.

Typical reasons to open the application:

- see how much energy the premises used and what it cost — this month, this week, today
- find out what is using the energy: which appliances, which circuits, which times of day
- check whether the current bill is trending higher than usual and what to do about it
- compare usage against previous periods or similar households to judge whether it is reasonable
- decide and act: turn things off, schedule or automate devices, shift usage to cheaper hours, pick a better rate plan, join a utility program
- for customers with solar or batteries: see production, self-consumption, grid imports and exports, and decide how to store, use, or sell energy

Secondary actors depend on the pole:

- in utility-provided tools, the **utility** configures and operates the experience on behalf of its customers (branding, programs, rates), and its **service agents** may use the same data to answer customer questions
- in customer-owned products, **household members** may share access to the same premises, and in business usage a customer may grant colleagues (facility or finance staff) access to the energy data
- device **installers** (solar, monitors) often have their own separate professional surfaces; the customer-facing application remains the customer's

The usage context is the customer's own life or business operations: the application is opened occasionally (a bill arrives, an alert sounds, a new device is installed) rather than operated continuously like a control room.

## Core Model

### The Defining Core

```text
The Customer's Premise  (the energy user's own site — home or business location,
                         bound to a utility account or to the customer's devices)
└── Energy flows made visible to the customer
    │   consumption recorded over time (meter / monitor / plug data)
    │   + production, storage, grid exchange where present
    └── Rates and tariffs applied → cost and savings
    └── Insight machinery (comparisons, forecasts, alerts, tips, goals,
        device-level detail) whose purpose is customer action
        └── Action: behavior change · device control & automation ·
            rate/plan choice · program participation
```

Three properties. If any one is removed, the product is no longer recognizable as this Type:

- **Customer-side operation on one's own energy.** The operator is the energy customer acting on their own premises — not an organization managing a portfolio of buildings, not a utility managing the grid, not a program managing events. The data, the decisions, and the benefits all belong to the customer.
- **The premise's usage made visible to the customer as data over time.** The customer's consumption exists in the application as recorded, browsable history attached to their site. Without this, the product is a marketing page or a device remote control, not energy management.
- **The insight → action loop.** The application exists to turn usage into findings — cost, comparisons, forecasts, anomalies, advice, goals — and those findings into customer action. An application that only displays raw data (a passive data feed) or only switches devices (a controller without usage visibility) falls out of the Type.

### Standard Capabilities

These are common across mature products but do not define the Type:

- **Cost machinery** — rates and tariffs attached to usage so energy becomes money: flat rates, time-of-use periods, demand charges, solar buyback credits. In some products the customer configures the tariff themselves; in utility-provided tools the tariff comes pre-integrated.
- **Comparison machinery** — this period vs last period vs the same period a year ago; usage against similar households (neighbor comparison is the utility-pole signature); usage against the customer's own goals or expectations.
- **Proactive outreach** — alerts when a bill is trending high, weekly or monthly usage summaries, notifications about anomalies, energy-saving tips, program and plan offers. Much of the value is delivered to a customer who is not looking at the app.
- **Device-level detail** — which appliance or circuit is using what: learned device identification, per-plug or per-circuit monitoring, or named devices behind the meter.
- **Bill relationship** — bill forecasts, bill-to-bill comparisons, usage data aligned to billing cycles and exportable for the customer's own analysis. The bill itself remains the utility's document; payment typically lives in the billing self-service, not here.
- **Action surfaces** — in customer-owned products: device control and automation (schedules, price- and solar-aware operation). In utility-provided tools: rate-plan comparisons and enrollment, program participation, personalized recommendations.
- **Multi-surface delivery** — mobile app as the primary surface, web as companion; account features such as sharing access to the same premises with other household members or colleagues.

### One Structure, Many Implementations

```text
Concept:                The customer's premise
Utility-pole form:      the utility account and its service point
Customer-owned form:    the "Home" / site defined around the customer's devices

Concept:                Usage data source
Implementations:        utility meter feed (AMI / smart meter), panel-mounted
                        monitor, smart plugs, solar/battery/EV gateway

Concept:                The action leg
Implementations:        advice and goals (behavioral), rate-plan choice and
                        program enrollment, direct device control and
                        automation, storage/EV orchestration
```

A reader who has only seen one pole (for example, a utility's usage web page) should be able to recognize the other pole (a homeowner's app controlling plugs and batteries) as the same Type, because the premise + visible usage + insight-to-action loop is intact in both.

## How It Works

### Energy data comes under the customer's view

```text
Identify the premise (utility account connection, device installation, or both)
→ usage data begins flowing (utility feed, monitor, plugs, gateway)
→ history accumulates under the customer's account
```

Setup establishes *whose* energy this is: the customer connects their utility account, or installs their own monitoring hardware, or both. Data cadence depends on the source — real-time where a monitor or smart meter feed exists, monthly where only monthly reads exist. The core loop does not depend on cadence.

### The insight loop

```text
Usage recorded over time
→ rates applied → cost (total, per device, per period)
→ comparisons: over time · against similar homes · against goals
→ findings: trends, high-bill risk, energy hogs, anomalies, savings opportunities
→ delivered in-app and proactively (alerts, updates, tips, reports)
```

The recurring questions the loop answers are the customer's questions: *Is my bill going to be high? What is using the energy? Is something wrong? What should I change?* Mature products answer them before the customer asks — a high-bill alert sent mid-cycle is the classic example.

### The action loop

```text
Findings → customer decides → acts
    behavior:   turn off, replace, change habits (advice and goals support this)
    devices:    schedule, automate, or directly control (customer-owned pole)
    money:      choose a rate plan, shift usage to cheaper hours,
                optimize solar self-consumption or battery dispatch
    programs:   enroll in utility efficiency, demand-response, or electrification offers
→ the effect shows up in the usage data → the next insight cycle sees it
```

In utility-provided tools the action leg is mostly advisory and programmatic — recommendations, plan comparisons, enrollment, and (in some deployments) program-controlled devices as a separate capability. In customer-owned products the action leg is often automated: devices respond to prices, schedules, panel limits, and surplus solar without per-event human action. Both are the same loop with different automation depth.

### The prosumer extension

For customers with solar, batteries, or EVs, the picture extends from consumption to flows:

```text
production + storage + grid import/export tracked beside consumption
→ self-consumption optimization (use your own energy first)
→ storage dispatch against rates and weather
→ managed EV charging against panel capacity and price windows
→ savings and independence metrics computed from the same flows
```

## Interfaces

The following surfaces are described conceptually; exact names and layouts vary by product.

### Home / premise dashboard

The entry surface: current usage (and, where present, production/battery state), costs, savings, and status at a glance. Primary actions: drill into usage, check alerts, jump to a device or a bill view.

### Usage explorer

Charts of consumption (and flows) over time with period switching and drill-down — year → month → day → hour; by total, by device, by circuit. Primary actions: change period, filter by device, compare periods, export data.

### Bill view

The cost story of the current billing cycle: forecast to date, comparison against the previous bill or the same bill a year earlier, sometimes the bill document itself. Primary actions: inspect the forecast, compare bills, understand what drove the change. (Bill *payment* belongs to the billing self-service, not here.)

### Device breakdown

What each appliance, circuit, or plug is doing: live and historical per-device usage, learned or metered device lists. Primary actions: inspect a device's usage, rename/merge detected devices, follow an energy hog over time.

### Alerts & messages

The proactive surface: high-bill warnings, usage updates, anomaly notices, tips, and program offers. Primary actions: read, act on the recommendation, configure notification preferences.

### Rates & plans

The money-decision surface: time-of-use tracking, rate-plan comparison with personalized cost estimates, plan switching or program enrollment where the energy seller supports it. Primary actions: configure the tariff, compare plans, enroll.

### Goals

Customer-set targets (reduce usage, cut peak-time usage) with progress tracking over time. Primary actions: create a goal, track progress, adjust.

### Device control (where present)

Schedules and automations for connected loads — plugs, chargers, thermostats, batteries — with the energy logic (prices, solar, limits) applied by the application. Primary actions: schedule, automate, override.

### Settings & access

Account, premise configuration, utility connection, device management, sharing access with other household members or colleagues, notification and data preferences (including data export and deletion).

## Important Rules / Behaviors

### The customer sees their own energy only

Everything in the application is scoped to the customer's own premise: data arrives by way of the customer's utility account authorization or the customer's own devices, and sharing is explicit (household members, invited guests, business colleagues). There is no browsing of other people's energy.

### The application complements the bill; it is not the bill

In-app cost figures are computed from metered or monitored data and configured rates — useful estimates, not billing documents. Products say this in various ways: insights arrive "in addition to receiving a bill", exports are "aligned with utility billing cycles", bill figures are "forecasts". Where accuracy matters (reconciliation, expense claims), the customer falls back to the utility bill and exports the underlying data.

### Fair comparison needs context

Comparisons are only meaningful with normalization: neighbor comparisons are made against *similar* homes; time-of-use tracking requires the rate periods to be configured; period-over-period comparisons are shaped by weather and occupancy in more mature products. An application that compares without context misleads — products therefore invest as much in the comparison setup as in the comparison itself.

### Proactive delivery is structural, not cosmetic

The customer is passive most of the time. Alerts (high-bill risk, anomalies), scheduled summaries, and program offers are how the loop actually reaches the customer; an insight that nobody sees changes nothing. Notification configuration is correspondingly a first-class surface.

### The action leg is bounded by the energy seller's world

In utility-provided tools, what the customer can act on (plans, programs, rebates) is whatever the utility offers; rate education and program enrollment follow the utility's catalog. In customer-owned products, automation operates within physical and safety limits (panel capacity, device constraints) and configuration changes typically require explicit user confirmation. The application does not silently rewrite the customer's energy contracts or override safety limits.

### Cadence follows the data path, and the data path does not change the Type

Real-time is a property of the data source (monitor, smart-meter feed), not of the Type. Monthly-read portals serve the same defining loop at monthly cadence.

## Variants

- **Utility-provided customer engagement** — the energy seller offers white-label web/mobile energy tools: usage insight, bill forecasting, alerts, tips, rate education, program marketing. Deployed as embedded widgets, branded pages, or apps; serves residential customers and, in a distinct business variant, small and midsize commercial customers with demand-level insights, data export, and delegated access.
- **Customer-owned home energy products** — the customer buys monitoring/control hardware (panel monitor, plugs) and gets an app: device-level insight, automation, and increasingly battery/EV orchestration. Insight-first and control-first philosophies both occur.
- **Prosumer / DER-integrated** — solar, battery, and EV charging woven into the household energy picture: self-consumption optimization, storage dispatch, import/export tracking, independence metrics.
- **Business-customer self-service** — commercial customers monitoring their premises' energy with demand-oriented analytics and multi-person access; sits closest to the building-energy-management seam.
- **Program-heavy pole** — the application as the front door to utility demand-side programs (efficiency, time-of-use shifting, demand response events), including event-day participation prompts and rewards.
- **Retail-plan extension** — in deregulated markets, the same customer relationship extending into selling electricity plans shaped to the customer's devices (EV charging windows, solar buyback).
- **Regional shapes** — time-of-use regimes, in-home display pairings, utility smart-meter programs that remove the need for customer-installed hardware, and data-portability exports that let customers take their usage data to third-party tools.

A variant stays a variant while the defining loop — own premise, visible usage, insight → action — remains the center. When the user becomes an organization managing a portfolio of buildings, the product has become building energy management; when the money side (billing and payment) becomes the center, it has become the billing system's customer surface.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Building Energy Management | adjacent (organizational pole) | BEM's user is an organization managing a *portfolio* of buildings (facility/energy manager role); here the user is the energy customer managing their *own* premises. A business customer managing one site's own energy sits here; an estate with portfolio analytics and verification workflows sits there. |
| Building Management System | adjacent | real-time control of building plant is primary there; here the customer's own energy picture is primary |
| Advanced Metering Infrastructure / Meter Data Management | upstream | utility-side metering and data collection; consumer portals built on that data are optional extensions of AMI, and the customer-facing management application is this Type |
| Utility Billing / Customer Information System | adjacent | billing owns accounts, tariffs-of-record, and payment; this Type's bill involvement is insight (forecast, comparison, export), not billing transactions |
| Demand Response Platform | adjacent | the DR platform owns utility-side program/event machinery; this Type carries the customer-facing participation experience as a capability |
| EV Charging Network Management | adjacent | charging-network operations vs home charging as one managed load inside the household energy picture |
| Energy Management System (utility domain) | namesake only | grid/utility-scale control and operations — different domain, different users |
| Energy & Carbon Management | adjacent | enterprise carbon accounting and decarbonization planning across all activities; household/business footprint estimates here are an optional derived view |
| Smart-home / thermostat applications | drift seam | comfort-centric device control is not energy management; the energy framing (usage, cost, savings) is the discriminator — control without usage visibility falls out of this Type |
| Solar/DER system monitoring | drift seam | production-first array monitoring for system owners is device monitoring; when production joins the household's energy decisions, it becomes this Type's prosumer pole |
| Personal Finance Management | different domain | PFM records money movements; this Type manages energy usage with cost as one derived view |

The most important seam is with **Building Energy Management**: the two share measurement-and-analysis machinery, and the discriminator is the operator-object relation — the customer acting on their own energy versus an organization acting on a building portfolio.

## Representative Products

- **Oracle Utilities Opower (Digital Self Service – Energy Management)** — the utility-provided pole: white-label customer energy engagement for residential and business customers, from bill forecasting and neighbor comparison to rate coaching
- **Emporia Energy** — the customer-owned pole with full control/automation: panel-level monitoring, smart plugs, EV charging, battery, and tariff-aware automations
- **Sense** — the insight-first pole: real-time home energy monitoring with learned device identification, from either a utility smart meter or an in-panel monitor
- **Enphase (Enphase App)** — the prosumer pole: solar production, battery, EV charging, and grid flows managed beside consumption

## Sources

Research date: **2026-09-07**

- Oracle Utilities — product catalog: https://www.oracle.com/utilities/
- Oracle Utilities — Opower Digital Engagement: https://www.oracle.com/utilities/products/opower-engagement/
- Oracle Help Center — Digital Self Service – Energy Management: https://docs.oracle.com/en/industries/utilities/digital-self-service/
- Emporia Energy — Home Energy Management Platform: https://www.emporiaenergy.com/home-energy-management/
- Emporia Help Center — Energy Management / Emporia App collections: https://help.emporiaenergy.com/en/
- Sense Help Center — "How Does Sense Help Me Save Energy and Money?", "How Sense Learns About Your Home's Energy Use": https://help.sense.com/hc/en-us
- Enphase — Enphase App: https://enphase.com/homeowners/enphase-app ; Enphase Support & Assistant FAQ: https://support.enphase.com/s/

> Sourcing limitations: no second utility-provided vendor was directly reachable during research (utility customer-experience suites returned HTTP 403 / timeouts), so vendor-specific mechanics of the utility pole (neighbor-comparison mechanics, business analytics details, export formats) rest on one vendor and are stated cautiously. Regional implementations (EU supplier apps, UK in-home-display ecosystems, Japan HEMS) were not directly examined; statements about them are kept general. No precise numeric limits, default settings, or vendor-published performance statistics are asserted in this document.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample check are recorded in the paired Research Notes.
