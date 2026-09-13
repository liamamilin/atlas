# Research Notes — Creator Course Commerce Platform

Research date: 2026-09-07
Leaf: Creator Course Commerce Platform (DIRECTORY §27 Media, Entertainment, Creator & Culture, line 1961)
Slug: creator-course-commerce-platform

---

## Research Goal

Understand what a Creator Course Commerce Platform actually is as an application type: what objects exist inside it, how a course goes from creation to money to consumption, which structures are definitional vs. common-market packaging, and where the type ends relative to its nearest neighbors (LMS, MOOC platform, coaching commerce, creator storefronts, paid communities, generic e-commerce).

This leaf sits in a dense creator-economy cluster. A previously processed sibling (coaching-commerce-platform, 2026-09-07) left a joint-review flag: the cluster seam test is "what a purchase converts into" — coaching commerce converts a purchase into a tracked human-service engagement; course commerce should convert it into self-serve content access. This pass must confirm or refute that seam with direct product evidence.

## Initial Boundary (hypothesis before research)

- Core hypothesis: software where an independent creator/expert packages their expertise as a structured course product, sells it through platform-operated checkout, and the purchase converts into standing self-serve access to that content for the buyer.
- Likely confused with:
  - LMS (organization-side training administration; commerce optional)
  - MOOC Platform (multi-provider marketplace; platform owns catalog/discovery)
  - Coaching Commerce Platform (purchase → human-service engagement)
  - Creator Storefront / Digital Product Commerce Platform (purchase → generic goods/downloads)
  - Paid Community Platform (purchase → access to a community venue)
  - E-commerce Platform / Online Store Builder (generic goods; no learning structure)
- Unknowns going in: whether the sales-site builder is definitional; whether the platform must operate payments directly or may only connect gateways; how the student/buyer side is modeled across products; whether cohort/live formats break the "self-serve" qualifier; how much the "creator" pole has drifted toward businesses (course platforms used for customer training).

## Research Questions

1. What is the sellable unit — the course itself, or a separate pricing object bound to it? How are pricing types structured?
2. What happens at purchase: what record is created, what access is granted, and what are the access rules (lifetime vs. subscription-tied vs. duration-limited, revocation, refunds)?
3. How is course content modeled (curriculum hierarchy, lesson types, drip/schedule/lock states)?
4. What does the buyer (student/member) see and do: login, library, player, progress, completion?
5. What sales surfaces exist (sales page, checkout, catalog/shop, full site builder) and which are definitional?
6. How far has the category drifted beyond courses (downloads, coaching, communities, podcasts, events) and does that drift break the type boundary?
7. What money machinery is standard (payment rails, coupons, upsells/order bumps, bundles, affiliates, taxes, payouts, refunds) and what is vendor-specific?
8. What marks the seam with LMS (compliance, SCORM, learner administration) and with MOOC marketplaces (catalog ownership, discovery)?

## Representative Products

Selection rationale: market representation + documentation completeness + different product philosophies + different customer tiers + coverage of the storefront-pole boundary.

| Product | Role in sample | Philosophy / positioning | Evidence tier |
|---|---|---|---|
| Teachable | Course-first creator platform; individual creators | "School" container; courses as flagship product, now with coaching/downloads/memberships/bundles as sibling product types; platform-operated payments (Teachable Pay) | A (help center: home, course creation, sell & get paid, student guides) |
| Thinkific | Commerce-led platform drifting to business/team pole | "All-in-one learning commerce platform"; courses + communities + TCommerce selling tools; Thinkific Plus for enterprise customer education | B/A− (official homepage + site structured data; support center 403 — no operational internals claimed) |
| Kajabi | All-in-one "knowledge commerce" pole; established infopreneurs | One platform selling Courses/Communities/Coaching/Podcasts/Newsletters/Downloads; Offer as explicit pricing object; Kajabi Payments | A (help center home + Courses overview) |
| LearnWorlds | Learning-feature-rich pole; straddles creator and LMS worlds | "School" with strong course authoring (interactive video, SCORM, exams); built-in affiliates, gateway-connected payments; markets to enterprise LMS too | A (help center knowledge-base index: Sell + course + site sections) |
| Podia | Storefront pole boundary sample | Creator shop: courses are one product type beside downloads, events, coaching, bundles; member-centric community; site builder + email built in | A (full help-center structure incl. products, pricing, access management) |

Udemy and similar marketplaces are noted as market context for the distribution-pole boundary but were not researched this pass (no claims).

## Sources

All fetched 2026-09-07:

- Teachable Help Center — https://help.teachable.com/hc/en-us (redirects to support.teachable.com); Create and Set Up Your Course — https://support.teachable.com/en/articles/11682451-create-and-set-up-your-course; Sell & get paid — https://support.teachable.com/en/collections/13696599-sell-get-paid; Student Guides — https://support.teachable.com/en/collections/13696561-student-guides
- Thinkific — homepage https://www.thinkific.com/ (incl. site JSON-LD organization description); features/selling-tools as named on homepage. Note: support.thinkific.com returned 403 twice → abandoned; no operational internals claimed for Thinkific.
- Kajabi Help Center — https://help.kajabi.com/ ; Courses overview — https://help.kajabi.com/articles/products/courses/courses-overview
- LearnWorlds Help Center — https://support.learnworlds.com/support/solutions ; Sell section — https://support.learnworlds.com/support/solutions/12000004747
- Podia Help Center — https://help.podia.com/ (full TOC: Products, Pricing, Shop, Community, Site Builder, Blog, Email)

---

## Product Observations

### Teachable (evidence layer A unless noted)

Container: the creator runs a "school" — their own branded site with custom domain, pages, and a public product directory. Help center is organized as: get started / build your products ("Create courses, coaching, downloads, memberships, and bundles") / customize your school / sell & get paid / manage your school / integrate & automate / student guides.

Product creation (course creation wizard, directly observed):
- Course created from Dashboard/sidebar/Courses index; wizard steps: title, author, description, thumbnail → optional pricing plan → curriculum build method (Generate with AI / start from scratch / bulk upload creating one lesson per file / copy from another course).
- Setup Guide checklist after creation: title/thumbnail, curriculum preview, pricing plans, sales page choice (course sales page / product details page / external URL), thank-you page, publish.
- Curriculum: sections → lessons; publishing visibility: published lessons visible to enrolled students, unpublished hidden, "public preview lessons" free for anyone as sales teasers, "drip lessons" release by dates or enrollment timing.
- Pricing types (verbatim table): One-time purchase (students pay once for lifetime access), Payment plan (fixed number of monthly payments), Subscription (recurring), Free (enroll without payment). Each plan: name, currency+price, optional subtitle/description.
- Course settings: publish/unpublish (controls whether new students can purchase or enroll) — distinct from product visibility (whether it appears in the public product directory); duplicate; delete (irreversible); categories for catalog discoverability; curriculum layouts; completion certificates; course compliance ("require students to complete videos or quizzes before moving on"); drip settings with per-student overrides (grant full access / restore original schedule); authors can hold revenue shares and author dashboards.
- Must have at least one published lesson before students can access content (FAQ).

Money (Sell & get paid collection, directly observed):
- Teachable Pay: "Accept student payments and get paid fast with flexible payouts, automated tax handling, and fraud protection" — platform-operated payment rails. Also legacy "Teachable Payments" gateway setup.
- Buy Now Pay Later as checkout payment option; collecting phone number at checkout; pre-sell a course; email lead forms; school affiliates program ("set up, manage, and work with affiliates").
- Analytics: Course Reporting Tools; Student Progress Reports. Taxes: automated handling via Teachable Pay.

Student side (Student Guides, directly observed):
- Students log in to the school account, navigate and view course content on web, use iOS/Android apps.
- For refunds, course access, and product questions the student contacts the school owner — the creator, not the platform, is the counterparty for the purchase relationship.

### Thinkific (evidence layer B for positioning; no operational internals)

Official homepage (2026-09-07) and site structured data:
- Self-description: "Online Course Platform to Sell Courses and Communities"; "all-in-one online course platform with a drag-and-drop builder, payments, and LMS tools"; organization JSON-LD: "all-in-one learning commerce platform that empowers entrepreneurs, educators, and businesses to create, market, and sell online courses, memberships, digital products, and branded communities… drag-and-drop course builder, AI-assisted course outlining, integrated TCommerce payments, mobile apps, and Thinkific Plus for enterprise customers."
- Product suite on homepage: Courses (drag-and-drop builder, AI generation, AI teaching assistant, SCORM import, branded native mobile app, live cohorts/self-paced/blended, quizzes/assignments/certificates, learning paths and prerequisites); Communities (public/private spaces with course-gated access, lesson-level discussions, member profiles with course progress, live events, moderation, branded mobile app, weekly digests); Selling tools/"TCommerce" (hosted checkout & order pages; one-time, subscription, payment-plan pricing; coupons, bundles, upsells, order bumps; multi-currency + local currency; automated sales tax and VAT; B2B invoicing, POs, seat licensing; refunds, dunning, failed-payment recovery; revenue/MRR/churn reporting).
- Audience drift marker: "Trusted by 20,000+ teams", enterprise/Plus pole for customer training — the platform is no longer creator-only.
- Note: support.thinkific.com 403 twice → abandoned. All Thinkific observations are Tier-2 positioning/market claims, not operational detail.

### Kajabi (evidence layer A)

Container: the creator runs a "site" (hosted website with pages, navigation, domains). Help center top-level: Cofounder (AI assistant), Amplify, Account, Products ("Create and manage Backstage, Courses, Coaching, Communities, Podcasts, Newsletters, and Downloads"), Sales ("payment processors, Offers and Coupons, checkout pages"), Website, Marketing (Funnels, Forms, Events, Automations), Contacts, Analytics, Media Library, Mobile Apps, API & Integrations.

Courses overview (directly observed):
- "A Course allows you to teach your customers through visual and written content. Each course can be made up of lessons and quizzes. Each lesson may include: Media (video, audio), Written content, Downloadable files. Lessons and quizzes live inside modules and submodules."
- Course types: **Evergreen** (self-paced, available as soon as purchased) or **Cohorts** ("students progress through material together in cohort groups, following a predetermined schedule", start date, import existing evergreen course).
- Content states per module/lesson via Status menu: **Publish, Schedule, Drip, Lock**.
- Course-attached capabilities: paywalls ("limited Course access to let your member experience the value before purchasing"), certificates (auto-sent on completion), comments, drip over time, live rooms, community channel embedding, transcripts/translations/dubbing, video timestamps.
- **Offer** = the pricing object: "The next step in the Course creation process is to create an offer so customers may purchase it." Pricing type Free or Paid; paid → payment frequency: One-time payment / Payment plan (weekly/monthly/yearly) / Subscription (billing interval); pay-what-you-want toggle on one-time; payment method = Kajabi Payments (+ additional options). Offer can be created later under Sales > Pricing; a course can be added to additional Offers.
- Student side: customers view courses on the website, the Kajabi mobile app, or a branded mobile app; purchased products appear in the customer's **member library** (title/description/thumbnail shown there).
- Content protection posture: "course content is protected by default. Videos… are view-only inside the platform and cannot be downloaded by students unless you explicitly enable that option. Attached files in lessons are downloadable by design."
- SCORM: "Courses are not SCORM compliant… If SCORM or xAPI compliance is a requirement for your use case, Kajabi may not be the right fit" — explicit anti-LMS boundary statement from a vendor.
- Business machinery: product limits per plan (duplicate blocked at limit), duplicating a course copies content but not customers, offers bind multiple products (bundles-shaped), MCP server exposing Courses/Offers/Contacts to external AI tools.

Money (help index + sales collection, directly observed):
- Kajabi Payments: accept payments, oversee purchases, manage refunds, initiate payouts; per-country setup, fees pages, Apple/Google Pay, BNPL, ACH for invoicing, payout schedules; QuickBooks sync; Kajabi Capital (funding based on sales performance).
- Sales objects: Offers, Coupons, Enhanced Checkout (customization/settings), Upsells and Order Bumps (explicit distinction article), subscription cancellation ("End future payments and remove access to the Products included with a customer's subscription"), subscription self-cancellation toggle, Affiliates (referral commissions).
- Marketing: Email Campaigns, Automations (conditional logic), Funnels, Forms, Events, Universal Inbox/Comment-to-DM; custom email domain.
- Contacts: "Manage your contacts and members"; marketing subscription status distinct from product access.

### LearnWorlds (evidence layer A)

Container: "school" with site builder (pages, sections, widgets, theme, blog, popups, SEO), custom domain connection, whitelabeling.

Knowledge base structure (directly observed):
- Create courses: create course, add learning activities (15 articles), **Interactive Video** (in-video quizzes, subtitles, interactive transcripts), Ebook, Multimedia (PDF/YouTube/Audio/SCORM), **Exams & Certificates**, course settings (access type, pricing, SEO), course player customization, courses library (clone, delete, reorder).
- Sell: **Marketing Products** (course bundles, subscriptions, learning programs — incl. "sell your courses only as a part of a Learning Program (not individually)"); **Marketing Tools** (auto-applied offers, coupon-based offers, bulk coupons, lead capture forms, UTM parameters); **Pricing Options** (pricing choices, presell, free lead magnets, cart feature, tiered subscription pricing); **Affiliate Program** (built-in, affiliate dashboards); **Get Payments** (payment gateways — Stripe plus EU local methods iDEAL/Bancontact/Przelewy24); **Payment Settings** (school currency, invoices & credit notes, sandbox test purchases, SCA/strong customer authentication).
- Report: user progress & segments, scheduled reports, **Course Insights** ("trends in how your students consume your content to optimize your offering"), exams/grading/certifications/question banks, **Track Sales** (financial activities), activity history logs.
- Manage: users (31 articles), GDPR/copyright protection, email notifications, video settings/transcription, **Learning Apps** (Daily news, Best Resources, Community, Gamification engine), user support tooling.
- Integrate: analytics pixels, email marketing (Mailchimp/ActiveCampaign/…), customer-service chats, live sessions (Zoom, Webex, Calendly, Teams, Meet), affiliates tools, Zapier, webhooks.
- Mobile App Builder: branded app, in-app purchases ("sell your courses via the app"), push notifications, app performance.
- AI: dedicated "Create AI-Powered content" section.
- Industry pages: Coaching, Creators, Customer training, Enterprise LMS, Finance, Fitness, Health, NGO — explicit straddle of the creator and LMS poles.

### Podia (evidence layer A)

Container: creator "site" (site builder with page sections incl. products, testimonials, FAQ, link-in-bio page), plus Blog, Email (built-in), Community.

Products (help TOC, directly observed):
- Product types: **Online courses** (lessons, quizzes, certificates, section access delays, per-customer unlocks, progress viewing, subtitles, per-file download toggles), **Digital Downloads**, **Events** (live + replay upload), **Coaching Sessions**, **Bundles**. Also physical products and company licenses/seats ("Selling company licenses or multiple seats for a product").
- Managing products: publish/unpublish, hide products, hide specific lesson/file, close signups, preview lessons/files, waitlists, product sales pages, checkout links, "adding someone to a product for free", "removing customer access", access duration period, sign-up limits, start dates, gifting, pay-what-you-want, pricing tiers, progress-gated section unlocks.
- Pricing: "Setting up an offer for your product", price, payment plans, upsells, subscription trials, tax codes.
- Shop: member-facing shop, wishlists, spotlight product, featuring products.
- Community: plans (paid community memberships), spaces, posts, members.
- Member side: "Understanding the member experience", member subscriptions management, home feed, chat, notifications.

---

## Cross-product Comparison

| Structure | Teachable | Thinkific | Kajabi | LearnWorlds | Podia | Reading |
|---|---|---|---|---|---|---|
| Course as curriculum product | yes (sections→lessons) | yes (drag-drop builder) | yes (modules/submodules→lessons+quizzes) | yes (activities, exams) | yes (sections→lessons) | Defining structure (B) |
| Course = one product type among several | yes (coaching/downloads/memberships/bundles) | yes (courses/memberships/digital products/communities) | yes (courses/communities/coaching/podcasts/newsletters/downloads/backstage) | bundles/learning programs; community app | yes (downloads/events/coaching/bundles) | Common mature packaging (B) — courses are the flagship that names the category, but all sampled platforms sell other product types |
| Sellable pricing unit bound to product | "pricing plans" on product | pricing on products (one-time/subscription/payment-plan) | **Offer** (product×pricing), multiple offers per course | "offers" (auto-applied/coupon-based), pricing choices | "offer for your product" | Defining structure (B): an offer/pricing-plan object distinct from content |
| Pricing types | one-time / payment plan / subscription / free | one-time / subscription / payment-plan | one-time (incl. pay-what-you-want) / payment plan / subscription / free | one-time / subscription / installment / free lead magnets | one-time / payment plan / subscription (+trial) / PWYW / free | Cross-product commonality (B): the four-type pricing grammar |
| Platform-operated payments | Teachable Pay (payouts, tax, fraud) | TCommerce (checkout, tax/VAT, dunning, refunds) | Kajabi Payments (refunds, payouts, fees, BNPL) | connected gateways (Stripe + local methods) | connected payments ("setting up payment details"), tax codes | Both postures exist: built-in rails vs. gateway connection (B); concept = the platform operates/connects the money rails (C) |
| Checkout as platform surface | yes (checkout pages, BNPL, phone capture) | hosted checkout & order pages | Enhanced Checkout | cart + checkout, sandbox test purchase, SCA | checkout links, checkout experience, success page | Defining structure (B) |
| Purchase → access binding | publish gates purchase/enroll; one-time = lifetime access | (positioning only) | purchase creates member access; cancel subscription removes product access | access type in course settings | adding/removing access, access duration, free adds | Defining structure (B/C) |
| Buyer account & library | student school account, student guides | member profiles with progress (community) | member library | school users, member management | member experience, shop | Defining structure (B): buyer becomes a logged-in member of the creator's school/site |
| Consumption surface (player, progress) | course view, progress bar (hideable), compliance gating | quizzes/assignments/certificates, learning paths | course player, certificates, comments | course player, interactive video, exams, gamification | lessons, completion, certificates | Common mature structure (B) |
| Drip / schedule / lock | drip by date/enrollment, per-student override | (learning paths & prerequisites) | Publish/Schedule/Drip/Lock statuses | access delays, progress-gated unlocks | section delays, start dates | Cross-product commonality (B) |
| Free preview / paywall | public preview lessons | (not claimed) | paywall feature | free lead materials, presell | preview lessons/files | Common (B) |
| Sales page per product | course sales page / PDP / external URL | order pages | landing pages (AI-generated on course create) | course sales pages via site builder | product sales pages, shop pages | Common (B): at minimum a per-product sales surface |
| Full hosted site builder | yes ("customize your school") | yes (site + landing pages) | yes (website builder) | yes (site builder) | yes (site builder + blog) | Common (B) — universal in sample but a single sales surface suffices conceptually |
| Catalog / shop / categories | product directory + categories | (positioning: shop not claimed) | products across site | courses library; bundles page | Shop, categories, spotlight | Common (B) |
| Coupons / promotions | coupons | coupons | coupons | coupons (incl. bulk) | coupons | Common (B) |
| Upsells / order bumps | (not observed this pass) | upsells, order bumps | upsells + order bumps (distinct article) | (auto-applied offers) | upsells | Common (B, 3/5 observed) |
| Bundles | yes (product type) | bundles | offers can hold products (bundle-shaped) | bundles / learning programs | bundles (product type) | Common (B) |
| Affiliates | school affiliates | (not observed) | affiliates | built-in affiliate program + dashboards | (not observed) | Common (B, 3/5 observed) |
| Built-in email marketing | lead forms; integrations | (integrations posture; AI content tools) | email campaigns, automations, funnels | integrations + lead capture | Podia Email built in | Variant: built-in (Kajabi, Podia) vs. integration-led (Teachable, LearnWorlds) (B) |
| Cohort / live formats | (not observed) | live cohorts, blended | Cohort course type, live rooms | live sessions via Zoom/Webex/Teams | events with replays | Common-optional (B) |
| Community inside platform | memberships product type | communities with course-gated spaces | community channel embedded in courses | community learning app | spaces + paid plans | Common (B) |
| Mobile apps | student iOS/Android apps | branded native app | free app + branded app | branded app builder + in-app purchases | not observed | Common-optional (B) |
| Certificates | yes | yes | yes | yes | yes | Common (B) |
| Quizzes/assessments | compliance quizzes | quizzes/assignments | quizzes | exams, question banks | quizzes | Common (B) |
| Revenue/progress analytics | course reports, progress reports | revenue/MRR/churn (claimed) | analytics + reports | course insights, track sales, user progress | customer progress viewing | Common (B) |
| SCORM | not claimed | SCORM import claimed | **explicitly not SCORM** | SCORM activities | not claimed | Split — the LMS-straddle marker (B); most creator-pole products reject it |
| AI assistance | AI curriculum outline | AI outlining + AI teaching assistant | Cofounder + AI outline + AI TA + MCP | AI content section | (not observed) | Era-common (B) |

## Canonical Model

### Level 0 — Defining Invariant

The smallest structure without which the type stops being recognizable:

```text
Creator-defined course product
  (curriculum: organized units → lessons of self-serve content)
+ Sellable offer bound to it
  (pricing option + checkout on the platform's money rails)
+ Purchase converts into a standing access entitlement
  (buyer becomes an identified enrolled member; access governed by the offer's rules;
   revocable by those rules — refund, cancellation, duration, manual removal)
+ Self-serve consumption surface
  (member-side place to work through the course content without the seller's labor)
```

Four invariants:
1. **Course product as structured curriculum** — content packaged as a curriculum (units/sections/modules containing lessons), not as loose files, a service, or a venue.
2. **Commerce-first sale** — the platform itself carries the sellable offer and checkout; selling is native, not bolted on. This is what separates it from pure LMS delivery systems.
3. **Purchase → access entitlement** — the money event creates a persistent binding between the identified buyer and the course content, with the offer's pricing type determining the access regime (one-time/lifetime, payment plan, subscription-tied, free).
4. **Self-serve consumption** — the buyer consumes the purchased content through the product's own member-facing surfaces, without per-unit seller labor (the seam vs. coaching commerce).

§24 historical check: a self-hosted WordPress + course-plugin + WooCommerce install (older/self-hosted pole) satisfies all four without any modern wrapper (no AI, no built-in email, no mobile app, no community). An email-delivered drip course (purchase → lessons sent by autoresponder) satisfies 1–3 and stretches 4 — the consumption surface is the inbox; treated as a boundary-adjacent primitive form, not a counterexample, since the access entitlement + self-serve consumption loop is intact. A marketplace course platform (provider sells through a shared catalog) satisfies the four but relocates discovery and branding to the platform — distribution pole, not definitional. Therefore the four invariants hold across era, hosting, and distribution variants.

Deliberately NOT in L0: site builder, community, email marketing, affiliates, certificates, quizzes, drip, mobile apps, AI, taxes automation, catalogs/shops, upsells, bulk content tooling. These are market expectations of mature modern products, not recognition conditions.

### Level 1 — Common Mature Structure

- Member/buyer account system distinct from the admin (login, profile, member library of purchases).
- Consumption machinery: course player, progress tracking, completion, certificates; quizzes/assessments.
- Content lifecycle controls: publish/unpublish (draft vs. live), scheduled release, drip by date/enrollment, free preview lessons, content protection posture.
- Per-product sales page + hosted checkout; coupon/promotion machinery; bundles; (in many) upsells/order bumps.
- Full hosted site builder for the creator's storefront; product catalog/shop surfaces.
- Money operations: payouts to the creator, refunds, sales/revenue reporting, tax handling (automated or via tax codes), student-side purchase support routing (students contact the creator for refunds/access).
- Audience machinery: email lead capture; affiliates; (in some) built-in email marketing/funnels/automations.
- Analytics: sales/revenue reports + student progress/consumption reports.
- Multiple product types beside courses (downloads, memberships, coaching, events, communities) sold through the same offers/checkout.
- Multi-practitioner features: authors/instructors with optional revenue shares; team/roles on the admin side.

### Level 2 — Variant / Optional Structure

- Payment-rail posture: platform-operated processing (MSP-style: payouts, automated tax, fraud tooling, BNPL, wallet support) vs. bring-your-own-gateway (Stripe-class + local methods).
- Audience posture: individual creator/solo expert vs. teams/businesses running customer-education academies (enterprise tiers, B2B invoicing, seat licensing, POs).
- Learning depth: light (creator-grade) vs. deep (interactive video, SCORM, exams, question banks, gamification, learning paths/prerequisites) — the LMS-straddle gradient.
- Content formats: video-first vs. mixed media (text, audio, ebooks, downloads, live rooms, cohort sessions).
- Distribution: standalone branded storefront vs. marketplace/listing participation (platform-owned discovery).
- Course formats: evergreen self-paced vs. cohort-based with start dates vs. blended.
- Built-in marketing suite depth (email campaigns, funnels, automations) vs. integration-led.
- Regional/compliance: EU payment methods, SCA, invoices/credit notes, GDPR tooling.
- Access regimes: lifetime vs. subscription-tied vs. fixed-duration vs. seat/company licenses; content-protection posture (view-only video vs. downloadable).
- AI depth: outline generation, AI teaching assistants answering from course content, AI site/cofunctor builders, MCP/API exposure to external AI tools.
- White-label/branding depth (custom domains, branded mobile apps, whitelabeled schools).

### Level 3 — Vendor-specific (research notes only)

- Teachable: "school" terminology; Page Editor 1.0 vs 2.0 split; Simple/Colossal curriculum layouts; "public preview lessons" naming; setup-guide checklist wizard; bulk upload one-lesson-per-file; authors with revenue shares; specific thumbnail specs (1024×576) and 760px content-width option; 160-char meta description cap; promo-video size limits; "Teachable Pay" branding.
- Thinkific: "TCommerce" branding; Thinkific Plus enterprise tier; AI "teaching assistant" branding; branded mobile app as feature line; JSON-LD claims (100M enrollments, 190 countries, $4.23B earned) — marketing figures, not verified.
- Kajabi: "Offer" as the canonical pricing object; Evergreen vs. Cohorts course types; member library; "Backstage" private 1:1 client spaces; Cofounder AI; Kajabi Capital; Creator.io; MCP server; 700-character description cap; Kajabi-heritage term overlays ("Categories/Post" older terms for modules/lessons); product limits per plan; "Heroes" community.
- LearnWorlds: "school" terminology; interactive video component system; learning apps (Daily news, Best Resources, Gamification engine); "sell only as part of a Learning Program"; tiered subscription pricing; sandbox test purchases; whitelabeling; vs-competitor comparison pages naming the whole category (Thinkific/Kajabi/Teachable/Podia/LearnDash/SamCart/ThriveCart/WooCommerce/Shopify).
- Podia: Spaces/plans community model; Shop with wishlists/spotlight; "New Podia" migration; Mover (done-for-you migration) heritage; per-file download toggles; link-in-bio page builder; coaching sessions as product type; sign-up limits.

## Vendor-specific Findings

(see Level 3 above; none of these enter the canonical document except as neutral, unnamed variant descriptions)

- The explicit anti-LMS statement (SCORM non-compliance as a positioning choice at one vendor) and the explicit LMS-straddle (enterprise-LMS industry pages at another) bracket the type's boundary on the learning-administration side.
- The cluster seam ("what the purchase converts into") is directly evidenced: subscription cancellation removes product access at one vendor; adding someone to a product for free / removing customer access at another; access duration settings at a third — the access-entitlement object is real, first-class, and operator-managed everywhere.

## Boundary Findings

1. **vs LMS (Learning Management System)**: sharpest structural seam. LMS is organization-side training administration (learners assigned by an organization; compliance/SCORM; gradebooks; HR/academic systems of record) where commerce is optional or absent. Course commerce platforms are seller-side and commerce-first: the offer/checkout/payout loop is definitional, learner administration is light. Evidence: one sampled vendor explicitly disclaims SCORM compliance as out of scope; another markets itself with an enterprise-LMS page — documenting the drift gradient, not a merge. Remove the commerce loop → you have an LMS/courseware system; remove the training-administration depth → you have this type.
2. **vs Coaching Commerce Platform (processed sibling)**: the recorded seam holds under direct evidence. Course platforms ship coaching product types (Teachable coaching, Kajabi Coaching + Backstage, Podia coaching sessions) and coaching commerce ships content delivery — feature overlap confirmed — but in a course commerce platform a purchase converts into standing self-serve access to curriculum content, not into a tracked human-service engagement (session credits/program delivery). Fulfillment structure, not feature presence, is the seam. This discharges the coaching pass's joint-review flag on this leaf's side.
3. **vs Creator Storefront / Digital Product Commerce Platform (unprocessed siblings)**: storefronts sell goods/downloads; the course product type is curriculum-structured content with consumption machinery. Evidence shows absorption rather than separation: every sampled course platform also sells downloads/memberships/etc. through the same offers. The recommended seam test for those leaves remains what the purchase converts into (goods/download vs. structured course access). Boundary recorded; do not merge this leaf.
4. **vs Paid Community Platform / Fan Membership Platform (unprocessed siblings)**: community/membership converts purchase into access to a venue or ongoing relationship; course commerce converts it into curriculum content access. All sampled course platforms embed communities (course-gated spaces, member areas) — again absorption. If the venue (spaces/feed) rather than the curriculum is the fulfillment object, it is the sibling type.
5. **vs E-commerce Platform / Online Store Builder / Checkout Platform**: generic commerce has no curriculum product type, no member consumption surface, no learning machinery; conversely course platforms are not general merchandise systems (no inventory/shipping as core). The overlap is checkout/offer machinery only.
6. **vs MOOC Platform / Online Course Marketplaces**: marketplace pole exists (provider sells through platform-owned catalog and discovery). The standalone branded-storefront posture is the center of gravity of this leaf's sample; marketplace is a distribution variant. Flagged for the MOOC leaf's own pass.
7. **vs eLearning Authoring Tool**: authoring tools produce courseware packages; they do not sell or deliver. Course commerce platforms author directly in-product (and sometimes import SCORM).

## Uncertainties

- Thinkific evidence is Tier-2 only (support center 403, abandoned after two attempts). Its operational details (access revocation mechanics, offer object structure, mobile app scope) are unverified; nothing precise is claimed for it.
- Upsells/order bumps were not directly observed at Teachable or LearnWorlds this pass; recorded as common (3/5) rather than universal.
- Built-in email marketing/funnels: posture varies (built-in at Kajabi/Podia; integration-led at Teachable/LearnWorlds); Thinkific unverified. Kept as variant.
- Whether the sales surface can be reduced to a single checkout link (no site builder) was not directly evidenced in-sample (all five ship site builders); conceptually treated as possible (external-URL sales pages are documented at Teachable), but noted as an inference.
- Udemy-class marketplace pole not researched; distribution-variant classification rests on structural reasoning, not product evidence this pass.
- Older/self-hosted pole (WordPress-plugin stack) not fetched this pass; §24 check rests on structural reasoning plus the in-sample evidence that no modern wrapper object is definitional.
- Refund workflows observed only as: refund management in payment rails (Kajabi) + student-contacts-creator routing (Teachable) + refund reporting posture (Thinkific claim). No per-product refund-rule details asserted.

## Final Synthesis

A Creator Course Commerce Platform is seller-side commerce software whose unit of trade is the creator's own packaged course. The defining core is fourfold: a curriculum-structured course product; a sellable offer (pricing option + checkout) carried by the platform's own money rails; the purchase event creating a standing, rule-governed access entitlement binding the identified buyer to that content; and member-side self-serve consumption of the purchased curriculum. Everything else — site builders, communities, email, affiliates, certificates, quizzes, drip, mobile apps, AI, multi-product catalogs — is the modern market's expected packaging and is documented as common or optional, not definitional. The type's edges are clean: remove the commerce loop and it becomes an LMS/courseware system; change what the purchase converts into (human-service engagement, goods, community venue) and it becomes a different creator-cluster sibling; remove the curriculum structure and it becomes generic digital-goods commerce. The leaf stands as an independent Type; the joint-review flag left by the coaching pass is discharged with the fulfillment-structure seam confirmed by direct product evidence.
