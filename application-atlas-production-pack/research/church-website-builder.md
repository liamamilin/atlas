# Research Notes — Church Website Builder

Research date: 2026-09-07
Leaf: Church Website Builder (DIRECTORY.md §25 Nonprofit, Membership & Religious Organizations)
Slug: church-website-builder

## Research Goal

Understand what a "Church Website Builder" actually is as an Application Type: what objects exist inside it, how a church staff member or volunteer builds and maintains the church's public website, how it relates to the neighboring §25 leaves (Church Management System / ChMS, Church Communication Platform, Church Giving Platform, Sermon Management) and to the generic website-building Types (Visual Website Builder §04.16, CMS §02.07).

## Initial Boundary (hypothesis before research)

- Hypothesis: a website-building application whose output is the church's public web presence, whose content model is organized around church life (service times/location, sermons, events, giving, guest welcome), built by non-technical church staff, and connected to the church's operational systems (giving, ChMS, church app).
- Likely confusions:
  - Visual Website Builder (§04.16) — same substrate; is this leaf just an audience-specialized variant?
  - CMS (§02.07) — generic content management vs domain-specialized hosted site assembly
  - Church Management System / ChMS (§25 sibling) — internal records vs public presence; suites bundle both
  - Church Communication Platform (§25 sibling) — targeted outbound messaging vs public web presence
  - Sermon Management (§25 sibling) — sermon record workflow vs site display object
  - Church Giving Platform (§25 sibling) — donation processing vs embedded giving
- Key open question: are church-shaped structures first-class objects inside the product (like menu semantics in Restaurant POS), or just templates over a generic builder (which would make this a Variant, not a Type)?

## Research Questions

1. What is the managed output — a hosted site under the church's domain? What does "building" consist of (templates, sections, drag-drop, AI drafts, done-for-you services)?
2. Which church-specific structures are first-class in the product (service times/locations, sermons/media, events, giving, plan-a-visit, prayer, livestream)?
3. How does the content workflow operate (sermon publishing → hub → podcast; events; banners)?
4. How does it connect to church operations — giving platform, ChMS (forms → people, content flow), church app, calendars, livestream platforms?
5. Who builds/maintains it — roles, permissions, editor surface, volunteer-friendliness?
6. What rules matter — domain/DNS, hosting/SSL, SEO, privacy of sensitive content (prayer), staging/launch?
7. Variants: standalone vs suite module vs all-in-one; instant/template/AI/expert build paths; proprietary vs WordPress substrate.
8. Historical check: older church website products (Ekklesia 360, Clover Sites, Sharefaith) and generic-tool church sites (WordPress/Squarespace) — do they fit the same core?

## Representative Products

| Product | Posture | Tier of evidence |
|---|---|---|
| Nucleus (nucleus.church) | standalone church website builder, engagement-led (Launcher/Flows/Prayer), design-led; Giving/Messages/Media as sibling products | Tier 1 (root product page + full Help Scout help center: Web/Sermons/Flows/Prayer/Giving/People/Posts/Messages collections + Web Getting Started article list) |
| Tithe.ly Sites | suite module inside Tithe.ly (giving-first bundle: Giving, ChMS, Church App, Sites, People) | Tier 2 (dedicated product page + extensive FAQ; help center not fetched) |
| Ministry Brands Amplify Websites | enterprise church-software suite module; three build paths (AI draft / WordPress-Elementor starter / expert-built Pro); absorbs legacy builders (Clover Sites, Ekklesia 360, Sharefaith) | Tier 2 (websites product page + FAQ + portfolio; cloversites.com redirect observed) |
| ChurchSpring | all-in-one church growth platform, websites at the core; instant pre-populated site, volunteer-friendly | Tier 2 (root + dedicated website-builder page with detailed feature list and FAQ) |
| Faithlife Sites | media/sermon-first ecosystem posture (Faithlife/Logos family) | none — faithlife.com/sites timed out ×2; market context only, no claims |
| Squarespace / WordPress | generic website builders/CMS used by churches | market context only (not fetched; boundary anchors) |
| Planning Center | ChMS without a website product (verified in the church-communication-platform pass: product nav has People/Groups/Calendar/Registrations/Check-Ins/Services/Giving/Publishing, no website builder) | boundary anchor via sibling pass |

Sample rationale: one standalone design/engagement-led product with deep Tier-1 operational docs (Nucleus), one giving-first suite module (Tithe.ly Sites), one enterprise suite module with three build paths and consolidation heritage (Amplify), one all-in-one SMB platform (ChurchSpring). Different philosophies (engagement-led / bundle-led / service-led / simplicity-led) and different customer tiers (church plants to networks/headquarters).

## Sources

Fetched 2026-09-07 (all successful unless noted):

- Nucleus root — https://nucleus.church/ (positioning, products: Web/Giving/Messages/Media; Sermons, Launcher, Prayer, Flows, Integrations, Banners, Info Cards, Templates, Advanced Permissions; pricing $99/$199)
- Nucleus Help — https://nucleus.church/help (help-center index; n2help.nucleus.church + legacy n1help "Nucleus Classic")
- Nucleus 2 Help Center — https://n2help.nucleus.church/ (full collection TOC: Start-up Guides, Web, The Launcher, Sermons, Flows, People, Posts, Messages, Prayer, Giving, Media, Church Settings, My Nucleus Account)
- Nucleus Web Getting Started — https://n2help.nucleus.church/category/1180-getting-started (11-article build flow: design → homepage → privacy → smart data/church info → pages → navigation → site settings → admins → pre-launch checklist → custom domain)
- Tithe.ly root — https://www.tithely.com/ (product line; Sites $19/mo; All Access $119/mo)
- Tithe.ly Sites product page — https://www.tithely.com/product/church-website-builder (features, FAQ: hosting, sermon player/podcast, livestream embed, Plan Your Visit, SEO, feature list)
- Ministry Brands Amplify Websites — https://www.ministrybrands.com/websites (three website paths, CMS/content integration, SEO, support services, FAQ)
- Clover Sites — https://www.cloversites.com/ (redirect into Ministry Brands Amplify; "You may have known us as…" legacy brand list incl. Ekklesia 360, Sharefaith, Fellowship One, Shelby Systems)
- ChurchSpring root — https://churchspring.com/ (all-in-one platform positioning)
- ChurchSpring Websites — https://churchspring.com/church-website-builder/ (90-second setup, Sermon Manager, Plan Your Visit, Event Management, Unlimited Designs, Easy Editing, Church Branding, Social Scheduler, Directory, feature list, FAQ)

Failed / abandoned (per source-access limitation rules):

- Faithlife Sites — https://faithlife.com/sites and https://www.faithlife.com/sites — timeout ×2 → abandoned; no claims rest on it
- Tithe.ly Sites URL guesses — /products/church-websites, /products/sites — 404 ×2 (correct URL found via root nav)
- Tithe.ly help center (help.tithe.ly) — not fetched; Sites claims kept at product-page/FAQ strength
- Subsplash — not attempted (unreachable in the sibling church-communication-platform pass; market context only)

## Product A — Nucleus (standalone, engagement-led)

### Key observations (evidence layer A unless noted)

- Self-description: "The premium church website builder"; products: Website Builder (/web), Giving, Messages, Media. "Nucleus is designed for church staff and volunteers. No web experience or coding skills are needed."
- **Sermons**: "Build your modern sermon hub. Organize your messages by date, topic, and speaker. Or create custom playlists from scratch." "Add Scripture references, transcripts, and bonus resources to any sermon." "Create private playlists… robust privacy controls." "Host your podcast. Nucleus powers your RSS feed to help distribute your church's podcast to Apple Podcasts, Spotify…"
- **The Launcher**: "Your most important next steps, all in one place… lives on every page of your website"; custom color/icon/messaging; featured event focus; custom trigger links for email/social/link-in-bio.
- **Prayer**: PrayerFlow (submit prayer requests), follow-up initiation from prayers, Prayer Wall (sign-in to view; email notifications), Prayer Time, "not indexed in search results" (privacy).
- **Flows**: "Anything forms can do, Flows can do better" — plan a visit, baptism signups, registrations and payments; one-piece-at-a-time chat-style collection; done-for-you Flow templates; automatic follow-up email triggers.
- **Integrations**: Planning Center (signup/contact info sync), Google & Apple Calendar display, embed sections/Launcher actions/buttons for everything else.
- **Banners**: time-sensitive alerts/announcements; scheduled visibility with expiry.
- **Info Cards**: "slimmed down web pages" as building blocks; connect to Banners and Flows for signup sequences.
- **Done-For-You Templates**: page-template library covering common church needs; edit in sections.
- **Advanced Permissions**: unlimited admins; church-specific permissions (manage a single Flow, the youth page, a prayer inbox); privacy for financial details/prayers.
- **Web help-center structure** (operational model): Getting Started (11 articles); Create, Build & Manage Pages ("the most basic element of a website: pages"); Add & Manage Page Sections (14 types); Navigation Menus; Customize & Design (fonts/colors/buttons); Advanced Web Settings (SEO, status pages, sitemaps); Manage Domains & Redirects; **Church Info** ("Manage info used in multiple places across your website"; "Input Your Smart Data").
- **Build flow** (Getting Started article sequence): Customize design → Start with homepage → Understand privacy options → Input Smart Data & church info → Construct & edit pages → Create navigation menu(s) → Manage site settings → Invite admins & manage access → Pre-launch checklist → Add & connect custom domain.
- **Other collections**: Posts (create/categorize/share; Collections & subscribers; Smart Campaigns emails; Post Hub), Messages (one-off/scheduled/sequenced email campaigns), People (database & profiles), Giving (GivingFlow, reports, giver profiles, receipts/annual statements), Church Settings (basic church info, administrators & permission levels, financial account), **My Nucleus Account** (congregant-side: My Account, My Giving, My Submissions).
- Included in Web plan: SSL certificate, web hosting, sitewide & on-page SEO, unlimited pages, custom CSS, works with any custom domain, unlimited users.
- Pricing: $99/mo (Web); Nucleus Complete $199/mo (adds Giving, Comms Engine, Media). Free church website makeovers ("Nucleus built the whole thing for us for free"). Status page claims 99.99% uptime.
- Vendor-specific (L3): Launcher/Flows/PrayerFlow/Info Cards naming; Posts/Collections/Smart Campaigns; Nucleus Classic vs Nucleus 2 split; Trustpilot/Capterra counts; "No bots. No AI." support positioning.

## Product B — Tithe.ly Sites (suite module, giving-first)

### Key observations (evidence layer A for product page + FAQ)

- Positioning: "Best Church Website Builder + Hosting… Build a Custom Church Website with Ease… No coding skills required. Only $19/month." Part of Tithe.ly suite (Giving, ChMS, Church App, Sites, People, Service Planning…); included in All Access ($119/mo).
- Headline capabilities: **Beautiful Church Templates** ("professionally designed, mobile-optimized templates made for ministries"); **Built-In Church Tools** ("Sermon library, events calendar, giving, prayer walls, and more—already integrated"); **Live Editing** ("Make updates in real time… publish and go"); **Fast, Secure Hosting** ("We handle uptime, maintenance, and security").
- Connection tools: **Plan Your Visit** ("Let guests schedule their visit, get a personal welcome… the system alerts you so you can make arrangements"); **Sermon Streaming & Archives** (live + past messages); **Online Giving** (integrated); **Interactive Events Calendar**; **Mobile-Ready**.
- FAQ feature list: sermon media player, events calendar, plan your visit, integrated online giving, photo gallery, video embedding, contact forms, multilingual support, site-wide search, SEO, "serve backups & security updates", unlimited user accounts, unlimited storage.
- Sermon/podcast: "Easily share your sermons, create a podcast feed… using the built-in Tithe.ly Sites sermon player"; livestream embed from Facebook, YouTube, or Vimeo.
- SEO: "Tithe.ly Sites perform very well with search engines… tweak and customize."
- No coding: "select a professionally designed church website template… or create your own church web design."
- Definition quote: "Tithely Sites is an easy to use custom website builder designed specifically for churches. From uploading sermons, and adding events, to changing features, and creating new pages with specific ministry designs, managing your church's website is a breeze."
- Vendor-specific (L3): $19/mo standalone price; All Access bundling; "front door to your ministry" framing; blog resource list.

## Product C — Ministry Brands Amplify Websites (enterprise suite, three paths)

### Key observations (evidence layer A for product page + FAQ)

- Context: cloversites.com now redirects into Ministry Brands Amplify ("As we move from CloverSites to Amplify…"); "You may have known us as…" lists Shelby Systems, EasyTithe, Fellowship One, Simple Church CRM, Kindrid, Elexio, Church Streaming TV, ShareFaith, E-Zekiel, **Ekklesia 360**, Bridge Element. "Over 42,000 Websites Built."
- **Three website paths**: (1) **Amplify Website Builder** — "Powered by Amplify Intelligence, skip the blank page and create a structured, ready-to-edit church website draft in minutes. Start with information your church already has online, answer a few simple questions, then customize the site before you publish." (2) **Amplify Starter** — "ready-to-edit templates and simple tools your team can manage without coding… Live within 2 to 3 weeks" (portfolio labels: "Wordpress Elementor design"). (3) **Amplify Websites Pro** — "Let Ministry Brands experts build a website tailored to your church's mission… church-specific features, personalized design, expert support."
- **One login**: "Access everything you need to manage your church's online presence with just one easy login."
- **Seamless CMS**: "our Ministry Content Management System. Utilize widgets, plugins, RSS feeds, and social media integrations for YouTube, ChMS, Google Calendar, and more. Plus, access all your content on any website you build with any Ministry Brands Amplify builder."
- **Content integration**: "pull in content like event info, sermons, and more, so you don't need to spend time uploading the same files multiple times"; FAQ: "Content flows automatically from your church management system. Update once, and it appears everywhere."
- **Robust SEO**; support services catalog: Website Strategy, Content Entry, Custom Logo, Logo Refresh, Custom Branded Mobile App, SEO, Module Training, Hourly Consulting.
- FAQ positions the Type: "Churches are moving beyond generic website platforms to purpose-built church website builders that actually understand ministry." "pre-built sections for everything churches need: volunteer opportunities, prayer requests, small groups, and more." Essential elements: "service times, location, staff introductions, your mission, online giving, events, and sermons."
- Suite context: Amplify bundles People, Giving, Mobile App, Websites, Streaming, Service Planning, Accounting, Safety, Media, Communications; Headquarters products for denominations/networks.
- Vendor-specific (L3): AI builder mechanics; WordPress/Elementor substrate; 14-day trial; portfolio sites; "Amplify Intelligence" branding.

## Product D — ChurchSpring (all-in-one, simplicity-led)

### Key observations (evidence layer A)

- Positioning: "all-in-one church website builder with online giving, a custom app, and church management tools already built in… no setup fees, no hidden costs"; "Launch your church website today—without setup, add-ons, or surprises."
- **90 Second Setup**: "pre-populated text, images, navigation menu, and design, you simply have to log in to customize"; "It often takes our customers 5-7 days to go live… you could go live in as little as 24 hours"; free website migration with annual plan.
- **Easy Editing**: "inline updating designed for the most seasoned church volunteer. Simply add images, text, sermons… Click. Type. Drag. Drop. Save."; "No coding or fancy tech knowledge needed!"
- **Sermon Manager**: "add sermon audio and video… Link your audio RSS feed to any podcast player to synch your church's podcast."
- **Plan Your Visit**: pop-up form; "save guests' contact information, capture service and event RSVPs, and follow up."
- **Event Management**: recurring events, registration, images.
- **Live Streaming**: "Integrate any 3rd party live streaming platform right into your ChurchSpring website"; "automatic website banner notifications" when live.
- **Unlimited Designs**: library of biblically-named designs (Acts, Calvary, Chronicles, Covenant, Esther, Eve, Exodus, Ezra, Galilee, Heritage, Jude, Light, Moses, Obadiah, Origin, Proclaim, Providence, Psalm, Revelation, Ruth, Titus); "Change your website's entire design with just one click of a button."
- **Church Branding**: "Update your church branding to instantly update sitewide"; Design Center (logo, colors, fonts, custom CSS).
- **Social Scheduler**: schedule sermons/events/blog posts to social media automatically.
- **Church Directory / People**: contact management with prayer requests, notes, giving history; secured member access.
- **Giving**: free with every plan (processing 2.9% + $0.30 per transaction, vendor-stated); **Mobile App**: free with every plan, "syncs with your website… no need to make updates in multiple locations."
- Feature list: no setup cost, no add-on fees, universal login, mobile optimized, media library (1,000+ images), analytics integration (Google Analytics/Facebook Pixel), feature sliders, photo galleries, comment moderation, drag & drop menu, unlimited pages, video backgrounds, **free subdomain (staging site)**, own domain with free setup, free hosting, SEO (sitemaps, automatic meta content), unlimited admins, user permissions, custom forms, **Blocks** (Map, Contact Form, Text, Image/Text, Headline), **password-protected pages**, page styles, calendar management.
- Vendor-specific (L3): biblical design names; 90-second claim; 2.9%+$0.30 rate; "Chick-fil-A level customer service" testimonials; version names (Hudson).

## Cross-product Comparison

| Structure | Nucleus | Tithe.ly Sites | Amplify Websites | ChurchSpring |
|---|---|---|---|---|
| Managed output | hosted site, custom domain, SSL, hosting included | hosted site, hosting included | hosted site (3 paths), hosting fees included | hosted site, free hosting + free subdomain staging |
| Build model | pages → sections; done-for-you page templates; design customization | mobile-optimized templates; live editing | AI draft from existing online info / WordPress-Elementor templates / expert-built | pre-populated site at signup; inline editing; one-click design swap |
| Church-shaped objects | Sermons (hub, playlists, speakers, scripture, podcast RSS), Prayer (hub/PrayerFlow/wall), Flows (plan-a-visit, baptism, registrations+payments), Launcher, Banners, Info Cards, Posts | sermon library/player + podcast feed, events calendar, Plan Your Visit, giving, prayer walls, livestream embed | pre-built sections: sermons, events, giving, volunteer sign-ups, prayer requests, small groups; service times/location/staff | Sermon Manager (audio/video + RSS), Event Management (recurring + registration), Plan Your Visit, Giving, Prayer, Groups, Directory, Live Streaming |
| Church identity data | Church Info / "Smart Data" reused across site | via templates | one login; ChMS content flow | Church Branding sitewide; universal login |
| People/submissions | People database; Flow submissions → People; congregant "My Nucleus" account | via ChMS | ChMS content integration | People/Directory; Plan Your Visit saves guests |
| Permissions | unlimited admins; scoped church-specific permissions | unlimited user accounts | (support services; not detailed) | unlimited admins; user permissions |
| Domain/DNS | custom domain connect + redirects | hosting included | hosting included | own domain + free setup; staging subdomain |
| SEO/analytics | sitewide & on-page SEO, sitemaps, status pages | SEO | robust SEO | SEO best practices, sitemaps, auto meta; GA/FB pixel |
| Ops integration | Planning Center sync; Google/Apple Calendar; embeds | built-in Tithe.ly Giving; app sync | ChMS content flow; YouTube; Google Calendar | Giving + App + ChMS sync; social scheduler |
| Guest capture | Flows (plan a visit, baptism) | Plan Your Visit | forms/volunteer sign-ups | Plan Your Visit pop-up |
| Launch support | pre-launch checklist; free makeovers | (templates) | Pro services; support services catalog | free migration; staging subdomain |
| Extras | Giving product, Messages (email campaigns), Media library | All Access bundle | AI builder, done-for-you Pro | social scheduler, media library, comment moderation, password-protected pages |

### Convergent findings (evidence layer B — cross-product commonality)

1. **Hosted public website as the managed output** — all four products deliver a hosted, publicly addressable site under the church's own domain, with hosting, security, and uptime handled by the vendor.
2. **Church-shaped content objects as first-class site building blocks** — every product ships ready-made structures for church life: sermon/message library with podcast feed, events calendar with registration, giving integration, guest welcome/plan-a-visit capture, prayer surfaces, livestream embedding. These are pre-built objects, not generic widgets the church assembles from scratch.
3. **Non-technical church operators** — all four explicitly target church staff and volunteers with no coding: visual/inline editing, templates, done-for-you content.
4. **Template/design system with church designs** — template or design libraries (Nucleus done-for-you templates; Tithe.ly ministry templates; ChurchSpring's named design library with one-click swap; Amplify's WordPress-Elementor templates), plus branding controls (logo/colors/fonts) that apply sitewide.
5. **Church identity data reused across the site** — Nucleus "Church Info / Smart Data" used in multiple places; ChurchSpring branding updates sitewide; Amplify one-login + ChMS content flow.
6. **Connection to church operations** — giving platforms (native or embedded), ChMS (form submissions → people records; content flow from ChMS to site), church apps (content sync), external calendars, livestream platforms, social media.
7. **Guest-capture machinery** — plan-a-visit forms/flows that save guest contact info and trigger follow-up (Nucleus Flows, Tithe.ly Plan Your Visit, ChurchSpring Plan Your Visit, Amplify forms).
8. **Multi-editor permissions** — unlimited admins/users with permission controls (Nucleus scoped permissions, ChurchSpring user permissions, Tithe.ly unlimited accounts).
9. **SEO + analytics** — sitemaps, meta content, on-page SEO, analytics integration in all four.
10. **Staging/launch support** — pre-launch checklist (Nucleus), staging subdomain + free migration (ChurchSpring), done-for-you build services (Amplify Pro, Nucleus makeovers).

### Divergent findings

- Build philosophy: instant pre-populated site (ChurchSpring) vs template-first (Tithe.ly) vs structured-sections + engagement widgets (Nucleus) vs three-path incl. AI draft and expert service (Amplify).
- Product posture: standalone (Nucleus) vs suite module (Tithe.ly, Amplify) vs all-in-one platform (ChurchSpring).
- AI site generation present in one sampled product (Amplify).
- Substrate: proprietary builders vs WordPress/Elementor (Amplify Starter path).
- Social scheduling (ChurchSpring only in sample); congregant-side account portal (Nucleus "My Nucleus"); done-for-you service depth varies.
- Market consolidation: legacy standalone builders (Clover Sites, Ekklesia 360, Sharefaith) absorbed into Ministry Brands Amplify — the standalone pole persists (Nucleus) but suites increasingly bundle websites.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

A Church Website Builder is definable by three properties. Remove any one and the product stops being recognizable as this Type:

1. **The church's public website as the managed output** — a hosted, publicly addressable website under the church's own identity (its domain), assembled and edited inside the application, with hosting/security/uptime operated by the vendor.
2. **Church-shaped site structure** — the product's building blocks are organized around church life (welcome/service times & location, sermons/messages with podcast distribution, events, giving, guest welcome/follow-up), provided as ready-made site objects rather than generic widgets the church must assemble.
3. **Non-technical church operators** — the site is built and maintained by church staff and volunteers through template-driven, visual editing, without code.

§24 historical check: the older purpose-built church website products (Ekklesia 360, Clover Sites, Sharefaith — now consolidated under Ministry Brands per that vendor's own legacy-brand list) share this core: church designs + sermons/media + events + giving, built by church staff. Churches building sites on generic tools (WordPress, Squarespace) perform the same *job* but without the Type's product shape (no church-shaped objects, no church-operations integration) — that difference is the boundary, and vendors themselves articulate it ("churches are moving beyond generic website platforms to purpose-built church website builders"). Instant-site and AI-draft onboarding are modern implementations, not part of the core; the older pick-a-design-then-fill-in flow satisfies the same three properties.

### L1 — Common Mature Structure

Present in essentially all mature modern products; not required for the definition:

- Page/section editing model (pages composed of sections/blocks; navigation menus; design customization: fonts/colors/branding)
- Template/design library with the ability to swap designs without losing content
- Custom domain connection (DNS/redirects) + staging/subdomain preview
- SEO machinery (sitemaps, meta, on-page SEO) + analytics integration
- Sermon/message publishing workflow (upload → categorize by series/speaker/date/scripture → display hub → podcast RSS feed)
- Events calendar with registration
- Online giving integration (native or embedded)
- Guest capture (plan-a-visit / connect forms) feeding people records or notifications
- Livestream embedding with site notification (banners)
- Multi-editor permissions (unlimited admins; scoped permissions)
- Mobile-responsive output by default
- Launch support (pre-launch checklists, migration, done-for-you options)

### L2 — Variant / Optional Structure

- Product posture: standalone product vs suite module vs all-in-one platform
- Build philosophy: instant pre-populated site vs template-first vs AI-draft-first vs expert/done-for-you service
- Substrate: proprietary builder vs WordPress/Elementor-based
- Depth of ChMS integration (content flow from ChMS vs standalone people records vs none)
- Church app companion with content sync
- Prayer surfaces (prayer walls, prayer flows with privacy controls), social scheduling, member-only/password-protected pages, congregant account portals
- Multi-campus support; denominational/network headquarters variants
- Denominationally-flavored design libraries
- AI site generation
- Email/blog modules (posts, collections, campaigns) adjacent to church communication

### L3 — Vendor-specific (research notes only)

- Nucleus: Launcher, Flows, PrayerFlow, Info Cards, Banners, Posts/Collections/Smart Campaigns, Messages, Media; free makeovers; $99/$199 pricing; Nucleus Classic vs Nucleus 2; "No bots. No AI." support; 99.99% status claim.
- Tithe.ly: $19/mo standalone; All Access $119/mo bundling; sermon player; Plan Your Visit alerts; "front door" framing.
- Amplify: three paths (AI builder/Starter/Pro); "Amplify Intelligence"; Ministry Content Management System; WordPress Elementor; 42,000+ websites claim; support-services catalog; Clover/Ekklesia/Sharefaith consolidation.
- ChurchSpring: 90-second setup; biblical design names; social scheduler; 1,000+ image media library; 2.9% + $0.30 processing; free migration; version names (Hudson).

## Vendor-specific Findings

See L3 above. None of these entered the canonical model.

## Boundary Findings

1. **vs Visual Website Builder (§04.16)** — closest seam. Same substrate: hosted site, templates, visual editing, custom domain, SEO. The distinguishing structure of this Type: church-shaped content objects as first-class building blocks + church-operations integration (giving/ChMS/app) + the church-operator framing. Remove the church-shaped objects and church integrations → a generic Visual Website Builder (which churches can and do use — the boundary the vendors themselves articulate). **Flag: probable audience/domain-specialized sibling relationship — joint review recommended** (same pattern as the church-communication-platform ↔ email/SMS-marketing flag).
2. **vs Content Management System / CMS (§02.07)** — a CMS is a general-purpose content authoring/management system; this Type is a domain-specialized hosted site assembly for churches. The seam blurs at the suite level (one sampled vendor literally brands its substrate a "Ministry Content Management System"), but the defining output here is the church's public site assembled from church-shaped blocks by non-technical staff — not general content management.
3. **vs Church Management System / ChMS (§25 sibling)** — ChMS is the internal record system (people, groups, giving, events); this Type is the public web presence. They meet at: form submissions → people records; content flow (events/sermons) from ChMS to site; giving. Remove the public site → ChMS; remove the records core → website builder. Market forms a spectrum: standalone builders with ChMS integrations (Nucleus → Planning Center), suite modules (Tithe.ly, Amplify), all-in-one (ChurchSpring); at least one major ChMS (Planning Center) ships no website product.
4. **vs Church Communication Platform (§25 sibling)** — comms platform is targeted outbound messaging to known people (members/guests); website builder is the public web presence for anyone. They meet at guest capture → follow-up, announcement banners, and blog/post + email surfaces (Nucleus Posts/Messages). Remove the public pages → comms platform; remove the messaging loop → website builder. Consistent with the boundary recorded in the church-communication-platform research.
5. **vs Sermon Management (§25 sibling)** — sermon management is the sermon record/prep/publishing workflow; in a website builder the sermon library is a site display object with podcast distribution. Deep sermon workflow belongs to the Sermon Management Type; the site object is a publishing surface.
6. **vs Church Giving Platform (§25 sibling)** — giving platform is the donation processing/management system; the website builder embeds or links giving. Remove the site → giving platform.
7. **vs Event Management / Event Registration (§26/§25)** — dedicated event operations vs the site's calendar/registration object.
8. **"Remove what to become another Type" tests**: remove the church-shaped objects → Visual Website Builder; remove the public site (keep records) → ChMS; remove the site assembly (keep messaging) → Church Communication Platform; remove hosting/site (keep sermon records) → Sermon Management; remove the church domain specialization entirely → generic website builder.

## Uncertainties

- Faithlife Sites unreachable (timeout ×2): the media/sermon-first ecosystem posture is not documented; no claims made about it.
- Tithe.ly Sites help-center-level operational detail not fetched; Sites claims kept at product-page/FAQ strength (no numeric limits asserted).
- Amplify's internal mechanics (AI draft pipeline, WordPress/Elementor starter internals) not documented beyond product-page descriptions; the WordPress substrate is evidenced by portfolio labels + FAQ wording.
- Exact numeric limits (storage, page counts, editor seats) are vendor-stated ("unlimited") and were deliberately kept out of the final document as facts; treated as vendor claims.
- Whether generic builders (Squarespace/Wix) actively market church-specific templates was not verified (not fetched); treated as market context only.
- Planning Center's lack of a website product is verified from navigation in the sibling pass (2026-09-06); not re-verified in this pass.

## Final Synthesis

A Church Website Builder is the church-side public-web-presence system: the managed output is a hosted website under the church's own domain, assembled from church-shaped building blocks (welcome/service information, sermon/message library with podcast distribution, events, giving, guest welcome) by non-technical church staff and volunteers using templates and visual editing. Around that core, mature products add design systems with swappable church designs, single-sourced church identity data reused across the site, SEO/analytics, staging and launch support, multi-editor permissions, livestream embedding, and connections into the church's operations — giving platforms, church management systems (form submissions and content flow), church apps, calendars, and social media. The Type exists as standalone products, as modules inside church-software suites, and as all-in-one platforms; the market has consolidated several legacy standalone builders into suites, but the defining structure — church-shaped site objects built by church volunteers on a hosted site — is stable across postures and eras.
