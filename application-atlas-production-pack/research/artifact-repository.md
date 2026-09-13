# Research Notes — Artifact Repository

## Research Goal

从现实产品中回答：这一类软件（Artifact Repository / binary repository manager / 仓库管理器）到底是什么、里面有哪些核心对象、publish（发布）与 resolve（解析/获取）两条主通路如何工作、哪些结构是定义性的、哪些只是现代市场常态。

## Initial Boundary

初步假设（研究前）：

- Artifact Repository 是构建/交付流水线侧的"制品系统的记录"：构建产物发布进去，依赖解析取出来，按仓库/版本持久化。
- 最容易混淆的邻近 Type：
  - **Package Registry**（同 §12 相邻叶子）——语言包注册表（公开或平台内嵌）
  - **Continuous Integration Platform** ——执行构建，而不是保管制品
  - **Dependency Management Application** ——管理项目内依赖声明，而不是托管制品本身
  - **Source Code Hosting Platform** ——托管源码版本，不是构建产物
  - **Model Registry**（§13）——ML 模型治理注册表
- 明显未知点：与 Package Registry 的边界在目录里同时存在两个叶子，如何切分？不可变性（同版本重复发布）是不是定义性规则？多格式（polyglot）是不是定义性要求？上游代理是不是定义性要求？

## Research Questions

1. 核心对象是什么？（repository、artifact/package、version、metadata、checksum）
2. 对象层次如何组织？（package → version → files；component → asset 等不同厂商词汇）
3. Publish 通路：谁发布（人/CI）、通过什么协议/客户端、如何认证？
4. Resolve 通路：消费者如何获取（package-manager 客户端端点、直接下载）？
5. 上游公共注册表的代理/缓存（proxy / remote / upstream）是共性还是定义？
6. 多仓库聚合（virtual / group / feed+upstream / upstream chain）如何工作？
7. 版本生命周期：删除/恢复、保留/清理（cleanup/retention/storage）如何管理？
8. 晋升/阶段（promotion / staging / views）如何建模？
9. 访问控制模型：匿名读？角色？token？
10. 安全扫描/治理是本 Type 的能力，还是相邻独立 Type？
11. 部署形态：自托管 / SaaS / 平台内嵌 / 云厂商托管？

## Representative Products

| Product | 哲学/位置 | 客户层级 |
|---|---|---|
| JFrog Artifactory | 通用（universal）企业级仓库管理器，自托管 + SaaS | 中型→大型企业 |
| Sonatype Nexus Repository | OSS 血统的仓库管理器，自托管为主 + 云 | SMB→企业，开源社区版 |
| GitLab Package Registry | 开发平台内嵌的包注册表（单一平台功能） | 团队→企业（GitLab 用户） |
| Azure Artifacts | ALM 套件/云托管的 feed 模型 | 企业（Azure DevOps 用户） |
| AWS CodeArtifact | 云厂商全托管的依赖/制品服务 | AWS 用户 |

组合理由：两大经典独立仓库管理器（Artifactory/Nexus）+ 平台内嵌（GitLab）+ 套件 feed（Azure）+ 云托管（CodeArtifact），覆盖不同产品哲学与客户层级。

## Sources

（研究日期：2026-09-06）

- GitLab Package Registry — https://docs.gitlab.com/user/packages/package_registry/ （Tier 1，直接抓取成功）
- AWS CodeArtifact concepts — https://docs.aws.amazon.com/codeartifact/latest/ug/codeartifact-concepts.html （Tier 1，直接抓取成功）
- JFrog Artifactory — https://docs.jfrog.com/artifactory/docs/understanding-artifacts-and-packages.md 、https://docs.jfrog.com/artifactory/docs/repository-management.md （Tier 1，markdown 版直接抓取成功）
- Azure Artifacts — https://learn.microsoft.com/en-us/azure/devops/artifacts/ （landing/TOC）、/start-using-azure-artifacts 、/concepts/feeds 、/concepts/views （Tier 1，直接抓取成功）
- Sonatype Nexus Repository — https://help.sonatype.com/repomanager3/ （Tier 1；**内容深层页 404，仅官方导航/目录可达**——观察以导航结构为据并降级断言强度，见 Uncertainties）

**Source-access limitation**：
- Nexus 深层文档页（repository-manager-concepts、repository-types 等）多次 404，仅有帮助站导航。hosted/proxy/group 三种仓库类型由导航中 "Hosted Repository for Docker / Proxy Repository for Docker / Grouping Docker Repositories" 条目直接确证（Layer A，但仅覆盖 Docker 格式语境，未读全文）；其余 Nexus 观察标注为"导航结构级证据"。
- 未做一般 web 搜索；未使用模型记忆填补精确数字/默认值。

---

## Product A — JFrog Artifactory

（来源：docs.jfrog.com markdown 版官方文档）

### Key observations

- **对象类型（Layer A）**：Artifactory 管理的对象包括 *Artifact*（以唯一 checksum 标识的独立文件）、*Package*（以包元数据定义的名字为单位的对象，如 npm 的 package.json、Docker 的 manifest.json）、*Build*（代表 CI 构建步骤的输出，含构建方法与依赖信息，即 Build Info）、*Release Bundle*（代表发布候选的不可变内容上下文，经 Release Lifecycle Management 晋升和分发）。
- **Artifact vs Package（Layer A）**：一个 package 可含单个或多个 artifact（npm 为单 artifact 包；Docker 镜像为多 artifact 包，每层是独立 artifact）。元数据文件被解析以重建包结构。
- **仓库类型（Layer A）**：*Local*（存储组织内部上传/生成的制品——构建产物、二进制、包）；*Remote*（对远程 URL 仓库——如公共注册表——的缓存代理，包含"来自外部"的制品，例如依赖）；*Virtual*（聚合任意数量 local+remote，形成受控的解析/搜索域）；*Federated*（与其他站点的 Federated 仓库同步内容）。
- **接入流程（Layer A）**：官方描述的三步——创建仓库（需管理员权限）→ 把开发者的包管理器客户端指向 Artifactory（按仓库/格式逐个配置，提供 "Set Me Up" 配置生成）→ push/pull。
- **格式广度（Layer A，产品页级）**：宣称支持 50+ 注册表/仓库格式（"more than 50 registries and repositories"）。
- **分发/边缘（Layer A）**：Enterprise+ 可用 JFrog Distribution 将制品和 Release Bundle 分发到 Artifactory Edge 节点。
- **搜索/浏览（Layer A）**：平台级搜索、制品树浏览。

## Product B — Sonatype Nexus Repository

（来源：help.sonatype.com 官方导航结构；深层内容页不可达）

### Key observations（导航结构级证据，Layer A-弱）

- **概念框架**：导航含 "Repository Manager Concepts"；对象模型为 **Component / Asset**（Components API、Assets API、"How Components are Defined"、Viewing Component/Asset Information、Searching for Components）。
- **仓库类型（Layer A，Docker 语境确证）**：Docker 格式下并列存在 *Hosted Repository for Docker*、*Proxy Repository for Docker*、*Grouping Docker Repositories* —— hosted/proxy/group 三类仓库是该产品的结构。
- **格式广度（Layer A）**：Formats 目录列出 30+ 格式：Alpine、Ansible、APT、Bower、CocoaPods、Composer、Conan、Conda、Docker、Git LFS、Go、Helm、Hugging Face、Maven、npm、NuGet、OCI、p2、Pub、PyPI、R、Raw、RubyGems、Rust/Cargo、Swift、Terraform、Yum 等。
- **运维与保留（Layer A）**：Cleanup Policies（清理策略）；Tasks（数据修复、仓库导出/导入、Maven SNAPSHOT 任务）；Storage Guide / Blob Stores（file、S3、Azure、GCS）；"Keeping Disk Usage Low"。
- **访问控制（Layer A）**：Privileges / Roles / Users / Content Selectors / IP Allow List；认证 Realms、Anonymous Access、LDAP、OIDC、SAML、User Tokens、认证限速。
- **拓扑/部署（Layer A）**：Deployment Pattern Library（HA、DR、Star Pattern、Federated Repositories、Scaling with Proxies、Bi-Directional Proxying、跨区 DR）；Content Replication；自托管 + Nexus Repository Cloud。
- **晋升（Layer A）**：Staging（含 Staging Concepts；从 Nexus Repository 2 升级文档亦涉 staging）。
- **自动化（Layer A）**：完整 REST API 套件（Repositories/Components/Assets/Search/Security/Tasks/Script 等）、Webhooks、Download artifacts using URI。
- **版本/许可结构（Layer A）**：Community Edition 与 Professional 特性分层（feature matrix、usage-based consumption）。
- **安全治理在本产品族之外（Layer A）**：Sonatype IQ Server、Repository Firewall、Lifecycle 是独立产品线（导航同级），Repository Health Check 是仓库内嵌的轻量健康功能。

## Product C — GitLab Package Registry

（来源：docs.gitlab.com 官方文档，全文可达）

### Key observations

- **定位（Layer A）**："use GitLab as a private or public registry for a variety of supported package managers. You can publish and share packages, which can be consumed as a dependency in downstream projects."
- **容器模型（Layer A）**：包注册表按 project / group 作用域组织；group 视图展示组内所有可访问项目的包（私有项目包对无权限者隐藏）。
- **格式（Layer A）**：支持 Composer、Conan 1/2、Debian、Go Proxy、Helm、Maven、npm、NuGet、PyPI、RubyGems、Yarn、Generic（任意文件包）；另有独立的 Container Registry 与 Terraform Module Registry；不支持清单（Conda、CRAN、RPM、Swift 待贡献）。
- **Publish 通路（Layer A）**：按格式的包管理器客户端配置说明（每格式文档含配置代码片段）；CI/CD 中用 `CI_JOB_TOKEN` 认证发布；CI 发布后包详情显示流水线级活动（哪个 pipeline、哪个 commit、哪个用户触发——文档注明历史仅保留最近若干次更新；精确数字只留本笔记）。
- **Resolve 通路（Layer A）**：包详情页提供"配置你的包管理器/安装该包"的代码片段；下游项目把包当依赖消费。
- **导入（Layer A）**：可从其他注册表导入既有包（package importer）。
- **可见性/权限（Layer A）**：包注册表可见性独立于代码仓库可见性；按项目可见性 × 操作（view/publish/pull）给出最低角色矩阵；可开关"允许任何人 pull"（匿名下载）；管理员可全局禁用匿名下载。
- **治理（Layer A）**：Protected packages（包保护规则）；审计事件（发布/删除，Premium+，可经 GraphQL 开启）；Per-namespace 包设置。
- **上游/代理（Layer A）**：Dependency proxy for packages；新版 Virtual registry（导航中与 Harbor registry 并列）。
- **运维（Layer A）**：Reduce package registry storage（存储缩减指引）；可按项目关闭该功能。

## Product D — Azure Artifacts

（来源：learn.microsoft.com 官方文档，全文可达）

### Key observations

- **定位（Layer A）**："feeds serve as repositories for storing, managing, and sharing packages"；单一 feed 可承载多种包类型（npm、NuGet、Maven、Python、Cargo、Universal Packages）。
- **Feed（Layer A）**：组织级构造，用于存储、管理、共享包并控制访问。作用域：project-scoped / organization-scoped；可见性：private / public（公共 feed 依托公共项目，2027 年公共项目退役）。
- **上游（Layer A）**：Upstream sources——从公共注册表（nuget.org、npmjs.com、Maven Central）"保存"包，即使公共源暂时不可用也持续可访问；有 "Safeguard against malicious public packages"、"Upstream behavior"、Package graphs、"Upstream from internal feeds"（feed 可互为上游）。
- **视图/晋升（Layer A）**：Feed views——向消费者共享包版本的特定子集；每个 feed 默认三个视图（`@local`、`@prerelease`、`@release`，后两个可改名/删除）；视图是**只读**的；包只能发布到基础 feed（进入 `@local`）；验证通过后把包"晋升"到 `@release`，消费者只见通过质量门槛的子集。
- **权限（Layer A）**：私有 feed 消费需至少 Feed Reader；删除 feed 需 Feed Owner；删除后有 30 天恢复窗口（恢复期内包不可下载、写挂起、名字保留）。精确数字留本笔记。
- **存储（Layer A）**：组织级/项目级存储监控；按包类型分解；免费额度存在（2 GiB，精确数字留本笔记）；Package sizes and count limits 存在参考页。
- **符号与管道制品（Layer A）**：Symbols（符号服务器，调试用）是并列能力；Azure Pipelines 另有独立的 pipeline artifacts / build artifacts 机制（与包 feed 并行的流水线中间产物通道）。
- **Universal Packages（Layer A）**：任意文件集合作为包发布/下载——非语言包管理器格式的"通用包"通道。

## Product E — AWS CodeArtifact

（来源：docs.aws.amazon.com 官方概念页，全文可达）

### Key observations

- **定位（Layer A）**：全托管服务；仓库是 polyglot 的（单仓库可含任意支持类型的包）；每个仓库为 npm/Maven/nuget/pip 等客户端暴露 fetch 与 publish 端点。
- **对象层次（Layer A）**：*Asset*（单个文件，如 npm .tgz、Maven POM+JAR）→ *Package version*（版本标识 + 版本级元数据 + 一组 asset；每次更新产生新的 *package version revision*）→ *Package*（名字 + 可选 namespace（npm scope / Maven groupID）+ 版本集合 + 包级元数据如 npm tags）。
- **Repository 与 Domain（Layer A）**：*Repository* 含一组包版本；仓库按 upstream 关系链接（"从客户端视角有效合并两个仓库内容"）。*Domain* 是更高层实体——所有 asset 与元数据存在 domain 中、经仓库消费；同一 asset 在 domain 内只存一份；domain 级 KMS 加密；domain 级组织策略（哪些账户可访问、哪些公共源可作上游）。
- **治理（Layer A）**：Package groups（按 format+namespace+name 模式批量配置）+ Package origin controls（block/allow 新版本的摄取或发布——防御 dependency substitution 攻击）。
- **格式（Layer A）**：Cargo、generic、Maven、npm、NuGet、PyPI、Ruby、Swift。
- **上游（Layer A）**：Upstream repository 概念明确；可建仓库间 upstream 关系。

---

## Cross-product Comparison

| 维度 | Artifactory | Nexus Repository | GitLab Package Registry | Azure Artifacts | CodeArtifact |
|---|---|---|---|---|---|
| 中央容器 | Repository（local/remote/virtual/federated） | Repository（hosted/proxy/group；Docker 语境确证） | 包注册表（project/group 作用域） | Feed（project/org 作用域） | Repository（隶属 Domain） |
| 对象层次 | Package（名字来自元数据）→ artifact（checksum 标识的文件） | Component → Asset | Package → version（project 内） | Package → version（feed 内） | Package（name+namespace）→ version（+revision）→ Asset |
| Publish | 部署/上传（客户端 + API） | 客户端发布 + Uploading Components UI | 客户端 CLI + CI_JOB_TOKEN 自动发布 | 客户端/CLI 发布 | 客户端端点发布 |
| Resolve | 包管理器指向仓库 URL | 客户端指向仓库 | 详情页配置代码片段；下游依赖消费 | 客户端配置 + restore 文档 | 仓库端点（fetch） |
| 上游公共源代理 | Remote repo（缓存代理） | Proxy repo | Dependency proxy / Virtual registry | Upstream sources（保存包） | Upstream repositories |
| 多仓库聚合 | Virtual repo | Group repo | group 视图 / Virtual registry | Feed + upstream 链 | Upstream 链（客户端视角合并） |
| 晋升/阶段 | Release Bundle + Release Lifecycle Management | Staging | Protected packages（保护而非晋升） | Feed views（@local→@release，只读视图） | （无晋升；有 origin controls） |
| 保留/清理 | （本次抓取页未直接覆盖——不断言） | Cleanup Policies + Tasks | Reduce storage 指引 | 删除/恢复窗口 + 存储监控 | （未直接覆盖） |
| 安全扫描 | Xray（独立产品扫描本仓对象） | IQ Server / Repository Firewall（独立产品线） | 审计事件 + 保护规则（扫描在平台其他功能） | upstream 安全行为文档 | Package origin controls |
| 认证 | 用户/token（Set Me Up 配置） | User Tokens、LDAP/OIDC/SAML、匿名访问 | PAT / CI_JOB_TOKEN / 匿名 pull 开关 | Entra ID / Feed 权限角色 | AWS IAM |
| 部署形态 | 自托管 + SaaS | 自托管 + Cloud（CE/Pro 分层） | Self-managed / Dedicated / SaaS | 云服务 + Server 本地版 | AWS 全托管 |

**Layer B（跨产品共性）观察**：

1. 五个产品都有：命名仓库容器、publish 通路、resolve 通路、按 name+version 寻址、持久保留。
2. 五个产品都有：多格式支持（polyglot）——但实现为"每格式仓库类型"（Artifactory/Nexus）或"单 feed 多格式"（Azure/CodeArtifact）或"每格式端点"（GitLab）。
3. 五个产品都有：对外部公共注册表的代理/缓存/上游机制（remote / proxy / dependency proxy+virtual / upstream sources / upstream repo）——命名全不同，机制同构。
4. 五个产品都有：多仓库聚合解析（virtual / group / feed+upstream / upstream 链）。
5. 五个产品都有：包管理器客户端集成（配置片段 / set-me-up）。
6. 五个产品都有：访问控制（角色/权限 + 某种匿名或只读消费选项）。
7. 至少四个产品有：Web 浏览/搜索界面 + REST API（Artifactory、Nexus、GitLab、CodeArtifact、Azure 均有；证据充分）。
8. 至少三个产品有：CI 发布集成与发布来源记录（GitLab pipeline 活动、Artifactory Build Info、Azure Pipelines 发布指南；Nexus 有 CI 生态但本次证据弱）。
9. 至少三个产品有：保留/清理或存储治理（Nexus cleanup policies、GitLab storage reduction、Azure storage/limits；Artifactory/CodeArtifact 本次未直接取证）。
10. 晋升/阶段结构存在但**形态迥异**：Nexus staging、Azure feed views、Artifactory Release Bundle/promotion、CodeArtifact origin controls、GitLab protection rules —— 这是变体区，不是共性区。

---

## L0 / L1 / L2 / L3 抽象

### L0 — Defining Invariant（去掉即不再是本 Type）

一个组织运营的、构建产物的持久系统：

1. **托管制品记录** —— 已发布软件制品（二进制/包）作为持久记录存储，按**命名仓库容器**组织。
2. **Publish 通路** —— 生产者（维护者或构建系统）能将制品置于稳定身份（坐标：格式内 name + version）之下。
3. **Resolve 通路** —— 消费者（开发者、其他构建、部署）能按坐标检索制品；现代形态是包管理器客户端可指向的仓库端点。
4. **持久保留** —— 发布的制品在发布之后持续可用（不是会话态/临时缓存；是"记录"）。

最小判据：若没有"发布进来的构建产物被按坐标持久保管并可被取回"，无论它叫什么，都不是 Artifact Repository；若一个系统只剩"执行构建"，它就是 CI；只剩"声明/选择依赖版本"，它是 Dependency Management；只剩"托管源码"，它是 Source Code Hosting。

### L1 — Common Mature Structure（市场常态，不定义）

- 多格式支持（polyglot）；每产品支持 8–50+ 格式不等
- 外部公共注册表的代理/缓存/上游（remote / proxy / upstream / dependency proxy）
- 多仓库聚合解析（virtual / group / feed 视图 / upstream 链）
- 包管理器客户端集成（配置生成、按格式配置指南）
- 访问控制：角色/权限、per-repository/per-feed 粒度、匿名只读选项
- Web 浏览/搜索 + REST API
- CI 发布集成与发布来源记录（build provenance）
- 删除/恢复、存储监控、保留/清理策略（至少三个产品直接取证；作为 common 而非 universal 表述）
- 版本内不可变性约束或重复发布限制——格式相关、产品相关，以 common 形式表述

### L2 — Variant / Optional Structure

- 仓库拓扑哲学：每阶段独立仓库（snapshot/release）vs feed views（@local/@release）vs staging 套件 vs 无晋升（扁平）
- 治理扩展：包来源控制（origin controls）、包保护规则、审计事件
- 安全扫描：多数作为**独立伴生产品**（Xray、IQ Server/Firewall）或平台其他功能——本 Type 常只提供钩子
- 分发/复制：联邦仓库、内容复制、边缘分发、多区 DR
- 容器镜像/OCI 制品类：有的并入通用仓库，有的拆分独立 container registry
- 公共托管姿态：对外公共包注册表 vs 纯内部
- 部署形态：自托管 / SaaS / 平台内嵌 / 云厂商全托管
- 存储后端与配额（blob stores、对象存储、按量计费存储）
- 非包管理器格式通道（generic/raw/Universal Packages——任意文件制品）
- 符号服务器等邻接制品服务

### L3 — Vendor-specific（只留本笔记）

- JFrog：Release Bundle v2、Artifactory Edge、JFrog Distribution、Project 模型、"Set Me Up"、Xray、Federated repos、"50+ formats" 宣称、JFrog Academy
- Nexus：blob stores（S3/Azure/GCS）、Content Selectors、Routing Rules、Staging（Pro）、Repository Health Check、Usage Center、CE/Pro 分层、IQ Server 同族
- GitLab：CI_JOB_TOKEN、包活动"仅保留最近 5 次更新"、Dependency proxy、Harbor registry 选项、project/group 可见性矩阵细节、Audit events（17.10 GA 于 18.2）、包导入器
- Azure：@local/@prerelease/@release 默认视图名、发布仅限 @local、30 天 feed 恢复窗口、2 GiB 免费存储、Universal Packages、Symbols、public feeds 2027 退役
- CodeArtifact：Domain/单 asset 单份存储、KMS per domain、Package version revision、Package groups + origin controls、1,000 repos/domain 上限

### Anti-overfitting 检查

- "Polyglot 是定义"——拒绝：早期 Artifactory/Nexus 从单一 Maven 生态起步；单格式仓库（Docker-only、Maven-only、CodeArtifact generic）仍是本 Type。
- "上游代理是定义"——拒绝：纯私有仓库（无上游）完全成立；且五个产品的代理机制名词/实现互不相同（L1 而非 L0）。
- "版本不可变是定义"——拒绝：行为随格式和产品而异（CodeArtifact 重复发布会产生新 revision；GitLab 包可多次更新）。以 qualified 规则表述。
- "安全扫描是定义"——拒绝：两大仓库管理器都把扫描放在独立伴生产品（Xray、IQ）；它是邻接 Type 的边界。
- 历史检查（更老/平台原生产品）：Nexus 2（2010 前后）与早期 Artifactory（2006 起）都满足 L0 四条；甚至"HTTP 文件服务器上的 Maven 仓库"也满足（命名容器 + 发布 + 坐标解析 + 持久）。L0 通过历史检查。§22 抽象——所有现代实现细节（客户端配置生成、SaaS、配额、token 类型）都在 L1/L2。

---

## Vendor-specific Findings

（详见 L3；补充结构观察）

- **晋升形态三分**：(a) 视图/指针型（Azure feed views——发布只进 @local，晋升是视图成员变化）；(b) 暂存区型（Nexus staging——待证全文，导航级）；(c) 打包签名型（Artifactory Release Bundle——不可变发布上下文）。三者目的相同：把"已验证"与"开发中"的制品分给不同消费者。
- **对象词汇映射**：artifact(文件)/package(名字)/version 三层结构跨产品同构，但命名不同：JFrog artifact+package；Nexus asset+component；CodeArtifact asset+package+version+revision；GitLab/Azure 直接用 package+version。"Component vs Asset"（Nexus）与"Package vs Artifact"（JFrog）是同一概念对。
- **组织容器**：CodeArtifact Domain（唯一把存储层单列的）；GitLab project/group（复用代码托管的作用域）；Azure organization/project + feed scope；Nexus 无显式组织容器（实例即边界）；Artifactory Project（未在本次抓取页深入）。

## Rejected Findings

1. ~~"Artifact Repository ≈ Container Registry"~~ —— 容器镜像只是制品类之一；GitLab 甚至把 Container Registry 拆成独立功能页；OCI 是 Nexus 支持格式之一。
2. ~~"Universal（全格式）是定义"~~ —— 见 anti-overfitting。
3. ~~"制品不可变（immutable）"作为统一规则~~ —— 证据只支持"部分格式/产品限制重复发布"，不能一般化。
4. ~~"内置漏洞扫描是核心能力"~~ —— 反例：两大经典产品均为伴生产品模式。
5. ~~"Build provenance/build info 是核心"~~ —— 常见（L1）但 CodeArtifact/Azure feed 模型中不是中心对象。

## Boundary Findings

| 邻近 Type | 关系 | 判据（去掉什么就变成另一个 Type） |
|---|---|---|
| **Package Registry**（§12 相邻叶子，未处理） | **重叠最高，建议联合评审** | 若系统中心是"一个语言生态的包按包管理器协议发布/消费"（如 npm registry、PyPI、平台内嵌单生态注册表），它是 Package Registry；Artifact Repository 的重心是**组织运营的构建产物记录 + 多格式仓库拓扑 + 上游代理/聚合 + 流水线治理**。平台内嵌产品（GitLab/GitHub Packages、Azure Artifacts）骑在边界上：本 Type 以"自含仓库管理器"为中心证据，平台内嵌作为变体。两叶子的切分线（生态协议中心 vs 构建记录中心）需要在 Package Registry 叶处理时联合确认——可能的结论是前者为后者的"单生态子集/变体"或需要 center-of-gravity 判决 |
| Continuous Integration Platform | 上游 | CI 执行构建；产物持久化在 Artifact Repository。Azure Pipelines 的 pipeline artifacts（流水线中间产物）与包 feed 并存且文档明确区分——中间产物 vs 策展发布的判据 |
| Dependency Management Application | 下游消费侧 | 它管理项目内的依赖**声明/版本选择**（lockfile、升级）；Artifact Repository 只是**满足**这些声明的供给方。判据：管理的是"用哪个版本"还是"制品本身" |
| Source Code Hosting Platform | 相邻（套件同伴） | 托管源码 + 版本控制 vs 托管构建输出。GitLab 两者都有但分属不同功能页/存储。判据：内容是否为构建产物 |
| Model Registry（§13） | 平行注册表 | Model Registry 以模型生命周期治理（阶段/审批/元数据）为中心；制品库可存模型权重（JFrog 营销含 AI/ML 模型），但治理中心不同。判据：治理对象是"模型版本生命周期"还是"构建产物保管"。建议在 Model Registry 叶处理时联合评审 |
| Software Composition Analysis / SC Supply-chain Security（§15） | 治理邻接 | 扫描/门禁/防火墙（Xray、IQ、Firewall 类）以风险决策为中心；仓库以保管/供给为中心，只留集成钩子 |
| Log/Monitoring 或通用对象存储 | 远邻 | 通用对象存储无坐标语义、无包管理器协议、无版本/元数据模型；判据 = 客户端协议集成 + 包坐标模型 |

## Uncertainties

1. **Nexus 深层文档不可达**（3 次 404）：hosted/proxy/group 仅在 Docker 格式语境直接确证；staging 的细节（是否 Pro-only、跨格式支持）未确认——最终文档只作 qualified 表述。
2. Artifactory 的 retention/cleanup 机制未在本次抓取页覆盖（文档索引存在但未读）——最终文档不就 Artifactory 清理策略作具体断言。
3. 公共包注册表（npm/PyPI/Maven Central 本体）是否算本 Type 的实例：市场用法倾向算作 Package Registry 的原型而非 Artifact Repository——本叶将公共注册表排除在中心之外（组织运营判据），留待 Package Registry 叶确认。
4. 重复发布/不可变性的确切规则（per-format per-product）未系统取证——保持 qualified。
5. GitHub Packages 未抓取（时间预算）；其形态与 GitLab 高度同构的判断仅凭市场常识，未写入最终文档的断言。

## Final Synthesis

**Artifact Repository 是组织运营的构建产物系统**：把构建/发布过程产生的软件制品（二进制、包、镜像、任意文件束）作为持久记录托管在命名仓库中，为生产者提供发布通路、为消费者提供按坐标取回的解析通路。现代成熟产品在此核心上叠加四类结构：多格式协议接入、对外部公共源的代理/上游、多仓库聚合、以角色/视图/保护规则呈现的流水线治理。它不是构建的执行者（CI）、不是依赖声明的管理者（Dependency Management）、不是源码的家（Source Code Hosting）；与 Package Registry 的切分线在于"组织构建记录 + 仓库拓扑"对"单一生态的包分发"，该边界需与相邻叶子联合评审。

**一句话 L0**：命名仓库中托管的已发布制品记录 + publish 通路 + 按坐标 resolve 通路 + 持久保留。
