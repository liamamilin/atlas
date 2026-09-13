# Application Atlas — 下游应用路线图（调研记录）

> 当前状态（2026-09-13）：正式语料 1,805 类型、29 大域、270 目录节点。已开始工程稳定性修复，运行与验证说明见根目录 README.md。
> 下文保留历史方案与实验记录；历史 94.2% 不能视为当前验收结果。现有回归原始标签为 44/52，计入已确认替代标签后为 46/52（88.5%），本轮尚未重跑在线分类。
> U17 当前设计（2026-09-13）：[产品设计](docs/U17_DESIGN.md)、[开发规划](docs/U17_DEVELOPMENT_PLAN.md)与 [M5 试点计划](docs/U17_M5_PILOT_PLAN.md)。M0–M4 与核心主线最小真实开发冒烟已完成；下一步先固定简单新想法案例的普通生成对照，再进入 M5 三类评估试点。新想法与已有项目改进均纳入首版，集成现有 agent 引擎并由 Atlas 管理项目编排与验收。下文相关旧规则已修订，历史工期估算不作为本次承诺。


---

## 0. 资产盘点（我们手里有什么）

每个叶子两份文件，结构完全统一（实测确认，machine-parseable）：

| 文件 | 关键字段 | 用途 |
|---|---|---|
| `applications/<slug>.md` | Overview（含 L0 不变式 + 结构树）、Users & Context、Core Model、How It Works、Interfaces、Rules、**Variants**、**Related Application Types（表格：关系 + 区分）**、**Representative Products**、Sources | 对外正式文档，导出的主数据源 |
| `research/<slug>.md` | Research Goal、Boundary、**Product Observations（含证据层级 A/B/C 标注）**、**L0/L1/L2/L3 分层**、Rejected Findings、**Boundary Findings（vs 其他类型）** | 过程记录，导出时提供证据层级与边界判据 |

关键结论：
- 所有叶子共享同一套标题骨架 → **导出不需要 LLM，纯规则解析即可**（成本≈0）
- Related Application Types 是三列表格（类型/关系/区分），关系词收敛在少数枚举值（adjacent / variant-adjacent / broader / different object model / weaker）→ 图谱边是**结构化**的，不是散文
- 证据层级（A=官方文档 / B=广泛佐证 / C=推断）是现成的置信度标注，下游分类时可直接引用为 prompt 里的"判断强度"

---

## 1. 用法目录（按启动顺序排列）

### U1 — JSON 本体图谱导出 【地基，最优先】

**价值**：把"1805 篇文章"变成"一个可编程的分类法"。其余所有用法都依赖这一步。

**做法**：
- 写一个解析脚本（`export_graph.py`），遍历 `applications/*.md`，按统一骨架抽字段 → 单文件 `atlas.json`（或每叶子一个 JSON + 一个 index）
- 解析是确定性的；对个别格式漂移的叶子，用轻量 LLM 调用兜底（预计 <5%）
- 成本估计：脚本半天 + 兜底 LLM 调用约 100 次 ≈ **$5 以内**

**产出 schema**（见 §2）

### U2 — 语义检索 / 导航引擎

**价值**："我要做个 XX 工具" → 命中叶子类型 + 相邻类型 + 边界判据。这是对内对外的第一入口。

**做法**：
- 基于 atlas.json，对每个节点做 embedding（invariant + overview 拼接），入向量库（sqlite-vec / Qdrant / 甚至 pgvector）
- 查询时返回：最佳匹配叶子 + 一跳邻居（用 Related 边过滤关系类型）+ 该叶子的 boundary questions
- 边界问题（Boundary Findings）是检索的杀手锏：它把"匹配到了但可能是另一个类型"提前告诉用户
- 成本：1-2 天工程量；embed 1805 节点 < $1

### U3 — 真实实例自动分类 / 打标

**价值**：把产品、公司、代码仓库、内部资产映射到树上。这是把静态资产变成"活的数据库"的一步。

**做法（两种）**：
- **便宜路径**：U2 的检索引擎当分类器 —— 实例描述 → 向量检索 top-3 叶子 → LLM 结合 boundary questions 做最终裁决（一次调用，~2K tokens）
- **增强路径**：分类时把候选叶子的 L0 不变式 + 排斥性边界（"如果主任务是 X 则不是本类型"）放进 prompt，让模型显式排除
- 置信度：引用叶子文档的证据层级；Boundary Findings 未覆盖的实例标记为 "unresolved"（这正是未来补叶子/拆叶子的输入）
- 成本：每实例一次 LLM 调用 ≈ $0.01–0.05，比生成叶子便宜一个数量级

**试点设计（重要）**：拿 50 个真实产品（Representative Products 里已有的产品名 + 手工标准答案）跑分类，人工核对准确率。目标 ≥90% top-1 准确率；低于则反馈回方法论（通常是 L0 写得不够判别性）。

### U4 — Agent 上下文原料

**价值**：atlas 成为其他 AI 任务的"类别定义供应方"。定义是最难写对的东西，现在有 1805 份。

**典型场景**：
- **生成类**：coding agent 造新应用前，先检索叶子 → 把 L0、典型结构、Variants、Interfaces 注入 context，避免"做出来不是这么回事"
- **评审类**：给定一份产品 spec / 代码库描述，agent 引用叶子的 boundary 判据做"这算什么 / 这混淆了什么"的评审
- **数据生成**：按 L1 结构清单生成测试用例、验收标准

**做法**：无独立工程，依赖 U2 的检索接口；写一个 `get_leaf(slug)` 工具函数供 agent 框架调用（MCP tool 形态可选）。

### U5 — 覆盖度分析（管理层视角）

**价值**：把产品组合 / 投资标的 / 内部代码资产映射到树上，看空白区与重复建设。

**做法**：U3 分类结果的聚合视图（树上热力图）；"我们占哪些叶子、空白叶子有哪些、哪些叶子挤了 3 个同类产品"。
**依赖**：U3 + 一个具体的组合数据源（**开放问题 OQ3**）。

---

## 2. 导出 Schema 设计（v0 草案）

```jsonc
{
  "slug": "raster-image-editor",
  "name": "Raster Image Editor",
  "parent": { "slug": "...", "name": "..." },        // 从 DIRECTORY.md 树回填
  "invariant": "直接编辑像素网格的通用图像编辑应用…",   // Core Model 首段的 L0 陈述
  "structure": ["Raster Document", "Direct pixel manipulation", "…"], // Overview 的结构树节点
  "users": ["retouchers and photographers", "…"],
  "variants": [{ "name": "professional desktop editor", "desc": "…" }],
  "related": [
    { "slug": "digital-painting-application", "relation": "adjacent", "distinction": "…" }
  ],
  "products": [{ "name": "GIMP", "evidence": "A" }],
  "boundary_questions": [{ "vs": "digital-painting-application", "rule": "primary job decides the Type" }],
  "rejected": ["…"],                                  // 显式不归入本类的发现
  "evidence_summary": { "A": 3, "B": 1 },              // 从 research note 统计
  "sources": [{ "url": "…", "layer": "A" }],
  "l0_level": 0,                                       // L0/L1/L2/L3 分级（自 research note）
  "meta": { "date": "2026-09-05", "methodology": "v1.1" }
}
```

**与标准的对齐（可选，建议做）**：
- 树关系 → **SKOS**：叶子 = `skos:Concept`，目录层级 = `skos:broader/narrower`
- Related 关系映射：`adjacent` → `skos:related`；`broader` → `skos:broader`（泛化）；`variant-adjacent` → `skos:related` + 本体注记；`different object model` → 自定义 `atlas:contrastsWith`
- 好处：将来可导入任何 SKOS 工具链（Protégé、TopBraid、启明星等各类本体平台），不被自有格式锁死
- 关系枚举需先从 1805 叶子里统计实际出现的全部关系词（完工后一次 grep 即可），收敛成封闭集合再定映射表

---

## 3. 优先级与启动条件

| 优先级 | 用法 | 前置依赖 | 工作量 | 成本 |
|---|---|---|---|---|
| P0 | U1 JSON 导出 | 生产完工 + Boundary Issues 联审完 | 脚本 0.5–1 天 | <$5 |
| P1 | U2 检索引擎 | U1 | 1–2 天 | <$1 |
| P1 | U3 试点分类（50 产品） | U2 | 0.5–1 天 | <$5 |
| P2 | U3 全量打标（有真实需求时） | 试点通过 | 视数据源 | ~$0.02/实例 |
| P2 | U4 Agent 工具化 | U2 | 0.5 天 | — |
| P3 | U5 覆盖度分析 | U3 + 数据源确定 | 1 天 | — |

**关键闸门**：U3 试点 ≥90% top-1 准确率 → 整套用法成立；不达标 → 回炉方法论，修 L0 判别性（这一步本身也是对 atlas 质量的最终验收）。

---

## 3b. 深度调研补充用法（2026-09-07 第二轮调研）

> 说明：本轮外网调研因沙箱网络超时未成行，以下基于业界分类法/本体的成熟实践梳理。
> 参照系：Google Product Taxonomy（广告投放体系）、UNSPSC（政府采购分类）、CB Insights 市场地图（VC 行业图谱）、Crunchbase/Dealroom 行业标签体系、TOGAF 应用组合管理、SCA/SBOM（软件成分分析）、Gartner 市场分区。

### 商业与市场情报类

**U6 — 市场地图与投资研究**（对齐 CB Insights / Dealroom 模式）
- 做法：把初创公司/融资事件批量分类到叶子（复用 U3），得到"每个赛道有多少玩家、钱流向哪、哪些叶子是空白"，产出行业图谱与赛道报告
- atlas 的独特优势：判别式定义（L0 + 边界）解决了行业地图最常见的病——"两家公司被塞进同一个不存在的赛道"；Boundary Findings 直接成为地图上赛道的分界线说明
- 成本：打标 ~$0.02/实例 + 聚合视图工程
- 依赖：U3 试点通过；数据源（Crunchbase API / 手工清单）

**U7 — 竞品分析自动化**
- 做法：输入一个产品 → 分类到叶子 → 自动产出"同赛道竞品清单（Representative Products）+ 相邻赛道的替代品（Related 边）+ 它在哪个维度上混淆了类型（boundary 提示）"
- 输出物就是一份结构化竞品报告初稿；叶子文档里的 Variants 节还给出该产品的行业位置参照
- 成本：每份报告一次 LLM 调用 + 模板渲染，~$0.05/份

**U8 — 赛道趋势雷达**
- 做法：为每个叶子挂时间序列（融资事件数、招聘岗位数、GitHub 星标增速、媒体报道量），观察哪些叶子在升温/降温
- 这是"地图 + 时钟"的组合：静态分类法 × 动态数据 = 趋势信号
- 依赖：U3 打标 + 外部数据采集（工程量最大的一项，建议最后做）

### 企业内部类

**U9 — 应用组合治理（对齐 TOGAF / APM 实践）**
- 做法：内部系统清单 → 分类到叶子 → 回答"我们有几个报销系统、几个 CRM？哪些叶子重复建设、哪些能力空缺"
- atlas 比通用 APM 标签强的地方：每个叶子的 Core Model 提供了"这个类别的东西本来该长什么样"的参照，功能重叠判断有据可依
- 常与 U5 覆盖度分析是同一件事的两个视角（U5 看市场空白，U9 看内部冗余）

**U10 — 采购与选型决策**
- 做法："我们需要一个 X 类工具" → 检索叶子 → 拿到该类的 Core Model（应该有的能力）、Variants（有哪些档次）、Representative Products（候选名单）、Rules（关键行为/合规约束）→ 自动生成 RFP 问卷或选型评分卡
- 叶子的"How It Works / Important Rules"节就是现成的需求清单底稿

### 软件工程与数据类

**U11 — 代码库 / OSS 组件归类**（对齐 SCA / SBOM 实践）
- 做法：开源项目、内部代码仓库 → 分类到叶子 → 技术雷达视图、重复造轮子检测、依赖风险评估（某类应用的典型攻击面可从叶子文档推知）
- 与 U9 的区别：对象是代码资产而非已部署系统

**U12 — 评测基准与检查清单生成**
- 做法：从叶子的 L1 结构清单自动生成"该类产品的验收检查表 / 评测基准 / 测试用例矩阵"
- 用途：QA 测试计划、产品评审、采购评分卡（与 U10 衔接）、给 agent 生成的应用写验收标准
- 成本：每叶子一次 LLM 调用，~$0.05/份，可按需生成

### AI 与数据资产类

**U13 — 训练 / 评测数据生成**
- 做法：以叶子为骨架生成分类任务的训练集与评测集（正例 + 边界上的易混淆负例）；atlas 本身就是现成的"难例生成器"——Boundary Findings 里的 pair 就是天然的 hard negative 对
- 也可生成 prompt 库：每叶子的 invariant 是下游分类模型的 system prompt 素材
- 这是 atlas 在 AI 工程中最被低估的用法：1805 个精心设计过边界的类别定义，市面上买不到

**U14 — 新类别发现（atlas 自进化）**
- 做法：U3 打标时落不进任何叶子的实例（unresolved）自动聚集 → LLM 聚类分析 → 提议新叶子或叶子拆分 → 走一遍方法论生成新文档
- atlas 从"一次建成的死树"变成"随现实生长的活分类法"；这也是现有方法论可复用性的最终检验

### 内容与教育类

**U15 — 对比文档 / 选型指南自动生成**
- 做法：任意两个叶子 → 合成"X vs Y：怎么区分、怎么选"的对比文档（Boundary Findings 已有 60% 底稿）；相邻叶子对可批量生成对比内容
- 可对外发布（博客/手册），也可内部用（产品经理培训）

**U16 — 教学与知识体系（深度设计版）**

- 双层教学：**教内容**（"软件世界有哪些物种、长什么样、怎么区分"）+ **教方法**（L0 最小定义、边界分析、证据分级——给类别下定义的元技能，PM/架构师核心训练，市面上无系统性教材）

#### 三个现成教学资产

| 资产 | 用途 |
|---|---|
| Boundary Findings | 最佳考题库："产品 X 为什么是 A 而不是 B？"——天然带 hard negative 的分类判断题，教育测量稀缺题型 |
| L1 成熟结构清单 | 每类一份实践清单 = 架构课"参考架构"素材 |
| Representative Products | 每类自带案例库，案例教学免找素材 |

#### 中文市场空白

英文侧有 Gartner 等零散分类，**系统性中文"软件应用类型学"参考几乎空白**。中文化 atlas + 方法论可成为：书 / 专栏课程 / 培训工作坊 / 个人品牌底座。生产链路现成（已有 book-writing 技能链 → atlas 可直接转 Quarto 书）。

#### 必须解决的设计问题：课程化裁剪

参考文档 ≠ 教材（参考是查的，教材是学的）：
- 按树的上层组织章节（大类 → 章），叶子降级为"例子和练习"
- 每章精讲 3-5 个代表叶子（选边界最有趣的），其余收进索引
- LLM 起草 + 人掌舵的编辑层；方法论 v1.1 的"去框架化"经验（§33）直接复用于教材措辞

#### 产品形态选项（按投入排序）

1. **考题/练习集**（最便宜）：抽 100 对边界 → 分类判断题集，可用于自测/招聘/培训
2. **中文术语词典**：1805 类型中英对照 + 一句话定义，工具书形态
3. **专栏/课程**：树 → 章节映射，精讲代表叶子
4. **书**：《软件应用类型学》——树即目录骨架，方法论即导论
5. **交互式学习站**：树探索器 + "猜类型"练习（复用 U2 检索 + U12 检查表）

- 依赖：U1 导出（术语/考题可直接从 atlas.json 生成）；形态 3-5 需课程化裁剪设计
- 注意：对外教学 = OQ2 的"对外"选项之一，与市场地图（U6）同列候选

**U17 — Atlas 项目设计与持续开发工作台（2026-09-13 修订）**

定位：从已有类型和应用知识出发，帮助用户阅读、分析、形成关联的开发文档，并围绕同一个项目持续改进。完整设计见 [U17_DESIGN.md](docs/U17_DESIGN.md)，执行顺序见 [U17_DEVELOPMENT_PLAN.md](docs/U17_DEVELOPMENT_PLAN.md)。

#### 两条首版路径

**新想法**：想法 → 搜索或浏览类型与应用 → 阅读和比较资料 → 建立项目资料集 → 分析取舍 → 生成关联文档 → 开发与验收 → 后续迭代。类型叶子可直接创建项目、固定当前类型正文并进入工作区；搜索可以随分析重复进行，不要求先锁定类型。

**已有项目改进**：接入本地项目及文档 → 读取现状与代码证据 → 围绕改进目标搜索资料 → 分析影响 → 更新相关文档与开发计划 → 实施、回归验证 → 更新现状。U17 生成的项目后续改动使用同一路径。

允许引用多个类型；组合需求需解释共享对象、数据归属与流程交接。未分类或没有合适类型时，仍可开展方案工作。

“是否值得做”提供替代方案、差异、难点和验证建议，注明事实与推断；不自动否决项目或转向购买产品。

#### 项目与文档

- 项目长期保存资料、决策与需求、文档版本、代码基线、迭代和执行记录。
- 项目可在明确确认后删除 Atlas 记录；活动生成或执行会阻止删除，本地工作区和源码保留。
- 默认文档包括调研分析、产品需求、交互与页面、技术方案、开发规划、验收方案；已有项目增加现状与变更说明。简单项目可以合并文件。
- 范围状态为待决定 / 本版做 / 以后做 / 不做；区分 AI 推荐与用户确认，保存取舍理由和来源。
- 需求、任务和验收通过稳定标识关联。修改要求后指出受影响内容，保留人工修改及旧版本。
- 导出可独立阅读的 Markdown 文档包；运行时按任务选取上下文并支持读取全文，不固定一页或 50 行。

#### Harness 与 agent 集成

- 自建 Atlas 的项目编排：资料选择、文档关联、迭代、任务上下文和成果核对。
- 集成现有执行引擎：阅读、生成文档、修改代码、验证成果；优先验证已在草稿流程使用的 OpenCode。
- 适配层需要会话、事件、停止与恢复、工具范围、工作目录和差异回收能力。现有 CLI 草稿接口不能直接等同完整开发集成。
- 暂不重写通用模型与工具循环。先接一个引擎，保留文档导出和外部开发后重新接入的能力。
- **长期架构决定（2026-09-13）**：Atlas 独立保存项目知识、决策、文档、迭代与验收状态；OpenCode 是首个可替换的执行后端，允许长期复用，不预设全面自研或淘汰时间表。
- **首版可替换性验收**：旧会话不可访问时，仍能依据 Atlas 记录和实际代码状态交接下一项任务。切换以任务边界为单位，不承诺长会话无损迁移；新会话或验证用适配器检查交接，不提前要求第二个正式引擎。
- **扩大自研条件**：实际行为控制、部署限制或可衡量的效果与总成本支持局部自研时再推进，记录现有方案的尝试及持续维护投入；详见设计稿 §9.4–9.5。

#### 质量与边界

| 风险 | 当前设计 |
|---|---|
| 分类错误带偏方案 | 类型仅作可调整参考，以用户目标和已读资料为依据 |
| 成熟能力被全部当成需求 | 按核心流程、约束与依赖取舍，不设置固定功能项数 |
| 跨类型组合被误判为违规 | 检查流程、数据和责任变化，区分明确冲突、需要决定和参考建议 |
| 资料不足却生成确定结论 | 保留来源、版本、读取完整性和未知问题 |
| 旧项目缺少观察被当成功能缺失 | 区分文档声称、代码线索、运行证据和未检查范围 |
| 文档与代码偏离 | 分开保存产品意图与实现现状，执行绑定文档版本和代码基线 |
| Agent 中断或错误报告完成 | 保留产物并核对状态，执行结束与验收通过分别记录 |

试点记录重要遗漏、错误建议、开发者必须追问的问题、范围决策时间、计划外改动与返工原因。使用相同模型和输入的普通方案生成作为对照，先建立基线；不以 L1 覆盖率或人工改字数衡量价值。

#### 与现有资产的衔接

- U1 提供索引与类型数据；生成时仍需读取完整正文、研究笔记和来源。
- U2 搜索与阅读是入口；U3 分类提供参考，不作为强制门槛。
- U12 的验收知识可复用，但完整独立工具不是 U17 首版的前置条件。
- 应用实例资料按实际深度使用，不等待 U18 全量拆解，也不编造产品细节。
- 2026-09-07 的 L0 强制必做、MVP 最多 3 项、跨类型禁令、成熟能力差距直接进入 backlog 等规则由本节替代。

### 本轮调研的优先级建议

| 用法 | 性价比 | 启动条件 |
|---|---|---|
| U12 评测清单 | ★★★（便宜且立即有用） | U1 导出即可做 |
| U15 对比文档 | ★★★（60% 底稿已有） | U1 导出即可做 |
| U7 竞品分析 | ★★★ | U2 + U3 试点 |
| U13 训练数据 | ★★★（取决于有没有 AI 项目） | U1 |
| **U17 项目设计与持续开发** | 价值待真实试点验证 | 搜索阅读、项目与文档版本、引擎验证；见 M0–M5 |
| U6 市场地图 / U9 组合治理 | ★★ | U3 + 数据源 |
| U10 选型 / U11 代码归类 | ★★ | U2 |
| U14 新类别发现 | ★★（长期正确的事） | U3 跑量之后 |
| U8 趋势雷达 / U16 教学 | ★ | 有明确需求再做 |

### 3c. 参考 MVP 调研：software-map（2026-09-09）

> 参考库：`github.com/setfireonSdom/software-map`（已克隆到 `_ref-software-map/`，可 `npm run dev` 本地体验）。
> 中文"软件地图"：按**任务**组织的软件发现与产品拆解库，~30 款软件、4 款深度拆解（Todoist/滴答/Linear/Asana），纯前端 + localStorage，零后端。

#### 定位：同一坐标系的两根轴

| | software-map | atlas |
|---|---|---|
| 组织轴 | 实例优先（真实产品的页面/流程/规则拆解） | 类型优先（1805 类型的定义与边界） |
| 深度策略 | 分层（brief/basic/deep，仅 4 个做深） | 均匀深度 |
| 证据标注 | observed/official/analysis/unverified | A/B/C 证据层（几乎同构） |
| 方案 | PlanItem（v1/later/skip + 理由 + 来源保留） | U17 资料、决策、关联文档和持续迭代（2026-09-13 修订） |

#### 直接采纳（3 项）

1. **U17 吸收 PlanItem 的取舍与来源记录**：增加“待决定”，区分 AI 推荐与用户确认；每项保存理由与来源，关联到完整文档及迭代，不默认将收集项纳入本版。该交互在 U17 中的效果仍需试点验证。
2. **U2 检索原型抄它的 IA**：搜索 → 详情 → 对比 → 方案，四步工作流已验证；纯静态站 + 浏览器端检索即可（零后端）
3. **深度分层方向**：高频叶子后续可做"深度拆解"（4/30 模式），不必一次性均匀加厚

#### 新增 U18 — 实例拆解层（类型 × 实例）

atlas 缺的恰好是它有的：具体产品的页面地图、流程步骤、规则细节。合并方向：
- atlas 类型（1805）× 实例拆解（精选产品）→ "类型定义 + 代表实例的可验证拆解"
- 实例层 schema 直接沿用其 teardown 模型：FunctionRecord / PageRecord / FlowRecord / RuleRecord，全部带 evidence 标注
- 生产方式：对精选产品跑 atlas-writer 同款 agentic 调研（观察官方文档/实际产品 → 按 schema 产出），A/B/C 对应其 observed/official/analysis
- 价值：让每个叶子从"定义"升级为"定义 + 眼见为实的拆解"，U16 教学案例库、U7 竞品分析、U12 检查表都因此变厚
- 优先级：P3（等 U1-U3 稳定、有明确对外产品意向后再启动）

#### 更新优先级表

| 用法 | 性价比 | 启动条件 |
|---|---|---|
| U18 实例拆解 | ★★（对外产品的差异化关键） | U1-U3 稳定 + OQ2 拍板对外 |

#### 3d. 基于 MVP 的功能规划（2026-09-09）

> 判断：MVP 的两个结构性瓶颈——只有实例没有类型轴、只有手工没有自动化——正是 atlas 的强项。

**第一层：直接增强（MVP 验证过需求，低成本）**
- F1 类型树导航：树形浏览 + 邻近类型发现（atlas 类型轴装进 MVP 壳）
- F2 归类型助手：输入产品/描述 → 自动归类 + 边界解释（复用 U3）
- F3 深度拆解规模化：agent 流水线批量拆解精选产品（U18，4 款手工 → 数百款）

**第二层：待验证的产品增强**
- F4 价值与替代方案建议：基于已读资料提供买/配置/自建的信息、差异和验证建议，注明来源与时间；用户决定，不自动否决或切换项目方向（2026-09-13 修订）。
- F5 空白雷达：类型 × 产品覆盖稀疏热力图 → 产品机会地图 / 创业方向库（1805 类型，无人做过）
- **F6 范围与一致性检查**：结合用户已确认要求、类型资料和项目证据，指出明确冲突、需要决定的依赖与参考建议；解释新增流程、数据和责任，不以跨类型为功能禁令（2026-09-13 修订）。
- F7 提交 → 自动调研闭环（战略级）：用户提交缺失的类型/软件 → agent 自动调研 → 生成新叶子/新拆解 → 进库（= U14 自进化，静态库变活生态）

**第三层：开发集成与后续生态（F8 纳入 U17 首版）**
- F8 项目 → agent 执行 → 成果回收：自建项目编排，接入一个现有执行引擎；任务关联文档版本和代码基线，回收差异与验收证据，支持后续迭代及独立导出（2026-09-13 修订）。
- F9 产品变化监控：verifiedAt 雏形 → 定期重查触发重新拆解
- F10 协作分享：方案/对比可分享可协作（MVP 已预留 better-auth）

**U17 当前顺序（2026-09-13）**：按 M0–M5 完成资料与引擎验证、项目资料集、关联文档、已有项目改进、集成执行和完整试点。F2/F6/F8 服务这条流程；F7、U18 及其他生态能力按各自需求推进，不成为 U17 首版的整体前置条件。

#### 3e. 二次开发决策：以 software-map 为产品基座（2026-09-09 确认）

> 决策：MVP 为用户本人的项目（Grok 沙箱构建，产品构想文档见 `attachments/产品构想：软件发现与产品拆解库_副本.md`），**无版权障碍，作为 atlas 对外产品的开发基座**。
> 本节保留当时的技术设想与工期估计；实际运行结构见 README，U17 当前范围与开发顺序以 2026-09-13 的设计稿和开发规划为准。

##### 可行性结论

- **数据与界面干净分离**：内容全在 `src/data/`（typed TS records），界面在 `src/routes/`（9 个路由）。二次开发本质是**换数据层**：用 U1 导出的 atlas.json 生成 TS 数据模块，界面壳保留
- **证据标注体系同构**：其 `EvidenceKind`（observed/official/analysis/unverified）↔ atlas A/B/C 层，类型定义几乎不用改
- **路由清晰**：`search → software.$slug → compare → plan → submit`；`tasks.$slug`（任务域页）改造为 `types.$slug`（类型页）+ 新增类型树页
- **预留基建正好够用**：pglite（F7 后端数据层）、better-auth + multiplayer 模块（F10 协作），作者已铺好"单机 → 协作"的路
- **技术栈**：TanStack Start + React 19 + Tailwind 4 + Radix + pglite + better-auth，有 typecheck/test/eslint 完整工程化配置

##### 三阶段改造路线

| 阶段 | 内容 | 量级 |
|---|---|---|
| **适配** | tasks 域 → atlas 类型树；数据层换成 atlas.json 生成的 TS 模块（`catalog.ts` → 1805 类型树，`teardowns/` → U18 实例拆解） | 1-2 周（agent 辅助） |
| **增强** | F1 树导航 + F2 归类助手 + F6 方案边界 lint + U17 方案模板吸收 PlanItem | 各 2-5 天 |
| **生态** | F7 后端 + agent 自动调研闭环 + U18 批量拆解 + F8 开发流水线对接 | 数周 |

##### 数据层生成管线（适配阶段的关键件）

```
atlas.json (U1 导出)
  → 生成 scripts/gen-data.ts
      → catalog.ts       // 1805 类型树 + 大类导航
      → types/*.ts       // 每叶子: invariant/structure/variants/related/boundary
      → products.ts      // Representative Products + evidence 标注
      → teardowns/*.ts   // U18 实例拆解（沿用原 PageRecord/FlowRecord schema）
  → 保持原 types.ts 的 EvidenceKind 语义映射（A→official, B→observed, C→analysis）
```

##### 建议的工程节奏

- 不直接改原仓库：fork 出 `atlas-web`（或 monorepo 加 package），原 MVP 保留为参照
- 数据模块全部**生成而非手写**——保证与 atlas.json 单一来源同步（叶子更新 → 重新生成）
- 第一个里程碑：**"atlas 类型轴跑在 MVP 壳里"**（F1+F2，一个周末原型）→ 演示用，同时服务 OQ2 决策

---

## 4. 开放问题（需要用户决定）

- **OQ1**：导出格式要不要正式对齐 SKOS？（建议：要，映射成本低，收益是长期可移植性）
- **OQ2**：atlas 的第一用途是内部（产品组合/代码资产归类）还是对外（做成检索产品/市场图谱）？这决定 U3 的数据源和 U2 的形态
- **OQ3**：U5/U9 覆盖度与组合治理用什么数据源？（内部产品清单 / 投资组合 / 竞品清单 / 内部系统清单，多选）
- **OQ4**：分类试点 50 个产品的"标准答案"由谁标？（建议用户参与标 20 个核心样本，其余 LLM 预标 + 人工抽检）
- **OQ5**（新增）：有没有在进行的 AI 项目可以用 atlas 做分类/评测的底座？这决定 U13 的启动时机

---

---

## 5. TODO — 用起来之前必须做的事（按序执行）

### 阶段 0：生产收尾（✅ 2026-09-10 完成）
- [x] 8 个 worker 全部跑完（batch-F 09-10 00:20、batch-D 07:05）
- [x] 终检清零：omen-alpha 上游故障后切换 glm-5.3-flash（单叶 3.5 分钟 vs 27 分钟），103 叶 + 兜底重试 → **1805/1805 全部产出**（含 1 个重复节点别名拼写，canonical 合并后 1804 叶）
- [x] **Boundary Issues 联审**：4 项所有者裁决（ELN 合并 / ESG 保留双叶 / social-profile-network 保留自造名 / 9 个新叶子候选记入 Pending Leaves）+ 追加发现并合并 4 组重复节点（Knowledge Graph Explorer、Telecom Expense、School Transportation、Self-storage）→ 目录 1804 唯一叶子，0 重名
- [x] 质量抽检：3 agent × 20 叶并行 → **0 FAIL**（章节/L0 最小性/框架词泄漏/证据校准全过；系统性小瑕疵：9 处悬空 Related 引用、个别 Overview "system of record" 措辞、ESG 叶证据最薄已自报）
- [x] 关系词封闭枚举：12908 → 10486 有效关系行，canonical 收敛为 **15 类**（adjacent 3435 / sibling 1477 / downstream 690 / overlaps 629 / capability_of 475 / upstream 459 / broader 431 / counterpart 263 / complementary 185 / narrower 133 / substrate 122 / contrasts 95 / authority 14 / alternative 1 / other 2077），见 logs/relation-words.txt

### 阶段 0.5：数据存储（✅ 2026-09-10 完成）
- [x] `export_atlas.py`：解析 DIRECTORY.md + applications/ + research/ + STATUS.md + logs → **SQLite 主存储** `atlas/atlas.sqlite`（226MB，FTS5 全文检索，bm25 验证通过）+ **atlas.json 可移植导出**（18.7MB）
- [x] 关系边解析：10486 条中 **9666（92%）已解析到目标叶子 slug**，820 条语义邻居记入 logs/unmapped-rel-targets.txt（含抽检发现的 9 处悬空引用）
- [x] 模型溯源：每叶记录写作模型（omen-alpha / glm-5.3-flash / qwen3.7-max）
- 注：**markdown 文件仍是 source of truth**，SQLite/JSON 是派生物，重跑 `python3 export_atlas.py` 即可再生成

### 阶段 1.5：双语化（✅ 2026-09-10 完成）
- [x] **中文翻译层**：`translate_zh.py` 直连 API（mimo-v2.5，12 并发，~80 分钟全量）→ 1804/1804 叶的 `name_zh / aliases_zh / l0_zh` 三列入库
- [x] **双语 FTS 检索**：`leaf_fts`（trigram 分词器，中文子串匹配）+ `leaf_fts_lat`（porter，英文词匹配）双索引；验证：酒店预订→酒店预订引擎 ✓ 宠物健康→宠物健康应用 ✓
- [x] 译名质量抽检 10/10（市场通用叫法 + 真实别名，如 HRIS→人事管理系统、Attraction Ticketing→景点票务/景区票务）
- [x] 数据层原则落地：**英文 canonical 不动**，翻译仅进检索/展示层（translatable columns，重跑可再生成）
- 成本：mimo-v2.5 直连 ~$5（vs 本地 27B 需 30h）
- [ ] 阶段 2 向量检索用多语言 embedding（本地已有 bge-m3，天然中英对齐）

### 阶段 1：U1 导出完善（P0，大部分已完成）
- [x] `export_graph.py` → 由 `export_atlas.py` 实现并超额完成（SQLite + JSON 双输出）
- [x] 从 DIRECTORY.md 回填 parent 关系（113 个 section 节点入 section 表）
- [ ] SKOS 对齐（OQ1 确认后）：15 类 canonical 关系词 → skos:related / skos:broader / atlas:contrastsWith 映射表（other 类 2077 条需人工/LLM 抽查校准）

### 阶段 2：U2 检索引擎 + 试点验证（进行中，管线已定版）
- [x] 向量方案：**bge-m3（本地 Ollama，免费）**，1024 维，1804 叶 4 分钟全量嵌入；中文查询靠双语列对齐
- [x] 混合检索管线 `classify.py`（定版配置）：bge top-10 → **关系图 1-hop 邻居扩展**（top-5 的邻居按相似度补 6 个，池上限 16）→ 便宜 LLM 打分制裁决（逐候选独立 0-10 分 + 语料库成对边界记录注入）→ argmax
- [x] 裁决器 A/B（52 样本）：qwen3.8-flash **88.5%** ✓ / glm-5.3-flash 84.6% / glm-5.3 63.5% / mimo-v2.5 48% / qwen3.7-max 78.8-80.8%（贵）→ **qwen3.8-flash 定版**（便宜且最强）
- [x] 真实产品子集：**19/21 = 90.5%**；合成盲测 27/31 = 87.1%
- [x] 迭代史：40.4%（首版）→ 53.8%（双语重嵌入）→ 63.5%（强裁决器）→ 78.8%（修生成漂移）→ **88.5%（图扩展+打分制+便宜模型）**；池召回上限 ~90.4%（bge-m3 通用模型天花板）
- [x] **闸门判定（2026-09-10 通过 ✅）**：3 例争议样本裁决（人工确认接受裁决器选择：钉钉→团队工作区、简道云→零代码、synthetic-20→看板）→ **最终 49/52 = 94.2%（真实产品子集 20/21）**，超过 ≥90% 闸门 → 进入阶段 3
- [x] 已知系统性短板（诚实记录）：bge-m3 通用模型对近义类型区分有限（池召回上限 ~90.4%）；后续可用语料对（场景描述→叶子）微调 embedding 模型
- [ ] OQ2/OQ3 拍板：atlas 第一用途（对内/对外）+ U5 数据源

## ⚠️ 模型使用纪律（2026-09-10 血泪教训）

- **qwen3.7-max 实验累计花费 ~$24**（多轮 A/B + 52 样本重跑），性价比远低于 qwen3.8-flash（88.5% vs 78.8%，还更便宜）
- **原则：能用便宜模型就不用贵的**。默认梯队：qwen3.8-flash / glm-5.3-flash（$级）→ glm-5.3 / kimi-k3（$$级）→ qwen3.7-max / 旗舰（$$$，仅在质量关键且经确认时使用）
- 本地 Ollama（qwen3.8:27b / bge-m3）零成本，优先考虑（但注意串行速度限制）
- **本地大批量实测教训（2026-09-12）**：27B 单叶 76-93s 正常，但 3 路并行持续 1-2h 后速率崩 10 倍（35-45/h）——Apple Silicon 满载热节流 + KV 缓存饱和。本地只用于短突发任务（抽样/embedding/小批），1800 级大批量交给 API 便宜模型；非要本地跑则 1-2 并发 + 分段冷却

### 语料强化回路实验（2026-09-11，已完成并冻结）
- 260 失败叶诊断：**65% 是检索池漏召**（真类型不在 16 候选内），判定词微调只能救 10.8%
- 消融结论：三路融合检索（body+ov+dc 等权）能把池外召回 5→41/169，但会重排 top-10 构成，在真实产品闸门上回归 2+ 个（钉钉/有赞/Pleo），**判净收益为负 → 回滚 v1 配置**（body-only 池16 + 原判定词，闸门 94.2% 冠军）
- 实验产物：`classify_v1_backup.py`（闸门冠军备份）、`atlas/gate_v5.json`、`atlas/stress_v2.jsonl`（v3 融合+池24 版恢复 47/260）、`atlas/stress_pool_misses.json`（169 池外清单）
- **原则性修复路径 = U11 embedding 微调**（用语料分界对/混淆对做训练对），非提示词或检索权重可解
- 260 失败叶清单仍有效 = 语料质量改进优先级（U12/U16 素材）

### 阶段 3：规模化应用（进行中）
- [x] **U3a 软件地图 30 app 打标（✅ 2026-09-10）**：33 个 app 全部分类完成（qwen3.8-flash，~$0.3）→ `mvp_apps_classified.json`；近义区分表现好（Todoist→任务管理 vs 滴答→待办、Linear→问题跟踪、Jira→敏捷PM、Trello→看板、Sunsama/Motion→时间块各归其位）；Notion→轻量结构化数据库（可争议）、Habitica→人生规划（边缘）——**这批标签可直接填进 atlas-web 数据层**
- [x] **U3b 合成压力测试（✅ 2026-09-11）**：1804 场景（mimo-v2.5 生成，$2）→ qwen3.8-flash 回分类（$4，6 并发+退避），**往返准确率 85.6%**（vs 盲测 94.2%，全谱系含最难近义区分）。错误 260 = 边界混淆 168（其中 143 已有区分文本仍错、25 缺文本）+ 完全偏移 92（检索池召回天花板）。**260 失败叶清单 = 语料质量改进优先级**（logs/stress-report.md）。最弱域：企业运营 69%、软件开发 76%、安全 77%
- [x] **U4 Agent 工具化（✅ 2026-09-10）**：`mcp_atlas.py` MCP server（5 工具：search_atlas / get_leaf / classify_product / get_section_tree / get_neighbors），已注册进 opencode.json，端到端验证通过（律所系统分类 10 分命中 + 邻居边界完整）。任何 opencode 会话现在可以即席查询 atlas
- [ ] U5 覆盖度分析：待 U3b 完成后做
- [ ] OQ2/OQ3 拍板：atlas 第一用途（对内/对外）+ U5 数据源

### atlas-web 全站中英文切换（2026-09-12 完成 ✅）
- **翻译层**：1804/1804 叶正文（overview/how/rules/variants/products）+ 14421 条关系分界文本 + 113 域名全部中文化（mimo-v2.5 为主力；本地 27B 因热/内存压制速率塌到 35-45/h 后退出）。`translate_bodies.py` / `translate_rels.py` / `translate_sections.py` → `import_zh.py` 入库（新表 leaf_zh_body / rel_zh / section.name_zh）
- **踩坑记录**：①mimo 英→中字符比 ~33% 是正常密度不是压缩；②JSON 内嵌 ```text 围栏会破坏围栏剥离解析；③mimo 关系输出键用 distinction 不是 zh（两键都收）；④双引擎共写一个 state 文件会互相覆盖（重跑浪费 ~$8）；⑤shell 工具 60min 超时会杀后台进程
- **成本**：API 总计 ~$26（略超批准的 $20-25，超额来自 state 覆盖导致的部分重跑）；本地 ~$0（贡献 358 叶）
- **前端**：`lib/lang.tsx`（Context + localStorage 默认中文）、头部 中/EN 按钮、全字段按语言取值缺失回退英文、搜索双语匹配、UI 骨架 30+ 条文案双语表
- 已验证：chat-room 等 1804 叶 zh 全字段 + 分界中文 + 域名中文；typecheck + build 通过

### 阶段 2.5：速赢项目（U1 导出后即可做，不等闸门）
- [ ] **本地体验参考 MVP**：`_ref-software-map/` 下 `npm run dev`，走一遍 搜索→拆解→对比→方案 工作流，记录手感与 U2 原型的取舍
- [ ] U12 评测清单生成：挑 10 个高频叶子生成"验收检查表"样例，验证格式与实用性
- [ ] U15 对比文档：挑 5 对相邻叶子（如 Raster Editor vs Digital Painting）生成对比文档样例
- [ ] U7 竞品分析样例：拿 2-3 个真实产品跑一遍完整流程（分类 → 竞品清单 → 报告初稿）
- [ ] U16 速赢样例：抽 100 对边界生成中文分类判断题集（考题形态，$10 以内）；顺手验证 1805 类型中英术语表的可生成性
- [ ] 以上样例可直接用于向团队/客户演示 atlas 价值（OQ2 决策的输入）

### 阶段 4：U17 项目设计与持续开发（2026-09-13 修订）

- [x] 明确产品方向并形成 [设计稿](docs/U17_DESIGN.md) 与 [开发规划](docs/U17_DEVELOPMENT_PLAN.md)。
- [x] M0：完整类型资料读取、OpenCode 异步执行/权限恢复/状态投影、工作区文件基线、含来源/需求/决定/迭代的独立项目存储、双场景关联文档样例及不依赖旧会话的交接包已实现。过程见 [验证档案](docs/archive/u17/U17_M0_VALIDATION.md)。
- [x] M1：多项目、类型与应用统一搜索、正式正文/研究笔记阅读、应用目录深度说明、项目资料收藏与固定来源版本。过程见 [M1 验证档案](docs/archive/u17/U17_M1_VALIDATION.md)。
- [x] M2：分析取舍、关联文档、人工修改、范围检查、版本、价值建议与独立导出。过程见 [M2 验证档案](docs/archive/u17/U17_M2_FOUNDATION_VALIDATION.md)。
- [x] M3：已有项目基线、变更规划、外部修改核对与后续迭代。过程见 [M3 验证档案](docs/archive/u17/U17_M3_BASELINE_VALIDATION.md)。
- [x] M4：一个 agent 引擎的集成、执行范围、恢复与成果回收；模拟旧会话不可访问并验证任务交接。过程见 [M4 验证档案](docs/archive/u17/U17_M4_EXECUTION_VALIDATION.md)。
- [x] 核心主线：最小真实开发冒烟已从类型入口连续走到迭代完成，阻塞问题已修复并完成最终全绿复验。过程见[核心主线验证](docs/U17_CORE_PATH_VALIDATION.md)。
- [ ] M5：按 [试点计划](docs/U17_M5_PILOT_PLAN.md)完成简单新想法、已有项目改进、多类型需求三个评估案例和至少一次后续修改，保留普通生成对照与真实问题。

### 阶段 5：产品基座 atlas-web（基于 software-map 二次开发，§3e）
- [x] **里程碑 1：类型轴跑进 MVP 壳（✅ 2026-09-11）**：新建独立 `atlas-web/`（Vite+React+react-router，复刻 software-map 设计语言：米色纸感 token/衬线标题/Button+Badge），剥离 auth/pglite/nitro 等后端件。数据管线 `scripts/gen-data.py`：atlas.sqlite + 33 app 分类 → `public/data/`（meta.json 含 29 域导航+检索索引 / sections/*.json 113 子域 / leaves/*.json 1804 全量档案按需加载 / apps.json）。5 个页面：首页（统计+域导航）/ 浏览类型树（29 域折叠展开）/ 类型详情页（定义核心+概览+工作结构+规则+变体+关系分界+真实产品）/ 搜索 / 应用实证（33 app→类型互链）。typecheck+build 通过，dev 跑在 :5188。语料更新后 `npm run gen` 重新生成
- [ ] F2 归类助手原型（检索 + 边界解释）
- [x] U17 项目资料、范围取舍、关联文档与 F6 一致性检查（M1–M3 已完成）
- [ ] 里程碑 2：F7 后端（pglite + agent 自动调研闭环，U14 落地）
- [ ] 里程碑 3：U18 实例拆解批量生产，充进 teardowns
- [x] F8 核心：集成 OpenCode、隔离执行、成果回收、独立验收与交接（U17 M4）
- [ ] F8 试点：在 U17 M5 三个完整案例中复核持续执行与产品价值，不依赖 U18 批量生产

### 日常运维（贯穿）
- [ ] 定期问 agent 跑批进度（或 `tail batch.log`）
- [ ] 新增领域时复用本套方法论（leaves.txt 提取 → 批处理 → 导出合并）

---

## 6. 备忘

- 完工后先做两件事：全量关系词统计（§2 枚举收敛）+ Boundary Issues 联审结果回写，再启动 U1
- 导出脚本解析失败率若 >5%，先修文档统一性而不是堆 LLM 兜底
- 本文档是活文档：试点后回填实测准确率与修正

## 2026-09-12 U15 语料补子节层（域 06-29）
- 动因：batch-A/B 生产史造成 01-05 有子节层、06-29 叶子直挂域（browse 页形态不一致）
- 做法：bge-m3 embedding(复用 sqlite embedding 表) KMeans 预聚类 → mimo-v2.5 每域提议 4-8 子节(EN+ZH 命名) → MECE 校验(全叶恰好一次，重复/遗漏自动重试) → apply_subsections.py 重写 DIRECTORY.md → export_atlas.py 重建 DB → 恢复 embedding 表(备份 attach 回填) → section-zh.json 补 157 项 → import_zh.py → atlas-web gen+build
- 结果：29 域全部有子节层，113→270 section，1015 叶归入 157 个新子节，总成本 <$1
- 坑：apply 脚本 f-string 循环变量泄漏造成叶子重复行，备份目录 md.bak + DB backup 救场；export 删库重建会丢 embedding 表，必须先备份回填
- 备份：atlas/atlas-backup-presubs.sqlite (449MB) + atlas/DIRECTORY.md.bak，确认稳定后可删

## 2026-09-12 U14 草稿叶系统启动（atlas 自进化第一块）

- 动机：1804 叶不保证全。人工/引擎提议新类型 → 查重 → 人确认 → 归类入库，让语料随现实生长
- 设计原则（用户拍板）：创建零摩擦先入草稿区；**查重是入库前置**（不归类不用查）；草稿独立页面不进正树不污染统计；**叶子必须完整**（非瘦叶，一次一片按 WRITING_GUIDE 全文生成）；正文英文为源、中文走翻译层，草稿页提供中文对照
- 组件：
  - `drafts/`（真相源 frontmatter+正文文件，进 git）；`leaf_lint.py` 结构校验器（正文≥12000/H3≥10/Related≥6/产品≥4，含产品 URL 逐一 fetch 验证的引擎纪律）；`drafts_prompt.md` 引擎无关写作模板
  - `drafts_engines/` **可插拔引擎**：generate(idea)->.body.md，当前 opencode headless adapter（`drafts/agent.json` 引擎专用权限配置，解决 headless 权限自动拒绝），engines.json 选引擎+模型
  - `drafts_api.py` stdlib :5199（vite proxy /api）：CRUD+dedupe+promote+sections+translate；`atlas-web/src/routes/drafts.tsx` 草稿页（列表/创建/编辑/查重裁决面板/归类控件）
  - `dedupe_judge.py`：向量 top-10 + 分界记录 → mimo 裁决 same/variant/new + 理由 + section_hint；review.json 存档
  - `promote_draft.py`：new（DIRECTORY.md 字母序插 bullet + applications/ + research/ + export→**embedding 快照回填**→embed 增量→translate 增量→import_zh→gen-data→gate 回归）/ merge（DIRECTORY 别名 ` / ` 机制）
- 首叶实战：CLI Accounting Tool（命令行记账工具）已入库 08.07，1804→1805，中文对照/l0_zh/embedding/FTS 全通
- 坑与教训：
  - headless opencode 权限 auto-reject（全局 ask 规则）→ OPENCODE_CONFIG 挂引擎专用配置
  - 直连 API key 只认**裸模型 id**（opencode-go/mimo-v2.5 → 401，mimo-v2.5 ✅）
  - mimo-v2.5 是推理模型：max_tokens=500 全被 reasoning 吃光 → 3000 + reasoning 字段兜底解析
  - 引擎最初"覆盖整文件"吃掉 frontmatter → 契约改为引擎写 .body.md 由包装器组装
  - 产品幻觉：生成稿混入死链产品（plainshell.com）→ prompt 强制逐 URL fetch 验证，不可验证即删
  - promote 幂等化（首次中途崩溃后 corpus 文件残留，重跑要能续）
  - gate_check 串行 ~35s/项，52 项约 30 分钟，后台跑

## 2026-09-12 U14 增强：生成信号 + 方案A（调研后定名）

- UX：创建成功跳转详情页；生成中 4s 轮询实时进度卡（调研/正文/当前小节/日志尾/更新时间，读引擎正在写的文件，引擎零配合）；生成期间隐藏 lint 报错（空骨架必然全红是噪音）
- **方案A（调研后定名）**：起名/主张从创建时浅调研（首页摘录+mimo）改为引擎深调研后定。创建时 name 留空 → 临时 `wip-<desc或域名>` slug（unique_slug 防撞）+ frontmatter name_source: pending → prompt 新增 Identity 步骤（先调研 → 写 `identity.json`{name,name_zh,desc} → 再按定名写正文）→ run_engine 的 `apply_identity` 回填 frontmatter + 定稿 desc 跑碰撞入 review → **入库（promote）时才按定名改名**（dn.rename_draft，草稿 id 稳定不破坏轮询；promote 前置改名是唯一改名点）
- 引擎调研发现重复（same/variant）→ identity.json 写裁决、不写正文 → 状态 failed + review 留档（查重门禁前移到生成期）
- 触发案例：用户拿 opencode（实为 AI 编码代理）链接测试 → 创建时浅起名定死「开源代码编辑器」+幻觉 Electron desc → 引擎深调研发现真相却无权改名硬写。根因=先起名后调研，方案A根治
- 单测过：identity 回填/裁决停机/rename 三路径；DELETE 补 .zh.json/.identity.json 后缀

## 2026-09-13 工程稳定性修复

- 保存首次本地版本基线，修复在 `codex/stabilize-atlas` 分支完成。
- 查重相似度按 slug 对齐；候选图扩展去重；分类数据按数据库版本自动刷新，单次请求固定同一快照。
- 查重裁决绑定当前草稿和语料版本。新建只接受 new，合并只能进入 same/variant 指定的类型。
- 入库先构建隔离副本，执行翻译、向量、网页生成和固定样本回归；90% 门禁失败或请求异常不发布。新增研究笔记必须存在，草稿 ID 保持稳定。
- 导出先生成临时数据库并校验，保留输入未变的向量；目录别名能解析回 canonical slug。切换使用原子替换及可恢复的发布日志。
- 回归评分明确保留原始准确率与已确认替代标签口径，失败返回非零退出码。离线测试不调用模型；在线成绩仍待后续运行验证。
- 网页英文各节取消截断，提供来源与完整原文；类型数量从数据读取；入库状态持续轮询，错误不再被裁决面板条件隐藏。
- 新增离线回归测试、Python 依赖清单、根目录运行说明与 CI 配置。历史中文翻译中的上游截断仍需另行补译。
