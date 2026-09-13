# Research Notes — Nonprofit Crowdfunding Platform

Research date: 2026-09-08
Leaf: Nonprofit Crowdfunding Platform (DIRECTORY §25 Nonprofit, Membership & Religious Organizations, line 1789)
Slug: nonprofit-crowdfunding-platform
Evidence layers used below: A = directly observed on an official source for a named product; B = cross-product commonality across the sample; C = canonical inference from comparison + Type-boundary reasoning.

---

## Research Goal

Understand the Application Type **Nonprofit Crowdfunding Platform** (§25) from real products: what its world consists of, what the organization and the crowd each do, how a campaign runs end-to-end, which rules constrain money flow and recognition, and where its boundaries sit against the three nearest §25 siblings (**Online Donation Platform**, **Fundraising Management Platform**, **Peer-to-peer Fundraising Platform** — all unprocessed at pass time) plus adjacent Types (Donor Management System, general/personal crowdfunding platforms, Nonprofit Event Management).

This pass must also adopt and extend two flags held by earlier §25 passes:

- donor-management-system pass (research/donor-management-system.md §Boundary Findings): vs online-donation-platform + fundraising-management-platform — discriminators adopted: **system-of-record side** (org-side constituency database vs donor-facing collection flow) and **center** (constituency stewardship vs campaign machinery).
- nonprofit-crm pass (STATUS line 2287): "vs online-donation-platform / fundraising-management-platform (donor-facing capture surfaces / campaign machinery vs org-side record system — donor pass's flags stand, adopt its discriminators)."

This pass adds the third axis: the **crowd-facing public campaign** as a capture surface with social-proof machinery, which neither sibling flag names.

## Initial Boundary

Initial hypothesis: the Type is the **campaign-centric, crowd-facing slice of nonprofit fundraising** — a specific cause/project runs as a public campaign with its own page, many individuals give to it, progress is publicly visible, and money flows to the organization. Nearest neighbors: Online Donation Platform (standing give-capability, transaction-centric), Peer-to-peer Fundraising Platform (supporters run the pages), Fundraising Management Platform (org-side program machinery), Donor Management System (org-side record system), and general crowdfunding platforms (GoFundMe/Kickstarter-class, personal/rewards beneficiary).

Key prior risk: this leaf could be merely a Variant of Online Donation Platform ("donation platform with campaign pages"). The research must test whether the campaign container + public crowd dynamic is a genuinely different center.

## Research Questions

1. What is the unit of work — a donation transaction, a fundraising program, or a campaign? What does a campaign contain?
2. Who may run a campaign (registered nonprofits only? individuals? social enterprises?) and what eligibility rules apply?
3. What is the public face of a campaign and what does it display (goal, progress, supporters, deadline)?
4. How does contribution capture work (checkout, payment methods, fees, donor recognition, receipts)?
5. Where does the money go (payout mechanics, platform fee vs processing fee models)?
6. How is the crowd dynamic manufactured (sharing, updates, matching, supporter pages)?
7. What happens after the campaign (donor records, stewardship, next campaign)?
8. Where is the line vs Online Donation Platform / Peer-to-peer Fundraising / Fundraising Management / personal-and-rewards crowdfunding?

## Representative Products

Selection rationale: market representation + documentation completeness + different product philosophies + different customer tiers + geographic spread.

1. **CauseVox** — connected nonprofit fundraising platform (US, SMB/mid-market) with crowdfunding as a first-class, explicitly named use case ("Nonprofit Crowdfunding Software", "Powering nonprofit crowdfunding since 2010"); org-ownership philosophy ("finish with every backer on your own donor record — not stranded on someone else's platform").
2. **Chuffed** — crowdfunding-native platform for nonprofits/charities/social enterprises and grassroots causes (global: AU/EU/CA/UK/US coverage per eligibility docs); zero-platform-fee economics; unusually complete operational help documentation (Front KB).
3. **Mightycause** — crowdfunding-native nonprofit platform (US), free-subscription economics ($0/month, ~0.95% avg processing fee), small-nonprofit pole; hosts GivingTuesday-class giving events; ships donor CRM alongside campaigns.
4. **Qgiv / Bloomerang Fundraising** — mid-market integrated suite pole (US) where crowdfunding-style campaign machinery lives inside Peer-to-Peer Fundraising rather than as a top-level product; documents the suite-embedded posture.

Boundary sample (studied but NOT a representative of this Type): **JustGiving** (UK, GoFundMe family) — explicitly operates *two* product lines, "Fundraising" (for registered charities, funds go to the charity) and "Crowdfunding" (personal causes, funds go to the page owner's own bank account). Vendor-drawn line between charity fundraising and personal crowdfunding; used for boundary calibration only.

Abandoned sources (per network-restriction rule, each after 1–2 failures, not filled from memory): Givebutter (givebutter.com + help.givebutter.com, 403 ×2), Classy / GoFundMe Pro (pro.gofundme.com timeout, www.classy.org 403, support.classy.org 403), Donorbox (donorbox.org/crowdfunding 403), Qgiv Zendesk help center (support.qgiv.com transport error ×2 — product pages on www.qgiv.com were reachable and used instead).

## Sources

Fetched 2026-09-08 (all official vendor surfaces):

- CauseVox — homepage: https://www.causevox.com/ (Tier 2: platform scope, donor-record philosophy); Nonprofit Crowdfunding use-case page: https://www.causevox.com/nonprofit-crowdfunding/ (Tier 1–2: five-step workflow, feature inventory incl. thermometer/countdown/donor feed/offline gifts/designations, FAQ incl. the consumer-crowdfunding boundary, deadline-optional statement, pricing)
- Chuffed — homepage: https://www.chuffed.org/ (Tier 2: positioning); Support hub index: https://docs.chuffed.org/ (Tier 1: category map); categories fetched: Basics of Crowdfunding (/en/categories/1438081), Eligibility (/1438337), Campaign Basics (/1438401), Managing your campaign (/1438593), Perks and Impact Levels (/1438529), Payments & Fees (/1438721), Receipts, Tax Deductibility and Gift Aid (/1438913)
- Mightycause — homepage: https://www.mightycause.com/ (Tier 2: features, free economics, GivingTuesday hosting); Pricing: https://www.mightycause.com/pricing/ (Tier 2); Nonprofits: https://www.mightycause.com/nonprofits (Tier 2)
- Qgiv — homepage: https://www.qgiv.com/ (Tier 2: rebrand to Bloomerang Fundraising, platform module map); Peer-to-Peer page: https://www.qgiv.com/peer-to-peer-fundraising/ (Tier 2: campaign machinery inside P2P)
- JustGiving (boundary sample) — https://www.justgiving.com/for-crowdfunding (Tier 2: personal-cause crowdfunding line, target/duration/withdrawal mechanics); https://help.justgiving.com/ (Tier 1 index: Fundraising vs Crowdfunding product split, separate charity help center)

---

## Product A — CauseVox

### Key observations

- Positioning (A): "Nonprofit Crowdfunding Software | CauseVox — Hit the goal. Keep the donors." "Powering nonprofit crowdfunding since 2010." Crowdfunding is a named use case alongside capital campaigns, giving days, memorial/tribute giving, etc.
- The product's own five-step crowdfunding workflow (A): 1. "Tell the story properly" — drag-and-drop campaign page with story sections, photos, video, impact metrics ("room to make the case, not a donate button bolted to a paragraph"); 2. "Show the momentum" — live fundraising thermometer, running donation count, countdown to deadline, continuously updating list of recent supporters ("Supporters give more readily when they can see that others already have"); 3. "Let your supporters carry it" — peer-to-peer pages for individuals and teams rolling up to the campaign total with leaderboards; 4. "Make giving frictionless" — mobile-first checkout (Card, ACH, PayPal, Venmo, Apple Pay, Google Pay), one-time/monthly/pledge, donor-covered fees, fund designations; 5. "Keep everyone you just met" — every backer lands in the org's donor records with full history; thank-yous, newsletters, automated series; "The campaign ends. The list doesn't."
- Social-proof framing is first-class (A): "Show the momentum. Supporters give more readily when they can see that others already have. A visitor arriving on day nine sees a campaign that's moving."
- Matching gifts (A): "A matching gift campaign gives that visitor a reason to give today rather than later — and the thermometer counts the match as it lands." Custom ratios and caps.
- Feature inventory (A): campaign page builder, story sections, thermometer, countdown timer, donation counter, recent donor feed, impact metrics, custom branding & domain, embeddable donation forms; personal fundraising pages, team pages, leaderboards, social sharing; payment methods, gift types, donor-covered fees, fund designations ("Direct gifts to a specific part of the project"), matching gifts, offline gift entry ("Log checks and cash into the same total"); donor records, built-in email & newsletters, email automations, monthly-giving conversion, automatic tax receipts, reporting & exports.
- Deadline is optional (A, FAQ): "Do we need a deadline? No, but they help. A countdown and a visible goal give people a reason to give now rather than later — though the campaign can run open-ended if that fits the project better."
- Fund designations (A): donors can direct gifts to a specific piece of the project, "each with its own page, description, goal, and live progress."
- The consumer-crowdfunding boundary, vendor-articulated (A, FAQ): "How is this different from a consumer crowdfunding site? The donors are yours. Every backer lands in your own donor records with their full history, so you can thank them, report back on the project, and invite them to keep giving — instead of finishing the campaign with a payout and a spreadsheet." Headline: "finish with every backer on your own donor record — not stranded on someone else's platform."
- Post-campaign continuity (A, FAQ): "What happens after the campaign ends? Your donor records, giving history, and email tools are all still there — the campaign is a page on your platform, not a separate account you close."
- Offline gifts (A, FAQ): "Offline gifts are logged alongside online ones so your public total reflects everything raised."
- Economics (A): free plan, paid plans from $100/month. Product modules: Donation Forms, Sites & Pages, P2P, Event Ticketing, Funds & Designations, Auction Management, CRM, Reporting, Email Marketing, AI.

## Product B — Chuffed

### Key observations

- Positioning (A): "Chuffed — Non-profit charity and social enterprise fundraising. The #1 platform for grassroots movements." "We're making the many as mighty as the powerful" (mission). Zero platform fees ("Chuffed is committed to zero platform fees").
- Who campaigns (A, Basics of Crowdfunding): "The most common campaigns on Chuffed.org are: Non-profits, charities and social enterprises looking for funding for a social cause project, product or..." — nonprofits dominate but individuals/grassroots campaigners are accepted; eligibility = Acceptable Use Policy compliance; campaigns restricted to campaigners based in a listed set of countries (AU, AT, BE, CA, DK, EE, FI, FR, ... per eligibility article).
- What crowdfunding is (A, Basics): "Crowdfunding is a way for you to raise funds online for a project, person or cause from a large number of people. There are many forms of crowdfunding..."
- Funding regime (A, Campaign Basics): "What is a 'Keep what you get' campaign? All campaigns on Chuffed.org are 'Keep what you get' campaigns. That means that the campaign receives all funds donated to it by the deadline, regardless..." — flexible funding is the platform-wide rule; campaigns have deadlines (with extension: "change the duration of your campaign for a set length (for up to 90 days), or extend it indefinitely").
- Campaign lifecycle (A): create (from dashboard, "up to 30 minutes" to be up and running), launch, duplicate (copy previous campaign into a new one), extend, archive ("effectively removes it from the public domain" — via support contact).
- Momentum machinery (A, Managing): campaign updates ("share the latest news with your donors and supporters"), messaging supporters (bulk email), pre-launch mode ("both a function within the website, and a concept... all about prep..."), UTM tagging for promotion tracking, on-demand reports via Campaigner Dashboard.
- Crowd-side engagement surfaces (A): Perks ("a great way to get more people involved...") and Impact Levels ("a great way of getting you..." [donors to give at levels tied to what their gift achieves]) — optional overlays on donation amounts; Fundraiser & Team Pages categories (supporter-run pages tied to a campaign); "Creating Fundraisers — Tips for supporters creating dedicated fundraiser pages to support existing campaigns."
- Offline gifts (A): "Someone gave me a cheque or cash. Can I add an offline donation to my total amount?" — yes, manual entry into the public total.
- Matched giving (A): "Matched Giving is a feature on Chuffed.org that lets you incentivize your donors to give more by matching their donations."
- Money flow (A, Payments & Fees): "Creating a campaign on Chuffed is free — we don't charge platform fees by default. The only fees you'll incur depend on which fee model your campaign [uses]" — fee models incl. a "Keep 100" model (with dated fee changes for Australia); card payments processed via the campaigner's own connected Stripe account ("funds are transferred to your bank account through Stripe, our payment [provider]"); PayPal alternative (donations arrive "immediately into your PayPal account"; business account required); Stripe payout cadence documented (rolling cycle, business days); international donations accepted (Visa/Mastercard/Amex); Stripe reports downloadable.
- Receipting is jurisdiction-dependent (A, Receipts/Tax/Gift Aid): tax-deductible receipts issued on the platform's behalf for US 501(c)(3) orgs, Australian DGR-endorsed charities, Canadian registered charities/RCAAA; UK charities collect Gift Aid declarations (platform "do[es] not process the Gift Aid Declaration[s]" itself); "Tax deductibility rules vary by country, but generally speaking, the rules... are the same regardless of whether you're givin[g]..." ; fiscal sponsorship: "connect a registered charity or non-profit organisation to your Chuffed campaign so they can receive and manage donations" — enabling campaigners without their own registered status to route funds to an eligible organization.
- Integrations (A): webhooks ("lets your own server hear about activity on your campaign in real time"), email journeys ("configure what emails go out to your donors, fundraisers and administrators when[ever]..."), integrations category (Salesforce/Mailchimp-class per Mightycause-analog; Chuffed lists its own set).

## Product C — Mightycause

### Key observations

- Positioning (A): "Free Nonprofit Software & Fundraising Platform — From donation forms to donor CRM—get everything you need to grow, with zero subscription costs." "If you're a US-based 501(c)(3), you already have a home on Mightycause" (org-claim flow: nonprofits are pre-listed and claimed). Stats shown: 0.95% avg processing fee, $1.6B funds raised, 76,000+ nonprofits.
- Feature map (A): Integrations (Salesforce, Mailchimp, HubSpot, 1,000+ apps), Donation Forms ("Turn your website into a destination to capture year-round fundraising"), Reports & Analytics ("real-time donation data and page metrics"), Donor Management ("Track, manage, and contact all of your supporters in one place"), Fundraising Campaigns ("Build unlimited campaigns for peer-for-peer fundraising, teams, events, and more"), Automated Marketing (personalized supporter messaging), Recurring Donations, Matches ("Maximize fundraising with easy-to-build donation matches").
- Embedded giving (A): "Increase donations with a streamlined donor experience on Mightycause, and embed customizable donation forms and buttons on your own website."
- Crowd/community layer (A): "Fundraise together. Reach more donors than ever before when you leverage peer-to-peer campaign creation and competitive team and event fundraising."
- Giving events (A): "Host a day of giving on the #1 giving day platform. Whether you're a Community Foundation uniting nonprofits or a university rallying students and alumni donors, a Mightycause Giving Event is your complete fundraising solution. Access a fully branded event website, user-friendly fundraising pages and campaign management tools..."; "Mightycause hosts GivingTuesday, the biggest giving event of the year."
- Economics (A): $0/month subscriptions ("Are you still paying for fundraising tools? Stop."), free to start; pricing page is image-led (details not text-readable in fetch).
- Support model (A): dedicated support team + fundraising specialists; "We made Mightycause so you can do it yourself."

## Product D — Qgiv / Bloomerang Fundraising (suite-embedded posture)

### Key observations

- Rebrand (A): "Qgiv is now Bloomerang Fundraising! The same trusted fundraising tools are now part of the Bloomerang Giving Platform!" — "A Unified Fundraising Platform for Nonprofits."
- Platform module map (A): Giving Platform, Donation Forms, Event Management, Text Fundraising, Peer-to-Peer Fundraising, Auction Fundraising, Donor Management | CRM, Data/Reports/Statistics, Integrations. **No top-level "crowdfunding" module** on the current site; crowdfunding-class machinery is documented inside Peer-to-Peer Fundraising ("races, bowl-a-thons, DIY fundraising, and other exciting events").
- Campaign machinery inside P2P (A): "Amplify generosity and boost campaign participation through live fundraising thermometers, personalized giving tools, and event store options"; "Acquire new donors by tapping into the power of your supporters' networks. Easy-to-share campaigns help amplify your reach"; personal dashboards with "dynamic visual trackers", team fundraising with "captain control, recruitment goals, and customizable fundraising pages", gamification tools ("milestone badges, competitive leaderboards"), virtual activity (livestreams, video, real-time tracking), online store.
- CRM adjacency (A): "Manage your entire constituent ecosystem, including donors, volunteers, sponsors, foundations, and more" — donor records sit in the same platform, separate module.

## Boundary Sample — JustGiving (personal vs charity line, vendor-drawn)

### Key observations

- Two product lines (A, help-center top nav): "Individuals — About Fundraising / About Crowdfunding" and "Charities — Join JustGiving / Help (separate help center at justgiving-charitysupport.zendesk.com)". Fundraising = page-for-charity (funds to the charity); Crowdfunding = "Raise money for your own personal cause, a person in need, clubs, schools, and communities."
- Crowdfunding line mechanics (A): "Start by setting up your online crowdfunding page... Once you've verified your bank details, you can start receiving donations." Withdrawal "to your own bank account within 14 days." "If you don't hit your target you'll still receive any funds you raised (minus some small fees)" — flexible funding. "Pages have an initial duration of 120 days. Once your page is active you can extend it up to 1 year." "Our data shows that pages with targets raise more than those without." Processing costs "2.9% + 35p per donation" with "no platform fee." FCA-regulated as a payment service. Use cases listed include charitable causes among personal ones — but funds still flow to the page owner's bank account, and the charity help center is a separate product.
- Significance for this pass: even a charity-rooted platform separates org-beneficiary fundraising (charity line: money to the organization, donation receipts via charity) from crowdfunding-for-personal-causes (money to the page owner). The beneficiary/money-flow line is the vendor's own Type boundary, matching the boundary this pass draws for §25's leaf.

---

## Cross-product Comparison

| Dimension | CauseVox | Chuffed | Mightycause | Qgiv/Bloomerang | Pattern |
|---|---|---|---|---|---|
| Unit of work | campaign (story-driven page + goal) | campaign ("Keep what you get", deadline-based) | campaign ("unlimited campaigns") under nonprofit account | campaign inside P2P events (races, DIY) | B: the campaign is the fundraising container in all four |
| Who runs it | the org (donors land in org records) | nonprofits/charities/social enterprises/grassroots; fiscal sponsorship routes to registered orgs | the claimed 501(c)(3) org account | the org, via P2P campaign setup | B: organization-for-cause posture; individual campaigners appear only as fiscally-sponsored or supporter-page actors |
| Public campaign face | story page + thermometer + donation counter + countdown + recent donor feed + impact metrics | campaign page (edited in-product) + updates + perks/impact levels | campaign pages + embedded forms | thermometers, personal dashboards, leaderboards inside P2P | B: public campaign face with visible progress is universal |
| Contribution capture | checkout: card/ACH/PayPal/Venmo/Apple/Google Pay, one-time/monthly/pledge, donor-covered fees, designations | card (Stripe), PayPal; international cards; optional perks/impact levels | donation forms + embedded forms/buttons; recurring | donation forms; store/registration purchases in events | B: platform checkout bound to the campaign; gift semantics |
| Money flow | to org (donor records + platform handles payout) | to campaigner's own connected Stripe/PayPal account; platform fee ~0 by default, fee models vary | to org; $0 subscription, ~0.95% avg processing fee | to org through platform | B: funds flow to the organization's account; platform economics vary (zero-fee+model, subscription-free, suite license) |
| Crowd dynamic | explicit step "Show the momentum"; matching counted in thermometer; P2P pages roll up | updates, messaging, pre-launch, matched giving, UTM promotion tracking, fundraiser/team pages | P2P campaign creation, team fundraising, matches, giving days w/ leaderboards | gamification, leaderboards, badges, easy-to-share campaigns | B: momentum/social-proof machinery is documented product surface in all four |
| Deadline/goal | optional ("can run open-ended") | deadline-based (90-day extensions or indefinite); flexible funding | campaign-configured | event-windowed (P2P events) | B: goal/deadline are configuration, not invariants |
| Receipts | automatic tax receipts | jurisdiction-dependent (US 501(c)(3), AU DGR, CA, UK Gift Aid declarations) | (not directly observed in fetched pages) | (not observed) | A→B: charitable receipting common, regime-dependent |
| Post-campaign | "The campaign ends. The list doesn't." — donors stay in org records | archive removes page; reports retained; email journeys continue | donor management is the standing product | CRM is the standing product | B: donor retention into the org's record system is a design goal (org-ownership posture) |
| Donor CRM | bundled (Fundraising CRM module) | integrations + donor-data category | bundled | bundled (separate module) | B: donor records adjacent or bundled; not the center |

## Canonical Model (three-layer filter applied)

### L0 — Defining Invariant (candidate, minimal)

Three jointly-held structures:

1. **The campaign as the public fundraising container of record.** A persistent, identified campaign for a specific cause/project, run by an organization for its mission (or by a campaigner routing funds to an eligible organization via fiscal sponsorship), carried by a public campaign page that tells the story and solicits contributions. Remove → a standing donate button / payment form (Online Donation Platform or payment-processor territory); remove the organization-for-cause posture → personal crowdfunding.
2. **Per-donor contribution capture bound to the campaign, with funds flowing to the organization.** Individuals give money to the specific campaign through platform-operated checkout; each contribution is recorded against the campaign (amount, donor, recognition preference); money is paid out to the organization's own account. Contributions are gifts to a cause (donation semantics), not purchases or investments. Remove → petition/awareness page (no money) or commerce/rewards territory.
3. **Public progress and share-out machinery that drives the crowd dynamic.** The campaign's running result — the total raised, commonly a goal target and supporter counts — is visible to prospective donors on the public campaign face, and the campaign is built to be spread (sharing links, embeds, promotion tools, updates). Remove → private payment collection; the "crowd" dynamic that makes this crowdfunding disappears.

Jointly-held is load-bearing: 1 alone = donation landing page; 2 alone = checkout/payment processor; 3 alone = broadcast/awareness surface; 1+2 without 3 = a quiet payment form for a project (the documented value claim "Supporters give more readily when they can see that others already have" is lost); 1+3 without 2 = awareness page; 2+3 without 1 = uncontainered fundraisers.

### L1 — Common Mature Structure (B-evidence)

- Donation checkout: preset/custom amounts, one-time and recurring, multiple payment methods, donor-covered processing fees, optional donor message
- Campaign storytelling editor: photos, video, long-form story sections, impact metrics; branding/custom domain; embeddable forms for the org website
- Progress implementations: goal thermometer, countdown timer, donation counter, recent-donor feed
- Donor recognition display with donor-controlled name/anonymity
- Charitable receipting (jurisdiction-dependent regimes); donor contact capture
- Campaign updates + supporter messaging; triggered email journeys/automations
- Offline gift entry counted in the public total
- Matched giving (ratios/caps; match counted into progress)
- On-demand reports and exports; campaign dashboards
- Payout through connected payment accounts (Stripe/PayPal-class)
- Campaign duplication/templates, pre-launch preparation, extension of duration
- Post-campaign donor retention into org records for stewardship and the next campaign

### L2 — Variant / Optional Structure

- Packaging: crowdfunding-native standalone (Chuffed, Mightycause) vs campaign type inside a fundraising suite (CauseVox use case; Qgiv/Bloomerang inside P2P) — same machinery, different packaging
- Economics: zero-platform-fee + fee models/tips (Chuffed), $0-subscription + processing (Mightycause), freemium + subscription (CauseVox), suite license (Qgiv/Bloomerang)
- Goal/deadline regimes: open-ended vs deadline-based; extension policies; **flexible funding ("keep what you get") is the sample-wide rule; all-or-nothing absent from the nonprofit sample** (consumer-crowdfunding territory)
- Perks/rewards and impact levels as optional overlays (Chuffed) — the rewards-crowdfunding spillover, not transactional
- Supporter-run pages (fundraiser/team pages) rolling up to the campaign — the p2p overlay; extent varies (CauseVox and Chuffed document it; it is the defining center of Peer-to-peer Fundraising Platform, not here)
- Giving days / GivingTuesday events (Mightycause; CauseVox use case) — multi-org campaign events with leaderboards
- Fund designations within a project (CauseVox)
- Fiscal sponsorship routing (Chuffed) for campaigners without registered charity status
- Regional receipting regimes (US 501(c)(3), AU DGR, CA, UK Gift Aid declaration collection)
- Geography/eligibility: country allowlists, acceptable-use policies (Chuffed)

### L3 — Vendor-specific (Research Notes only)

- Chuffed: "Keep what you get" terminology; "Keep 100" fee model (with dated Australian fee changes); Impact Levels; pre-launch mode; 90-day extension cap; archive-via-support; Front-KB docs
- Mightycause: 0.95% avg processing fee claim; $1.6B raised / 76,000+ nonprofits stats; GivingTuesday hosting; org-claim onboarding ("you already have a home")
- CauseVox: "since 2010"; free plan / paid from $100/month; funds & designations module; Bespoke custom solutions; AI suite (dedupe, setup help, insights)
- Qgiv/Bloomerang: rebrand to Bloomerang Fundraising; "P2Peeps" framing; gamification badge system; event store; hosted under bloomerang.com umbrella
- JustGiving (boundary sample): 120-day initial duration extendable to 1 year; withdrawal to own bank within 14 days; 2.9%+35p processing; FCA Payment Services regulation; separate charity support center

## Vendor-specific Findings

- **Org-ownership of the donor relationship** is the differentiated philosophy pitch in the sample (CauseVox FAQ explicitly against "finishing with a payout and a spreadsheet"); Mightycause/Qgiv bake donor CRM in; Chuffed exposes donor-data export/integration categories. This is a philosophy + packaging commonality (B), not a definitional leg — the L0 survives without an in-product CRM (payout + export satisfies "funds to org").
- **Zero-fee economics** (Chuffed zero platform fees; Mightycause $0 subscriptions; JustGiving no platform fee on crowdfunding) is a current-market pricing pattern, not structure.
- **Rebrands**: Qgiv→Bloomerang Fundraising; Classy→GoFundMe Pro (observed indirectly via blocked fetch attempts and homepage claims; not directly documented in this pass — do not assert details).

## Boundary Findings

1. **vs Online Donation Platform (§25 sibling, UNPROCESSED — forward flag for joint review).** The donation platform's center is the standing donor-facing give-capability of the organization (evergreen donate forms/buttons, transaction-centric). This Type's center is the campaign container with a public face and crowd progress; a "Donate" page with no campaign container is not crowdfunding. Overlap is real: most crowdfunding platforms also ship standing donation forms (Mightycause "year-round fundraising" forms; CauseVox donation forms module) — suite overlap, not type fusion. Remove-the-test both ways: remove campaigns+crowd machinery → donation platform remains (a pure donate-button product exists in the market); remove the standing transaction capability → crowdfunding remains (campaign-only platforms exist). Keep-both recommended; discriminators: transaction-of-record (gift) vs campaign-of-record (public container).
2. **vs Peer-to-peer Fundraising Platform (§25 sibling, UNPROCESSED — forward flag).** P2P's center: supporters run their own fundraising pages for the org and solicit their networks (page-owner = supporter). Here: the organization runs the campaign and donors give to it (page-owner = org). Supporter pages appear in this Type as an optional overlay that rolls up to the org's campaign (CauseVox "Let your supporters carry it"; Chuffed fundraiser/team pages; Qgiv P2P module). Seam = who owns the fundraising page and who the solicitor is. Qgiv/Bloomerang is the market's clearest straddling pole: it sells the same machinery (thermometers, leaderboards, personal dashboards) under Peer-to-Peer, with no top-level crowdfunding product.
3. **vs Fundraising Management Platform (§25 sibling, UNPROCESSED — forward flag).** Adopting the donor pass's discriminators (donor-facing collection flow vs campaign machinery vs org-side record system): this Type is the donor-facing public-campaign capture surface; fundraising management is the org-side machinery across the whole fundraising program (planning, appeals, pipeline, performance). Crowdfunding platforms increasingly ship slices of the other two (donor records, reports, email) — the suite drift noted by the donor pass — but the public crowd-facing campaign is the center that neither sibling flag names.
4. **vs Donor Management System (processed).** Org-side constituency system of record; this pass keeps its center on the donor-facing campaign capture flow. Per the donor pass, donor-management products ship donation forms writing back — same seam posture adopted here.
5. **vs general/personal/rewards crowdfunding (no DIRECTORY leaf; consumer territory).** Vendor-articulated line (A): CauseVox FAQ "How is this different from a consumer crowdfunding site? The donors are yours... instead of finishing the campaign with a payout and a spreadsheet." JustGiving runs personal-cause crowdfunding (money to the page owner's bank) as a separate product line from charity fundraising (money to the charity). Structural markers: beneficiary (organization-for-cause vs individual/rewards), money destination (org account vs personal account), semantics (gift with optional charitable receipt vs pledge/purchase), funding regime (keep-what-you-get dominant vs all-or-nothing typical in rewards crowdfunding). When consumer platforms serve nonprofits (GoFundMe-class charity products), they cross into this Type — the boundary is the beneficiary/money-flow structure, not the brand.
6. **vs Nonprofit Event Management / Event Ticketing.** Events center on registration/attendance with ticket purchases; campaigns here center on cause-giving. Event-branded fundraising (runs/walks) appears inside both as overlay (Qgiv P2P events with registration + fundraising; CauseVox run/walk use case) — the giving machinery, not the event logistics, is this Type's contribution.
7. **Taxonomy check (keep-both verdict).** Is this leaf merely a Variant of Online Donation Platform? Research verdict: no — the campaign-of-record + public crowd dynamic is a different center, realized by products that are *only* this (Chuffed-class crowdfunding-native platforms), and the market itself names the category ("nonprofit crowdfunding software" — CauseVox; "crowdfunding" product line naming across the sample). The four §25 leaves (donation / fundraising mgmt / p2p / crowdfunding) form a family grid on two axes: **who runs the fundraiser** (org vs supporters) and **record center** (transaction vs campaign vs program). Recorded as Boundary Issues for the pending siblings.

## §24 Historical / Market-Sample Check

- **Analog charity drive / capital campaign** (paper era): a named building-fund or mission drive (campaign of record), a public poster/notice and wall thermometer showing the total toward the goal (public progress), pledge envelopes/cash collected and logged per giver in the drive ledger (per-donor contribution capture), funds held by the organization (org account). Satisfies all three legs at analog level. ✓
- **Telethon era**: broadcast campaign toward a running tote-board total, call-in pledges processed by phone operators, funds to the charity. The broadcast is the share-out surface of its era; the tote board is the public progress machinery. ✓
- **Spreadsheet-era website fundraising**: a project page with an HTML progress counter and a donate form wired to a payment processor. ✓
- The definition therefore names **no specific digital implementation**: no thermometer widget, no deadline, no goal requirement (CauseVox: campaigns "can run open-ended"; JustGiving: "pages with targets raise more" — target encouraged, not required), no social network, no Stripe. Goal/deadline/thermometer are common implementations (L1); keep-what-you-get vs all-or-nothing is a regime variant (L2).
- Era-bound machinery correctly excluded from L0: tip-based platform funding, UTM tracking, webhooks, AI page builders, GivingTuesday (2000s-era construct).

## Uncertainties

1. Classy/GoFundMe Pro (the market's largest enterprise pole) could not be fetched (timeout + 403). Its crowdfunding campaign type is not directly evidenced in this pass; the enterprise-suite posture is instead covered by CauseVox (use-case packaging) and Qgiv/Bloomerang (P2P-embedded). Assertion strength for "enterprise suites package crowdfunding as a campaign type" is correspondingly reduced to the observed sample.
2. Givebutter and Donorblock— Givebutter (explicit free crowdfunding marketing) and Donorbox blocked; their absence slightly narrows the "explicit crowdfunding naming" breadth, though CauseVox/Chuffed/Mightycause already provide the naming evidence (B holds on 3+ products).
3. Mightycause operational detail (campaign settings, payout mechanics, receipting) was only partially documentable — its fetched pages are marketing-level. No operational claim rests on Mightycause alone.
4. Qgiv's historical standalone "Crowdfunding" module (pre-rebrand) could not be confirmed from current pages; only the current P2P-embedded posture is asserted.
5. Exact fee percentages, payout cycle lengths, duration caps etc. were observed for single products (Chuffed Stripe payout cycle; JustGiving 120 days) and are kept L3/product-specific — not generalized.
6. Whether any nonprofit crowdfunding platform operates an all-or-nothing mode was not observed anywhere in the sample; asserted only as "absent from the researched sample", not as an industry universal.

## Final Synthesis

A **Nonprofit Crowdfunding Platform** is the crowd-facing, campaign-centric slice of nonprofit fundraising technology: the organization launches a public campaign — a persistent, identified fundraising container for a specific cause/project with a story-carrying public page — many individuals give to that specific campaign through platform checkout as gifts, each contribution is recorded against the campaign with the money paid out to the organization's own account, and the campaign's running result and supporter activity are publicly visible and built for share-out, which is what manufactures the crowd dynamic. Goal targets, deadlines, thermometers, matching, perks, supporter pages, giving days, receipting regimes and donor CRM are the common mature machinery wrapped around that core; who *runs* the fundraiser (org vs supporters) and where the record center sits (campaign vs transaction vs program vs constituency) separate it from its three §25 siblings. The Type is era-stable: the wall-thermometer charity drive and the telethon satisfy the same three-legged core, so the definition names no digital implementation.
