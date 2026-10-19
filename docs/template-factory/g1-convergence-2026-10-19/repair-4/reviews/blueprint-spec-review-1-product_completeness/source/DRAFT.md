{
  "acceptance": [
    {
      "features": [
        "F01",
        "F08"
      ],
      "goal": "保存一条链接后，同进程与重启后的新进程都能读到该记录，且 id 与内容稳定。",
      "id": "A01",
      "implementation": "acceptance/p0_library.py",
      "phase": "P0",
      "status": "not_run",
      "type": "positive"
    },
    {
      "features": [
        "F01",
        "F10"
      ],
      "goal": "保存表单与 JSON 均接受绝对可解析的 http/https URL（含单标签主机，如 http://localhost）并保留原始字符串；缺协议、非 http/https、空/非法 hostname
被拒绝为 400 invalid_url，且库中不新增记录。",
      "id": "A02",
      "implementation": "acceptance/p0_library.py",
      "phase": "P0",
      "status": "not_run",
      "type": "negative"
    },
    {
      "features": [
        "F01",
        "F02"
      ],
      "goal": "不选归类保存时记录落入“未整理”，保存时给出的新归类名被自动创建，首启可见预置归类。",
      "id": "A03",
      "implementation": "acceptance/p0_library.py",
      "phase": "P0",
      "status": "not_run",
      "type": "positive"
    },
    {
      "features": [
        "F03"
      ],
      "goal": "通过真实归类页表单完成新建、重命名、删除：重名、非法名与默认归类保护给出可读 form-error 且不改数据；删除归类后活动与软删除记录都迁回“未整理”，软删记录仍可恢复。",
      "id": "A04",
      "implementation": "acceptance/p0_organize.py",
      "phase": "P0",
      "status": "not_run",
      "type": "positive"
    },
    {
      "features": [
        "F04",
        "F08"
      ],
      "goal": "在给定的 base_url 目标把记录从“未整理”移动到另一归类，并用独立实例证明该归属跨重启仍然有效。",
      "id": "A05",
      "implementation": "acceptance/p0_organize.py",
      "phase": "P0",
      "status": "not_run",
      "type": "positive"
    },
    {
      "features": [
        "F05"
      ],
      "goal": "通过真实归类页/记录表单浏览与计数：侧栏与接口的 count 只计活动记录，并在移动、软删除、恢复后与实际列表和 JSON 保持一致。",
      "id": "A06",
      "implementation": "acceptance/p0_organize.py",
      "phase": "P0",
      "status": "not_run",
      "type": "positive"
    },
    {
      "features": [
        "F06"
      ],
      "goal": "从真实归类页提交 category 与 q：页面保留所选归类与查询并显示匹配/明确空结果；同一关键字在两个归类分别命中各自记录，且 JSON 检索仍覆盖标题、域名与描述、大小写不敏感。",
      "id": "A07",
      "implementation": "acceptance/p0_find_open.py",
      "phase": "P0",
      "status": "not_run",
      "type": "positive"
    },
    {
      "features": [
        "F07"
      ],
      "goal": "打开记录跳转到保存时的原始 URL（302 Location 等于保存值），未知 id 返回 404。",
      "id": "A08",
      "implementation": "acceptance/p0_find_open.py",
      "phase": "P0",
      "status": "not_run",
      "type": "positive"
    },
    {
      "features": [
        "F08",
        "F09"
      ],
      "goal": "通过真实记录表单软删除并恢复：默认视图排除、回收站可见、恢复后字段与归类回归；删除归类时软删记录迁回“未整理”仍可恢复，且删除状态跨重启保持。",
      "id": "A09",
      "implementation": "acceptance/p0_recovery.py",
      "phase": "P0",
      "status": "not_run",
      "type": "positive"
    },
    {
      "features": [
        "F10"
      ],
      "goal": "未知 id 与畸形 JSON 返回结构化错误（bad_request/not_found）且不产生 5xx、不改变数据；真实表单的非法 URL 显示可读 form-error、保留输入，并在修正后成功保存。",
      "id": "A10",
      "implementation": "acceptance/p0_recovery.py",
      "phase": "P0",
      "status": "not_run",
      "type": "negative"
    },
    {
      "features": [
        "F11"
      ],
      "goal": "健康检查返回就绪，首页外壳在空库下渲染录入表单与列表容器，入口不报错。",
      "id": "A11",
      "implementation": "acceptance/p0_library.py",
      "phase": "P0",
      "status": "not_run",
      "type": "positive"
    },
    {
      "features": [
        "F04",
        "F10"
      ],
      "goal": "真实表单与 JSON 提交空名/超长名/非法归类时显示可读 form-error 并返回 400 invalid_category；归类集合、记录集合与被移动记录归属均不变。",
      "id": "A12",
      "implementation": "acceptance/p0_organize.py",
      "phase": "P0",
      "status": "not_run",
      "type": "negative"
    },
    {
      "features": [
        "F12"
      ],
      "goal": "外部网络不可用时保存仍然成功，图标与标题降级为本地派生结果，缺失增强不阻塞或报错。",
      "id": "A13",
      "implementation": "acceptance/p1_maturity.py",
      "phase": "P1",
      "status": "not_run",
      "type": "positive"
    },
    {
      "features": [
        "F13"
      ],
      "goal": "导出为浏览器书签 HTML 可包含已存记录，且导入该 HTML 后相应记录可再次检索到。",
      "id": "A14",
      "implementation": "acceptance/p1_maturity.py",
      "phase": "P1",
      "status": "not_run",
      "type": "positive"
    },
    {
      "features": [
        "F14"
      ],
      "goal": "重复 URL 默认被拒绝（409 duplicate_url）且库不变；显式允许重复时可新增第二条。",
      "id": "A15",
      "implementation": "acceptance/p1_maturity.py",
      "phase": "P1",
      "status": "not_run",
      "type": "negative"
    }
  ],
  "confirmed_scenario": {
    "acceptance": [
      "用户主动保存的链接在多次会话之间持久保留，形成不断增长的个人收藏",
      "每条记录都以 URL 锚定到外部网页，打开记录即跳转到该页面",
      "用户可以在归类之间移动记录或新建归类，操作结果在重新打开后仍然有效",
      "通过归类浏览或关键字检索，用户能找到此前存入的特定链接"
    ],
    "audience": "习惯先把感兴趣的网页存起来、之后再回头处理的普通网络用户",
    "id": "scn_7756e0007f6a463a97316f3f49c15248",
    "leaf": "bookmark-manager",
    "leaf_name": "书签管理器",
    "name": "生活待购与灵感收藏夹",
    "objective": "把偶然看到但当下不处理的外部网页链接留存，日后需要时能重新找到并回到原页面",
    "revision": 2,
    "status": "ready",
    "updated_at": "2026-10-16T14:18:20.407897+00:00",
    "workflow": [
      "用户在浏览时看到想记住的商品页、教程或灵感图片，主动保存该链接",
      "保存时选择一个简单归类，如“待购”“家居改造”或“以后看看”",
      "未经整理的链接可先进入默认归类，之后再手动移动到更合适的位置",
      "用户在需要实际处理时打开个人库，浏览或检索相关归类",
      "用户从记录打开链接，回到原始网页继续购买、阅读或参考"
    ]
  },
  "contract_coverage": {
    "features": [
      {
        "acceptance_ids": [
          "A01",
          "A02",
          "A03"
        ],
        "action": "填写原始 URL，可选标题/描述，选择已有归类、留为默认「未整理」或输入新归类名并提交。",
        "design_basis": "场景 workflow 1–2 与验收 1/2：用户主动保存外部网页链接，记录以 URL 锚定并持久保留。",
        "entry": "首页 GET / 的保存表单 form[action=/bookmarks/new]，字段 url、title、description、category。",
        "failure": "非法 URL 返回 400 invalid_url，非法归类返回 400 invalid_category；HTML 同页显示 [data-testid=form-error]，不写入。",
        "feature_id": "F01",
        "navigation": "成功后 303 到 /?category=<归类> 或 /，浏览器显示新记录行。",
        "recovery": "失败页保留已填 url/title/description/category，用户修正后重新提交；也可返回列表。",
        "success_state": "303 返回首页，新记录出现在所选归类，GET /api/bookmarks/{id} 返回同一原始 URL；SQLite 行已持久化。"
      },
      {
        "acceptance_ids": [
          "A03"
        ],
        "action": "不另选归类直接保存；首启查看预置归类。",
        "design_basis": "场景 workflow 3：未经整理的链接先进入默认归类，之后再移动；成熟产品普遍提供未被整理收件区。",
        "entry": "首页保存表单的 category 字段（默认「未整理」）与侧栏/归类页的预置归类列表。",
        "failure": "默认归类缺失或写入失败时返回明确错误页或 JSON 错误，不伪装成功。",
        "feature_id": "F02",
        "navigation": "303 到首页或未整理归类视图。",
        "recovery": "重试保存；应用启动时在事务中补齐预置归类。",
        "success_state": "记录的 category_id 为默认「未整理」，可在 /?category=未整理 看到；“未整理”“待购”“家居改造”“以后看看”均可见。"
      },
      {
        "acceptance_ids": [
          "A04"
        ],
        "action": "在真实表单提交 name 新建/重命名，提交 category_id 删除；删除默认归类被拒绝。",
        "design_basis": "场景验收 3 与 workflow 2：用户可新建归类并把记录放入合适位置；源包没有 collections，属目标新设计。",
        "entry": "首页 a[data-testid=category-manager] 进入 /categories；该页含 category-create-form、category-rename-
form、category-delete-form。",
        "failure": "重名 409 duplicate_category、空名/超长 400 invalid_name、默认归类 400 protected_category；页面显示 form-error
且数据不变。",
        "feature_id": "F03",
        "navigation": "创建/重命名/删除成功后 303 到 /categories。",
        "recovery": "保留已填 name/category_id 并允许改正或选择其他归类；可返回 /categories 重试。",
        "success_state": "303 到 /categories；新建/重命名可见且计数正确；删除归类后其活动与软删除记录都迁回「未整理」，软删记录仍可恢复。"
      },
      {
        "acceptance_ids": [
          "A05",
          "A12"
        ],
        "action": "选择目标归类（API 归类 ID）并提交；HTML 适配器把 ID 翻译为归类名后调用现有 move 服务。",
        "design_basis": "场景验收 3 与 workflow 3：记录可在归类之间移动，重新打开后仍保持新归属。",
        "entry": "每条 tr[data-testid=record-row] 内的 form[data-testid=record-move-form]，含 input record_id 与 select
name=category_id。",
        "failure": "空/超长/非法归类 400 invalid_category，未知 record_id 404 not_found；不移动、不写入。",
        "feature_id": "F04",
        "navigation": "成功后 303 到 /?category=<目标归类> 或来源视图。",
        "recovery": "保留选择并显示 form-error；用户改选有效归类或返回列表重试。",
        "success_state": "303 回列表；记录离开原归类并出现在目标归类，JSON 的 category 与持久化结果一致。"
      },
      {
        "acceptance_ids": [
          "A06"
        ],
        "action": "点击归类链接或从搜索表单选择归类并查看列表。",
        "design_basis": "场景验收 4：用户通过归类浏览找回记录；来源标签计数被调整为按归类聚合。",
        "entry": "首页侧栏 [data-testid=category-count][data-category-id] 与归类链接；/categories 同显计数；GET /?category=<name>。",
        "failure": "未知归类返回空结果而非 5xx；计数查询失败显示错误页。",
        "feature_id": "F05",
        "navigation": "GET /?category=... 或 GET /categories；无记录时显示明确空状态。",
        "recovery": "选择其他归类或清空筛选。",
        "success_state": "页面只列该归类活动记录；HTML count 与 JSON count 都等于活动（未软删）记录数；移动、删除、恢复后仍一致。"
      },
      {
        "acceptance_ids": [
          "A07"
        ],
        "action": "选择归类、输入关键字并提交。",
        "design_basis": "场景验收 4：用户凭记得的关键字找回已存链接；来源仅搜标题，目标扩展到可识别来源的字段。",
        "entry": "首页 form[data-testid=category-search-form]，字段 category（归类名）与 q；action 为 GET /。",
        "failure": "无匹配不是错误（200 + 空结果）；非法请求返回可读错误且不写入。",
        "feature_id": "F06",
        "navigation": "GET /?category=...&q=...，同一页面更新结果。",
        "recovery": "修改 q 或切换归类重新提交；清空 q 恢复归类浏览。",
        "success_state": "URL 与表单保留 category 与 q；页面显示所选归类、保留查询和匹配行；同一关键字在两个归类分别命中各自记录；无匹配显示明确空结果；JSON 返回匹配集。"
      },
      {
        "acceptance_ids": [
          "A08"
        ],
        "action": "用户点击打开链接。",
        "design_basis": "场景验收 2 与 workflow 5：打开记录即回到保存时的外部网页，库只保证引用而非内容。",
        "entry": "记录行 a[data-testid=record-open-link] 与 GET /go/{id}。",
        "failure": "未知 id 404 not_found；目标不可达不影响库中记录可读。",
        "feature_id": "F07",
        "navigation": "浏览器导航到原始 URL（新标签）；服务端只发 302。",
        "recovery": "返回收藏列表选择其他记录；如 URL 有误，可由现有 PATCH API 更新并重算 hostname。",
        "success_state": "链接 href 恰为保存时原始 URL，target=_blank、rel 含 noopener；GET /go/{id} 302 Location 为同一字符串；P0 不请求目标页。"
      },
      {
        "acceptance_ids": [
          "A01",
          "A05",
          "A09"
        ],
        "action": "执行真实写操作，停止应用进程，再以同一实例目录重启并读取。",
        "design_basis": "场景验收 1：主动保存的链接在多次会话之间持久保留；目标以 SQLite 实现本地单用户持久化。",
        "entry": "保存、移动、删除/恢复等写操作后重新请求页面；重启适配器从同一 app_root 与实例数据目录启动。",
        "failure": "数据库不可写或损坏时返回明确 5xx 错误页而非成功假象；事务回滚保持旧状态。",
        "feature_id": "F08",
        "navigation": "无自动导航；下次 GET / 读取持久状态。",
        "recovery": "恢复可写数据目录后重试；重启应用重新初始化 schema。",
        "success_state": "重启后 id、原始 URL、标题、描述、归类与 trashed 状态与写入后一致；HTML 与 JSON 都来自 SQLite。"
      },
      {
        "acceptance_ids": [
          "A09"
        ],
        "action": "提交 record_id 软删除；在回收站提交 record_id 恢复。",
        "design_basis": "场景要求可恢复的失败；来源仅有归档记录的瞬时 Undo，目标改为显式软删除与恢复。",
        "entry": "记录行 form[data-testid=record-delete-form]；GET /?trash=1 的软删记录行 form[data-testid=record-restore-form]。",
        "failure": "未知 record_id 404 not_found；失败不改变 trashed_at，不产生 5xx。",
        "feature_id": "F09",
        "navigation": "删除成功 303 到 /?trash=1；恢复成功 303 到恢复后归类。",
        "recovery": "回收站提供可提交的恢复表单；失败可重试或返回列表。",
        "success_state": "默认视图与计数排除软删记录，回收站仍显示；恢复后原始字段与归类回归并重新可见；归类删除后软删记录仍在「未整理」可恢复。"
      },
      {
        "acceptance_ids": [
          "A02",
          "A10",
          "A12"
        ],
        "action": "提交非法 URL、空/超长/非法归类、畸形 JSON 或未知 ID。",
        "design_basis": "场景要求非法输入可恢复；源表单校验被调整为服务端 HTML 表单与 JSON API 共用的显式错误合同。",
        "entry": "所有 HTML 表单（保存、归类、移动、删除、恢复、搜索）与 JSON API 端点。",
        "failure": "出现 5xx、静默写入或不可恢复的错误页即视为失败。",
        "feature_id": "F10",
        "navigation": "HTML 错误留在当前表单页并保留输入；JSON 无导航。",
        "recovery": "修正字段后重新提交；失败页保留可运行的表单或返回链接。",
        "success_state": "错误路径本身成功执行：JSON 返回 400/404/409 与结构化错误码，HTML 返回 400/409 与 form-error；畸形 JSON 为 bad_request；均无
5xx、无写入。"
      },
      {
        "acceptance_ids": [
          "A11"
        ],
        "action": "首启或空库时打开首页。",
        "design_basis": "场景是单用户本地工具，需要可打开的应用入口；目标采用 Python 服务端渲染外壳而非来源 SPA。",
        "entry": "GET / 与 GET /api/health。",
        "failure": "健康检查非 200/非 JSON、首页 5xx 或缺少表单时显式失败。",
        "feature_id": "F11",
        "navigation": "无自动导航（首页即入口）；可进入 /categories 或归类筛选。",
        "recovery": "启动或重启应用；修复后刷新首页。",
        "success_state": "200 text/html；含保存表单 name=url、归类管理链接、记录列表/空状态容器；预置归类与空库不报错；health 200 JSON。"
      }
    ],
    "review_rules_version": "atlas.current-required-contract.v1",
    "schema": "atlas.contract-coverage.v1"
  },
  "decisions": [
    {
      "default": "单选归类（bookmark.category_id 标量外键）。场景流程明确“选择一个简单归类”，单归属让移动、计数与浏览语义无歧义；未来若需多值可迁移到关联表而不丢数据。",
      "id": "D01",
      "impact": "决定数据模型（标量外键 vs 关联表）以及浏览、计数与检索的实现路径。",
      "question": "记录应归属于单一“归类”，还是允许像标签一样同时属于多个？",
      "status": "decided",
      "when_to_ask": "当真实用户反馈同一条记录必须同时属于多个主题，或需要跨主题交叉检索时再评估多标签。"
    },
    {
      "default": "落入默认“未整理”，保存始终成功。场景流程第3步要求未经整理的链接可先进入默认归类，快速保存不应打断浏览。",
      "id": "D02",
      "impact": "决定保存接口是否允许缺省 category，以及首启预置数据内容。",
      "question": "保存时不选归类，应阻止保存还是落入默认“未整理”？",
      "status": "decided",
      "when_to_ask": "当目标用户群要求强制归类（例如团队共享库）时再改为必选。"
    },
    {
      "default": "自动创建（名称大小写不敏感去重），重名则复用现有归类；保持保存流程不中断。",
      "id": "D03",
      "impact": "决定 categories 的唯一约束、写入事务边界与 409/400 的语义；HTML 归类表单与 JSON API 共用服务层，重名、非法名与默认归类保护都不得产生部分写入。",
      "question": "在保存或移动界面输入一个尚不存在的归类名，应自动创建还是报错？",
      "status": "decided",
      "when_to_ask": "当出现拼写错误导致归类碎片化的证据时，改为只允许从既有归类中选择。"
    },
    {
      "default": "软删除：记录标记 trashed_at，默认视图排除，提供撤销恢复；场景要求可恢复的失败。",
      "id": "D04",
      "impact": "决定数据模型的 trashed_at 列、默认列表过滤条件、/restore 恢复路径，以及删除归类时活动与软删记录同迁默认归类；不引入 purge 或永久删除接口。",
      "question": "删除是立即物理删除，还是软删除到可恢复区并支持短时撤销？",
      "status": "decided",
      "when_to_ask": "当用户要求彻底清除隐私数据或回收站增长需要释放空间时，再提供永久删除与清空。"
    },
    {
      "default": "本地优先：图标由域名派生本地路由，第三方元数据抓取为可选增强且失败静默降级，保证离线可保存。",
      "id": "D05",
      "impact": "决定保存流程的时延与可用性依赖，以及收藏响应中的 favicon/title 字段形态。",
      "question": "标题、描述与图标是否依赖第三方抓取服务？",
      "status": "decided",
      "when_to_ask": "当部署环境确认可访问外部服务且用户需要富预览时再启用增强。"
    },
    {
      "default": "自 P1/F14 起默认检测并返回 409 duplicate_url（附已有 id 供跳转查看），保存方显式 allow_duplicate 时可强制新增；P0
核心用例不依赖去重，软删除记录不参与判定；场景与成熟产品都倾向一址一记录。",
      "id": "D06",
      "impact": "决定服务层去重查询、allow_duplicate 语义与导入时的合并或跳过策略（不使用 url 唯一索引）。",
      "question": "同一 URL 再次保存时，阻止还是允许？",
      "status": "decided",
      "when_to_ask": "当用户明确需要对同一地址保留多个不同上下文的记录时再放宽。"
    },
    {
      "default": "标题加域名(hostname)加描述，大小写不敏感，可与归类过滤叠加；不检索正文（无抓取）。",
      "id": "D07",
      "impact": "决定查询实现与检索参数语义：category 与 q 可叠加，HTML 归类检索表单必须同时保留两者；计数与列表只统计未软删记录，移动、删除、恢复后保持一致。",
      "question": "关键字应匹配哪些字段？",
      "status": "decided",
      "when_to_ask": "当需要按网页正文全文检索时再引入抓取与索引（属后期能力）。"
    },
    {
      "default": "python-web 加 Python 3.12 标准库 http.server 加单文件 SQLite；满足离线、单用户与可独立验收，无需外部依赖。",
      "id": "D08",
      "impact": "决定交付 profile 为 python-web（Python 3.12 标准库 + SQLite + 服务端渲染 HTML），验收通过独立 HTTP 实例与真实表单提交进行。",
      "question": "采用何种运行时与持久化方式？",
      "status": "decided",
      "when_to_ask": "当需要多用户、并发写入或托管部署时再引入 Web 框架与服务端数据库。"
    },
    {
      "default": "默认无认证；交付进程在独立验收网络中监听测试者可路由的接口（`--host 0.0.0.0`），日常本机使用可绑定 127.0.0.1；不引入凭据文件，符合个人本地库的定位。",
      "id": "D09",
      "impact": "决定部署方式与验收的认证契约（验收默认不携带凭据）。",
      "question": "是否需要登录或口令？",
      "status": "decided",
      "when_to_ask": "当应用需要暴露到局域网或公网时，必须加入认证，否则只允许本机绑定。"
    },
    {
      "default": "Netscape 浏览器书签 HTML（本类型的交换约定），归类映射为文件夹或标签字段。",
      "id": "D10",
      "impact": "决定 P1 导入/导出的解析与生成实现。",
      "question": "导入/导出采用什么格式？",
      "status": "decided",
      "when_to_ask": "当需要与某个具体产品双向同步时再适配其专有格式。"
    },
    {
      "default": "P0 不做：本地单实例，数据在单一 SQLite 文件；跨设备属后期能力。",
      "id": "D11",
      "impact": "影响运行形态与数据归属，不阻塞 P0 核心旅程。",
      "question": "是否提供云同步或多用户共享？",
      "status": "deferred",
      "when_to_ask": "当用户明确需要在多设备访问同一库时再设计同步或托管。"
    },
    {
      "default": "P0 使用扁平单选归类加“未整理”收件区；嵌套与标签属成熟能力，按需在后期启用。",
      "id": "D12",
      "impact": "影响侧栏结构与检索实现，可后续迁移而不破坏现有数据。",
      "question": "归类是否需要嵌套层级，或与标签并存？",
      "status": "deferred",
      "when_to_ask": "当扁平归类数量增长到难以浏览，或需要交叉主题时。"
    },
    {
      "default": "本期不做：抓取与归档在离线验收下不可验证；先保证引用记录与打开回跳。",
      "id": "D13",
      "impact": "涉及外部抓取与存储扩展，属后期可选能力，不纳入 P0/P1 验收。",
      "question": "是否需要保存网页副本并检测失效链接？",
      "status": "open",
      "when_to_ask": "当用户明确要求内容留存，或需要清理死链时再评估。"
    }
  ],
  "features": [
    {
      "acceptance": [
        "A01",
        "A02",
        "A03"
      ],
      "applicability": "current required",
      "id": "F01",
      "name": "保存收藏（URL 必填，标题/描述可选）",
      "phase": "P0",
      "reason": "场景流程第1-2步要求看到想记住的页面即主动保存；上游记录了新记录默认字段与保存落盘（S02、S06），并把 URL 校验与编辑回填收敛在表单（S04）。",
      "sources": [
        "S02",
        "S04",
        "S06",
        "S17"
      ]
    },
    {
      "acceptance": [
        "A03"
      ],
      "applicability": "current required",
      "id": "F02",
      "name": "默认“未整理”与预置归类集合",
      "phase": "P0",
      "reason": "场景流程第3步要求未整理的链接先进入默认归类；上游只有 Home/Archived 视图、无默认桶（S16），故按场景新增默认收件区，并借鉴其标签聚合思路（S20）。",
      "sources": [
        "S16",
        "S20"
      ]
    },
    {
      "acceptance": [
        "A04"
      ],
      "applicability": "current required",
      "id": "F03",
      "name": "归类管理（新建/重命名/删除）",
      "phase": "P0",
      "reason": "场景验收第3条要求可新建归类；上游明确没有 collections/folders（S16），因此归类实体与增删改必须新设计并落库。",
      "sources": [
        "S16",
        "S20"
      ]
    },
    {
      "acceptance": [
        "A05",
        "A12"
      ],
      "applicability": "current required",
      "id": "F04",
      "name": "记录在归类间移动",
      "phase": "P0",
      "reason": "场景验收第3条要求记录可在归类之间移动且重开后仍有效；上游检索按标签交集筛选（S16），这里把多值交集改造为单一归属迁移。",
      "sources": [
        "S16"
      ]
    },
    {
      "acceptance": [
        "A06"
      ],
      "applicability": "current required",
      "id": "F05",
      "name": "归类浏览与条目计数",
      "phase": "P0",
      "reason": "场景验收第4条要求通过归类浏览找回；上游侧栏按标签聚合计数（S20、S16），改为按归类聚合与筛选。",
      "sources": [
        "S16",
        "S20"
      ]
    },
    {
      "acceptance": [
        "A07"
      ],
      "applicability": "current required",
      "id": "F06",
      "name": "关键字检索（标题/域名/描述）",
      "phase": "P0",
      "reason": "场景验收第4条要求关键字检索；上游仅匹配标题小写（S16），需扩展到域名与描述以覆盖只记得来源的场景。",
      "sources": [
        "S16"
      ]
    },
    {
      "acceptance": [
        "A08"
      ],
      "applicability": "current required",
      "id": "F07",
      "name": "打开原始网页（URL 锚定与回跳）",
      "phase": "P0",
      "reason": "场景验收第2条与流程第5步要求打开记录即回到原页；上游 Visit 以 window.open(noopener,noreferrer) 打开并由 URL
派生域名（S15、S08），保留打开与派生、去掉访问计数。",
      "sources": [
        "S15",
        "S08"
      ]
    },
    {
      "acceptance": [
        "A01",
        "A05",
        "A09"
      ],
      "applicability": "current required",
      "id": "F08",
      "name": "多会话持久化（跨重启保留）",
      "phase": "P0",
      "reason": "场景验收第1条要求多次会话之间持久保留；源包以 Dexie/IndexedDB 落盘并在启动时全量载入（S09、S13、S06），README 定位 local-
first（S11）。目标保留本地单用户与跨会话/跨重启持久化的行为，但把存储实现调整为 Python 服务端 SQLite：不宣称浏览器 profile 持久化、多设备同步或客户端内存映射是目标设计；每个请求从数据库查询。",
      "sources": [
        "S09",
        "S13",
        "S06",
        "S11"
      ]
    },
    {
      "acceptance": [
        "A09"
      ],
      "applicability": "current required",
      "id": "F09",
      "name": "删除与撤销恢复",
      "phase": "P0",
      "reason": "场景要求可恢复的失败；上游删除配 5 秒 Undo 恢复（S07），去掉“仅归档可删”前置限制，保留删除加恢复的兜底。",
      "sources": [
        "S07"
      ]
    },
    {
      "acceptance": [
        "A02",
        "A10",
        "A12"
      ],
      "applicability": "current required",
      "id": "F10",
      "name": "输入校验与错误合同",
      "phase": "P0",
      "reason": "上游以 Valibot 约束 http/https、标题长度与标签数量（S04），并由 getHostname 派生域名（S08）；场景把标签必填改为可选归类，需要显式错误的保存与移动契约。",
      "sources": [
        "S04",
        "S08"
      ]
    },
    {
      "acceptance": [
        "A11"
      ],
      "applicability": "current required",
      "id": "F11",
      "name": "本地应用外壳与首启（空库）",
      "phase": "P0",
      "reason": "场景是单用户本地工具；源包 index.html 提供 #root 并由客户端入口挂载 SPA（S10、S18）。目标外壳调整为 Python 服务端渲染的 HTML
页面与表单（POST/redirect/GET），保留保存—浏览—检索—打开的用户闭环与空库就绪视图，不采用 SPA 挂载或客户端对话框状态。",
      "sources": [
        "S10",
        "S18"
      ]
    },
    {
      "acceptance": [
        "A13"
      ],
      "applicability": "later",
      "id": "F12",
      "name": "元数据与图标增强（离线降级）",
      "phase": "P1",
      "reason": "场景希望一眼辨认商品页/教程/灵感图，但上游依赖 api.microlink.io、images.weserv.nl 与 Google favicon 三个未验证端点且失败仅
console.error（S14、S21、S08）；因此把可用性依赖降为本地域名派生，外部抓取降级为可选增强。",
      "sources": [
        "S14",
        "S21",
        "S08"
      ]
    },
    {
      "acceptance": [
        "A14"
      ],
      "applicability": "later",
      "id": "F13",
      "name": "导入/导出（浏览器书签 HTML）",
      "phase": "P1",
      "reason": "互操作是成熟产品的标准配置，但上游 manifest 没有导入/导出（S22 无测试脚本、无导入导出能力），属场景后期新增。",
      "sources": []
    },
    {
      "acceptance": [
        "A15"
      ],
      "applicability": "later",
      "id": "F14",
      "name": "重复链接检测",
      "phase": "P1",
      "reason": "成熟产品趋向一址一记录，上游未实现去重（S16、S17 无重复处理）；P1 在保存与导入路径新增服务层重复检测（D06），P0 核心用例不依赖该能力。",
      "sources": []
    },
    {
      "acceptance": [],
      "applicability": "not applicable",
      "id": "F15",
      "name": "浏览器扩展/分享目标抓取",
      "phase": null,
      "reason": "场景交付为本地 Web 工具，扩展与移动分享目标不在本期范围，手工录入与打开回跳已覆盖核心旅程。",
      "sources": []
    },
    {
      "acceptance": [],
      "applicability": "not applicable",
      "id": "F16",
      "name": "多设备与云同步",
      "phase": null,
      "reason": "本期是单机单实例的本地库，数据在单一 SQLite 文件；跨设备同步属后期形态，不阻塞核心旅程。",
      "sources": []
    },
    {
      "acceptance": [],
      "applicability": "decision needed",
      "id": "F17",
      "name": "网页留存副本/快照",
      "phase": null,
      "reason": "记录只保证引用而非内容（场景与原类型定义如此）；是否保存副本依赖外部抓取与存储，离线验收不可验证，需用户明确要求后再定。",
      "sources": []
    },
    {
      "acceptance": [],
      "applicability": "decision needed",
      "id": "F18",
      "name": "失效链接检测与修复",
      "phase": null,
      "reason": "链接腐坏是本类型的结构性风险，但检测需要主动外呼，外部网络在验收中禁用；先保证引用与打开回跳，是否检测待用户决定。",
      "sources": []
    },
    {
      "acceptance": [],
      "applicability": "decision needed",
      "id": "F19",
      "name": "嵌套归类与多标签并存",
      "phase": null,
      "reason": "场景明说“选择一个简单归类”，扁平单选加收件区已足够；嵌套/标签是成熟能力，待归类数量或交叉主题增长时再评估。",
      "sources": []
    },
    {
      "acceptance": [],
      "applicability": "not applicable",
      "id": "F20",
      "name": "置顶/归档与多排序模式",
      "phase": null,
      "reason": "上游置顶与归档、三种排序属书签阅读器语境（S19、S16、S03），会给编辑与删除增加前置条件，与快速保存、快速清理相冲突，故不采用。",
      "sources": [
        "S19",
        "S16",
        "S03"
      ]
    },
    {
      "acceptance": [],
      "applicability": "not applicable",
      "id": "F21",
      "name": "公开分享与协作库",
      "phase": null,
      "reason": "场景是私有个人收藏箱，分享不在核心旅程内；公开或协作需要多用户身份与权限，属不同类型定位。",
      "sources": []
    },
    {
      "acceptance": [],
      "applicability": "not applicable",
      "id": "F22",
      "name": "阅读稍后与未读标记",
      "phase": null,
      "reason": "场景重心是留存引用并可回跳，而非消费队列；未读标记会使产品向 Read-it-later 漂移。",
      "sources": []
    },
    {
      "acceptance": [],
      "applicability": "not applicable",
      "id": "F23",
      "name": "复制 URL 动作",
      "phase": null,
      "reason": "上游提供 Copy URL（S12），但本场景终点是打开原页而非分发链接，去掉可减少每条记录的操作噪音。",
      "sources": [
        "S12"
      ]
    },
    {
      "acceptance": [],
      "applicability": "not applicable",
      "id": "F24",
      "name": "访问计数与最近访问时间",
      "phase": null,
      "reason": "上游 Visit 会累加 visitCount 与 visitedAt（S15、S17）；场景只需打开动作，不需访问统计，故不保留这两个字段。",
      "sources": [
        "S15",
        "S17"
      ]
    }
  ],
  "limits": [
    "不实现云同步、多用户共享或托管部署（D11、F16、F21）。",
    "不保存网页快照、不做正文全文检索、不做失效链接检测（F17、F18、D13）。",
    "不引入置顶/归档、多排序模式、复制 URL 与访问计数（F20、F23、F24）。",
    "归类为扁平单选，不支持嵌套层级或多标签并存（F19、D01）。",
    "第三方元数据与图标抓取未验证可达性，仅作可选增强且失败静默降级（F12、D05）。",
    "验收不携带认证凭据；若目标要求认证，验收必须显式报告基础设施未就绪而非跳过或通过（D09）。",
    "不设置未经验证的性能或成本目标。"
  ],
  "phases": [
    {
      "acceptance": [
        "A01",
        "A02",
        "A03",
        "A04",
        "A05",
        "A06",
        "A07",
        "A08",
        "A09",
        "A10",
        "A11",
        "A12"
      ],
      "features": [
        "F01",
        "F02",
        "F03",
        "F04",
        "F05",
        "F06",
        "F07",
        "F08",
        "F09",
        "F10",
        "F11"
      ],
      "goal": "用户可保存链接（可选归类或落入未整理）、按归类或关键字找回、打开原页、清理并撤销，且全部数据跨会话与重启保留，非法输入得到可恢复的明确错误。",
      "id": "P0",
      "status": "not implemented",
      "title": "个人收藏箱核心旅程"
    },
    {
      "acceptance": [
        "A13",
        "A14",
        "A15"
      ],
      "features": [
        "F12",
        "F13",
        "F14"
      ],
      "goal": "在离线可用的前提下增强记录可辨识度（本地派生图标、外部抓取仅作增强），并支持浏览器书签格式的导入导出与重复链接检测，用于长期库维护。",
      "id": "P1",
      "status": "not implemented",
      "title": "成熟增强：元数据、互操作与库清理"
    }
  ],
  "roles": [
    {
      "id": "R01",
      "name": "收藏者（个人用户）",
      "responsibility": "在浏览时主动保存外部网页链接，选择或新建简单归类、把未整理的链接移动到合适归类、按归类或关键字找回、打开记录回到原页，并清理误存条目。"
    },
    {
      "id": "R02",
      "name": "本地收藏应用（服务端与页面外壳）",
      "responsibility": "校验录入、派生域名、持久化收藏与归类、提供保存/浏览/检索/打开/恢复接口，并在离线条件下保持可用。"
    },
    {
      "id": "R03",
      "name": "独立验收执行者",
      "responsibility": "以 URL 与 CLI 参数驱动真实目标，执行正负向行为断言、重启持久化验证与错误恢复验证，不修改应用、不自报运行结果。"
    }
  ]
}