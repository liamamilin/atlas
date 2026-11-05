# B2C 电商商城 · 可能性图谱（v0.5 新研究稿）

ATLAS 叶子：**E-commerce Platform** · `e-commerce-platform` · `05.01`。依据技能 `59c4fc4`，研究日期 2026-11-05。范围是单一商家面向消费者销售其经营商品，不包括以独立卖家入驻、平台分账为中心的交易市场。[A1][A2]

本轮新增阅读三个产品体系的操作资料。以下具名产品的行为不推广为全部商城的默认能力。金额、数量和日期仅是判别用例，不是实测店铺数据、实际税率或市场汇率。

## 主要领域覆盖情况

先完成了[主要领域逐项覆盖表](COVERAGE.md)，再形成下文。该表分别列出商品发现、规格、促销、购物车、结算、运税、订单、付款、库存、交付、售后、客户、数据处理、经营、权限及整体形态的实质内容与缺口。

本稿保留未研究和证据不足的部分，没有将它们改写成“不支持”，也不宣称已经完成整个类型的梳理。每个领域中的例子是代表性机制，不是该领域的全部可能性。覆盖与语言的作者复核结果分别记录在[双门禁记录](RESEARCH_AND_REVIEW.md)中。

## 可能性概览：同一商家可以形成哪些店铺形态

这里同时列出期望状态和对应期望变化；领域 18 的整体形态先于内部业务状态呈现。

| 期望状态 | 期望变化：原情况 → 条件或触发 → 新结果 | 反例与证据边界 |
| --- | --- | --- |
| **同一商城的可售目录中含实体书和下载电子书。** 这是产品类型组合的归纳。[W2][W13] | 原目录只有实体书；商家发布带价格与交付文件的电子书后，目录新增可购买的电子书。 | 免费说明书不是新增的可售电子书；发布商品不等于某个顾客已经获得下载资格。 |
| **同一商家的商品 P 在店面甲的分类 C 中出现，在店面乙的分类 C 中不出现（PrestaShop 8）。** [P8] | 原 P 尚未与两店面的 C 关联；商家仅在甲的店面上下文建立关联后，P 在甲的 C 中出现，乙的 C 不因此出现 P。 | 两店面都存在 C，不等于 P 自动在两处展示；这不是引入两个独立卖家。 |
| **顾客可切换到商城已启用的第二种前台语言（PrestaShop 8）。** [P10] | 原只有一种可选语言；导入并启用另一种语言后，顾客可在前台选择该语言。 | 只添加但保持禁用的语言不满足；能选择语言不证明所有商品与模块文字均已翻译。 |
| **商品金额可按店铺配置汇率显示为另一已启用币种（PrestaShop 8）。** [P9] | 原只选用基础币种，商品金额为 100；假设另一币种的换算率配置为 2，启用并选择该币种后，对应金额为 200。 | 只改货币符号而不按配置换算，不满足该陈述；显示汇率不代表银行结算汇率。 |

## 期望状态与期望变化：按已核查领域展开

领域名称是查找线索。每行只有期望状态与期望变化两个核心对象；第三列用来判别相近但不成立的情形。

### 1. 商品发现：搜索解释与属性筛选

| 期望状态 | 期望变化：原情况 → 条件或触发 → 新结果 | 反例与边界 |
| --- | --- | --- |
| **已配置的搜索别名按目标词查找已索引商品（PrestaShop 9 文档情形）。** 例：将误拼 palyer 映射到 player。[P1] | 原没有该别名；商家保存映射后，输入 palyer 可按 player 查找已索引且匹配的商品。 | 没有匹配商品或商品未被索引，不保证产生结果；不能用“建立了商品记录”代替“商品已可搜索”。 |
| **只选蓝色属性条件时，结果集合仅列出匹配该条件的商品（WooCommerce Product Search 扩展）。** [W1] | 原结果包含不同颜色的商品；顾客选择蓝色筛选条件后，扩展刷新匹配商品集合。 | 仅把页面标题改成“蓝色”不是筛选；匹配蓝色属性也不证明该颜色规格有现货。该扩展不是所有商城的必备组件。 |

### 2. 商品与规格：变体价格、缺货预订和评论审核

| 期望状态 | 期望变化：原情况 → 条件或触发 → 新结果 | 反例与边界 |
| --- | --- | --- |
| **一个商品变体有自己的售价（WooCommerce）。** [W3] | 蓝色 M 码原价为 100；商家将该变体售价保存为 120 后，该变体价格改为 120。 | 只修改描述中的“120”不算改变实际售价；没有价格的变体不能据此当作正常可售规格。 |
| **已发布且有价格的变体，允许缺货预订时可在零库存下接受订购（WooCommerce）。** [W3] | 蓝色 M 码已启用变体库存管理，库存为零且不允许缺货预订；启用该变体的缺货预订后，零库存不再仅因这一数量条件阻止订购。 | 只写“接受预订”宣传文字而未改变库存策略，不满足该变化；不推断其他结算限制也已解除。 |
| **一条商品评论的审核状态为已批准（WooCommerce）。** [W4] | 在启用人工审核的情形中，评论原待审核；商家执行 Approve 后，该评论变为已批准。 | 顾客提交五星评价不等于商家已批准；星级与审核状态是不同属性。 |

复杂组合商品和商品资料版本仍见覆盖缺口；不能由本节几个已研究的商品状态推断其余商品类型机制均已覆盖。

### 3. 价格与促销：券条件与客户组折扣

| 期望状态 | 期望变化：原情况 → 条件或触发 → 新结果 | 反例与边界 |
| --- | --- | --- |
| **满足优惠券配置条件的购物车获得该券的折扣（WooCommerce）。** [W5] | 假设券 C 有效且未耗尽，只限制最低商品小计 100、固定优惠 10；原未税小计 90，增加商品至 110 并应用 C 后，券折扣为 10。示例不含运税及其他优惠。 | 只输入一个已过期代码不满足；有运费不代表达到了商品小计门槛。不补写所有叠券优先级。 |
| **客户的商品报价采用其客户组折扣（PrestaShop 8）。** [P6] | 假设 U 仅属于组 G、商品未税价 100 且无其他优惠；G 的全店折扣从 0 改为 10% 后，该情形下 U 的商品报价为 90。 | 只给客户添加一条文字备注“九折”不算改变组折扣；多组及多优惠叠加结果没有由此推出。 |

### 4. 购物车：数量改变与尚未成交的记录

| 期望状态 | 期望变化：原情况 → 条件或触发 → 新结果 | 反例与边界 |
| --- | --- | --- |
| **购物车中商品甲的购买数量已更新（WooCommerce Cart block）。** [W6] | 原数量为 1；顾客通过数量控件改为 2，且商城接受该数量后，购物车记录显示 2。 | 只在页面文本中写“2 件”不算；购物车记录存在不证明已提交订单或已锁库存。 |
| **商家可查看尚未转换为正式订单的购物车（PrestaShop 8）。** [P2] | 原该顾客没有购物车记录；顾客加入商品并保存购物车、尚未提交订单后，后台新增一条未转订单的购物车记录。 | “未转订单”不证明顾客主观上决定放弃；提醒顾客也不等于已经挽回成交。 |

### 5. 结算提交：购买摘要与提交条件

| 期望状态 | 期望变化：原情况 → 条件或触发 → 新结果 | 反例与边界 |
| --- | --- | --- |
| **结算页的订单摘要列出本次购买的商品（WooCommerce Checkout block 的文档归纳）。** [W6][W7] | 原顾客仍在购物车；进入该购买的结算页后，订单摘要列出本次购买的商品。 | 静态展示几件促销商品不能代替本次订单摘要；进入结算也不代表支付已确认。 |
| **开启 Require Checkbox 时，未勾选条款确认的顾客不能继续提交结算（WooCommerce）。** [W7] | 原该选项已启用而顾客未确认；顾客勾选后，这一条款确认条件由未满足变为满足。 | 勾选只满足该项条件，不代表地址、库存、网关等其他条件全部通过，更不等于订单已付款。 |

### 6. 配送选择与费用：地址决定可选范围

| 期望状态 | 期望变化：原情况 → 条件或触发 → 新结果 | 反例与边界 |
| --- | --- | --- |
| **顾客可见的配送方式来自其地址首个匹配的配送区域（WooCommerce）。** [W8] | 地址原匹配区域甲；改为只匹配区域乙的地址后，可选方式改用乙中已配置的配送方式。 | 不能把所有区域的方式直接汇总给顾客；没有可用方式也不能只因商品有库存就推断可配送。 |

### 7. 税费计算：配置地址与价格含税口径

| 期望状态 | 期望变化：原情况 → 条件或触发 → 新结果 | 反例与边界 |
| --- | --- | --- |
| **商品税额由店铺选定的计税地址及匹配规则计算（WooCommerce）。** [W9] | 原尚未提供用于本次计算的收货地址；假设计税依据选为收货地址、商品未税价 100、无优惠运费、配置税率为 10%，填入匹配该规则的地址后，示例商品税额为 10。 | 已把 110 作为含税价格录入时，不能再按同一示例机械加 10；示例不说明任何地区依法应收多少税。 |

### 8. 订单记录：正式购买与取消

| 期望状态 | 期望变化：原情况 → 条件或触发 → 新结果 | 反例与边界 |
| --- | --- | --- |
| **商家能够查询顾客已提交的正式订单（WooCommerce）。** [W10][W11] | 原只有购买意图或临时结算草稿；顾客提交结算并形成正式订单后，商家可在订单范围中继续查询本次购买。 | 只有临时 Draft 记录不能证明顾客已提交；订单存在也不证明款项已确认。 |
| **订单已记录为取消（WooCommerce）。** [W11] | 原订单未取消；管理员执行取消后，订单的取消状态成立。 | 支付被拒与取消不是同一个结果；订单已取消不能单独证明发生了退款。 |

### 9. 付款、商家出款与争议：分别跟踪不同的钱款结果

| 期望状态 | 期望变化：原情况 → 条件或触发 → 新结果 | 反例与边界 |
| --- | --- | --- |
| **待发实物订单的收款已被商城确认（WooCommerce 文档情形）。** [W11] | 原仍待付款确认；网关确认收款，或商家核实线下款项并据此更新订单后，待发实物订单可进入 Processing，表示收款已确认且仍待履约。 | 仅获得支付授权不等于实际收款；顾客返回成功页面不能单独代替付款确认。两项区别为业务语义归纳。 |
| **交易款项进入可出款余额，但尚未因此成为银行到账款（WooPayments）。** [W17] | 原款项处于 Pending funds；在文档所述待结算期间结束后，该款项转入 Available funds，等待账户出款安排。 | Available funds 不等于银行已收到；不承诺统一到账天数或所有账户都能即时出款。 |
| **一笔出款可被记录为仍在转账途中（WooPayments）。** [W18] | 原该笔出款为 Pending；平台已发送款项且仍在途时，该笔出款记录为 In Transit。 | 订单的 Paid 或 Completed 不能代替出款状态；不把在途记录说成已经核实银行可用余额。 |
| **支付争议可记录为发卡行审查中的 Under Review（WooPayments）。** [W18][W19] | 原争议需要商家回应；商家提交挑战材料后，由发卡行审查的阶段与最终 Won/Lost 分开记录，不承诺固定处理时长。 | 提交材料不等于胜诉；争议不是一笔普通付款失败，也不是退货申请。 |

### 10. 库存占用与实际库存：预留和出库不是同一个扣减

| 期望状态 | 期望变化：原情况 → 条件或触发 → 新结果 | 反例与边界 |
| --- | --- | --- |
| **已提交订单的预留减少该库存范围内的可售数量（Adobe Commerce）。** [M1] | 假设某 SKU 无其他预留、阈值为零、可售量为 10；提交 2 件订单形成相应预留后，示例可售量为 8。 | 不能由此断言仓库已实际出库 2 件；也不将所有“加购物车”都写成这种预留。 |
| **取消尚未发货的预留数量会释放相应可售量（Adobe Commerce）。** [M1][M2] | 订单 2 件仍被预留且尚未发货；取消这 2 件后，对应补偿释放该占用。 | 这不是把已寄出的两件货搬回仓库；存在其他库存变动时，不能仅凭取消算出库存总值。 |
| **实物发货减少实际发货库存源的商品数量（Adobe Commerce）。** [M2] | 某源原有 10 件且没有其他库存变化；从该源发货 2 件后，该源数量为 8。 | 只收到订单而未发货，不等于该库存源已经扣减了实际出库量。 |

### 11. 实物履约：部分发货仍留下未发数量

| 期望状态 | 期望变化：原情况 → 条件或触发 → 新结果 | 反例与边界 |
| --- | --- | --- |
| **订单可以只有部分商品数量被记录为已发货（Adobe Commerce）。** [M2] | 假设订单需交付 4 件且未取消；先记录发货 2 件后，仍有 2 件未发；余量可在后续发运中处理。 | 只因第一批已发就标为整单全部交付，会丢失未发数量；发货记录也不证明承运签收。 |
| **同一订单含不同库存源的发运记录（Adobe Commerce）。** [M1][M2] | 原 4 件订单已开票但尚无发运记录，来源甲至少可发 1 件、乙至少可发 3 件；商家分别从甲记录发 1 件、乙记录发 3 件后，同一订单具有两来源的发运结果。 | 一个订单备注写了两个仓库名称，不证明已形成分来源发运记录；不推断哪种选择一定最省运费。 |

### 12. 数字交付：授权时点与撤销

| 期望状态 | 期望变化：原情况 → 条件或触发 → 新结果 | 反例与边界 |
| --- | --- | --- |
| **开启付款后授权时，顾客可在订单 Processing 阶段获得所购文件资格（WooCommerce）。** [W13] | 原顾客尚无该订单文件资格；店铺已启用付款后授权，订单进入 Processing 后，该项文件资格被授予。 | 未启用该选项时需等待 Completed；不能把“已付款”普遍等同于所有店铺均已开放文件。混合实物订单可在实物未到时已有数字资格。 |
| **某订单中的文件下载资格可被商家单独撤销（WooCommerce）。** [W13] | 原该顾客有订单甲的文件权限；商家在订单下载权限中撤销后，该项授权不再保留。 | 不是删除原订单；也不证明顾客已下载到本机的文件被收回，或所有外部直链均已失效。 |

### 13. 售后与客户服务：申请、授权、实物与钱款各自有结果

| 期望状态 | 期望变化：原情况 → 条件或触发 → 新结果 | 反例与边界 |
| --- | --- | --- |
| **顾客的退货请求已成为待确认的申请（PrestaShop 8）。** [P3] | 原没有本次申请；退货已启用、仍在配置期限内、订单历史满足已付款及已发货标记时，已登录顾客从订单历史选择退回商品与数量并提交，产生 Waiting for confirmation 的申请。 | 单纯咨询“能否退”不是申请；该状态不代表商家同意退货或已退款。 |
| **一份退货授权中只有部分申请商品获准退回（Adobe Commerce）。** [M3] | 原申请待处理；商家允许商品甲、拒绝乙后，可记录 Partially Authorized。 | 全部商品获准不属于“部分授权”；数字、虚拟或礼品卡商品不能直接套用该文档的 RMA 范围。 |
| **商家将退货包裹记录为已收到（PrestaShop 8）。** [P3] | 原申请等待包裹；商家收到后将状态改为 Package received，包裹接收结果被记录。 | 包裹已收到不证明商品可再售，也不证明退款完成。 |
| **订单中存在一笔退款金额记录（WooCommerce）。** [W12] | 原没有该笔退款；商家手动记入 20 元后，订单新增相应退款记录。 | 退款申请不等于已记账；手动记账不能证明支付渠道已经返款。 |
| **兼容支付网关已确认一笔退款成功（WooCommerce）。** [W12] | 原该笔退款尚无成功确认；网关支持该退款方式并处理成功后，订单可形成成功说明。 | 只把订单状态改为 Refunded 不等于完成网关退款；部分与全额也需分别判断。 |
| **顾客消息已保存为商家可查询的客服会话（PrestaShop 8）。** [P4] | 原客服工具中没有本次消息；联系对象开启 Save messages，且顾客提交联系消息后，消息进入客服工具。 | 若该选项未开启，消息可能只发往邮箱，不满足保存在客服工具的状态。 |
| **客服会话可由 Open 改为 Closed（PrestaShop 8）。** [P4] | 原会话 Open；员工将其标为 handled 后，会话变为 Closed。 | 关闭会话不证明订单取消、顾客满意或退款发生；这些不是该会话状态的定义。 |

### 14. 客户身份与关系：账号、游客订单和历史查询

| 期望状态 | 期望变化：原情况 → 条件或触发 → 新结果 | 反例与边界 |
| --- | --- | --- |
| **顾客账号可以在没有订单时存在（WooCommerce）。** [W14] | 原没有账号 U；店铺允许 My Account 注册且顾客完成注册后，可形成尚无订单的 U。 | 未登录访客浏览商品，不等于已经形成注册账号；账号存在也不证明已有成交。 |
| **普通购买可以形成未绑定注册用户账号的游客订单（WooCommerce）。** [W14] | 原访客尚未提交本次订单；在开启游客结算的非订阅购买中，访客提交结算形成游客订单，该订单不必绑定注册账号。 | 订阅购买的账号要求不能由本行否定；之后能否关联账号需另看身份核验规则。 |
| **商家可在某客户详情中查看关联的历史订单（PrestaShop 8）。** [P5] | 原客户 U 无订单甲；U 的购买形成其关联订单甲后，客户详情的订单范围包含甲。此处是文档中关系的归纳。 | 仅因两个访客邮箱相同就合并全部订单，超出了本行的归属依据；历史可查不等于可查看任意顾客资料。 |

### 15. 个人数据与营销订阅：改变字段不等于删除所有副本

| 期望状态 | 期望变化：原情况 → 条件或触发 → 新结果 | 反例与边界 |
| --- | --- | --- |
| **订单个人信息可被匿名化而订单仍保留（WooCommerce）。** [W20] | 原订单含顾客姓名、邮箱等个人字段；已开启批量移除选项时，对选定订单执行移除，相关字段改为文档所示删除占位信息，订单记录仍在。 | 隐藏页面列不等于移除字段；这不证明备份、邮件或外部服务副本均已删除。 |
| **客户的新闻订阅标记可改为未订阅（PrestaShop 8）。** [P5] | 原 U 的 Newsletter 标记为已订阅；商家在客户记录中取消后，该标记为未订阅。 | 仅拥有顾客邮箱或注册账号，不能据此当成已订阅；不推断所有外部发送系统已同步停止发送。 |

### 16. 经营统计：销售口径和日期范围

| 期望状态 | 期望变化：原情况 → 条件或触发 → 新结果 | 反例与边界 |
| --- | --- | --- |
| **净销售额按商品销售额扣除商品退货金额和优惠券折扣计算（WooCommerce Analytics）。** [W15] | 在相同报表范围且数据已更新的例子中，销售额 100、券折扣 10；再计入商品退款 20 后，净销售额由 90 变为 70。 | 不把运费税费加进该净销售额；也不等同于利润、所有退款现金流或银行出款。 |
| **同一订单是否计入某日报表可随日期口径改变（WooCommerce Analytics）。** [W15] | 假设甲 11 月 1 日创建、2 日付款，其他筛选不变；1 日报表从创建日期切换到付款日期后，甲不再落入该日范围。 | 订单没有因此被删除；只把折线图改成柱状图，不是更改日期口径。 |

### 17. 员工权限：查看、编辑与角色归属

| 期望状态 | 期望变化：原情况 → 条件或触发 → 新结果 | 反例与边界 |
| --- | --- | --- |
| **非 SuperAdmin 员工的菜单编辑权限可以未被授予（PrestaShop 8）。** [P7] | 原员工所属配置档没有该菜单的 Edit 权限；有权管理员授予后，该配置档新增编辑权限。 | 只有 View 不等于已有 Edit；不据此宣称现有会话何时刷新，或已验证所有越权路径。 |
| **默认权限配置中的 Shop Manager 具有处理订单退款的能力（WooCommerce）。** [W16] | 在默认角色配置下，原用户仅为 Customer；管理员将其设为 Shop Manager 后，该角色包含退款处理能力。 | 能登录商店不代表可退款；该角色也不等于完整 WordPress Administrator 权限，不推演第三方自定义角色配置。 |

## 这些可能性之间的关系

- **可组合，但不互相代替**：同商家的多店面可以兼售实物与文件；商品是否出现在某店面，与某订单是否已有文件资格，是不同关系。此组合是跨材料归纳，不代表本轮运行过完整配置。[P8][W2][W13]
- **部分发货不是另一种订单**：同一订单可以分别有收款确认、库存预留和部分发运结果；不能让其中一个“完成”标签替代另外两种结果。[W11][M1][M2] 这是对象关系归纳。
- **售后申请不是退款，客服关闭也不是售后结案证明**：申请授权、包裹接收、资金确认分别有判别依据；它们可以先后发生，但本稿没有给出跨产品统一的固定顺序。[P3][M3][W12][P4]
- **客户组优惠不自动变成企业采购平台**：B2C 客户组折扣在本稿范围内；以企业账号、报价与采购审批为中心的经营，需要相邻类型的额外对象。[P6][A1]
- **币种和语言不是跨境责任结论**：配置语言、币种可改变店面体验，不能证明进口义务、关税或跨境售后责任已经被软件处理。[P9][P10][A1]
- **多个店面不等于多个独立卖家**：若商品经营者由自营商家变为入驻的独立卖家，才引入 Marketplace 所关注的卖家归属及平台经济关系；此部分只作边界提示。[P8][A1]

## 未覆盖部分及原因

[覆盖表](COVERAGE.md)已逐域区分三类原因：尚未研究、证据不足、超出本次类型范围。以下缺口尤其不能从现有条目中自行补出：

- **尚未研究**：个性化推荐效果、会员积分与储值、购物车跨设备合并、换货差价与维修保修、运输丢损、利润成本、获客归因及完整审计。
- **证据不足**：通用支付重复通知规则、并发库存竞态、旧游客订单的归属冲突、多渠道订单汇集、退款与下载资格撤销的全部自动联动。已读下载权限文档证明手工撤销可行，没有证明每次退款都自动撤销。
- **超出本次范围**：以多卖家入驻分账、组织采购审批、持续订阅履约承诺为主对象的完整产品模型；它们可与商城组合，但不是本稿已经展开的单商家模型。各地税务义务判定亦未作为软件配置结果来断言。

## 参考依据与研究状态

全部实际依据及来源版本见[研究与双门禁记录](RESEARCH_AND_REVIEW.md)。本轮既新增领域，也新增原始资料；不属于“在完全固定资料上只改写措辞”的实验。

WooCommerce 文档、WooCommerce Product Search/WooPayments 扩展文档、PrestaShop 8 官方文档仓库、PrestaShop 9 搜索文档及 Adobe Commerce 文档各自保留产品边界。Adobe 的 RMA 例子没有写成 Magento Open Source 或所有商城的默认功能。没有实际运行这些产品。

**制品状态：待人工审阅的研究稿。** 覆盖检查和语言复核分别有记录；它们不构成整个软件类型已穷尽、读者理解效果已验证或产品运行验收通过的结论。既有版本与个人任务管理案例保持不变。

[A1]: ../../../application-atlas-production-pack/applications/e-commerce-platform.md
[A2]: ../../../application-atlas-production-pack/research/e-commerce-platform.md
[W1]: https://woocommerce.com/document/woocommerce-product-search/blocks/
[W2]: https://woocommerce.com/document/managing-products/
[W3]: https://woocommerce.com/document/variable-product/
[W4]: https://woocommerce.com/document/product-reviews/
[W5]: https://woocommerce.com/document/coupon-management/
[W6]: https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/cart-block/
[W7]: https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/checkout-block/
[W8]: https://woocommerce.com/document/setting-up-shipping-zones/
[W9]: https://woocommerce.com/document/setting-up-taxes-in-woocommerce/
[W10]: https://woocommerce.com/document/managing-orders/
[W11]: https://woocommerce.com/document/managing-orders/order-statuses/
[W12]: https://woocommerce.com/document/woocommerce-refunds/
[W13]: https://woocommerce.com/document/digital-downloadable-product-handling/
[W14]: https://woocommerce.com/document/configuring-woocommerce-settings/accounts-and-privacy/
[W15]: https://woocommerce.com/document/woocommerce-analytics/
[W16]: https://woocommerce.com/document/roles-capabilities/
[W17]: https://woocommerce.com/document/woopayments/payouts/payout-schedule/
[W18]: https://woocommerce.com/document/woopayments/managing-money/
[W19]: https://woocommerce.com/document/woopayments/fraud-and-disputes/managing-disputes/
[W20]: https://woocommerce.com/document/managing-orders/removing-personal-data-from-orders/
[P1]: https://docs.prestashop-project.org/v.9-documentation/user-guide/configuring-shop/shop-parameters/search/search-parameters.md
[P2]: https://github.com/PrestaShop/user-documentation-v8-en/blob/main/user-guide/selling/managing-orders/shopping-carts.md
[P3]: https://github.com/PrestaShop/user-documentation-v8-en/blob/main/user-guide/selling/managing-customer-service/merchandise-returns.md
[P4]: https://github.com/PrestaShop/user-documentation-v8-en/blob/main/user-guide/selling/managing-customer-service/customer-service.md
[P5]: https://github.com/PrestaShop/user-documentation-v8-en/blob/main/user-guide/selling/managing-customers/your-customers.md
[P6]: https://github.com/PrestaShop/user-documentation-v8-en/blob/main/user-guide/configuring-shop/shop-parameters/customer-settings/groups.md
[P7]: https://github.com/PrestaShop/user-documentation-v8-en/blob/main/user-guide/configuring-shop/advanced-parameters/team/permissions.md
[P8]: https://github.com/PrestaShop/user-documentation-v8-en/blob/main/user-guide/managing-multiple-stores/sample-usages-and-specifics.md
[P9]: https://github.com/PrestaShop/user-documentation-v8-en/blob/main/user-guide/improving-shop/going-international/localization/currencies.md
[P10]: https://github.com/PrestaShop/user-documentation-v8-en/blob/main/user-guide/improving-shop/going-international/localization/languages.md
[M1]: https://experienceleague.adobe.com/en/docs/commerce-admin/inventory/basics/selection-reservations
[M2]: https://experienceleague.adobe.com/en/docs/commerce-admin/inventory/basics/order-status
[M3]: https://experienceleague.adobe.com/en/docs/commerce-admin/stores-sales/order-management/returns/returns
