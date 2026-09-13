# Research Notes — Package Registry

## Research Goal

从现实产品中回答：Package Registry（包注册表）作为 Application Type 到底是什么 —— 它在包管理器生态中承担什么角色（client/server 切分的哪一侧）、核心对象（package / version / 发行文件 / metadata）如何组织、publish（发布）与 resolve（解析/消费）两条通路如何工作、公开生态注册表与私有/平台内嵌注册表如何统一在一个 Type 里，以及它与三个已处理邻居（Artifact Repository、Dependency Management Application、Build Automation System）的待决边界如何判决。

本叶处理时存在三个 pending 联合评审标记（均已读取对方记录）：

1. **artifact-repository pass**：两叶子切分线待联合确认 —— "生态协议中心 vs 构建记录中心"；开放问题：公共注册表（npm/PyPI/Maven Central 本体）算不算本 Type。
2. **dependency-management-application pass**：client/project 侧 vs server/venue 侧接缝待从本侧确认。
3. **build-automation-system pass** 的三方跨越（cargo/npm-class 融合 build + dependency + publish 的生态原生工具 ↔ dependency-management ↔ package-registry）最终 settlement 推迟到本叶。

## Initial Boundary (working hypothesis before research)

初步假设（研究前）：

- Package Registry 是包管理器生态的**服务端场所**：包按 name+version 发布进去，包管理器客户端按生态协议解析/下载出来。
- 邻近 Type：
  - **Artifact Repository**（已处理）—— 组织构建产物托管（多格式仓库拓扑），重叠最尖锐
  - **Dependency Management Application**（已处理）—— 项目侧声明/解析/记录选择；注册表是它配置的供给源
  - **Build Automation System / Continuous Integration Platform**（已处理）—— 构建执行 / 运行编排，不经营包场所
  - **Source Code Hosting Platform** —— 源码的家，不是包的家
  - **Model Registry**（§13，已处理）—— ML 治理记录 vs 包坐标
  - 容器镜像注册表（OCI distribution protocol）—— 疑似邻接而非同型
- 明显未知点：公共开放注册表与私有组织注册表能否用同一核心刻画？"托管制品文件本体"是不是定义性要求（纯元数据聚合型注册表如 Packagist 是否存在且算不算）？多格式商业注册表（Gemfury/Cloudsmith 类）应划入本叶还是 Artifact Repository 叶？上游代理（proxying public upstreams）在本 Type 是否普遍（artifact pass 声称那是它们的差异层）？

## Research Questions

1. 注册表自己的"世界"由什么构成？package、version、发行文件（tarball/gem/wheel/.crate）、metadata 的对象层次是什么？
2. Publish 通路：谁发布（维护者/CI）、通过什么认证（token/2FA/OIDC trusted publishing）、发布进入什么（catalog/namespace）？
3. Resolve 通路：包管理器客户端如何把注册表当作"配置的包源"使用？生态协议（index/endpoint）如何定义客户端-服务端关系？
4. 名字治理：namespace/scope、first-come 注册、dispute 政策、名字所有权如何在注册表侧建模？
5. 所有权/权限模型：owner/maintainer/collaborator、组织/团队、继承 vs 独立授权？
6. 版本生命周期：不可变性（同版本不可覆盖/文件名不可复用）、yank/unpublish/deprecate/archive/delete+restore 各产品如何实现？
7. 公开注册表的平台化结构：搜索、README 渲染、下载统计、漏洞数据展示、镜像与统计 API？
8. 私有/平台内嵌注册表：多格式（每生态协议端点）、组织作用域、计费/配额、webhooks、上游代理是否存在？
9. 公共注册表（npm/PyPI/crates.io 本体）是否应进入本 Type 的中心（artifact pass 的开放问题）？
10. 历史检查：CPAN 时代（1995+）、Maven Central 时代的注册表形态是否满足核心定义？

## Representative Products

| Product | 哲学/位置 | 客户层级 |
|---|---|---|
| npm public registry | 最大公开单生态注册表；开放自助发布 + 付费私有包 | 个人开发者 → 组织 |
| PyPI (Python Package Index) | 公开注册表，非营利基金会（PSF/PyPA）运营 | 个人 → 社区 |
| crates.io | 公开注册表，Rust 项目/基金会运营，最强不可变政策 | 个人 → 社区 |
| GitHub Packages | 平台内嵌、按生态协议端点组织的多格式注册表（私有+公开） | 团队 → 企业 |
| Gemfury | 商业托管多格式私有包注册表（独立厂商，非平台内嵌） | 团队 → 中小企业 |

组合理由：三个公开注册表覆盖三种治理哲学（公司化开放 / 基金会非营利 / 项目方强政策）+ 平台内嵌多格式 + 商业独立托管，覆盖个人→社区→组织→企业客户层级；公开/私有两极都在样本内。

## Sources

（研究日期：2026-09-09）

- npm Docs — https://docs.npmjs.com/about-the-public-npm-registry （Tier 1，全文抓取成功；含完整站点导航结构）
- PyPI Help — https://pypi.org/help/ （Tier 1，全文抓取成功）
- Cargo Book — Regsitries: https://doc.rust-lang.org/cargo/reference/registries.html ；Publishing on crates.io: https://doc.rust-lang.org/cargo/reference/publishing.html （Tier 1，全文抓取成功）
- GitHub Packages documentation — https://docs.github.com/en/packages （landing，抓取成功）+ https://docs.github.com/en/packages/learn-github-packages/introduction-to-github-packages （Tier 1，全文抓取成功；首试 URL 404 一次，landing 页给出正确路径后成功）
- Gemfury Dev Center — https://gemfury.com/help （索引，抓取成功）+ https://gemfury.com/help/getting-started （Tier 1，全文抓取成功）

**Source-access limitation**：

- https://crates.io/policies 为 JS-gated 页面，抓取失败一次后放弃；crates.io 政策证据改以 Cargo Book publishing 参考章（官方文档，引用 crates.io 政策页锚点）为准。
- npm 深层文章（unpublish policy、scopes、trusted publishing 细则等）未逐篇抓取；npm 观察以 "About the public npm registry" 全文 + 官方导航结构为准，导航级条目（如 staged publishing、ECDSA registry signatures、Package Name Disputes、Unpublish Policy、Replication policy）作为结构存在性证据。
- Gemfury 仅抓取 Dev Center 索引 + getting-started；per-client 集成页未逐篇抓取。
- 未使用模型记忆填补精确数字/默认值；样本内直接取得的精确数字（如 PyPI 默认文件大小限制、crates.io .crate 大小限制、GitHub 计费结构）只保留在本笔记。

---

## Product Observations

### Product A — npm public registry（evidence layer A：about 页全文 + 官方文档导航结构）

- **定位（A，引用）**："The public npm registry is a database of JavaScript packages, each comprised of software and metadata. Open source developers and developers at companies use the npm registry to contribute packages to the entire community or members of their organizations, and download packages to use in their own projects."
- **对象模型（A，导航结构级）**：packages and modules；public vs private packages；scopes（个人/组织 scope）；package.json（名字、版本、依赖声明）；semver；dist-tags；README。
- **Publish 通路（A，导航结构级）**：creating & publishing unscoped/scoped/private packages；access tokens；2FA（含 "Requiring 2FA for package publishing and settings modification"）；trusted publishing with OIDC；staged publishing；ECDSA registry signatures + provenance statements（安全机制族）。
- **管理通路（A，导航结构级）**：deprecate/undeprecate；transfer package；unpublish（有 Unpublish Policy 政策页）；change visibility；collaborators 管理；组织/团队/角色。
- **Consume 通路（A，导航结构级）**：searching for and choosing packages；downloading and installing locally/globally；updating；audit reports（`npm audit`）。
- **治理（A，导航结构级）**：Package Name Disputes、DMCA、malware reporting（"Reporting malware in an npm package"）、Replication and web crawler policy（对镜像/复制的立场）、Threats and mitigations 专题。
- **私有侧（A，导航结构级）**：组织（orgs）、teams、组织 roles/permissions、组织 scope 包、付费计划（"Paying for your npm user account"）；CI/CD 工作流中的私有包使用。

### Product B — PyPI（evidence layer A：pypi.org/help 全文）

- **对象模型（A，引用）**："A 'project' on PyPI is the name of a collection of releases and files"；"A 'release' is a specific version of a project… A release consists of one or more 'files'"；"A 'file', also known as a 'package', on PyPI is something that you can download and install"（release 可含多个文件：sdist + wheel）。
- **Publish 通路（A）**：需验证邮箱才能注册项目/上传版本；API tokens（账号级或项目级 scope；CI 中建议最小 scope）；Trusted Publishers（"delegate publishing authority… to a trusted third party service, eliminating the need to use API tokens"）；2FA **强制**（"Two-factor authentication is required on your PyPI account"）；敏感操作需密码确认；浏览器上传已弃用（twine 上传）。
- **不可变性（A，引用）**：文件名 = 项目名+版本号+发行类型；"PyPI does not allow for a filename to be reused, even once a project has been deleted and recreated. This ensures that a given distribution for a given release for a given project will always resolve to the same file, and cannot be surreptitiously changed one day… (it can only be removed)."
- **版本生命周期（A）**：yank（"always ignored by an installer, unless it is the only release that matches a version specifier"）；archive 项目（不再更新、不进搜索、仍可解析）；删除（"permanent and irreversible, without exception… releases the project name for use by any other PyPI user. Deleted files cannot be re-uploaded"）；quarantine（疑似恶意/违规时"not installable by clients, and cannot be modified by its maintainers"，管理员审查后恢复）。
- **角色（A）**：Maintainer（可上传 release；不能加协作者/删除）vs Owner（可上传 + 加协作者 + 删除文件/release/项目）。
- **名字治理（A）**：名字不可用四原因（标准库冲突/与现有项目过于相似易混淆/管理员明令禁止如 typo-squat 类名字/已注册未发布）；PEP 541 名字转让与放弃名claim。
- **公开平台结构（A）**：README 渲染（渲染失败会拒收上传）；trove classifiers 分类；RSS/API；BigQuery 下载统计；漏洞数据展示（来自 OSV/advisory DB）；镜像机制（bandersnatch，"storage requirements… exceed 1 terabyte"）。
- **公开/私有立场（A，引用）**："PyPI does not support publishing private packages. If you need to publish your private package to a package index, the recommended solution is to run your own deployment of the devpi project." ← 公开注册表与私有索引是**同构的软件**（devpi/自部署 Warehouse 类）在不同场所运营。

### Product C — crates.io（evidence layer A：Cargo Book registries + publishing 两章全文）

- **定位（A，引用）**："Cargo installs crates and fetches dependencies from a 'registry'. The default registry is crates.io. A registry contains an 'index' which contains a searchable list of available crates. A registry may also provide a web API to support publishing new crates directly from Cargo." ← 官方把 registry 定义为生态的 server 角色：index（目录）+ 发布 API。
- **生态协议（A，引用）**：Cargo 支持两种 registry 协议（git index / sparse HTTP index）；"If you are implementing a registry server, see Running a Registry for more details about the protocol between Cargo and a registry" ← 客户端-服务端协议是**明文规范**的，第三方可实现注册表服务。
- **备用注册表（A）**：`.cargo/config.toml` 中按名字注册 registry（index URL）；依赖可指定 `registry = "my-registry"`；`package.publish` key 限制包允许发布到哪些注册表（"useful to prevent accidentally publishing a closed-source package to crates.io"）；**"crates.io does not accept packages that depend on crates from other registries"** ← 注册表边界与生态边界绑定。
- **Publish 通路（A，引用）**："Publishing a crate is when a specific version is uploaded to be hosted on crates.io"；cargo login（网站获取 API token）→ cargo publish（客户端校验 → 打包 .crate → 本地编译验证 → 上传 → **registry 侧再执行检查**后入库）。
- **不可变性（A，引用）**："a publish is generally permanent. The version can never be overwritten, and the code cannot be deleted"；yank 语义："no new dependencies can be created against that version, but all existing dependencies continue to work"（已有 Cargo.lock 不破坏，新生成的 lock 不含 yanked 版本）；政策哲学："One of the major goals of crates.io is to act as a permanent archive of crates that does not change over time, and allowing deletion of a version would go against this goal."
- **名字治理（A，引用）**："crate names on crates.io are allocated on a first-come-first-serve basis. Once a crate name is taken, it cannot be used for another crate."
- **所有权（A）**：owner 是唯一可发布新版本者；named owner（全权，含增删 owner）vs team owner（`github:org:team`，可发布/yank 但不能管理 owner 名单）—— 权限分级的注册表侧建模。
- **产品细节（仅本笔记）**：.crate 文件 10MB 上限；crates.io 登录绑定 GitHub 账号。

### Product D — GitHub Packages（evidence layer A：landing + introduction 全文）

- **定位（A，引用）**："GitHub Packages is a software package hosting service that allows you to host your software packages privately or publicly and use packages as dependencies in your projects."
- **多格式结构（A，引用）**："GitHub Packages offers different package registries for commonly used package managers, such as npm, RubyGems, Apache Maven, Gradle, Docker, and NuGet. GitHub's Container registry is optimized for containers and supports Docker and OCI images." ← 伞形产品下**按包管理器分设注册表**，每格式一套端点；表格逐格式列出 package format（package.json/Gemfile/pom.xml/build.gradle/nupkg/Dockerfile）与 package client（npm/gem/mvn/gradle/dotnet/Docker）。
- **客户端集成（A，引用）**："GitHub Packages uses the native package tooling commands you're already familiar with to publish and install package versions."；per-format 文档："configure npm to publish packages to GitHub Packages and to use packages stored on GitHub Packages as dependencies in an npm project"。
- **权限（A）**：包权限继承自 repository 或单独授权给用户/组织；"Some registries only support permissions inherited from a repository"（注册表间权限模型不齐）；公共包自由，私有包按存储+流量计量计费（budgets 控制）。
- **认证（A）**：PAT (classic) scopes；Actions 中 GITHUB_TOKEN 发布本仓库包、跨仓库消费需授权。
- **运维（A）**：包 README/许可/下载统计/版本历史视图；delete + restore（UI/REST/GraphQL，GraphQL 仅限 repo-scoped 注册表）；webhooks（package published/updated 事件）；包与仓库可关联（connected repository）。
- **边界自证（A，引用）**："Linked artifacts" 页 —— "Unlike GitHub Packages, the linked artifacts page does **not** host the package or image files themselves. Instead, it provides an authoritative source for the metadata" ← 平台自己区分"托管包文件的注册表"与"仅元数据视图"；托管文件本体是 Packages 的角色。
- **容器注册表分立（A）**：Container registry（GHCR）与包注册表在 GitHub 自家模型中是并列的不同产品面 —— 支持本叶的 OCI 边界判断。

### Product E — Gemfury（evidence layer A：getting-started 全文 + Dev Center 索引）

- **定位（A，引用）**："Welcome to Gemfury's Package Repository, a hosted service to securely store and deploy your code packages. After you upload your code to Gemfury, you can use your account as an additional (or alternative) package source and install using standard library tools." ← 私有注册表 = "additional (or alternative) package source"，被标准包管理器工具消费。
- **Publish 通路（A）**：dashboard 上传按钮；cURL；Gemfury CLI；git-push（由 Gemfury 代为构建打包）—— 多条发布路径并存。
- **多格式（A，索引级）**：按包管理器生态逐个提供集成指南 —— RubyGems、PyPI、Yarn、npm、Composer、Go Modules、Maven、Bower、NuGet、APT & DEB、YUM & RPM、Alpine（beta）、Rust crates（beta）。
- **组织与治理（A，索引级）**：organization accounts、collaboration、access tokens（含 custom permissions）、collaborator tokens、2FA/MFA 确认、SAML SSO、SCIM provisioning、GPG signing、package archiving、public packages 分发支持、limits 页。

---

## Cross-product Comparison

| 维度 | npm registry | PyPI | crates.io | GitHub Packages | Gemfury |
|---|---|---|---|---|---|
| 自我定位 | JS 包 database（software+metadata） | project/release/file 的目录与托管 | crates 的 index + 发布 API + 永久档案 | package hosting service（按包管理器分设注册表） | hosted package repository / additional package source |
| 对象层次 | package（scope 名字）→ versions | project → releases → files | crate → versions（.crate 文件） | package → versions（每格式端点内） | package 列表（账号作用域） |
| Publish | npm publish + token/2FA/OIDC/staged | twine 上传 + token/Trusted Publishers/2FA 强制 | cargo publish + token（服务端复查） | 原生客户端命令 + GITHUB_TOKEN/PAT | dashboard/cURL/CLI/git-push |
| Resolve | npm 客户端指向 registry | pip index | cargo index（git/sparse 协议） | 原生客户端按格式配置 | 标准工具指向账号 URL |
| 托管文件本体 | 是（tarball） | 是（files） | 是（.crate） | 是（A 引用自证 vs linked artifacts） | 是 |
| 名字治理 | scope + name guidelines + disputes | PEP 541 + 混淆名拦截 + 禁用名 | first-come，永久占用 | 用户/组织命名空间 | 账号命名空间 |
| 所有权模型 | collaborators + org teams | Owner vs Maintainer | named owner vs team owner | repo 继承或独立授权（按注册表不齐） | collaborators + org 角色 |
| 不可变性 | unpublish 受政策约束（政策页在导航，未读全文） | 文件名永不可复用；"always resolve to the same file" | "permanent… never overwritten, never deleted" | delete+restore 可用（跨注册表行为不一） | archiving 功能（细则未取证） |
| 软移除手段 | deprecate、unpublish | yank、archive | yank | delete+restore | archive |
| 公开/私有 | 两者（私有付费） | 仅公开（私有建议 devpi 自部署） | 仅公开 | 两者 | 私有为主 + 可选公开 |
| 多格式 | 否 | 否 | 否 | 是（每生态协议端点） | 是（十余生态） |
| 上游公共源代理 | （未见为中心能力） | （无——建议自部署 devpi） | **明确拒绝跨注册表依赖** | （未见为中心能力） | （未取证） |
| 信任机制 | 2FA、granular token、ECDSA 签名、provenance、malware 上报 | 强制 2FA、token、quarantine、 compromised-password 检查 | token、服务端上传检查 | PAT scopes、GITHUB_TOKEN、webhooks | token 权限、MFA、SAML/SCIM、GPG |

**Layer B（跨产品共性）观察**：

1. 五个产品都有：以 name+version 寻址的包目录（catalog）——这是注册表的记录结构。
2. 五个产品都有：发布通路（人 + 认证 + 进入目录的动作）与消费通路（标准包管理器客户端按生态协议解析/下载）。
3. 五个产品都有：名字空间治理（谁可以拥有/使用一个包名）——scope、first-come、dispute、角色。
4. 五个产品都有：包版本不移除时的某种"不可覆盖"姿态，与某种"软移除"手段（yank/deprecate/archive/unpublish/delete+restore）。形态差异大（见 L2），但"已发布版本在被软移除前是稳定解析目标"是共同契约。
5. 五个产品都有：维护者/所有权权限模型（至少 owner/maintainer 两级）。
6. 五个产品都有：Web 界面（包页面/搜索/账户管理）+ 程序化 API（至少客户端协议之外还有 Web API/feeds/webhooks 之一）。
7. 至少三个产品有：CI/自动化发布集成（npm OIDC/staged、PyPI Trusted Publishers、GitHub Actions/GITHUB_TOKEN、Gemfury CLI/cURL 脚本；crates.io 的 cargo publish 可入 CI 脚本）——表述为 common。
8. **多格式不是共性**：3/5 单生态、2/5 多格式；多格式实现为"伞形产品下每生态协议一套注册表"（GitHub、Gemfury），而非单一混合目录。
9. **上游公共源代理不是本样本的共性**：crates.io 明确禁止跨注册表依赖；PyPI/npm/crates.io 本身就是公开源；GitHub Packages/Gemfury 的上游代理能力未在其已抓取文档中作为中心能力出现——与 artifact-repository pass 的记录（其 5 样本中代理/聚合普遍）形成对照，支持 center-of-gravity 切分。
10. 托管文件本体：5/5 直接托管制品文件（PyPI/npm/crates.io/GitHub/Gemfury）；GitHub 的 linked-artifacts 引用从反面确证"不托管文件本体的元数据视图**不是**注册表"。
11. 治理强度谱系（公开端）：npm（公司化开放+政策工具箱）→ PyPI（基金会+强制 2FA+quarantine）→ crates.io（永久档案哲学）—— 公开注册表的安全/治理军备是共同演进方向（provenance/签名/恶意包处理），但机制各不相同（L2/L3）。

---

## L0 / L1 / L2 / L3 抽象

### L0 — Defining Invariant（去掉即不再是本 Type）

**Package Registry 是包管理器生态的服务端场所（venue）**——生态在此切分为客户端（包管理器/依赖工具）与服务端（注册表），注册表是客户端所面向的"包的家"。三个结构联合持有：

1. **生态的包目录（catalog of record）** —— 以生态的名字词汇组织的持久包记录（name → versions），携带生态的包语义（版本、元数据、包内声明的依赖关系——由客户端消费）。目录定义生态的共享名字空间（谁拥有什么名字）。
2. **进入目录的发布通路** —— 维护者（人或其自动化）通过注册表协议向目录添加新包/新版本，受名字所有权与权限规则约束。没有发布通路的目录是**镜像**（mirror）。
3. **面向生态客户端的解析通路** —— 生态的包管理器客户端把该场所作为**配置的包源**，按 name+version 解析并取回包。没有客户端解析通路的发布库只是发布归档（artifact-store 一极）。

三者缺一不可：去掉 1 → 无目录的投递点/流；去掉 2 → 镜像；去掉 3 → 未接入生态的文件库；去掉"生态协议绑定"（目录+发布+解析都以包管理器生态的协议与包语义为 vocabulary）→ 通用文件托管。多格式产品在 L0 下依然成立：它是**一个场所承载多个生态协议**，对每个生态它都完整充当 catalog+publish+resolve。

**为何这是"场所"而非"应用"的严格化**：L0 描述的是注册表作为软件系统扮演的角色。无论该系统是公开基金会运营（PyPI/crates.io）、公司运营（npm registry）、平台内嵌功能（GitHub Packages）、还是商业托管服务（Gemfury），都是同一角色的实现。

### L1 — Common Mature Structure（市场常态，不定义）

- 包页面/发现面：README 渲染、元数据展示、搜索、版本历史、下载统计
- 所有权/权限模型：owner/maintainer/collaborator 分级、组织与团队、scope 命名空间
- 发布认证与信任机制：API token（常可分 scope）、2FA/MFA、CI 自动化发布、OIDC trusted publishing、（公开端）签名/provenance
- 版本不可变姿态：已发布版本不可覆盖/文件名不可复用（公开端近乎普遍；私有平台实现不一）
- 软移除手段族：yank / deprecate / archive / unpublish（政策约束）/ delete+restore —— 具体集合产品相关
- Web UI + 客户端协议之外的程序化 API（REST/GraphQL/feeds/webhooks）
- 托管发行文件本体（hosting artifacts，不只元数据）
- 私有侧：组织作用域、访问控制、计量/配额、与开发平台/CI 的集成钩子

### L2 — Variant / Optional Structure

- 场所姿态：公开开放自助（npm/PyPI/crates.io）vs 私有组织（Gemfury/GitHub 私有包）vs 两者兼有
- 生态广度：单生态 vs 多格式伞形（每生态协议一套端点/作用域）
- 发布门控：直接自助发布 vs 策展/评审制（Maven Central 类，本次未直接取证，仅边界提及）vs staged publishing
- 身份基底：生态自有账号（npm/PyPI）vs 平台账号（GitHub）vs 联合身份（crates.io 经 GitHub 登录）
- 托管形态：自托管产物 vs （存在性未证实的）纯元数据聚合——见 Uncertainties
- 镜像与源替换：生态的客户端机制（bandersnatch、bandersnatch 类镜像、Cargo source replacement、scope 指向私有源）——镜像无发布通路故不是注册表
- 信任深度：签名/证明/隔离区/恶意包处置（公开端军备）；GPG signing/SSO/SCIM（私有端）
- 公共源上游代理：本样本中**非**共性（对照 Artifact Repository）
- 计费形态：免费公益 / 免费+付费私有 / 计量存储流量

### L3 — Vendor-specific Structure（只留本笔记）

- npm：dist-tags、scopes 语义、staged publishing、ECDSA registry signatures、Unpublish Policy/Package Name Disputes 政策体系、组织付费计划
- PyPI：PEP 541 名字转让、trove classifiers、默认文件 100 MiB/项目 10 GiB 大小限制、quarantine 状态机、bandersnatch 镜像、BigQuery 统计、 Warehouse 开源实现
- crates.io：.crate 10MB 限制、named/team owner 机制与 GitHub org 读取权限细节、sparse 协议、git index 历史包袱
- GitHub Packages：repo 权限继承 vs granular permissions 的注册表间差异、PAT-classic-only 认证、GITHUB_TOKEN、linked artifacts（元数据视图）、budgets 计费、Container registry（GHCR）分立
- Gemfury：Stacks、git auto-versioning、GPG signing、Rust crates/Alpine registry 的 beta 状态、fury CLI

---

## Rejected Findings

- ~~"公开注册表不算本 Type，本 Type 只是私有仓库功能"~~ —— 拒绝：npm/PyPI/crates.io 是市场对 "package registry" 一词的原型用法（artifact pass 自己记录的市场倾向），且私有注册表（Gemfury/GitHub）公开自述为 "additional package source"，两者是同一角色的不同姿态。本判决同时解决 artifact pass 的开放问题：**公共注册表属于本叶，且是原型中心**。
- ~~"托管制品文件本体是定义性要求"~~ —— 部分拒绝、部分保留：5/5 样本都托管文件本体，GitHub 又自证"不托管文件的元数据视图不是注册表"，故托管文件是**强常态（L1）**；但纯元数据聚合型注册表（Packagist 类）未取样，其存在与否未证实，L0 不押注于此（L0 要求"目录+发布+解析"，文件托管在解析路径上可以由生态的镜像/源替换机制分担——CPAN 即如此，见历史检查）。
- ~~"多格式（polyglot）是定义"~~ —— 拒绝：3/5 单生态；多格式产品也是"每生态协议一套注册表"的并列结构。
- ~~"上游公共源代理是核心能力"~~ —— 拒绝：crates.io 明确拒绝跨注册表依赖；代理/聚合在 artifact-repository pass 是普遍结构，在本样本不是——这是两 Type 切分线的有力佐证。
- ~~"2FA/签名/provenance 是定义"~~ —— 拒绝：都是近年公开端军备（L2）；CPAN/早期注册表时代无此结构。
- ~~"yank 语义是统一的"~~ —— 拒绝：PyPI（安装器默认忽略、除非唯一匹配）与 crates.io（新依赖不可建、旧锁继续用）表述相近但机制各自定义；npm 用 unpublish 政策而非 yank 作为主手段。

## Boundary Findings

1. **vs Artifact Repository（§12 已处理）—— 判决：center-of-gravity 切分维持，重叠带如实记录。** 本叶中心 = 包管理器生态的场所（catalog+publish+resolve per ecosystem protocol；公共生态注册表是原型）；artifact 叶中心 = 组织运营的构建产物托管（多格式仓库拓扑 + 上游代理/聚合 + 流水线治理）。两个证据系互相印证：(a) 上游公共源代理在 artifact 5 样本普遍、在本 5 样本不普遍（crates.io 明确禁止跨注册表依赖）；(b) 公共注册表的市场原型地位属于本叶；(c) 平台内嵌多格式产品（GitHub Packages；artifact pass 的 GitLab Package Registry）骑在边界上——它们的每格式端点+组织治理同时服务两叶的需求，两叶都以对方为变体收录。**联合评审结论：两叶保留，切分线 = 生态协议中心 vs 构建记录中心；公共注册表归本叶（关闭 artifact pass 开放问题）；重叠带以 center-of-gravity 检验个案归属。**
2. **vs Dependency Management Application（§12 已处理）—— 判决：client/venue 接缝从本侧确认（关闭该 pass 的标记）。** 注册表是依赖管理器**配置的供给源**（本叶证据：Cargo alternate registry 按名字注册+按依赖指定+publish key 限制、Gemfury "additional (or alternative) package source"、GitHub per-client 配置文档）；版本选择/解析语义在客户端（本叶证据：Cargo 的 resolver/source replacement/lock 均为客户端机制，注册表只服务被请求的名字+版本——crates.io 服务端仅做上传检查）。移除测试双向成立：去掉项目侧声明/解析/记录选择 → 注册表仍是注册表；去掉注册表 → 管理器无供给但 manifest/lock 记录仍在（与 dependency pass 记录一致）。
3. **vs Build Automation System（§12 已处理）—— 三方跨越关闭。** 三方声明：生态原生工具（cargo/npm-class）在**一个客户端工具**里融合 build + dependency + publish 三个功能；注册表是这些工具面向的**服务端场所**，不是工具本身。证据：Cargo 官方文本区分 "cargo publish"（客户端命令）与 "the registry will perform some additional checks"（服务端行为）；crates.io 的文档面向"注册表服务实现者"另有专章（Running a Registry）。Atlas 三叶保留；融合工具作为 straddle case 记录于 dependency 与 build 两叶（已各自记录），本叶确认工具≠场所。
4. **vs Source Code Hosting Platform** —— 平台内嵌注册表（GitHub Packages）是托管平台的一个**并列产品面**：包权限可继承自 repo 但内容与源码分属不同存储/页面/权限体系；包可不关联任何仓库存在。GitHub 官方将 Packages、Container registry、linked artifacts 三者分开叙述。判据：内容是包制品（按生态协议寻址）还是源码版本。
5. **vs Continuous Integration Platform / Build Automation（已处理，交叉确认）** —— CI 归档运行产物（Jenkins fingerprints 类）不是注册表服务；Buildkite 把 Package Registries 作为**独立产品**出售（CI pass 记录的厂商自家切分），从本侧再次成立：注册表不是 CI 的附属功能而是独立 Type。
6. **vs Model Registry（§13 已处理）** —— 与该 pass 的判决一致：注册表记录的语义（ML 治理：指标/签名/训练谱系/审批状态 vs 包坐标/依赖元数据）与消费者（部署流水线取"哪个模型版本在用" vs 包管理器解析依赖）切分。本叶补充：模型也可经包语义分发（如 Python 生态的包），但那已是本叶的角色——两叶按记录语义与治理中心区分，无冲突。
7. **容器/OCI 镜像注册表** —— 排除在本叶中心之外：镜像分发用 OCI distribution protocol，不是包管理器生态协议；GitHub 自家把 Container registry 与包注册表分列。目录无对应叶，记录为潜在缺口（artifact pass 已把 OCI 列为其格式类之一）。
8. **镜像（mirror）vs 注册表** —— 镜像无发布通路（不接收发布、只复刻目录），是生态的客户端侧机制（bandersnatch、Cargo source replacement、npm scope 指向）。判据即 L0 第 2 条。
9. **vs Software Supply Chain Security / SCA（§15）** —— 公开注册表的恶意包处置/quarantine/签名/审计是场所治理（本叶），组合分析（对依赖集的风险决策）是 §15 的中心（dependency pass 已记录该侧）。注册表提供数据与钩子（advisory 展示、provenance、审计事件），不做依赖组合的风险判决。留给 SCA 处理时确认。

## Historical / Market-Sample Check

- **CPAN（1995+）**：PAUSE 上传 + indexer first-come 权限（发布通路+名字所有权）+ CPAN 目录（catalog）+ 全球镜像网络服务客户端解析（解析通路经镜像分担）。满足 L0 三条——且证明"解析通路可由镜像实现、文件托管可分散"不破坏定义。** canonical inference（形态常识），未抓取当代资料 —— 标记为概念性检查，置信中等。**
- **Maven Central（2004 前后）**：策展/评审式发布（publish 门控变体）、托管制品、Maven 客户端按坐标解析。满足 L0。概念性检查，未直接取证。
- **RubyGems.org（2003+）**：直接 gem push 发布、托管 .gem、Bundler/gem 客户端解析。满足 L0。概念性检查。
- **npm（2010+）/ PyPI 现代平台 / crates.io（2014+）**：直接取证，满足 L0（见上）。
- 结论：定义未过拟合到现代 Web 平台时代——L0 不含搜索、统计、2FA、签名、组织计费；CPAN 时代的"目录+发布+镜像解析"与 2026 年的"目录+发布+CDN 解析+治理军备"共享同一核心。名字空间作为"生态共享地址空间"的刻画对 1995 年与 2026 年都成立。

## Uncertainties

1. **纯元数据聚合型注册表**（如 Packagist 类：目录/发布在注册表、文件从 VCS 取）未取样。若其存在，L0 仍容纳（catalog+publish+resolve 都在），但"托管文件本体"作为 L1 常态的强度需下调；本笔记不做断言。
2. Go module proxy（按需缓存型场所）、NuGet.org、Maven Central Portal（策展发布）、Packagist、Cloudsmith（Gemfury 的同极对手）未直接取样；多格式商业极仅 Gemfury 一个证据源。
3. Gemfury 的公共源上游代理能力未取证（其 Limits/integration 页未读）。
4. crates.io 政策页（JS-gated）未读；不可变性/删除政策证据来自 Cargo Book 引用（官方但二手转述）。
5. npm unpublish 政策细则（时间窗等精确规则）未读全文——最终文档仅表述"unpublish 受政策约束"。
6. 公开注册表的恶意包处置机制（takedown 流程、quarantine 触发条件）差异未系统研究。
7. PyPI 文件名唯一性规则与 npm 版本覆盖拒绝规则的确切表述随时间变化的可能性——本笔记按抓取日快照记录。

## Final Synthesis

**Package Registry 是包管理器生态的服务端场所**：一个包管理器生态在结构上切分为客户端（开发者机器上的包管理器/依赖工具，负责声明、解析、选择、安装）与服务端（注册表——包的持久目录与交换场所）。注册表持有该生态的**包目录**（name → versions，携带生态包语义与名字所有权），提供**发布通路**（维护者经生态协议把新包/新版本置入目录）与**解析通路**（生态客户端把注册表作为配置的包源，按 name+version 解析取回）。公开注册表（npm/PyPI/crates.io）、平台内嵌注册表（GitHub Packages）与商业托管多格式注册表（Gemfury）是同一角色的不同实现姿态；多格式产品是"一个场所承载多个生态协议"。它与 Artifact Repository 的切分线是"生态协议中心 vs 构建记录中心"，与 Dependency Management 的切分线是"场所 vs 项目侧选择记录"，与 Build Automation 的切分线是"服务端场所 vs 客户端工具（即使工具融合了发布命令）"。

**一句话 L0**：包管理器生态的持久包目录（定义生态名字空间）+ 进入目录的发布通路（名字所有权规则下）+ 生态客户端的解析取回通路 —— 三者联合，以生态协议为绑定词汇。
