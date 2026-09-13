# Research Notes — Online Store Builder

## Research Goal

Determine what an "Online Store Builder" is as an Application Type, and settle the pre-hung alias question from the sibling §05.01 passes:

- `e-commerce-platform` (processed 2026-09-08) left Finding 2: "probable alias or DIY-store-creation-emphasis variant of the same Type; joint review recommended with candidate outcomes alias / variant / packaging-split" — this pass must discharge that flag from this side with real evidence.
- `headless-commerce-platform` (processed) pre-hung a posture-spectrum flag naming this leaf, with two working tests: center-of-gravity test and by-design test ("can the product run commerce with no platform-shipped storefront at all?").
- `creator-storefront` (§27, processed) recorded a spectrum flag: "remove the bundled machinery and audience-native posture → store builder; Big Cartel is the straddling pole."
- `cross-border-commerce-platform` (§05.24) recorded a border-machinery test for e-commerce passes to apply.

Core research questions: what exactly is the "building" act? What machinery does the product operate around it? Which merchant population and skill level does the product presuppose? Where is the boundary against the E-commerce Platform sibling, the Visual Website Builder, and the marketplace/creator poles?

## Initial Boundary

Working hypothesis before research:

- An Online Store Builder is a hosted service through which a non-technical merchant creates and runs its own online store: pick a template, add products, connect payments, launch — with hosting, checkout, and order management bundled.
- Closest neighbors and expected seams:
  - E-commerce Platform (§05.01 sibling) — the alias/variant risk; the two labels are used almost interchangeably in market language for hosted template-first products.
  - Visual Website Builder (§04.16) — site-building with commerce attached vs store-building as the organizing purpose; Wix/Squarespace straddle both labels.
  - Headless Commerce Platform (§05.01 sibling) — engine posture vs storefront posture.
  - Online Marketplace / Multi-vendor Marketplace (§05.02) — venue of many sellers vs one merchant's own store.
  - Creator Storefront (§27) — platform-bundled production/payments machinery + audience-native goods vs raw store machinery.
  - Checkout Platform / Shopping Cart Platform (§05.06) — completion-stage machinery slices vs the whole store.
  - Mobile Commerce Application (§05.01 sibling) — expected buyer-side surface vs this seller-side platform.
- Unknowns: whether "no-code self-service assembly" is genuinely definitional or merely universal packaging; whether hosting/service-operation is an invariant or an era artifact; whether AI store generation changes the act of building; whether Big Cartel belongs here or to Creator Storefront.

## Research Questions

1. What are the steps by which a merchant creates the store, as the products themselves document them? What machinery performs each step?
2. What does "no code" actually cover — design only, or the whole operation?
3. What commerce machinery does the same product operate (catalog, cart, checkout, payment, orders)? Where is payment processing vs payment-processor connection?
4. What does the merchant manage after launch (orders, shipping, inventory, customers)?
5. Who is the intended merchant (skill level, scale, goods type), and how does the product say so?
6. Which capabilities are universal vs plan-gated/variant (apps, marketing, multi-channel, international, AI)?
7. Historical check: would the 2000s hosted store services (Yahoo! Store-class; early Shopify) fit the definition? Would self-installed cart scripts fail it, as expected?
8. Verdict material for the pre-hung flags: is the builder leg load-bearing enough to keep-both with E-commerce Platform, or does the evidence force alias?

## Representative Products

Selected for market representation, documentation quality, distinct product philosophy, and distinct customer tiers:

| Product | Philosophy / posture | Customer tier |
|---|---|---|
| Shopify | hosted store builder that grew into a full commerce platform; self-describes under both "online store" and "e-commerce platform" labels; theme-first creation with developer paths alongside | SMB → enterprise |
| Squarespace Commerce | design-led all-in-one builder; designer-crafted templates as the creation anchor; creatives and small brands | micro/small creative |
| Wix eCommerce | template-first general website builder whose commerce subsystem (Wix Stores) makes the store the organizing purpose; AI-first creation | micro/small |
| Big Cartel | minimalist DIY builder for makers/artists; the creator-storefront boundary pole; seller-operated machinery | micro/artist |
| Square Online (Square Websites) | store builder bundled with POS/money machinery for retail- and service-adjacent merchants; catalog imported from Square POS | small brick-and-mortar SMB |

Rejected as primary samples: GoDaddy/IONOS (hosting-bundle packaging, weaker help docs), Ecwid (embed-anywhere posture — useful mention, weaker docs), Volusion (declining category anchor), PrestaShop/OpenCart/osCommerce (self-installed cart scripts — used for the historical check conceptually, not fetched), WooCommerce (already sampled by the e-commerce-platform pass; its self-assembly posture is that pass's evidence).

## Sources

All fetched 2026-09-08 (Layer A = direct observation of official operational documentation; Layer B = cross-product commonality; Layer C = canonical inference):

- Big Cartel — https://help.bigcartel.com/ (Tier 1 — help-center topic map: Set Up Your Shop, Manage Products, Set up Checkout, payment processors, Manage Your Orders, Ship Your Orders, Customization/Templates, Dashboard, Discounts, custom domains, Apps & Integrations, FAQ); https://www.bigcartel.com/product/how-it-works (Tier 2 — 4-step creation flow, DIY positioning, templates, audience).
- Square — https://squareup.com/us/en/online-store (Tier 2 — product page with 5-step creation flow, hosting FAQ, POS sync, plans).
- Wix — https://www.wix.com/ecommerce/website (Tier 2 — 6-step creation flow, AI builder, store management, product types).
- Shopify — https://www.shopify.com/online-store (Tier 2 — theme-first creation, visual editor, no-code statement, headless alternatives, built-in checkout, apps).
- Squarespace — https://www.squarespace.com/ecommerce (Tier 2 — 6-step creation flow, store management, payment processors, product types, FAQ).

Sourcing limitations: Shopify's merchant help center (help.shopify.com) was not fetched — prior passes recorded HTTP 403 from this environment; Shopify evidence rests on product-page material (Tier 2). Wix and Squarespace support-knowledge articles were not fetched beyond the product pages' own step-by-step guides; order-lifecycle detail for both is therefore held at cross-product strength (B), not product-exact. All numeric figures encountered on vendor pages (theme counts, app counts, uptime, conversion uplift, live-store counts, per-product variant limits, transaction-per-second claims) are marketing figures and are deliberately not asserted as operational facts in the Application Document.

## Product Observations

### Big Cartel — DIY builder for makers (Layer A, Tier 1 help center + Tier 2 product page)

- Help-center structure is itself the product's map: **Set Up Your Shop** ("Getting Started: Your First Steps to Online Selling", "Add and Update Products", "Set up Checkout", shipping setup for US and non-US sellers, "How to Customize your Theme"), **Manage Products** (variants, variant groups, imports, digital products, scheduled drops), **Accept Online Payments** (payment processors topic; "Getting Paid"; troubleshooting), **Accept In-person Payments**, **Manage Your Orders** (notifications, order details, bulk edit, notes, packing slip), **Ship Your Orders** (automatic shipping rates, shipping profiles), **Customization** (Templates topic, theme customization, backup/restore templates, custom pages, custom domains), **Dashboard** (order & visitor stats, conversion tracking, product/category stats), **Discounts**, **Apps & Integrations** (sales channels; product creation & sourcing — Printful/Printify print-on-demand; marketing; shop management & shipping; shop design; customer service).
- Creation flow (product page, "How it works"): "4 simple steps" — **1. Choose a template** ("Pick a customizable design that meets your needs") → **2. Add your products** ("Create new listings or import directly from Shopify, Etsy, or Squarespace") → **3. Set up your store** ("Dial in shipping, payments, and design details") → **4. Tell the world!**
- No-code framing, verbatim: "Not a designer? No problem!" / "Easily bring your brand to life with beginner-friendly, customizable templates. Choose a template with preset colors and fonts or go fully bespoke—your call." / "Design made easy. Launch your store fast, no coding required."
- Positioning: "WHERE DIY GOES PRO — Big Cartel is where do-it-yourselfers turn their passion into profit," with a maker audience list (bands, printmakers, jewelry makers, designers, ceramicists, painters, illustrators, photographers, publishers). Compare pages named: Etsy-alternative, Shopify-alternative, Wix-alternative, Squarespace-alternative.
- Machinery: payment processors for cards, wallets, Venmo, PayPal; iOS/Android app to "run your store and take payments wherever you are"; easy-install apps (print-on-demand, product reviews, marketing); plans include a free tier.
- FAQ question "Does Big Cartel make the products I sell?" — the product explicitly does **not** produce the seller's goods (platform-vs-machinery seam vs POD/creator platforms).
- Mobile admin app + in-person payments exist as companion surfaces, not the core.

### Square Online / Square Websites — POS-bundled builder (Layer A, Tier 2)

- Page title: "Sell online - build a free online store or eCommerce website"; product renamed: "Why did Square Online change to websites? — We renamed Square Online to websites to better highlight the website-building tools our product offers. All of the same features and capabilities you use today are included to create a full online store — only the name has changed."
- Creation flow (FAQ, "How to create an online store?"): "create an online store quickly with **no coding required**. Choose your layout, customize your design, add products, set up payments and shipping, and start selling fast" — enumerated: **1.** Design and customize your site by choosing a layout and personalizing it with your brand's colors, fonts, and images. **2.** Add your products by listing items with photos, descriptions, and variations — "or by importing them directly from Square POS." **3.** Set up payments and shipping by enabling secure online payments and choosing shipping, pickup, or delivery fulfillment methods. **4.** Connect a custom domain or register a new domain, then publish. **5.** Promote with built-in SEO, marketing, and social integrations.
- Hosting bundled (FAQ): "Do I get free web hosting when I create a website with Square? — Yes. Our free web hosting platform provides… no restriction on bandwidth… free SSL certificate… SSL also helps power eCommerce by enabling customers to check out directly on your domain."
- Commerce machinery: themes "crafted for online selling. No coding necessary"; customer accounts with order tracking and recommendations; product spotlights; scheduled sales/product drops; shipping (rates, discounts), in-store pickup, local delivery; inventory "across all store locations and sales channels so you never oversell"; catalog/orders/customers synced with Square Point of Sale ("Connect in-person and online sales… Your online store integrates with Square Point of Sale").
- Money posture: Square's own payment processing is built in (processing-fee monetization; free plan tier), unlike processor-connection postures elsewhere.
- Plan-gated feature packaging documented on-page (expanded site customization, advanced item settings, QR code ordering and subscriptions, real-time shipping rates, advanced reporting — plan tiers).

### Wix eCommerce (Wix Stores) — template-first general builder with a commerce core (Layer A, Tier 2)

- Page heading: "BUILD AN ECOMMERCE WEBSITE… Get everything you need to build, run and scale your business—on one AI-powered eCommerce platform."
- Creation flow ("How to create an eCommerce website — Follow these 6 steps"): **1.** Sign up to a free eCommerce site builder. **2.** Build your eCommerce website — "Pick from 100s of templates or use our AI website builder to create your custom store." **3.** Add products to your site (own products, or dropshipping/POD suppliers). **4.** Set up payments and shipping. **5.** Choose your domain and go live. **6.** Manage your online store — "Run orders, inventory and shipping from one dashboard."
- AI store generation: "AI eCommerce Site Builder — Create a professional storefront in minutes. Describe your business and generate a unique site, customize any detail and launch with free hosting." AI design agent (Aria) plus marketing/ops/front-desk AI agents as era-current machinery.
- Store management: sell physical products (variants), print on demand, dropshipping, digital products ("A download link will be delivered to your customer automatically as soon as payment is received"), subscriptions, gift cards.
- Multi-channel: "Sell on your website… on leading marketplaces—all synced to one dashboard" (marketplace/social channel sync); POS; international selling (multilingual, currency conversion).
- Payments: "Accept payments from 80+ global providers" — payment as provider connection; monetization via site plans.
- Site-builder sibling products share one platform (portfolio, blog, restaurant, event sites) — the store is one purpose of one building system, organized around the same template/editor machinery.

### Shopify — the straddling pole (Layer A, Tier 2)

- Page: "The world's best online stores are built on Shopify… flexible options for every size of business."
- Creation, dual posture documented side by side ("Choose how you want to build"): **"Start with a theme"** — "Generate a store design with AI, or pick from 800+ proven themes, then customize things with our easy-to-use visual editor" — and **"Build completely custom"** — "Create a theme from scratch, go headless with Hydrogen…, or choose your own stack using Shopify's APIs."
- No-code statement for the theme path, verbatim: "Powerful customization tools that let you nail every detail. **No coding required—just your imagination**"; "Drag and drop — Effortlessly add pages and switch up the layout with Shopify's online store editor"; AI bespoke blocks ("Just say what you want in a few words and let AI build new content blocks").
- Commerce machinery "built into every store": the operated checkout ("The world's best-converting checkout — Powered by the best checkout in the world" [marketing claim]; checkout as product), payments, taxes; infrastructure operation ("99.9% uptime" [marketing]; "Monitoring uptime, optimizing for speed…—we handle it all").
- Post-purchase machinery in nav scope: Orders & Inventory, Shipping, Finances, Workflow Automation, Analytics, Marketing & Discounts, Customer Accounts; App Store ("16,000+ apps" [marketing]) and Theme Store ecosystems; international/B2B/marketplace/POS/Shop-app channel breadth.
- The same product documents headless alternatives (Storefront API, Hydrogen toolkit, Oxygen hosting) — headless is an option, not the identity; the theme-first path is presented first.

### Squarespace Commerce — design-led builder (Layer A, Tier 2)

- Page title: "Ecommerce Website Builder - Start an Online Store — Squarespace"; "Sell anything — All you need to power your ecommerce website."
- Creation flow ("How to create an ecommerce website"): **1.** "Find an ecommerce template and start your free trial." **2.** Register or transfer your business's domain name. **3.** "Set up your online store by adding products and connecting a payment processor." **4.** (services via scheduling) **5.** "Customize your online store categories and content with the website builder." **6.** Grow with email marketing and SEO.
- Templates as the creation anchor: "Our easy-to-customize templates are crafted by world-class designers to help create the web's most expressive online stores"; AI product descriptions/page copy as era-current assistance.
- Store management, verbatim list: "Handle shipping and fulfillment, taxes, payments and more, all in one place" — flexible shipping options (flat-rate, weight-based, real-time), "Simple payment and checkout options for your customers," "automatically calculate up to date sales tax rates," "Effortlessly manage your orders and engage with your customers."
- Product types: physical products, subscriptions, digital content ("via direct download from your site"), services (scheduling/invoicing), memberships; print-on-demand via a named fulfillment partner (5-step connection flow documented); POS on iOS for in-person selling with synced inventory.
- Payments: processors connected (Stripe/PayPal/Apple Pay/Afterpay/Klarna named as integrations) — payment as processor connection, not built-in processing.
- FAQ self-positioning: "Squarespace is more than a website builder – it's an all-in-one platform designed to launch your ecommerce website" — and the same platform sells blogs, portfolios, memberships: site-builder and store-builder share one machinery base.

## Cross-product Comparison

| Structure | Shopify | Squarespace | Wix | Big Cartel | Square | Evidence |
|---|---|---|---|---|---|---|
| Template/theme-first store creation as the documented front door | Yes ("Start with a theme… visual editor" presented first) | Yes (step 1 = find an ecommerce template; designer templates as anchor) | Yes (step 2 = pick templates or AI builder) | Yes (step 1 = choose a template) | Yes (themes "crafted for online selling"; layout choice step 1) | A×5 → B |
| No-code self-service assembly stated as the normal path | Yes ("No coding required—just your imagination"; drag-and-drop editor) | Yes ("easy-to-customize… with the website builder") | Yes (AI builder + step list; "no coding required" FAQ) | Yes ("no coding required"; "beginner-friendly") | Yes ("no coding required" FAQ) | A×5 → B |
| Guided setup sequence: template/design → products → payments/shipping → launch/promote | Setup steps as article not fetched; theme/checkout/products onboarding structure visible | Yes (6 steps) | Yes (6 steps) | Yes (4 steps) | Yes (5 steps) | A×4 (+B for Shopify) → B |
| Service operates hosting/security/technical operation | Yes (infrastructure operation, "we handle it all") | Yes (all-in-one platform posture) | Yes ("launch with free hosting") | Yes (hosted service; plans) | Yes (hosting FAQ: "Yes… free web hosting… SSL") | A×5 → B |
| Merchant-defined product catalog in-product (products/variants) | Yes | Yes | Yes (variants; product types) | Yes (add/update products, variants, variant groups, import) | Yes (list with variations, or import from POS) | A×5 → B |
| Buying surface operated by the same product (browse → cart → checkout → payment) | Yes ("built into every store" checkout) | Yes ("Simple payment and checkout options") | Yes | Yes (Set up Checkout help topic; processor setup) | Yes ("customers can check out directly on your domain") | A×5 → B |
| Orders held and managed in-product after purchase | Yes (Orders & Inventory scope; B for lifecycle detail) | Yes ("Effortlessly manage your orders") | Yes ("Run orders… from one dashboard") | Yes (Manage Your Orders help topics: details, bulk edit, notes, packing slip) | Yes (orders synced with POS; fulfillment methods) | A×4 + B(Shopify) → B |
| Payment processing vs processor connection | Platform payments + gateways (checkout owned) | Processors connected (Stripe/PayPal/…named as integrations) | Providers connected ("80+ global providers") | Payment processors topic (cards, wallets, Venmo, PayPal) | Own processing built in (MoR posture; processing-fee monetization) | B — both postures present; processing not definitional |
| Custom domain connection/registration | Yes | Yes (domain step; registrar) | Yes (domain step) | Yes (custom domains help topic) | Yes (domain step) | A×5 → B |
| Promotions/discounts | Yes (Discounts in scope) | Yes (promotional discounts in FAQ) | Yes (marketing suite) | Yes (Discounts help topic) | Yes (scheduled sales/drops) | A×5 → B |
| Shipping/fulfillment configuration | Yes (Shipping scope) | Yes (flat-rate/weight-based/real-time) | Yes (shipping step; fulfillment methods) | Yes (shipping profiles, automatic rates help topics) | Yes (shipping/pickup/delivery step) | A×5 → B |
| Inventory linkage | Yes (Orders & Inventory) | Yes (inventory management in FAQ; POS sync) | Yes (inventory in dashboard) | Product management; stock not directly observed (weak) | Yes ("never oversell" across locations/channels) | B — linkage common, depth varies |
| Customer accounts (shopper) | Yes (Customer Accounts product) | Yes (accounts implied in FAQ) | Yes (accounts with order tracking) | Not directly observed | Yes ("Let customers create accounts to track orders") | B |
| Apps/extensions ecosystem | Yes (App Store) | Yes (Extensions) | Yes (apps; also "no extra plugins or add-ons required" for core commerce) | Yes (Apps & Integrations incl. POD) | Yes (app marketplace) | B |
| Marketing/SEO built in | Yes (Marketing & analytics nav) | Yes (SEO, email campaigns) | Yes (SEO, email, social) | Yes (marketing help topics) | Yes (SEO, marketing, social) | A×5 → B |
| Analytics/dashboard | Yes (Analytics) | Yes (Analytics; commerce insights) | Yes (website analytics) | Yes (Dashboard stats topics) | Yes (reporting) | A×5 → B |
| Mobile admin companion app | Not directly observed this pass | Yes (Squarespace app: inventory, products, shipping labels) | Yes (Wix app: "Run your business on the go") | Yes (iOS/Android app: run store + take payments) | Yes (POS sync posture) | B |
| Multi-channel breadth (marketplaces/social/POS/international) | Yes | Yes (POS iOS; POD partner) | Yes (marketplace sync; international) | Yes (in-person payments; POD apps) | Yes (POS sync central) | B — channel breadth common, not definitional |
| Non-store content capability (blog/pages/portfolio) | Yes (pages; custom content structures) | Yes (blog/portfolio on same builder) | Yes (portfolio/blog/event site siblings) | Yes (custom pages help topic) | Basic pages; single ordering-page variant | B — common, not definitional |
| AI-assisted store creation | Yes (AI theme/design generation; AI blocks) | Yes (AI builder; AI descriptions) | Yes (AI builder; AI agents) | Not observed | Not observed | A×3 — era-current, optional |
| Self-installed software anywhere in the flow | No | No | No | No | No | A×5 — supports service-operation as invariant |

## Canonical Abstraction

### L0 — Defining Invariant (deliberately small)

An Online Store Builder is the merchant's self-service way to create and run its own online store. Three jointly-held structures:

1. **No-code, self-service store assembly by the merchant** — the merchant builds the store itself inside the product: it selects from ready-made designs (templates/themes), shapes the store through visual/design editing and guided setup, and connects its catalog, payments, shipping, and domain — with development work outside the product's normal path. The template is the common implementation, not the invariant; the invariant is that a non-technical merchant performs the assembly. *(Remove → a developer-operated e-commerce platform or engine; the "builder" act is gone and the product becomes the sibling's territory.)*
2. **The merchant's own store as a service-operated venue** — one store per merchant relationship, branded and owned by the merchant (its own name/domain, its own catalog, its own orders), while the service operates the technical infrastructure — hosting, security, availability — so the merchant never runs it. *(Remove service operation → self-installed shopping-cart software; remove merchant ownership of the venue → a marketplace.)*
3. **The complete buying-and-ordering machinery of record operated by the same product** — the merchant-defined catalog is presented and sold through the product's own storefront, cart, checkout, and payment path, and each purchase becomes an order the merchant manages inside the same product (fulfillment, shipping configuration, refunds). *(Remove → a website builder with third-party buy buttons; remove the catalog → a designable shell; keep only checkout → the completion-stage machinery slice.)*

Jointly-held is load-bearing:
- 1 alone = a website builder / template site with no selling machinery
- 2 alone = plain hosting / a hosted page
- 3 alone = installed cart machinery assembled by technical effort (the cart-script heritage)
- 1+2 without 3 = an attractive storefront with nothing to buy
- 1+3 without 2 = store machinery the merchant self-hosts and assembles (open-source cart scripts)
- 2+3 without 1 = a hosted commerce operation without the builder posture = the E-commerce Platform sibling

### L1 — Common Mature Structure

Present across the sample; expected by the market, not definitional:

- product catalog depth: variants/options, product types beyond physical (digital downloads, subscriptions, gift cards), media, imports
- discounts/promotions; scheduled sales/drops
- shipping configuration (manual profiles, automatic/real-time rates) and tax configuration/calculation
- inventory linkage with multi-location/multi-channel sync in deeper products
- customer (shopper) accounts with order tracking
- order-management tooling: order details, notes, fulfillment actions, refunds, packing slips, notifications
- analytics/dashboard (orders, visitors, conversion, product performance)
- custom domain registration/connection
- built-in SEO/marketing/email tools
- app/extension ecosystems
- mobile admin companion apps
- plan/subscription monetization with feature gating

### L2 — Variant / Optional Structure

- product philosophy: design-led (templates as brand expression) ↔ commerce-machinery-led ↔ bundle-led (store as an extension of POS/money machinery)
- audience: makers/artists/micro-sellers ↔ small businesses ↔ retail- and service-adjacent merchants
- money posture: own processing bundled (processing-fee monetization, free tiers) ↔ third-party processor connections
- AI-assisted store generation and AI agents (era-current; absent from some products)
- site-builder breadth: the same building system selling non-store sites (blogs, portfolios) vs store-only products
- channel breadth: marketplace/social sync, in-person POS, international selling (border-machinery test from the cross-border pass applied: multi-currency/multilingual without a foreign-market model stays inside this Type)
- headless/custom-storefront escape hatches offered by the largest products (options, not identity)
- single-page ordering page vs multi-page store (bundle pole's minimal form)

### L3 — Vendor-specific (kept in Research Notes only)

- Shopify: theme-count/AI-generation/visual-editor claims, Horizon theme family names, Liquid/Hydrogen/Oxygen tooling names, Sidekick, metaobjects/metafields, contextual storefronts, Editions, conversion/uptime marketing figures, app/theme store scale figures.
- Squarespace: template names, Acuity Scheduling/Tock/Bio Sites/Unfold satellite products, Printful "Custom Merch" 5-step flow, Extensions program, Premium/Pros programs.
- Wix: Aria/Kleo/Juno/Omni agent names, Wix Headless as a separate product line, Wix Checking/Capital, Cart2Cart migration, live-store and transaction-rate marketing figures, per-product variant limit figure.
- Big Cartel: plan names/tiers, catalog import from Shopify/Etsy/Squarespace, testdrive demo shops, live classes, "Does Big Cartel make the products I sell?" FAQ framing.
- Square: Square Online→websites rename, free plan with processing fees, POS catalog import, QR code ordering (plan-gated), processing-rate-per-tier structure.

### Rejected Findings (anti-overfitting)

- "Store builder = templates" — **rejected** as definitional: AI store generation is documented as an alternative creation path in 3/5 samples; templates are the common implementation of no-code assembly. The invariant is merchant-performed assembly, not the template artifact.
- "Store builder = SaaS subscription product" — **rejected** as a definitional framing: monetization varies (site plans, free tiers with processing fees, premium tiers); what is universal is that the *service operates the infrastructure* (5/5), not the billing shape.
- "Built-in payment processing defines it" — **rejected**: processor connection is the dominant posture (3/5 observed); one sample bundles its own processing (variant). The owned *checkout* is definitional; the processor is not.
- "AI store generation defines it" — **rejected**: 2/5 samples carry none; era-current capability.
- "Blogging/portfolio content defines it" — **rejected**: content capability is common (site-builder siblings share machinery) but two store-only samples satisfy L0 without it.
- "Multi-channel/marketplace sync defines it" — **rejected**: breadth varies; L2.
- "Free tier + processing-fee monetization defines it" — **rejected**: monetization posture, 2/5 observed clearly.

## Boundary Findings

1. **vs E-commerce Platform (§05.01 sibling) — pre-hung flag DISCHARGED from this side; verdict: keep-both as seam-defined siblings, NOT alias.** The e-commerce-platform pass's three candidate outcomes were alias / DIY-emphasis variant / packaging-split. Evidence from five builder-side samples: the no-code self-service assembly leg is A-layer universal (5/5, each product's documented front door — "no coding required" verbatim in 4), while that sibling's own sampled population does not carry it as defining (WooCommerce presupposes merchant-assembled WordPress hosting; Adobe presupposes enterprise technical operation). The two L0s differ by exactly one load-bearing leg over a shared three-part commerce spine (merchant catalog, operated buying surface, checkout→order). Removal tests run in both directions: remove assembly → the sibling; add assembly-as-the-act → this Type. This matches the keep-both precedent for surface-defined sibling Types sharing a spine. The market's labeling overlap is real (Shopify self-describes under both labels; the sampled population contains a strong straddling pole) but labeling overlap is not structural identity. Final consolidation (if any) left to the taxonomy owner; no directory change.
2. **vs Headless Commerce Platform (§05.01 sibling) — posture-spectrum flag DISCHARGED from this side using that pass's own tests.** By-design test: a store builder cannot run commerce with no platform-shipped storefront — the storefront assembly *is* the product (L0 leg 1); every sampled product's creation flow begins with the store surface. Headless surfaces appear only as options inside the largest products (Shopify Hydrogen/Oxygen documented on the same page as the theme path; Wix ships headless as a *separate product line* — supporting that the headless posture is a different product identity, not a feature). Center-of-gravity test: whenever storefront assembly is the defining act, the product is a store builder regardless of optional APIs. Consistent with the sibling pass's continuum finding; the store builder is the storefront-first extreme of the monolith pole.
3. **vs Visual Website Builder (§04.16) — NEW flag for joint review.** The same two products (Wix, Squarespace) market "website builder" and "ecommerce" from one shared machinery base (templates, editor, hosting), and both self-describe as "more than a website builder." The seam this pass adopts: the buying-and-ordering machinery of record (catalog → cart → checkout → orders operated by the product) is what makes the product a store builder rather than a site builder with commerce attached; dedicated store-admin surfaces (products, orders, payments) mark the store-first organizing purpose. Wix/Squarespace are straddle poles by marketing but store-first in structure. Recommended: joint review when the Visual Website Builder leaf is processed; candidate outcomes keep-both with the machinery-of-record seam.
4. **vs Creator Storefront (§27, processed) — spectrum flag DISCHARGED from this side; keep-both ratified.** The creator pass's diagnostic is confirmed from this side: Big Cartel — sampled here — is structurally a store builder (raw machinery: merchant picks template, connects processors, configures shipping, handles support; FAQ confirms the platform does not produce the goods) marketed to makers, while creator storefront platforms bundle production/payments/support and are audience-native. Remove the bundled machinery and audience posture → store builder. The spectrum seam stands as recorded.
5. **vs Online Marketplace / Multi-vendor Marketplace (§05.02, processed)** — one merchant's own venue vs one operator's venue of many independent sellers. The marketplace pass's remove-test ("remove many-sellers → operator's own webstore") lands exactly on this Type's territory; Big Cartel's own compare page ("Etsy alternative") is the market naming the seam from this side. Keep-both.
6. **vs Checkout Platform / Shopping Cart Platform (§05.06, processed)** — those are machinery slices (standalone completion stage; pre-purchase accumulation). Here cart/checkout are internal, owned structures of the whole store operation (consistent with the checkout pass's own seam note). Keep-both.
7. **vs Mobile Commerce Application (§05.01 sibling, unprocessed)** — mobile appears in this sample as (a) responsive storefronts the builder produces, and (b) merchant-side mobile admin/POS companion apps. Both are channel/companion surfaces; the seller-side platform is the Type. Ratified from this side as expected.
8. **vs Cross-border Commerce Platform (§05.24, processed) — border-machinery test applied as requested.** Multi-currency/multilingual/international selling appear as standard capabilities in-sample; no foreign-market model or border-obligation machinery observed in any sampled L0. The test passes: without border machinery, an internationally-capable store builder remains this Type.
9. **vs CMS (§02.07, processed)** — presentation vs transaction. Adding the buying-and-ordering machinery of record to a site-builder base produces exactly this Type (Wix/Squarespace are the visible seam products: one machinery base, store-first organizing purpose, dedicated commerce admin). Presentation-only remains CMS/website-builder territory.

## Historical / Market-Sample Check

- **Hosted store-service generation (late 1990s–2000s, conceptually)**: merchant signs up with a hosted store service, picks a template, adds products in a web admin, sells through the service's hosted cart/checkout, manages orders in the same admin. Satisfies all three L0 legs without theme marketplaces, app stores, AI, or mobile apps. The category name itself ("build your online store") was the marketing of this generation. Historical check **passed** at conceptual level; no primary source fetched this pass, so the claim is held at C-strength (canonical inference from the documented structure of the category and its continuity into the sampled products).
- **Self-installed cart-script generation (osCommerce-class and lineage, conceptually)**: merchant assembles hosting, installs software, configures templates and code. Fails the service-operation leg and the self-service-assembly-as-normal-path leg — correctly outside; this is the e-commerce-platform/cart heritage the builder category defined itself against.
- **Paper-era analog (thin ancestor)**: a craftsperson's printed catalog + mail order form + order ledger satisfies the pattern structurally but has no product-operated digital buying surface — recorded as the pre-history, not a member.
- **Regional products**: regional hosted store services satisfy the L0 with region-specific payment methods — supporting payment posture as variant, not definition.
- **Tier poles**: minimalist maker-tier products and the largest multi-product platforms both satisfy the three legs — supporting depth items as L1/L2.

## Uncertainties

- Shopify's merchant-side setup articles and order-status vocabulary were not directly observed (help center unreachable per prior passes); Shopify setup-sequence evidence is held at B-strength (structure visible on product pages) and its order lifecycle at the e-commerce spine level (consistent with the sibling pass's same limitation).
- Big Cartel's in-product order statuses and Squarespace's order lifecycle detail were not fetched at article depth; both held at B-strength (help-center topic maps observed, not article contents).
- Whether any self-hosted product genuinely carries the "no-code assembly without service operation" combination was not researched in depth (candidate class not found in market labeling; recorded as an open edge).
- Plan-gated feature packaging (which capabilities sit at which tier) deliberately not asserted; pricing out of scope.
- All numeric product figures (theme/app counts, uptime, conversion, store counts, limits) are marketing figures, used nowhere as operational facts.

## Final Synthesis

An Online Store Builder is the service through which a merchant creates and operates its own online store by itself: the merchant assembles the store through no-code builder machinery — ready-made designs, visual editing, guided setup, increasingly AI generation — the service hosts and runs the store's technical operation under the merchant's own brand and domain, and the same product operates the store's complete buying-and-ordering machinery, from the merchant's catalog through storefront, cart, checkout, and payment to orders managed in place. Around this core, mature products add catalog depth, discounts, shipping and tax configuration, inventory linkage, customer accounts, analytics, marketing/SEO, domains, app ecosystems, and mobile admin apps. The Type's name names its act — building — and that act is the load-bearing difference from the E-commerce Platform sibling: same commerce spine, opposite entry posture. It is bounded on one side by surfaces that assemble without transacting (visual website builder), on another by machinery that transacts without the merchant-assembled venue (headless engine, checkout slice), and on a third by venues that sell many merchants' goods (marketplace) or bundle the seller's production and audience (creator storefront).
