# Research Notes — Database Sandbox Platform

Research date: 2026-09-07
Slug: `database-sandbox-platform` (§12 Software Development & Product Engineering)

## Research Goal

Establish what a Database Sandbox Platform is from real market products: what the platform provides (the unit of provision), who uses it and for what, what the sandbox lifecycle looks like, how far it extends (does "sandbox" imply free? ephemeral? browser-only? SQL?), and where its boundaries sit against the already-processed siblings (Database IDE, Database Management Console, Database Dev/Test Environment Manager) and against managed database platforms.

## Initial Boundary (hypothesis before research)

- Working hypothesis: a platform that gives individuals isolated, disposable database environments for hands-on experimentation (learning, prototyping, evaluating an engine) without owning infrastructure and without touching any system of record.
- Nearest neighbors per the directory: Database Dev/Test Environment Manager (§12, processed — its pass left an explicit boundary flag for this leaf), Database IDE (§12, processed), SQL Client (§12, unprocessed), Database Schema Design Tool (§12, unprocessed), Database Management Console (§12, processed), Cloud IDE / Dev Container / Developer Environment Manager (§12, unprocessed), Agent Tool / Computer-use Platform (§13, processed — code-execution sandboxes), Data Science Workbench (§13, processed), Malware Analysis Sandbox (§15 — homonym).
- Counterparty obligation: the dev/test pass proposed "sandbox = isolated scratch database NOT derived from a defined authoritative source and NOT fleet-managed" and asked this pass to ratify/refine; it also flagged platform-native database branching (Neon) as a packaging variant watch item.

## Research Questions

1. What is the unit the platform provisions (instance / cluster / project / schema / environment)? What does "create" look like step by step?
2. What does the user actually do inside: run queries, load/create data, prototype schemas, connect their own tools and application code?
3. What acquisition model applies: anonymous vs account; free tier vs credits vs trial; no-card vs payment method?
4. What limits and lifecycle consequences define the sandbox posture (size caps, compute caps, scale-to-zero, suspension, expiry, deletion-after-grace, reset)?
5. What starting material is provided: empty environment vs prebuilt datasets/templates vs sample code?
6. What interfaces exist: web console, in-browser query surface, connection details for external tools, CLI/API?
7. Is "sandbox" the product or a tier/posture of a broader managed-database platform? (packaging question — central to this leaf)
8. Boundary vs dev/test environment manager: does the derivation-from-source discriminator hold from the sandbox side?
9. Historical check: would pre-cloud forms (university teaching servers with per-student schemas, early web SQL playgrounds, zero-install local engines, free developer editions) satisfy the definition?

## Representative Products

Selection principles: market representation across engine classes and postures, documentation completeness, different product philosophies, different customer tiers. The market turned out to have few pure-play "sandbox" products; the sample therefore spans the packaging spectrum deliberately.

| Product | Engine class | Packaging posture | Sources reached |
|---|---|---|---|
| Neo4j Sandbox | graph (Cypher) | literal named sandbox product: free, browser-launched, pre-seeded use-case environments | product page (Tier 2); docs 404 ×2 |
| Neon | Postgres | managed backend platform; permanent free plan + anonymous "Claimable" expiring projects + branching (dev/test overlap specimen) | docs root + pricing page (Tier 1–2) |
| Supabase | Postgres + app backend | hosted backend platform; project-per-user provisioning via dashboard | docs root + platform overview (Tier 2) |
| CockroachDB Cloud | distributed SQL | managed DB service; trial-credit clusters + monthly free Basic allowance with payment method | quickstart + free-trial docs (Tier 1) |
| Redis Cloud | key-value / data structures | managed DBaaS; fixed-size free database + subscription tiers | docs index (Tier 1–2) |

Candidates unreachable this pass (recorded, no claims made about them): MongoDB Atlas free-cluster docs (404 ×3), Google BigQuery Sandbox documentation (timeout ×2 → abandoned per network rule), Oracle Live SQL (404 + 403). These are commonly referenced named sandbox/learning offerings; their omission narrows the playground and analytics poles of the sample (see Uncertainties).

## Sources

- Neo4j — Sandbox product page: https://neo4j.com/sandbox/ (fetched 2026-09-07)
- Neon — Documentation root: https://neon.com/docs/introduction (fetched 2026-09-07)
- Neon — Pricing plans: https://neon.com/pricing (fetched 2026-09-07)
- Supabase — Docs root: https://supabase.com/docs (fetched 2026-09-07)
- Supabase — Platform overview: https://supabase.com/docs/guides/platform (fetched 2026-09-07)
- Cockroach Labs — Quickstart with CockroachDB: https://www.cockroachlabs.com/docs/cockroachcloud/quickstart (fetched 2026-09-07)
- Cockroach Labs — Try CockroachDB Cloud for free: https://www.cockroachlabs.com/docs/cockroachcloud/free-trial (fetched 2026-09-07)
- Redis — Redis Cloud docs index: https://redis.io/docs/latest/operate/rc/ (fetched 2026-09-07)

Sourcing limitations: MongoDB, Google Cloud, and Oracle surfaces repeatedly failed (404/403/timeout). Neo4j Sandbox operational docs could not be reached (docs URL 404 ×2; the sandbox application itself is JS-gated), so Neo4j evidence is product-page level. Supabase free-plan specifics (limits, pause behavior) were not verified. No numeric claims in this research rest on inaccessible sources; all precise numbers below come from the fetched pages and stay in these notes.

## Product Observations

### Neo4j Sandbox (product page evidence, Layer A for what the page states)

- Named offering: "Get started with Neo4j Sandbox"; CTA "Launch the Free Sandbox" (free).
- "No Download Required" — the platform operates the environment; browser is the entry.
- "Pick a project and get started in less than 60 seconds" — provisioning is near-instant and choice-driven.
- The sandbox is chosen as a pre-seeded **use-case project**: Movies ("Learn Cypher with the Movie Database"), Network and IT Management, Crime Investigation (POLE — Person/Object/Location/Event model), Paradise Papers by ICIJ (dataset + guide from ICIJ). Evidence that sandboxes commonly carry guided datasets rather than empty instances — at least at the learning pole.
- Not observed this pass: lifecycle/expiry details, instance limits, console internals (docs 404; app JS-gated). No claims made.

### Neon (docs root + pricing page, Layer A)

- Positioning: "Neon is the backend for apps and agents"; the database product is serverless Postgres with "branching, autoscaling, scale to zero, and instant restore" (Lakebase Postgres naming current at fetch time).
- The **project** is the top-level container: "primary database, branches, compute. Like a Git repo, with one project and many branches."
- Free plan documented as **permanent (not a trial); no credit card required**; audience framing "Prototypes, side projects, and small teams" vs the Scale plan's "Production-grade workloads" — an explicit two-posture split inside one platform (experiment pole vs production pole).
- Free-plan mechanics (all documented on the pricing page): compute limit (100 CU-hours/project), storage cap (0.5 GB/project), egress allowance (5 GB); "Hitting any Free monthly limit … suspends compute until the next billing month"; scale-to-zero after 5 minutes of inactivity; 10 branches per project.
- **Claimable Neon**: "an instant project, with no signup and no card. Provision from that page or the API. Claim it to a Neon account before expiration to keep it." — anonymous, expiring, claimable environment provisioning; the purest sandbox-acquisition mechanic observed in the sample.
- Branch TTLs documented in cost guidance ("Delete unused branches, or set TTL") — bounded-lifetime machinery at the environment/artifact level.
- Connection machinery: per-framework/language/ORM connection guides; Data API for HTTP queries; full management API and CLI; MCP integrations for AI coding tools; an "Agent Plan" for AI agent platforms (era note: sandboxes are increasingly consumed by agents, not only humans).
- Boundary-relevant: Neon's branching documents dev/test, CI, and preview workflows (per the dev/test pass's research). From this pass's viewpoint: same product, two workflow families — branching/derived-branch workflows (dev/test family) vs instant free/claimable projects for trying Postgres (sandbox surface).

### Supabase (docs root + platform overview, Layer A for structure; free-tier specifics unverified)

- "Supabase is a hosted platform that allows you to get started without needing to manage any infrastructure. Visit dashboard and sign in to start creating projects." — platform-operated environments, dashboard entry, account-gated.
- Each **project** bundles: "A dedicated Postgres database", auto-generated APIs, Auth and user management, Edge Functions, Realtime API, Storage — i.e., the environment is a working database plus attachable backend services.
- **Organizations** group projects with team members and billing settings; access control documented; SLA offered (production-facing posture alongside the self-serve start).
- Free-plan limits/pause mechanics: not verified this pass (docs pages 404). No claims.

### CockroachDB Cloud (quickstart + free-trial docs, Layer A)

- Provisioning workflow, step by step: create account → Get Started page → "Create cluster" → select plan (Standard) → choose cloud provider (GCP/AWS) and region(s) → set capacity (default 2 vCPUs) → name cluster → "Create cluster" → **"Your cluster will be created in a few seconds"** → Create SQL user dialog → generate & save password (shown only once) → connection dialog → copy connection string → run vendor-provided sample app (creates a table, inserts data, reads it back).
- The environment is a real working cluster the user immediately connects their own code to.
- Low-commitment entry documented in two forms: **$400 free trial credits** for the first organization (billing begins when credits are used/expired; payment method required by trial end), and a **monthly free Basic allowance** ($15 ≈ 50M request units + 10 GiB storage) that requires a payment method on file.
- Lifecycle consequences documented: without a payment method at trial end, a 30-day grace period begins ("clusters are throttled… restricted from modifying configuration"); at grace end, "all clusters in the organization are deleted. Deleted clusters can not be restored." — explicit expiry → degradation → deletion machinery.
- Posture: evaluation/trial of a commercial service — the sandbox mechanics (bounded, disposable, credits-funded) are present, but the product's center is the paid DBaaS.

### Redis Cloud (docs index, Layer A for what the index states)

- "A fully managed database-as-a-service… The fastest way to set up Redis."
- **"Try Redis Cloud to set up your free 30MB database"** — a fixed-size free database as the standing sandbox offer.
- Quick start path: create free database → connect with redis-cli, a Redis client, or **RedisInsight** (vendor GUI) — connection handoff to the user's own tools, GUI companion included.
- Databases are created and managed under **subscriptions** (Essentials vs Pro plans) — tier ladder from free/small to production; REST API and a CLI (`redisctl`) for management.

## Cross-product Comparison

| Dimension | Neo4j Sandbox | Neon | Supabase | CockroachDB Cloud | Redis Cloud |
|---|---|---|---|---|---|
| Provisioned unit | sandbox instance from a use-case project | project (primary database + branches + compute) | project (dedicated Postgres + backend services) | cluster (plan/cloud/region/capacity) | database (under a subscription) |
| Created via | web launch page | console / API / claimable page | dashboard sign-in | console wizard | console / quick start |
| Speed / friction framing | "less than 60 seconds", no download | "instant"; claimable = no signup, no card | self-serve sign-in | "created in a few seconds" after account | "fastest way to set up"; free 30MB |
| Identity at acquisition | launch page (login not directly observed) | none (claimable) → account on claim | account required | account required | account (trial flow) |
| Hands-on handoff | browser-first, guided | connection guides, Data API, CLI/API | project APIs + dashboard | SQL user + connection string + sample code | CLI / client / GUI tool |
| Free/low-commitment offer | "Free Sandbox" | permanent free plan, no card | (free plan exists per market; not verified this pass) | $400 trial credits; $15/mo Basic allowance (card required) | free 30MB database |
| Bounded by | (not observed) | compute/storage/egress limits; suspend at limit; scale-to-zero; claim expiry; branch TTL | (not verified) | credit exhaustion → trial end → grace → deletion | fixed size (30MB) |
| Starting material | pre-seeded use-case datasets + guides | empty projects (+ branch templates) | project with instant APIs | sample code repos | quick start, GUI |
| Production pole in same product | (separate commercial Neo4j offerings) | Scale plan "production-grade" | paid tiers + SLA | Standard/Advanced plans | Pro plan |
| Programmatic control | (not observed) | management API + CLI + MCP | Management API + CLI | (console-centric in fetched docs) | REST API + CLI |

**Stable commonalities (Layer B, across the sample):**

1. The platform provisions and operates a **real, working database environment** the user never installs (4/5 direct; Neo4j's "No Download Required" is the fifth).
2. Creation is **self-service and near-instant** through a web surface (Neo4j, Neon, CockroachDB direct; Redis "fastest" framing; Supabase dashboard).
3. The environment is **handed over for hands-on use** — query in place or connect external tools/code via credentials/connection details (all five).
4. A **low-commitment entry offer** (free tier / fixed-size free DB / credits / claimable no-signup) sits at the front door of the same platform that sells production tiers (4/5 direct; Supabase unverified).
5. **Experiment-vs-production posture split** — the low-commitment pole is framed for trying/prototyping; the paid pole for production (explicit language at Neon; tier ladders at Redis/CockroachDB/Supabase).
6. **Bounded environments with lapse consequences** — limits that suspend, claims/expiries that lapse, deletion after grace (Neon, CockroachDB direct; Redis bounded by size; this is where the sample is thinnest — 2/5 fully documented).
7. **Guided starting material** (datasets, guides, sample code) appears at the learning pole (Neo4j strongest; CockroachDB sample code; Redis quick start).

**No commonality was found for:** shared/fleet environment governance, refresh-from-source machinery, multi-environment template management — these appear only in the dev/test manager Type, supporting the proposed discriminator.

## Canonical Abstraction

### Level 0 — Defining Invariant

A Database Sandbox Platform is a platform that **provisions real, working database environments on demand and hands them to individuals for hands-on experimentation**, under a posture in which the environment is **isolated, bounded, and expendable** — nothing in it is a system of record.

Four properties; removing any one changes the Type:

1. **Platform-provisioned working environment** — the platform creates and operates an actual database environment (instance/cluster/project/schema) that supports the engine's real query language and real drivers; the user installs and operates nothing. (Remove → tutorials, local engines, simulators, product tours.)
2. **Hands-on use by an individual** — the user works *inside* the environment: runs queries, creates/changes schema and data, connects their own tools and application code. (Remove → canned demo/marketing sandbox.)
3. **Isolation with nothing-of-record** — the environment is self-contained (separate from other users of the platform and from any production system of the user); no data in it is authoritative; changes have no outward effect. (Remove → shared hosted database or a production service.)
4. **Bounded-and-expendable posture** — the environment is acquired with low commitment (free, credits, no-signup, or trial-like terms), lives under explicit limits or a bounded arrangement, and is expected to be discarded, to lapse, or to be recreated — never depended on. (Remove → a commercial managed database service with production commitment.)

Historical check: a university teaching server issuing each student a disposable personal schema, and an early web SQL playground with scratch schemas, both satisfy the four properties without any cloud marketing, free-tier mechanics, or modern console — the definition survives. A zero-install local engine (e.g., single-file embedded databases) fails property 1 (no platform operation); a "free developer edition" download fails it too (a license, not a platform-provided environment). Free web delivery is therefore NOT definitional.

### Level 1 — Common Mature Structure

- Self-service creation from a web console/dashboard (account-gated in most products; anonymous in some).
- Near-instant provisioning (seconds).
- An environment list/dashboard showing environments, status, and usage against limits.
- Credentials/connection machinery: connection strings, generated passwords, per-language connection guides; companion GUI tools in some engines.
- Query/work access: in-browser worksheet/console for browser-first products; connection details for external tools; increasingly HTTP data APIs.
- A free or near-free entry tier with documented size/compute limits.
- Lapse/cleanup mechanics: suspension at limits, scale-to-zero, claim/expiry windows, deletion after grace.
- Guided starting points: seeded datasets, sample code, tutorials (strongest at the learning pole).
- Programmatic control: management APIs/CLIs (era-typical in developer platforms).
- An upgrade path into the same platform's production tiers — the sandbox as adoption funnel.

### Level 2 — Variant / Optional Structure

- Packaging: standalone named sandbox product; free/entry tier of a managed database platform; anonymous claimable provisions; trial-credit windows; browser-only playgrounds.
- Environment form: connectable full instance vs browser-only worksheet.
- Seeding: empty vs prebuilt datasets/templates vs sample code.
- Lifetime model: expiring claims/trials vs permanent free tiers with standing limits.
- Audience/occupation: learning a query language; evaluating an engine; prototyping an application; proof-of-concept work.
- Engine scope: single-engine adoption funnel vs multi-engine.
- Consumption by AI agents and coding tools (agent plans, MCP integrations) — era-typical.

### Level 3 — Vendor-specific (research notes only)

Neon's numeric plan limits (0.5 GB storage, 100 CU-hours, 5 GB egress, 5-minute scale-to-zero, 10 branches/project, 5,000-branch paid cap), Claimable Neon mechanics, branch-TTL billing guidance, Agent Plan; CockroachDB's $400 credits, $15/month Basic allowance (50M request units + 10 GiB), 30-day grace and deletion semantics, 2-vCPU default capacity, one-time password display; Redis Cloud's 30MB free database, Essentials/Pro subscriptions, RedisInsight, `redisctl`; Neo4j Sandbox use-case names (Movies, Network and IT Management, Crime Investigation/POLE, Paradise Papers by ICIJ); Neon "Lakebase Postgres" naming.

## Rejected Findings (anti-overfitting)

- **"Sandbox = free"** — rejected: CockroachDB's free allowance requires a payment method; trial credits are a paid product's entry. The invariant is low *commitment* and expendability, not zero price.
- **"Sandbox = ephemeral (days)"** — rejected: permanent free plans with standing limits are equally documented. Lifetime mechanics are variant.
- **"Sandbox = browser-only worksheet"** — rejected: connectable full instances with credentials/connection strings dominate the sample; the browser-only playground is one variant.
- **"Sandbox = SQL"** — rejected: graph (Cypher) and key-value/data-structure engines in sample.
- **"Sandbox = learning tool for students"** — rejected: the platform-pole products frame the sandbox pole for prototyping/side projects by working developers; learning is one occupation among several.
- **"Prebuilt datasets definitional"** — rejected: empty environments satisfy the Type; seeding is a variant common at the learning pole.
- **"Sandboxes are standalone products"** — rejected: the dominant market realization is the free/entry tier or named sandbox offering of a broader database platform; pure-play sandbox products are a minority pole.
- **"Anonymous access definitional"** — rejected: account-gated self-service is dominant; anonymous claimable provisioning is a minority mechanic (one product documented).

## Boundary Findings

1. **vs Database Dev/Test Environment Manager (counterparty ratification)** — RATIFIED from the sandbox side. The discriminator holds: sandbox environments are scratch (empty, seeded, or template-based), individually acquired, with **no derivation-from-authoritative-source relationship and no governed fleet lifecycle** (no refresh/reset-from-source discipline). When environments are derivations of a named source database under refresh/expiry governance, the product is the dev/test Type. The overlap specimen is Neon: its branching documents dev/test/CI/preview workflows (dev/test family, as that pass recorded), while its permanent free plan and anonymous claimable projects are the sandbox surface — one product straddles both Types by workflow family; "the Type is defined by the job, not the packaging" holds from both sides. The dev/test pass's watch item (whether platform-native branching splits into its own Type) is answered from this side: it did not; it remains a dev/test workflow family, with the sandbox surface as the same platform's low-commitment pole.
2. **vs Database IDE / SQL Client** — tool vs environment. The IDE/client connects to whatever database it is pointed at; the sandbox platform supplies the database. They compose (the Database IDE pass already records Sandbox Platform as "environment neighbor"). A sandbox's in-browser worksheet is a minimal query surface, not an IDE.
3. **vs Database Management Console** — consoles administer databases of record (production included); sandbox environments are never of record. Remove the disposable nothing-of-record premise from the sandbox and it converges toward console/platform operations.
4. **vs managed database service (DBaaS)** — no dedicated directory leaf exists for DBaaS; the sample shows the sandbox offering is typically the low-commitment pole of a DBaaS platform (free plan, trial, claimable projects). Classification is by center of gravity of the offering: expendable/no-stakes → sandbox; production commitment with SLAs → the (unnamed) DBaaS category. TAXONOMY NOTE: if a managed-database-service leaf is ever added, these two Types must be drawn together.
5. **vs Cloud IDE / Dev Container / Developer Environment Manager** — those provision code/tooling workspaces (compute, editors, dependencies); this Type provisions the database environment they point at. Compose, not overlap.
6. **vs Agent Tool / Computer-use Platform (code sandboxes)** — agent code-execution sandboxes hand an agent a compute runtime; this Type hands a human (or an agent, increasingly) a database environment. Homonym "sandbox", different object.
7. **vs Data Science Workbench** — workbench = interactive stateful analysis session; sandbox = standing, disposable database environment that can back such sessions. Different unit of work.
8. **Naming drift** — "sandbox" is used market-wide for: API/test sandboxes of payment/communication platforms, SaaS organizational sandboxes (CRM-class), malware analysis sandboxes, and AI-agent execution sandboxes. None of these are database-environment sandboxes; the leaf name covers only the database-environment sense.

## Uncertainties

- BigQuery Sandbox, Oracle Live SQL, and MongoDB Atlas free clusters (commonly referenced named offerings) were unreachable this pass; the browser-playground pole and the analytics-warehouse sandbox pole are under-observed. No claims about them appear in the final document.
- Neo4j Sandbox lifecycle/expiry/limit details unverified (docs 404). The final document makes no expiry claims for it.
- Supabase free-tier specifics (limits, pause behavior) unverified; Supabase evidence covers structure (projects, dashboard, organizations) only.
- Reach of anonymous no-signup provisioning beyond one product is unknown.
- Whether paid team-scale "sandbox environment" purchasing (organizational experimentation budgets) forms a distinct segment — under-observed; the sampled low-commitment offers are individual/self-serve.
- Eras: pre-cloud teaching servers and web playgrounds were reasoned about structurally (historical check), not documentarily; no specific historical product was fetched this pass.

## Final Synthesis

The Database Sandbox Platform is best understood at the level of the **sandbox environment offering**, not the packaging. Its defining core is the conjunction of: platform-provisioned working database environment + hands-on individual use + isolation with nothing-of-record + a bounded-and-expendable posture. The market realizes this core overwhelmingly as the low-commitment pole of managed database platforms (free plans, fixed-size free databases, trial credits, anonymous claimable projects), with a minority of literal named sandbox products and browser playgrounds as pure-play poles. Standard capabilities (console, instant provisioning, connection machinery, limits, lapse mechanics, guided content, upgrade path) cluster around making the experiment cheap to start and safe to abandon. The Type is separated from the Database Dev/Test Environment Manager by the absence of derivation-from-source and fleet governance, from IDEs/clients by supplying rather than connecting to the environment, and from production DBaaS by the expendability posture.
