# Research Notes — Advocacy Platform

## Research Goal

Understand what an **Advocacy Platform** (DIRECTORY §25, Nonprofit/Membership/Religious Organizations) really is as an Application Type: its core objects, actors, workflows, rules, and boundaries — from real products, not from category marketing.

Note on scope: the directory also contains **Customer Advocacy Platform** (§06, Marketing). The two share only the word "advocacy". This research covers the nonprofit/civic "Advocacy Platform"; the §06 leaf is a different domain (customer references/reviews/referrals) and is treated as a boundary case only.

## Initial Boundary

Initial hypothesis before research:

- An Advocacy Platform is software an organization (nonprofit, association, union, chamber) uses to mobilize its supporters/members to take policy-directed actions (contact legislators/officials, sign petitions, post publicly) and to track that participation.
- Likely adjacent/confusable Types:
  - Petition / Public Comment Platform (§24) — public, citizen-side signature collection
  - Civic Engagement Platform (§24) — citizen-side engagement with government
  - Nonprofit CRM (§25) — relationship/donation records, not campaign→action→target loops
  - Email Marketing Platform (§06) — org→audience one-way messaging (advocacy's defining flow is supporter→target)
  - Government affairs / legislative tracking tools — professional staff-side, not supporter mobilization
  - Customer Advocacy Platform (§06) — same word, different domain entirely

## Research Questions

1. What is the central object — campaign? action? What does it contain?
2. Who are the actors, and what distinct surfaces do operators vs action-takers get?
3. How does an action travel from supporter to target (email, call, petition, social)?
4. How are targets identified and matched to supporters (legislative datasets, address lookup)?
5. What lifecycle does a campaign have (draft → live → archived)?
6. What rules govern participation (limits, moderation, deliverability)?
7. What tracking/reporting does the org get?
8. How does the platform relate to the org's CRM/email/list tools?
9. Where is the boundary with petition platforms, civic engagement platforms, and government-affairs suites?

## Representative Products

Selected for market representativeness, different product philosophies, and different customer tiers:

| Product | Positioning / market | Philosophy | Customer tier |
|---|---|---|---|
| **New/Mode** | Nonprofit/union advocacy & engagement platform (Canada-based; US/CA/international datasets) | Multi-channel advocacy tactics for mission orgs; free entry tier up to "Movement Builder" plans | Nonprofits, unions, activist coalitions |
| **One Click Politics (OCP)** | "Comprehensive digital advocacy software" (US-centric; also Canada/Australia/UK) | Full-service advocacy for associations/corporations/chambers/agencies; managed services + software | Associations, corporations, chambers, agencies, nonprofits |
| **Actionable** (at countable.com, by CSAG) | Self-service advocacy platform | Radical self-service: template → publish, no sales call; real-time reporting emphasized | Individuals, small orgs; enterprise tier exists |

Products considered but **not researchable** in this environment (see Sources): Quorum/Phone2Action, VoterVoice, Action Network, Muster, Speak4, Capitol Canary, Rally Congress. These are commonly cited market products; their absence limits cross-product breadth (3 products, one with Tier-1 documentation).

## Sources

Fetched 2026-09-06.

### New/Mode (Tier 1 + Tier 2)
- https://www.newmode.net/ (homepage)
- https://www.newmode.net/solutions (solutions)
- https://www.newmode.net/email (email tool)
- https://support.newmode.net/ (knowledge base index)
- https://support.newmode.net/support/get-started-with-new-mode (campaigning basics index)
- https://support.newmode.net/support/advocacy-action-in-depth-guides
- https://support.newmode.net/support/advocacy-action-general-guides
- https://support.newmode.net/support/new-mode-targeting-and-datasets
- https://support.newmode.net/support/how-do-new/mode-datasets-work
- https://support.newmode.net/support/campaigns (Email & Petition Campaigns)
- https://support.newmode.net/support/creating-your-call-campaign
- https://support.newmode.net/support/moderating-submission-limits

### One Click Politics (Tier 2)
- https://oneclickpolitics.com/ (homepage; features, audiences, case study)
- https://oneclickpolitics.com/advocates-actions/ (advocate acquisition)
- Knowledge base at https://help.oneclickpolitics.com/hc/en-us — **unreachable (timeout ×2)**

### Actionable (Tier 2)
- https://countable.com/ (homepage + FAQ content; note: the countable.com domain currently serves the "Actionable" product by CSAG)

### Unreachable / abandoned (per network-restriction rule)
- https://www.quorum.us/product/grassroots-advocacy/ — JS-rendered, no content
- https://help.quorum.us/ — 403
- https://votervoice.com/ , https://www.votervoice.com/ — transport error ×2
- https://actionnetwork.org/docs , /advocacy , https://help.actionnetwork.org/ — timeout ×4
- https://muster.ngo/ — transport error
- https://www.speak4.com/ — domain parked (for sale)
- https://www.rallycongress.com/ — 403
- https://capitolcanary.com/ , https://phone2action.com/ — transport error
- https://actionkit.com/docs/ — 403

**Sourcing limitation**: only one product (New/Mode) yielded Tier-1 operational documentation. OCP and Actionable evidence is Tier-2 (official product pages). All cross-product claims below are therefore calibrated: single-product operational details are marked product-specific; cross-product claims rest on 2–3 products, one of which is documented only at marketing depth. No model-memory filling of unreachable vendors' operational details.

## Product Observations

### New/Mode (evidence layer A — official help center + product pages)

**Positioning**: "digital activism platform"; homepage triad: **Target** government decision makers (database), **Mobilize** the community (advocacy tools), **Transform** (real-time analytics: "who's engaging, how they take action, which messages drive results"). Audiences: nonprofits, unions, grassroots.

**Campaign model** (KB: Email & Petition Campaigns; Call Campaign):
- Org dashboard → "Create Campaign" → choose **campaign type**: Petition, Email, Call, LTE (letter to the editor), Social media (mentions/hashtags). [A]
- Campaign configuration is a stepped flow: **Recipients → Message → Design → Review → Launch**. [A]
- **Recipient types**: (1) *Individual recipients* — contacted regardless of supporter location; (2) *Group dataset* — location-generated (e.g., "Canadian House of Commons" → supporter's local MP based on entered address); (3) *Custom recipient* — org-added contacts not in the system; must be **publicly available information**. Types can be mixed. [A]
- **Fallback recipient** required when a group dataset is used without an individual recipient — the contact shown/generated when location lookup finds no recipient. [A]
- Max recipients contacted per campaign: **10** (system randomly selects 10 if more are selected). [A — product-specific limit]
- Recipient visibility toggle: recipient info hidden from supporters by default ("greater than 10% improvement in conversion rates" — vendor claim). [A]
- **Message**: call campaigns have Introduction (text-to-speech read to supporter before patching), Talking Points (script displayed on submission), introduction settings (phone number that rings the supporter, TTS voice); all campaign types have an editable **thank-you email** (can be disabled). [A]
- **Design**: campaign form fields (add/edit), extra content, 2- or 3-column layout, theme/colors; separate Campaign design and Thank-you design tabs. [A]
- **Review**: choose hosting (New/Mode-hosted link vs embed on external webpage), thank-you page (provided vs custom URL redirect), **test configuration** (trigger a test phone call, send test thank-you email), review recipients, social share buttons, launch checklist. [A]
- **Launch**: copy campaign link, share to Facebook/X/LinkedIn. [A]
- **Petition vs Email semantics** (KB): Petition = gather support/awareness among supporters, deliver demands to one specific recipient; representatives "notified periodically" — a *contactable* petition recipient is emailed **for every 100 signatures**; a *name-only* recipient is listed symbolically on the form. Email campaign = each submission sent automatically to the supporter's representatives (templated or personalized). [A]
- **Call mechanics**: system rings the supporter's phone, TTS introduction, patches through to recipients; supporter presses "\*" to end the current call and auto-connect to the next recipient. [A]
- **Targeting datasets** (KB: How do datasets work): org chooses a location-based target dataset when creating a tool; contacts are generated when a supporter enters postal code/zip/address; behind the scenes data comes from external sources **scraped once a day**; US coverage from **Google Civic** (federal House/Senate, state lower/upper houses, municipal); **supplementary datasets** fill gaps (e.g., missing Twitter handles); **subscriber-funded custom datasets** (school boards, previously unsupported countries, elections). [A]
- **Submission limits** (KB: Supporter Submission Limits): per-campaign per-supporter limits — defaults: Petition 1, Email 3, LTE 3, Call 10; modifiable (1–10); exceeding shows "you've already participated in this campaign"; org members exempt; cloned campaigns inherit limits; guidance to avoid recipients perceiving spam. [A — product-specific defaults]
- **Moderation**: "Submission Approvals" guide exists; LTE guidance recommends **auto-approval off** so staff review letters before passing to editors. [A]
- **Analytics**: Submissions & Analytics tabs per campaign (progress, download signatures, performance); higher tiers add supporter locations, engagement tips, "Advanced Analytics, Insights and AI driven recommendations". [A]
- **Supporter messaging**: "Message Your Supporters" — email supporters with campaign alerts and progress. [A]
- **Plan tiers**: Individual / Grassroots / Teams / Movement Builder gate features (customization, analytics depth, contacting supporters, call campaigns Teams+). [A]
- **Other**: cloning campaigns (templates), message variations, custom form fields, thank-you pages, import/export contacts, multiple organizations, team members, remove branding, internationalization (French/Spanish), Stripe Connect (campaign funding), Salesforce sync, archiving when finished. [A]

### One Click Politics (evidence layer A for product-page claims — official product pages; no Tier-1 docs reachable)

**Positioning**: "Comprehensive digital advocacy software"; audiences: state/local advocacy, agencies, associations, corporations, chambers of commerce, nonprofits; US + Canada/Australia/UK pages. Claims 22,000+ campaigns managed. [A]

**Model**:
- "Quickly build **custom widgets** for campaigns at **Legislators, Custom Targets and Regulators**." [A]
- **Multi-Action Tool**: "emails, patch-thru calls, social media, and/or video submissions in one easy step." [A]
- **Patch-through calls**: advocates record up to 30-second voice greetings; system connects them to officials' offices; "all activity is tracked". [A]
- **Message Rotator**: rotating subject lines and bodies "with proportional display and delivery"; purpose: avoid messages being "flagged as a form email by legislative correspondents". [A]
- **AI campaigns**: generative AI writes "multiple versions of the emails going to legislators or custom targets" (OneClickAI). [A]
- **Pre-filled web forms**: auto-populate advocate data to raise conversion. [A]
- **Delayed delivery**: harvest advocate responses and "deliver them to their designated targets en masse at a time of your choosing". [A]
- **Video messages**: advocates submit personalized videos; **after approval**, sent to targets and usable by the org. [A]
- **Comment on Regulations**: integrated with Regulations.gov; advocates submit comments during open comment periods; "fully tracked and reportable". [A]
- **SMS & mobile keywords**: mass SMS, text-to-join keywords, dedicated short code. [A]
- **UTM tracking** of action-page traffic. [A]
- **Targeting database**: "local and state to federal, committee to caucus" + custom targeting; constituent logic implied ("advocates who are constituents of the legislators you are attempting to influence"). [A]
- **Surfaces**: embed Take Action forms on the org's website **or** hosted pages. [A]
- **Integrations**: Salesforce, NationBuilder sync; APIs; Zapier. [A]
- **Agency dashboard**: manage multiple accounts/clients/chapters from one dashboard. [A]
- **Bill tracking**: federal and state bill tracking as a separate solution line. [A]
- **Advocate acquisition** (Advocates & Actions page): paid acquisition campaigns with guarantees on cost per advocate, number acquired, geographic location, timeline. [A]
- **Sentiment tool**: run a poll "to get numbers to back your messaging". [A]

### Actionable (evidence layer A for homepage/FAQ claims — official product pages; thin documentation)

**Positioning**: "simple, self-service way to turn concern into action"; "the only self-service advocacy platform"; made by CSAG. [A]

**Model**:
- Campaign page intents: "rally people to contact their elected officials", "gather signatures", "collect powerful video stories", "grow my movement with new leads", "poll people". [A]
- Setup: choose template → add required information → publish. [A]
- "From petitions and pledges to lawmaker messages and supporter mobilization." [A]
- **Real-time in-platform reporting**: conversion rates, participation, supporter growth, engagement across campaigns. [A]
- Own branding; own domain (assisted). [A]
- Self-service pricing tier; enterprise tier exists. [A — product-specific pricing omitted from canonical doc]

## Cross-product Comparison

| Dimension | New/Mode | One Click Politics | Actionable | Strength |
|---|---|---|---|---|
| Org-authored campaign as central object | "Create Campaign" (typed) | "build custom widgets for campaigns" | "campaign pages", "launch, manage, and measure campaigns" | 3/3 |
| Supporter/advocate population | supporters; import contacts; message supporters | advocates; acquisition campaigns; pre-filled data | supporters; supporter growth | 3/3 |
| Policy-directed targets | recipients: datasets (Google Civic etc.), custom, fallback | legislators, custom targets, regulators | elected officials | 3/3 |
| Location-based supporter→target matching | postal/zip/address lookup → local MP etc. | constituent matching implied; local→federal database | not evidenced | 2/3 |
| Action page: hosted or embedded | hosted link or embed | hosted pages or embed | hosted campaign pages | 3/3 |
| Email-to-official action | yes (auto-send per submission) | yes (multi-action) | yes ("contact elected officials") | 3/3 |
| Petition/signature action | yes | yes (signatures referenced) | yes | 3/3 |
| Call action | call campaign (TTS intro, patch-through, "*" next) | patch-through calls with recorded greeting | not evidenced | 2/3 |
| Social action | social media campaigns (mentions/hashtags) | social media in multi-action | not evidenced | 2/3 |
| Message authoring + variation | talking points, message variations, AI strategist | AI generation, message rotator | templates | 3/3 (variation: 2/3) |
| Participation tracking/analytics | submissions & analytics, exports | tracked activity, UTM, reports | real-time conversion/participation/growth | 3/3 |
| Thank-you follow-up | thank-you email + page (configurable) | not evidenced | not evidenced | 1/3 |
| Moderation/approval | submission approvals; LTE review; video approval (OCP) | video approval | not evidenced | 2/3 |
| CRM/integration sync | Salesforce; CRM/analytical tools | Salesforce, NationBuilder, APIs, Zapier | not evidenced | 2/3 |
| Campaign lifecycle draft→live→archived | draft mode, launch, archiving guide, cloning | not evidenced (implied) | publish | 1/3 strong |
| Submission limits per supporter | explicit, typed defaults | not evidenced | not evidenced | 1/3 |
| Delayed/batched delivery | petition recipient updates every N signatures | delayed delivery en masse | not evidenced | 2/3 |
| Multi-client/agency management | multiple organizations | agency dashboard | not evidenced | 2/3 |
| Bill tracking / gov-affairs adjacency | no | separate bill-tracking solution | no | 1/3 |
| Paid advocate acquisition | no | yes (guaranteed) | no | 1/3 |
| Campaign funding (donations) | Stripe Connect | no | no | 1/3 |

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which the product stops being an Advocacy Platform:

```text
Organization-authored advocacy campaign
└── mobilized supporter population (identified people the org activates)
    └── policy-directed action (aimed at decision-makers / public targets)
        ├── supporter→target matching (typically location-based lookup)
        ├── action execution (message sent / call placed / signature counted / post staged)
        └── participation record (captured, counted, reported to the org)
```

Five properties:

1. **Organization-authored campaign** — the org (not the platform's public) defines an appeal for others to act. Remove → email marketing or a personal petition site.
2. **Mobilized supporter population** — the org activates a base of identified people (members, supporters, employees). Remove → a civic tool any anonymous citizen uses, or a legislative directory.
3. **Policy-directed action** — the action's destination is a policy decision-maker (legislator, official, regulator) or a public-demand target. Remove → marketing/fundraising/communications.
4. **Action execution toward the target** — the platform carries the action out (sends the email, patches the call, counts and forwards the petition), not merely records intent. Remove → a CRM or survey tool.
5. **Participation record reported to the org** — every action is captured and surfaced as counts/analytics for the campaign owner. Remove → a static web form.

**Historical/market-sample check**: 2000s-era grassroots tools (fax/letter generators to Congress, e.g., the CapWiz/VoterVoice generation), Canadian/UK tools, and modern AI-era platforms all satisfy this L0 — campaign, supporter base, targets, delivery, tracking. Petition-only public platforms (no org-side mobilization console; public discovery) and citizen-side civic tools (no org campaign) do **not** satisfy properties 1–2 as primary structure. The L0 therefore does not over-fit the current mobile/AI era.

### L1 — Common Mature Structure

Present across the researched sample (or strongly expected in the category), but not definitional:

- **Multi-channel action types** from one campaign model: email to officials, petition, call (patch-through/click-to-call), social posting, letter-to-editor, video messages, poll/sentiment
- **Target datasets** of officials with geographic coverage (federal/state/local; jurisdiction-dependent) + **custom targets**
- **Location-based matching** (supporter address/postal code → their representatives) with **fallback recipients**
- **Message authoring layer**: templates, talking points, message variations/rotation (deliverability-driven)
- **Action page** as the supporter surface: hosted page or embeddable widget/form
- **Analytics & reporting**: participation counts, exports, campaign performance
- **Supporter follow-up**: thank-you email/page, campaign updates to supporters
- **CRM/list sync** (Salesforce and similar) and contact import/export
- **Campaign lifecycle**: draft → configured → live → archived; cloning/templates
- **Moderation/approval** for supporter-generated content (letters, videos)
- **Team/multi-org management** (staff roles, agency/multi-client dashboards)

### L2 — Variant / Optional Structure

- **Channel breadth**: SMS-to-supporters, mobile keywords, regulations.gov comment submission, video messages, campaign funding/donations (Stripe), pledges, lead capture
- **Targeting data posture**: which jurisdictions/levels are covered (US federal/state/municipal via Google Civic; Canadian parliamentary datasets; subscriber-funded custom datasets; committee/caucus depth)
- **Delivery mechanics**: immediate vs delayed/en-masse delivery; per-recipient call chaining; TTS introductions; recipient visibility to supporters
- **AI posture**: AI message generation/variation, AI-driven recommendations
- **Acquisition services**: paid advocate-recruitment campaigns with guarantees (service, not software structure)
- **Government-affairs adjacency**: bundled bill tracking, advisory services
- **Plan/tier gating** of features; self-service vs sales-led onboarding
- **Internationalization** (multi-language action pages)
- **Regional coverage**: US-centric vs Canada vs UK/Australia datasets

### L3 — Vendor-specific (research notes only)

- New/Mode: max 10 recipients per campaign; default submission limits (petition 1 / email 3 / LTE 3 / call 10); "\*" key to advance chained calls; daily dataset scraping; Google Civic as US source; "Add Contactable Recipient" emailed every 100 signatures; plan names (Individual/Grassroots/Teams/Movement Builder); Stripe Connect funding
- OCP: 30-second voice greetings; "22,000+ campaigns" claim; money-back acquisition guarantees; OneClickAI branding; Regulations.gov integration; NationBuilder sync
- Actionable: self-service pricing figure; "only self-service advocacy platform" positioning claim; president's-email support culture

## Vendor-specific Findings

See L3. None of these were promoted into the canonical model. The message-rotation/deliverability concern appears in **two** products (New/Mode message variations + spam guidance; OCP message rotator) and is promoted to L1 as "message variation", but the specific mechanisms (proportional rotation, AI variation) stay vendor-level.

## Rejected Findings

- **"Advocacy Platform = email marketing to legislators"** — rejected: the defining flow is supporter→target with location matching and multi-channel execution; email is one channel among several.
- **"Advocacy Platform = petition tool"** — rejected: petitions are one action type; the org-side mobilization console, target datasets, calls, and analytics exceed petition-site structure.
- **"Advocacy Platform includes bill tracking / lobbying compliance"** — rejected as definitional: only 1/3 sampled products bundles bill tracking; it is an adjacency from government-affairs suites.
- **"Supporter base = donor base"** — rejected: supporter records serve mobilization; donation handling is optional (1/3) and belongs to fundraising/CRM Types.
- **"Advocacy requires legislative (parliamentary) targets only"** — rejected: regulators, agency comment periods, custom targets (e.g., corporate decision-makers) are evidenced; the invariant is *policy-directed decision-maker*, not *legislator* specifically.

## Boundary Findings

| Neighboring Type | Relationship | Distinction (what to remove to become the other) |
|---|---|---|
| **Petition / Public Comment Platform** (§24) | adjacent | Petition platforms are public discovery surfaces where anyone finds and signs; remove the org-side campaign console + mobilized supporter base + multi-channel targeting, keep public signature collection → petition platform. Advocacy petitions are org-distributed to the org's base. |
| **Civic Engagement Platform** (§24) | adjacent | Civic engagement tools serve citizens engaging with government (follow legislation, contact reps, town halls) without an organization authoring campaigns; remove the org-authored campaign + supporter population → civic engagement platform. |
| **Nonprofit CRM / Donor Management** (§25) | adjacent, integration partner | CRM's central object is the relationship/donation record over time; advocacy's central object is the campaign→action→target loop. Advocacy platforms *sync supporters into* CRMs (Salesforce evidenced in 2/3). Remove campaign/target/action execution, keep relationship+donations → CRM. |
| **Email Marketing Platform** (§06) | frequently confused | Email marketing sends org→audience; advocacy's defining flow is supporter→target (org authors, supporter sends). Remove target matching/execution toward decision-makers → email marketing. |
| **Government Affairs / Legislative Tracking** (§24 "Legislative Tracking Platform"; Quorum-class suites) | adjacent suites | Professional staff-side monitoring/lobbying vs grassroots mobilization. Suites bundle both (OCP bill tracking; Quorum = gov affairs + grassroots). Remove supporter mobilization → legislative tracking/gov affairs. |
| **Customer Advocacy Platform** (§06) | **same name, different domain** | Customer advocacy mobilizes *customers* to produce references/reviews/referrals for commercial outcomes; no policy targets, no legislative datasets. Remove policy-direction and insert commercial-reference outcomes → customer advocacy platform. Directory keeps both leaves; they are not aliases. |
| **Online Donation / Fundraising Platform** (§25) | adjacent | Fundraising's transaction is money; advocacy's transaction is an action toward a target. Funding appeals inside advocacy platforms (1/3) are optional. |
| **Volunteer Management System** (§25) | adjacent | Volunteers are scheduled/shifted for operational work; supporters are activated for policy pressure. Different action semantics. |

**"去掉什么就变成另一个 Type" summary**:
- Remove policy-directed targets (aim at customers/prospects) → Email Marketing / Marketing Automation
- Remove org-side campaign authorship + supporter base (open to any citizen) → Civic Engagement / Petition Platform
- Remove action execution & tracking (only send content to supporters) → Email Marketing
- Remove supporters (staff-only professional engagement) → Government Affairs / Legislative Tracking
- Remove the campaign container (persistent relationships + donations) → Nonprofit CRM

## Uncertainties

1. **Sample breadth**: only 3 products researched; the market's most-cited vendors (Quorum/Phone2Action, VoterVoice, Action Network) were unreachable. Cross-product claims rest on 3 products, one with Tier-1 docs. Risk: some L1 items (e.g., thank-you follow-up, moderation) may be more or less universal than the sample suggests.
2. **Constituent-matching formality**: OCP's location matching is implied by marketing copy ("constituents of the legislators"); its exact mechanics unverified (KB unreachable).
3. **Action Network / ActionKit structures** (petition+email+lobby targeting for progressive orgs) could not confirm whether their model adds anything the L0 misses; based on category knowledge they fit, but this is not evidence-backed here.
4. **Corporate/employee advocacy** (corporations mobilizing employees) is evidenced only via OCP's "Corporations" audience page; depth unknown.
5. **Whether "Advocacy Platform" and "Grassroots Advocacy Software" are one market or two**: evidence suggests one market with different emphases (New/Mode sells "Grassroots Advocacy" as its solution name); treated as one Type.

## Final Synthesis

An Advocacy Platform is **organization-operated mobilization software**: the organization authors campaigns; a supporter population is activated through action pages (hosted or embedded); each supporter's location (or the org's explicit choice) resolves policy targets from maintained datasets; the platform executes the action toward those targets (email, call, petition, social, letter, video) and records participation for the org's analytics and follow-up. Everything else — channel breadth, AI, acquisition services, bill tracking, funding — is variant or adjacency.

The Type sits deliberately between **communications tools** (which it uses as channels) and **government-affairs tools** (which monitor the policy side): its unique structure is the *supporter→target action loop under an org-authored campaign*, with participation measurement as the org's proof of mobilization.
