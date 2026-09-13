# Research Notes — Employee Recognition Platform

## Research Goal

Understand what an Employee Recognition Platform actually is as an Application Type: its defining core structure, its standard mature capabilities, its variants, and its boundaries against the neighboring §09 workforce Types (Employee Engagement Platform, Employee Experience Platform, Performance Management, Employee Communication Platform).

## Initial Boundary

Hypothesis before research:

- Core use: employees give each other named, attributed appreciation ("recognition") inside an organization-scoped program, often tied to company values and often paired with points redeemable for rewards.
- Primary users: all employees as givers/receivers; HR program administrators as program owners; managers as high-volume givers.
- Nearest neighbors: Employee Engagement Platform (survey/measurement-centered), Employee Experience Platform (umbrella consolidation), Performance Management (formal evaluation), Employee Communication Platform (org-authored distribution), Benefits/Compensation administration.
- Known sibling-pass flags to verify:
  - employee-engagement-platform pass: WorkTango ships Recognition & Rewards as a separate bundleable product; Culture Amp/Officevibe bundle recognition as secondary modules; test = remove the measurement loop → recognition platform remains.
  - employee-experience-platform pass: recognition is one of the domains EX platforms consolidate.

## Research Questions

1. What is the core object, and what attributes does a recognition event carry?
2. Is the points/rewards economy definitional or a common (configurable) layer?
3. Who can give recognition to whom (peer-to-peer, top-down, budgets, approvals)?
4. How do company values / reasons / badges work — required or optional?
5. What does the social layer look like (feed, reactions, comments)?
6. How do milestones (birthdays, anniversaries, service awards) relate to the core?
7. What does the admin side govern (program settings, eligibility, moderation, reporting)?
8. What are the delivery surfaces (web, mobile, chat integrations)?
9. Where is the boundary to engagement/survey platforms and to performance management?

## Representative Products

| Product | Segment / philosophy | Why selected |
|---|---|---|
| Bonusly | SMB/mid-market; recognition-first with a playful points economy | Best-in-class public help center (Tier-1 operational docs) |
| Awardco | Mid-market/enterprise; rewards-catalog philosophy ("world's largest configurable reward network") | Different center of gravity: rewards infrastructure |
| Achievers | Enterprise recognition suite (Recognize / Reward / Celebrate) | Enterprise-tier program science; survey modules sold separately |
| Workhuman | Large enterprise; recognition-as-culture-practice heritage (service milestones, consulting) | Oldest lineage (Globoforce); social-recognition philosophy |

Sample intentionally spans segment (SMB → enterprise) and philosophy (points-native → rewards-catalog → culture-practice).

## Sources

### Tier 1 — official operational documentation (fetched 2026-09-06)

- Bonusly Help Center root: https://help.bonus.ly/en/
- Bonusly — "How to give recognition": https://help.bonus.ly/en/articles/7216623-how-to-give-recognition
- Bonusly — "How do Bonusly points work?": https://help.bonus.ly/en/articles/357124-how-do-bonusly-points-work
- Bonusly — "Managing Program Settings": https://help.bonus.ly/en/articles/9458206-managing-program-settings
- Bonusly — "Managing Peer-to-Peer Recognition Settings": https://help.bonus.ly/en/articles/9458998-managing-peer-to-peer-recognition-settings
- Bonusly — "For All Users" collection (article inventory incl. Recognition + Redeeming Rewards collections): https://help.bonus.ly/en/collections/20728-for-all-users

### Tier 2 — official product pages (fetched 2026-09-06)

- Bonusly product pages: https://bonusly.com/ , https://bonusly.com/product/recognition
- Awardco homepage + recognition platform page (incl. on-page FAQ): https://www.awardco.com/ , https://www.awardco.com/platform/employee-recognition
- Achievers homepage (platform module structure: Recognize / Reward / Celebrate / Voice of Employee / Pulse surveys): https://www.achievers.com/
- Workhuman homepage + platform page: https://www.workhuman.com/ , https://www.workhuman.com/platform

### Cross-references (from sibling passes, same research date)

- research/employee-engagement-platform.md (WorkTango two-product evidence; Culture Amp/Officevibe bundling)
- research/employee-experience-platform.md (recognition as consolidated EX domain)

### Source-access limitations

- Achievers help center, Awardco help center, and Workhuman customer community were not fetched (product pages + FAQ only for these three vendors). Operational mechanics for them are asserted at positioning/structure level only.
- No precise numeric facts (allowance sizes, catalog sizes, country counts, exchange rates) from marketing pages are promoted into the final document; the only precise mechanics in this file come from Bonusly Tier-1 docs and are marked product-specific.

---

## Product Observations

### Bonusly (evidence layer: A — directly observed, Tier-1 docs)

**Recognition post (the core object) — "How to give recognition":**
- Ingredients: recipients (individuals via @, or groups such as team/department/location/everyone, "depending on how your organization set up Bonusly"), optional points or a custom currency ("if your company uses points… Preset amounts may be available based on admin settings. If your program doesn't require points… you can leave this out"), a written reason ("what did they do, and why did it matter?"), and hashtags connecting recognition to company values/themes/priorities (admin-set, with descriptions visible in the picker).
- Composer ("Givebox") sits on top of the home feed; recognition can also be given from Microsoft Teams, Slack (bot; coaching gauge not available there), Google Chat bot, mobile.
- Optional enrichments: GIF/emoji, image/audio/video, link preview, tagging additional people, "Post-Wrap" gift-wrap decoration.
- After posting: appears on the home feed and notifies recipients. Edit/delete within 24 hours of posting; amount not editable if spent; amount/recipients not editable if comments exist; nothing editable if created in a previous month. (product-specific rules)
- Coaching: "Gratitude Gauge" scores drafts on five dimensions (specificity, impact, values alignment, personalization, authenticity) but never blocks posting. (vendor-specific)
- Moderation: users can hide or report a recognition post (dedicated help article exists).

**Points economy — "How do Bonusly points work?":**
- Two balances: **giveable** points (monthly allowance for recognizing others; resets each budget period; unused expires; admin-grantable boosts; managers get additional allowance per direct report) and **redeemable** points (earned when recognized; do not expire by default; spent in the rewards catalog).
- Redeemable sources: peer recognition, celebrations (birthdays, work anniversaries, new-hire welcomes), company-awarded bonuses/incentives. "Lifetime earnings" tracked.
- Catalog: gift cards, charitable donation, curated gifts, custom rewards, cash-equivalent (PayPal), Points Boost re-conversion.
- Zero-point mode explicitly documented: "Some teams run Bonusly without giveable points — for example, paid programs that focus on recognition messages and rewards without a per-user point allowance." Monthly allowance can be set to 0; giveable-balance UI auto-hides. → points are configurable, not definitional, even in the most points-native product.

**Admin program governance — "Managing Program Settings" / "Managing Peer-to-Peer Recognition Settings":**
- Points can be renamed ("high fives to rainbows"); fixed exchange rate to base currency (10:1; product-specific); orgs may allow recognition without points.
- "Points visibility" setting hides point amounts in feed posts/notifications/reports while recipients still receive them.
- Company-value hashtag modes: company-value required / any-hashtag required / optional; up to 12 value hashtags with descriptions (product-specific cap); hashtag analytics feed "Achievements" per value.
- Monthly allowance defaults uniform across users; custom allowance rules by department/location/role (from HRIS-imported properties); per-direct-report manager allowance; one-time allowance boosts; suggested give amounts.
- Reports: Recognition Activity Report (every post, hashtag filterable, CSV export), Recognition Quality Score Report (named in related articles).

**Suite surface:** product modules beyond recognition — Rewards, Celebrations (automated milestones), Check Ins (1:1s), Growth, Insights (people analytics); Slack/Teams/email/mobile delivery. (from product pages + help collection inventory)

### Awardco (evidence layer: A for on-page claims/FAQ; positioning level otherwise)

- Self-description: "employee recognition and rewards platform"; platform modules: Recognition, Rewards ("world's largest configurable reward network"), Celebrations ("automating everyday moments and milestones"), Incentives ("custom incentives to drive behavior for any goal"), Benefits & Perks, Awardco Intelligence (AI), Awardco Engage (surveys/feedback — a separate module like engagement platforms).
- Recognition modes on one platform: Spot Recognition (peer-to-peer, manager-to-team, social visibility), Service Awards (automated milestone workflows, global delivery), Performance Incentives (goal-linked), Nominations, External Recognition™ (from customers/patrons), AwardCodes™, Lifestyle Spending Accounts, Onboarding, Birthdays/Special Occasions.
- FAQ (structural gold): supports peer-to-peer and manager-to-employee recognition and nomination programs; "Organizations can design moments that are more public, more private, more social, or more structured"; recognition "tied to company values, milestones, or program rules" configurable; rewards = "employees choose their own reward from a catalog of millions of options" with client-curated catalogs; deskless/offline recognition and outside-in recognition supported.
- Integrations: Slack/Teams recognition, SSO ("One login"), mobile-first, bi-directional Workday partnership, Amazon Business reward fulfillment.
- MemoryBooks™ (keepsakes of coworker shoutouts), A-Pay card. (vendor-specific)

### Achievers (evidence layer: A for homepage claims; positioning level otherwise)

- Self-description: "enterprise recognition platform with a global rewards marketplace."
- Platform modules: **Recognize** ("non-monetary and monetary recognition; nomination-based individual and team awards"), **Reward** (rewards marketplace; points-based; experiences/merchandise/gift cards), **Celebrate** (service awards, milestone cards, "automated onboarding recognitions"). Plus adjacent modules: Communications, Employee Connections, Voice of Employee, Pulse surveys (the engagement half, sold as additional features — consistent with the engagement-pass boundary finding).
- Enterprise posture: HRIS/Workday embedding, Slack/Microsoft/Zoom integrations, deskless and frontline reach, external recognition for frontline.

### Workhuman (evidence layer: A for platform-page claims; positioning level otherwise)

- Platform modules: **Social Recognition** ("peer-to-peer employee recognition that fuels culture, engagement and productivity"), **Service Milestones** (work anniversaries), **Community Celebrations**, **Life Events**, **Conversations** (continuous performance development), **Workhuman iQ** (insights).
- Capabilities: Admin Hub ("tracking and sharing program success to delegating and permissions"), Global Rewards store (worldwide distribution), Inclusion Advisor (AI bias-coaching on recognition messages), Integrations, Team Awards, Frontline Recognition.
- Product UI described on the platform page: dashboard greets the user to "recognize someone today," recognition updates for named people, "Recognize" and "Redeem" actions, and "notifications about approvals" — award approval workflows visible to end users. Award example carries a value tag ("Teamwork") with like/comment counters.
- Heritage: longest-standing enterprise lineage (Globoforce-era service awards), consulting practice, program-participation commitments.

---

## Cross-product Comparison

| Structure / capability | Bonusly | Awardco | Achievers | Workhuman | Judgment |
|---|---|---|---|---|---|
| Organization-scoped population of identified employees | A | A | A | A | Core |
| Recognition event: identified sender → identified recipient(s) + written message | A | A | A | A | Core |
| Reason/occasion layer: values / behaviors / award type attached to the event | A (value hashtags, 3 admin modes) | A (values/rules configurable per FAQ) | A (award types; Recognize module) | A (value-tagged awards) | Core (the *attachment* is core; requiring it is L1 config) |
| Persistent attributed recognition history + program surface (feed/profile) | A (home feed, profile, recaps) | A (social visibility; MemoryBooks) | A (platform + analytics) | A (newsfeed-style UI, award history) | Core |
| Points + redemption catalog | A (dual-balance; zero-point mode exists) | A (marketplace; client-curated) | A (Reward module; non-monetary also exists) | A (Global Rewards store) | Common mature structure (near-universal, but non-monetary/zero-point programs are documented) |
| Automated milestones: birthdays / anniversaries / service awards / new hires | A (Celebrations) | A (Celebrations, Service Awards) | A (Celebrate) | A (Service Milestones, Life Events) | Common mature structure (module, not definition) |
| Nominations / formal awards | (not sampled) | A (Nominations) | A (nomination-based awards) | A (Team Awards) | Common |
| Admin console: program settings, allowances/budgets, rules | A | A (program rules per FAQ) | A (admin controls referenced) | A (Admin Hub) | Common |
| Moderation (hide/report), visibility config (public/private) | A (hide/report article; visibility per settings) | A (public/private per FAQ) | (implied; not asserted) | (implied; not asserted) | Common (only two products directly evidenced) |
| Approvals on awards | (not evidenced) | (not evidenced) | (not evidenced) | A (approval notifications in UI) | Optional / variant |
| Chat integrations (Slack/Teams), mobile, notifications | A | A | A | A (integrations capability) | Common |
| HRIS/SSO integration as population source | A (HRIS properties for allowance rules) | A (Workday bi-directional) | A (Workday embedding) | A (enterprise deployments) | Common |
| Program analytics (participation, values trends) | A (Insights, activity report) | A (real-time reporting claim) | A (built-in analytics) | A (Workhuman iQ) | Common |
| Surveys / listening as adjacent module | A (Check Ins ≠ surveys; no survey module sampled) | A (Awardco Engage) | A (Voice of Employee, Pulse) | (not sampled; iQ is analytics) | Vendor suite extension — NOT part of this Type |
| Performance/1:1 modules | A (Check Ins, Growth) | (not sampled) | (not sampled) | A (Conversations) | Vendor suite extension — NOT part of this Type |

## Abstraction Hierarchy

### L0 — Defining Invariant

```text
Organization-scoped employee population (identified individuals)
└── Recognition event: attributed sender → addressed recipient(s)
    + written message + an occasion/reason (value, behavior, or award type)
    └── Persistent, attributed recognition history per person
        └── surfaced on an organization-facing program surface
            (visibility governed by program configuration)
```

Four properties. Remove any one and the product stops being an Employee Recognition Platform:

1. **Organization-scoped population of identified members** — senders and receivers are real, identified employees of a defined organization (not anonymous users, not customers).
2. **Attributed directed recognition event** — a named sender recognizes named recipient(s) with a message; recognition without attribution is just content posting.
3. **Persistent attributed history** — recognition accumulates as a durable record per person (profile/recaps/award history), not ephemeral chat.
4. **Program-level surface** — recognition is displayed and browsable across the organization/program under configured visibility; this is what makes it a *platform program* rather than private messaging. (Private recognition moments exist, but they are configuration within a visible program, not the whole surface.)

Deliberately excluded from L0 (tested against the historical/sample check below): points, rewards catalogs, values-hashtag mechanics, feeds' social reactions, milestones, approvals, chat integrations.

### L1 — Common Mature Structure

- **Points economy** — giving allowances/budgets + redeemable balances + rewards catalog (gift cards, merchandise, experiences, charity, cash equivalents). Present in all four sampled products and near-universal in the market, but explicitly configurable: Bonusly documents zero-point allowance programs; Achievers markets non-monetary recognition. Concept: *optional monetary weight attached to the recognition event*.
- **Values / reasons taxonomy** — program-configurable set of values/behaviors/award types the sender attaches; admin-configurable from optional to required (Bonusly hashtag modes; Awardco FAQ; Workhuman value-tagged awards).
- **Milestones & celebrations** — automated birthdays, work anniversaries, service awards, new-hire welcomes, sometimes with physical/global fulfillment.
- **Nominations & formal awards** — nomination workflows culminating in awards (Awardco, Achievers, Workhuman).
- **Social layer** — reactions/comments on recognition posts; group recognition; media/GIF enrichment.
- **Admin console** — program settings (currency naming, visibility, taxonomy), allowance/budget rules by org attributes, suggested amounts, moderation (hide/report), reporting.
- **Delivery surfaces** — web home feed + composer, mobile apps, chat integrations (Slack/Teams), notifications.
- **Integrations** — SSO; HRIS sync as population source-of-truth (attributes drive eligibility/allowance rules); chat/embed.
- **Analytics** — participation rates, values frequency/trends, recognition quality scores, leaderboards.

### L2 — Variant / Optional Structure

- Monetary posture: points-with-allowance vs points-with-central-budget vs zero-points message-first; currency naming metaphor; expiry rules.
- Recognition scope: internal employees only vs external givers (customers/patients — Awardco External Recognition) vs deskless/offline recognition.
- Visibility defaults and moderation posture (public-first vs configurable private moments).
- Service-award depth: physical keepsakes, global shipping, MemoryBooks-style artifacts.
- Suite posture: standalone recognition product vs recognition bundled inside engagement/EX suites (WorkTango, Culture Amp, Viva/Workvivo per sibling passes).
- Adjacent modules sold beside recognition: surveys/listening, communications, 1:1s/performance, benefits/perks, incentives.
- Segment packaging: SMB self-serve vs enterprise with consulting/implementation programs.
- Global rewards fulfillment: multi-country/multi-currency catalogs.

### L3 — Vendor-specific (kept out of the final document)

- Bonusly: Givebox, Gratitude Gauge (five dimensions), Bizy AI sidekick, Post-Wrap, dual-balance giveable/redeemable points, 10:1 exchange rate, 12-value-hashtag cap, 24-hour edit window, month-creation edit lock, timezone fallback for resets, per-direct-report manager allowance, Points Boost, Recognition Quality Score Report, Hubot integration.
- Awardco: MemoryBooks™, AwardCodes™, External Recognition™, Lifestyle Spending Accounts, A-Pay card, Amazon Business catalog, "Return on Recognition" framing.
- Achievers: Recognize™/Reward™/Celebrate™ module names, Achievers Intelligence, Employee Connections.
- Workhuman: Workhuman iQ, Conversations, Human Intelligence™, Inclusion Advisor, Community Celebrations naming, ROI guarantee, consulting practice.

## Rejected Findings

- "Recognition platforms *are* points-and-rewards systems" — rejected. The most points-native sampled product documents zero-point programs; a sampled enterprise product markets non-monetary recognition as first-class. Points → L1.
- "Recognition platforms include surveys/engagement measurement" — rejected as definition. Two sampled vendors ship surveys as clearly separate modules; the sibling engagement pass showed the reverse bundling. Surveys → suite extension (L2).
- "Peer-to-peer only" — rejected: top-down, team, nomination, and even external recognition are documented modes in the sample.
- "Recognition = public always" — rejected: Awardco FAQ explicitly documents configurable private moments; Bonusly supports hiding/reporting and private-ish flows. Visibility is program governance, not invariance.

## Boundary Findings

1. **vs Employee Engagement Platform (sibling §09)** — confirms the engagement-pass flag: engagement platforms center a measurement loop (survey programs → aggregated results → action), and bundle recognition as a secondary module (Culture Amp/Officevibe) or sibling product (WorkTango's separate Recognition & Rewards product); recognition platforms center the recognition event loop and bundle surveys only as adjacent modules (Awardco Engage, Achievers Voice of Employee). Structural test: remove the measurement loop → the recognition platform remains fully functional; remove the recognition event → the survey platform remains. Two Types, heavy bundling in both directions — flagged for joint review.
2. **vs Employee Experience Platform (sibling §09)** — consistent with the EX pass: recognition is one of the domains EX suites consolidate. EX umbrella positioning over this Type; no structural conflict.
3. **vs Performance Management Platform (§09)** — recognition is informal, frequent, values-anchored appreciation with no evaluative record, ratings, cycles, or goal objects. Performance suites (and Bonusly Check Ins / Workhuman Conversations) add evaluation machinery as adjacent modules. A recognition platform does not produce performance-of-record outputs.
4. **vs Employee Communication Platform (§09)** — opposite authorship direction: communication platforms distribute organization-authored items to targeted audiences; recognition platforms collect peer-authored individual events. Consistent with the comms-pass flag.
5. **vs Compensation / Total Rewards (§08)** — the rewards layer is a closed, program-governed economy of small-denomination recognition currency, not payroll, incentive compensation, or benefits administration. No compensation-of-record object exists here.
6. **vs consumer Loyalty / Rewards platforms (§05.15)** — same "points + catalog" machinery, different population (customers vs employees) and different occasion (purchases vs workplace behavior); no directory conflict.
7. **Service-milestone programs** — the oldest recognition form (service anniversary catalogs predate all software sampled). Modern products implement milestones as an automated module. Kept as L1: a recognition platform without any milestone module still satisfies L0.
8. **Terminology observation** — the market sells this Type as "employee recognition software/platform" and "rewards and recognition (R&R) platform"; "rewards" names the L1 redemption layer of the same Type, not a separate Type. No separate directory leaf exists, so no conflict.

## Uncertainties

- Approvals: directly evidenced only in Workhuman's UI (approval notifications). Likely common in enterprise programs (large monetary awards), but asserted only as optional/variant.
- Private recognition mechanics: Awardco FAQ confirms configurability; per-product visibility models (who sees what: company/department/manager) were not researched in depth.
- Whether any mainstream product exists that lacks a feed-style program surface entirely (i.e., pure award-issuance engines) — not found in the sample; if one exists it would stress L0 property 4.
- Tax treatment of rewards (grossing-up, payroll integration) varies by jurisdiction and was not researched; no claims made in the final document.
- Achievers/Awardco/Workhuman help centers not fetched; their mechanics are documented at structure level only (recorded under Source-access limitations).

## Final Synthesis

An Employee Recognition Platform is an organization-scoped program application in which identified employees give each other attributed recognition — a directed event (sender → recipient(s)) carrying a written message and an occasion/reason — and in which those events accumulate as a persistent, attributed, browsable history on a program surface. Around that core, mature products add a configurable monetary layer (points/budgets and a redemption catalog), a program-configurable values/reasons taxonomy, automated milestones and service awards, nominations, a social layer, an admin console (allowances, rules, visibility, moderation, reporting), delivery through web/mobile/chat, and analytics. The monetary layer is the most market-visible feature but is not definitional: zero-point and non-monetary programs are documented by the sampled vendors themselves. Surveys/listening, performance, and communications appear only as adjacent suite modules sold by the same vendors, which fixes the boundary with the engagement/comms/performance Types.
