# Push Notification Marketing Platform

## Overview

A **Push Notification Marketing Platform** is a marketer-side platform for composing, targeting, delivering, and measuring **push notifications** — short messages that the mobile operating system or web browser renders on the user's device on behalf of the marketer's app or website.

The defining core is a four-part loop:

```text
Compose a push notification
  → target an audience of opted-in app/browser users
    → deliver through the OS/browser push services
      → measure delivery and engagement
```

What makes this Type distinct from other campaign-messaging Types is the **channel mechanics**, not the campaign grammar it shares with email or SMS marketing:

- delivery is mediated by the operating system or browser (platform push services such as the Apple and Android push services and the web push protocol), not by an inbox or carrier;
- the audience is addressed through **device/browser registrations** (push tokens) that the platform maintains, not through personal contact addresses;
- the user must grant **notification permission at the OS/browser level** before they can be reached — the platform's reachable audience is by construction the opted-in subset;
- the message is a **transient banner/alert surface**, not a persistent inbox item.

Everything commonly bundled with modern products — journey automation, A/B testing, in-app messaging, email and SMS channels, AI copywriting — is standard or optional capability layered on this core, not what makes the product a push marketing platform.

## Users & Context

**Primary users** are marketing and growth teams of companies that operate a mobile app and/or a website:

- **Mobile app marketers** re-engage users outside the app (promotions, content, reminders, win-back), drive feature adoption, and recover abandoned funnels.
- **Web publishers** reach browser audiences without requiring an app install.
- **Lifecycle/CRM marketers** run onboarding, activation, and retention programs against app audiences.
- **Product marketers** announce features and updates.

**Secondary users** are developers, who perform the one-time integration the channel requires: registering the app/website with the platform, configuring credentials with the OS push services, and embedding the platform's SDK so devices can register and events can flow. Marketers then work day-to-day without engineering help.

The work context is campaign operations: planning sends against audience segments, composing and testing message variants, scheduling and automating delivery, monitoring results, and managing the health of the permission-based audience.

## Core Model

### The defining core

```text
Push Notification (composed message)
└── Audience (opted-in app/browser users)
    └── Device/browser registrations (push tokens) held by the platform
        └── Delivery through OS/browser push services
            └── Campaign (the send: broadcast / scheduled / triggered)
                └── Delivery & engagement measurement
```

- **Push notification** — the message object: a title and body rendered by the OS/browser, optionally with an image, action buttons, a launch/deep-link target, and a custom data payload for the app to process. Two structural sub-forms exist across products: **display notifications** (visible alerts) and **silent/data notifications** (wake the app for background work without showing anything).
- **Audience registry** — the platform's record of who can be reached: each user's app installs and browser opt-ins are registered as addressable device entries (push tokens). Products commonly unify multiple device registrations under one person record keyed by an external ID from the marketer's own systems, so a "user" may carry several reachable devices.
- **Opt-in state** — because the OS/browser gates delivery behind a permission, the platform tracks, per user and per device, whether notification permission has been granted, whether the user has expressed a messaging preference, and whether a valid registration still exists. A user can match every targeting criterion and still be unreachable if permission or a valid registration is missing — reachability, not segment membership, determines who actually receives a message.
- **Campaign** — the unit of sending: a composed message bound to an audience and a delivery plan (send now, at a scheduled time, on a recurring schedule, when a user performs an action, or when called via API).
- **Measurement** — per-campaign reporting of sends, deliveries, opens/clicks, and downstream conversions, plus audience-level views (reachable users, opt-in rates, uninstalls in some products).

### Targeting data and segments

Around the registry, mature products maintain the data that makes targeting possible:

- **Tags / attributes / custom properties** — marketer-defined values attached to users or devices (preferences, tier, language, app version).
- **Events** — actions taken in the app or website (viewed, added to cart, purchased), used both to build segments and to trigger sends.
- **Device properties** — automatically collected facts such as language, timezone, OS version, app version, and notification permission status.
- **Segments** — saved, dynamically evaluated groups defined by filters over the above data (with AND/OR logic). Segments update as users behave, and products show the estimated or exact audience size — usually split into reachable (opted-in, valid registration) and unreachable members.

### Standard capabilities of mature products

These are widespread across the researched sample and expected in the market, but they are additions to the core rather than its definition:

- **Journey/automation builders** — multi-step, multi-message flows with entry criteria, waits, splits, and exit conditions.
- **A/B testing and experimentation** — variant distribution across a test group with automatic winner selection, fixed-percentage split delivery, and control groups/holdouts for measuring incremental impact.
- **Delivery governance** — per-user frequency capping, quiet hours/do-not-disturb windows, send-rate throttling for very large audiences, message expiration windows for offline devices, and per-timezone or optimized per-user send times.
- **Message design machinery** — rich media, action buttons, badges, sounds, deep links, collapse/replace semantics (a newer message replaces an older one on the device), localization, personalization tokens, and reusable templates.
- **Consent and preference management** — opt-in prompt tooling (including in-app "primers" shown before the OS prompt), opt-out handling, topic-level subscription lists, and preference centers.
- **Multi-channel expansion** — the same audience and campaign machinery extended to email, SMS, in-app messages, and chat messengers. All researched products ship this; pure push remains the historical and definitional center.
- **Integration fabric** — connections to analytics tools, CRMs, CDPs, and data warehouses; event streaming; webhooks; REST APIs for programmatic sending and audience management.

### One structure, many implementations

```text
Concept:   Reachable audience
Implementations:  device push tokens, browser push registrations,
                  unified person records over multiple devices

Concept:   Permission state
Implementations:  OS notification permission per device, browser permission,
                  user-level subscription preference, topic-level subscription lists

Concept:   Campaign trigger
Implementations:  manual send, calendar schedule, recurring schedule,
                  user action/event trigger, inaction trigger, API call
```

## How It Works

### Connect the app or website (one-time setup)

```text
Create a project/workspace in the platform
→ register credentials with the OS push services (and web push keys for websites)
→ embed the platform SDK in the app / site
→ devices begin registering themselves as they install and open the app
→ verify with a test device
```

From this point the audience registry grows automatically as people install the app, open it, and grant (or decline) notification permission.

### Build the audience

```text
Targeting data arrives (SDK events, attributes, imports, integrations)
→ define filters (behavior, properties, device facts, past message engagement)
→ save as a segment or select ad hoc
→ review audience size and the reachable (opted-in) portion
→ optionally exclude segments or reserve a control group
```

### Compose and test the message

```text
Create a campaign
→ write title/body (optionally from a template or with AI assistance)
→ add image, buttons, deep link, custom data
→ personalize per user; add language variants
→ preview on device types; send test pushes to test devices/profiles
→ optionally set up A/B variants or split delivery
```

### Deliver

```text
Choose the delivery plan:
  send now  |  scheduled time  |  recurring schedule
  |  triggered by user action/event  |  triggered via API
→ platform evaluates the audience at send time
→ messages queue through the OS/browser push services to each registered device
→ delivery controls apply (frequency caps, quiet hours, throttling, expiration)
→ a send can usually be cancelled while still in flight;
  already-delivered notifications generally cannot be recalled,
  though some can be replaced via collapse semantics
```

### Measure and iterate

```text
Campaign report: sent → delivered → opened/clicked → conversions (goal events)
→ audience views: opt-in rate, reachable users, uninstalls (in some products)
→ iterate: duplicate the campaign, adjust copy/timing/audience
→ retarget: build a follow-up audience from a previous campaign's responders/non-responders
```

The recurring operational loop is: grow and clean the permissioned audience → target → send → measure → refine.

## Interfaces

Exact layouts and names vary by product; the following surfaces are common.

### Campaign composer

The central working surface.

- Purpose: create a push message and bind it to an audience and delivery plan.
- Typical information: message preview per platform, audience selector with size estimate, schedule options, variant setup.
- Primary actions: compose content, personalize, add variants, schedule or send, test on device.

### Audience / segments

- Purpose: define and maintain who can be targeted.
- Typical information: segment definitions (filters), audience counts split by reachability and platform, per-user profile views (devices, permission state, tags, event history).
- Primary actions: create/edit segments, import audiences, inspect individual users, manage test devices.

### Campaign dashboard / message list

- Purpose: oversee all campaigns and their states.
- Typical information: campaign names, status (draft/scheduled/sending/sent/paused/stopped), key metrics per campaign.
- Primary actions: create, duplicate, pause/resume, cancel, archive, view report.

### Analytics / reports

- Purpose: quantify delivery and impact.
- Typical information: delivery and open/click rates, conversion goals, funnel and retention views, audience trends (opt-in rate, uninstalls where offered).
- Primary actions: filter by campaign/date/platform, define conversion goals, export or stream data.

### Channel/platform settings (developer-facing)

- Purpose: keep the channel technically alive.
- Typical information: OS push-service credentials and their validity, SDK versions, registered apps/sites, error logs for failed sends.
- Primary actions: configure platforms, rotate credentials, diagnose delivery errors.

### Consent surfaces

- Purpose: win and manage permission.
- Typical information: prompt designs, subscription states per user, preference center configuration.
- Primary actions: configure prompts/primers, manage opt-out and topic subscriptions.

## Important Rules / Behaviors

### Permission gates everything

The single most important rule of the Type: **no OS/browser permission, no delivery**. A user can satisfy every segment condition and remain unreachable. Products therefore expose reachability explicitly (reachable vs. total audience) and treat opt-in rate as a first-class metric. Losing permission (or an expired/invalid device registration) silently removes a user from the reachable audience.

### Reachability has three parts

Products commonly distinguish: (1) the user's messaging preference held by the platform, (2) the OS/browser-level permission on a specific device, and (3) the existence of a valid device registration. All three must hold for a push to be deliverable to that device. A change on the device (e.g., permission revoked in system settings) does not always propagate instantly to the platform's records — a known source of delivery surprises.

### The audience is evaluated at send time

For scheduled and triggered sends, segment membership is evaluated when the send runs, not when the campaign is created — the audience reflects who qualifies at that moment.

### Delivery is best-effort and transient

Push delivery depends on device connectivity and OS behavior: offline devices receive a message only within its validity window (if one is set); the OS controls rendering, truncation, grouping, and do-not-disturb behavior; delivered notifications are transient banners, not inbox items. The platform can report what the OS push services confirm, and some products verify on-device display, but ultimate display behavior belongs to the OS.

### Frequency discipline is structural

Because the channel interrupts the user on the marketer's behalf, mature products build in delivery discipline: per-user frequency capping and send-rate throttling are near-universal; quiet-hours/do-not-disturb windows and per-campaign overrides are common. Over-messaging has a visible cost: users revoke permission or uninstall, shrinking the reachable audience — which is why opt-in rate and uninstall tracking appear as platform metrics.

### Consent is managed, not assumed

Opt-out and preference changes must be honored and synced back into the platform's records. The platform's record of a user's messaging preference and the device's actual OS-level permission are two different states, and some products require explicit synchronization between them — making consent-state management an explicit operational duty rather than an automatic background behavior.

### Cancellation has limits

A queued send can typically be cancelled; a delivered notification generally cannot be recalled. Replacement (rather than removal) is possible only where collapse semantics were set on the message.

## Variants

- **Pure-play push platforms** — push (mobile + web) as the center, with lighter adjacent channels; typically self-serve, from free tiers up to mid-market.
- **Omnichannel engagement suites** — push as one channel inside a broader customer-engagement platform (email, SMS, in-app, messengers, journeys, CDP-like data features); typically enterprise, contract-based.
- **Mobile-first vs web-first** — products originating from app push vs products treating browser push as a first-class equal.
- **Analytics-led engagement platforms** — the platform doubles as the app's behavioral analytics system of record, with campaigns built on top of its own event store.
- **Regional-platform variants** — support for regional Android push ecosystems and regional chat messengers, important in specific geographies.
- **Location-driven variants** — geofence/geozone-triggered push for apps whose use cases are place-sensitive (retail, mobility).
- **OS-surface extensions** — live-updating notification surfaces (e.g., ongoing activity cards) and rich interactive notification styles as add-on capabilities in some products.

A variant remains a variant while the defining loop (compose → opted-in audience → OS-mediated delivery → measure) still describes it. When push becomes merely one channel inside a system whose center is cross-channel orchestration or data infrastructure, the product is drifting toward Marketing Automation / Customer Engagement or CDP territory.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Email Marketing Platform | sibling channel Type | Same campaign grammar (audience → message → schedule → measure), but delivery is inbox-based, addressed by email addresses, persistent, and governed by anti-spam consent rather than an OS permission gate. |
| SMS Marketing Platform | sibling channel Type | Carrier-delivered, phone-number-addressed, per-message telecom costs and telecom consent regimes; no OS permission gate or device registration layer. |
| Mobile Marketing Platform | broader umbrella | Includes paid user acquisition, app-store optimization, mobile advertising, and other channels; the push platform is one owned channel's machinery within that umbrella. |
| Marketing Automation Platform | overlapping capability | Channel-agnostic orchestration of journeys and lifecycle programs (often email-centric, lead-oriented). Journey builders appear in push platforms too, but the push platform's identity is the push channel's audience registry and delivery mechanics. |
| Marketing Campaign Management Platform | adjacent | Manages campaigns across channels, teams, budgets, and approvals; does not itself own device registrations or OS push delivery. |
| In-app Messaging | bundled sibling surface | Renders inside the running app, requires no OS notification permission, and cannot reach users when the app is closed. Frequently sold in the same product; structurally a different delivery surface. |
| Customer Data Platform | data-layer neighbor | CDPs are identity-resolution and data infrastructure; push platforms consume/activate that data for messaging. Some push platforms add CDP-like features, blurring positioning but not the structural seam. |
| Push messaging infrastructure (developer gateways) | upstream substrate | OS/vendor push services and developer messaging consoles move notifications but lack the marketing layer — no audience registry, campaign lifecycle, or marketing measurement. Adding that layer is exactly what creates this Type. |

The sharpest boundary is with the developer push gateway: **remove the marketing layer (audience registry + campaign + measurement) and this Type becomes a messaging utility; remove the push channel mechanics (swap in inbox/carrier delivery) and it becomes an email or SMS marketing platform.**

## Representative Products

- OneSignal — pure-play push/web push, self-serve
- Braze — enterprise customer-engagement suite with push as flagship channel
- Airship — enterprise mobile-first push pioneer
- CleverTap — mobile analytics-led engagement platform
- Pushwoosh — pure-play push with broad channel and regional coverage

The definition was checked against the category's older, push-only generation and against developer-grade push gateways (as negative cases) to avoid over-fitting to today's omnichannel, AI-heavy market.

## Sources

Research date: **2026-09-07**

Official product documentation (Tier-1):

- OneSignal Documentation — https://documentation.onesignal.com/docs/ (Push overview; Segments)
- Braze User Guide — https://www.braze.com/docs/user_guide/home/ (Push subscription states; messaging fundamentals)
- Airship Docs — https://www.airship.com/docs/ (Your audience; Push notifications)
- CleverTap User Docs — https://docs.clevertap.com/docs/push-notifications (Create Message — Push)
- Pushwoosh Documentation — https://docs.pushwoosh.com/product/ (User guides; How to send push notifications)

> Sourcing note: all five samples were researched from live official documentation with no access failures. Precise operational numbers (payload size limits, scheduling horizons, variant counts, plan-gated limits, retention windows) vary by product and plan and are intentionally not stated in this document; they are recorded, where observed, in the paired Research Notes.

Detailed product-by-product observations, the cross-product comparison matrix, and the boundary analysis are recorded in the paired Research Notes.
