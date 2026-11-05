# B2C 电商商城 · 研究与双门禁记录（v0.5）

研究日期：2026-11-05；技能提交：`59c4fc4`。本记录随[领域覆盖表](COVERAGE.md)、[状态与变化正文](e-commerce-platform.md)一起阅读。

## 本轮研究范围与资料条件

先对照 ATLAS 类型正文、研究笔记及本地目录的真实项目关联识别主要领域，再补读各领域官方操作资料，最后生成状态与变化并逐条复核语言。领域分组服务于发现遗漏，不增加核心概念。个人任务管理及 v0.1—v0.4 样本保留。

PrestaShop 是只读查询确认的本叶子关联项目；查询时记录的 README blob 为 `dc9da0328582549d48ae22bf7f84cbd225c99724`。本轮没有确认 WooCommerce 或 Magento2 在目录中的直接叶子关联，使用的是其官方产品资料，不把“参考资料”写成“已关联项目”。

本轮新读了三个产品体系的相关资料，所以不能把与 v0.4 的全部差异归因于技能变化。材料证明文档中描述的行为；没有安装运行参考产品、验证店铺配置或测量读者认知效果。

若干 PrestaShop 9 GitBook 页面未能读取，相应主题改读官方版本 8 文档仓库。正文逐处标为版本 8；只有搜索别名条目采用实际读到的版本 9 页面。未将失败页面列为已读证据。下面只说明实际阅读的相关部分，不声称逐字读完所有页面。外部全文未归档；版本 8 文件的 blob 校验标识和稳定 API 地址记录在 [INPUTS.json](INPUTS.json)。

## 实际阅读依据

| 编号 | 官方资料或本地资料 | 本轮阅读范围 |
| --- | --- | --- |
| A1 | [ATLAS E-commerce Platform](../../../application-atlas-production-pack/applications/e-commerce-platform.md) | 类型范围、能力与相邻类型 |
| A2 | [ATLAS E-commerce Platform research](../../../application-atlas-production-pack/research/e-commerce-platform.md) | 现有类型研究线索 |
| W1 | [WooCommerce Product Search blocks](https://woocommerce.com/document/woocommerce-product-search/blocks/) | 商品属性筛选；扩展 |
| W2 | [WooCommerce Adding and Managing Products](https://woocommerce.com/document/managing-products/) | 商品类型 |
| W3 | [WooCommerce Variable Products](https://woocommerce.com/document/variable-product/) | 规格价格、库存与缺货预订 |
| W4 | [WooCommerce Product Reviews](https://woocommerce.com/document/product-reviews/) | 评论审核 |
| W5 | [WooCommerce Managing Coupons](https://woocommerce.com/document/coupon-management/) | 优惠券限制与金额 |
| W6 | [WooCommerce Cart block](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/cart-block/) | 购物车修改 |
| W7 | [WooCommerce Checkout block](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/checkout-block/) | 结算摘要与条款 |
| W8 | [WooCommerce Shipping zones](https://woocommerce.com/document/setting-up-shipping-zones/) | 配送区域 |
| W9 | [WooCommerce Taxes](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/) | 税费计算设置 |
| W10 | [WooCommerce Managing orders](https://woocommerce.com/document/managing-orders/) | 订单记录 |
| W11 | [WooCommerce Order statuses](https://woocommerce.com/document/managing-orders/order-statuses/) | 订单与付款状态 |
| W12 | [WooCommerce Refunding orders](https://woocommerce.com/document/woocommerce-refunds/) | 退款记账与网关退款 |
| W13 | [WooCommerce Digital/Downloadable Product Guide](https://woocommerce.com/document/digital-downloadable-product-handling/) | 授权时点与撤销 |
| W14 | [WooCommerce Accounts and Privacy Settings](https://woocommerce.com/document/configuring-woocommerce-settings/accounts-and-privacy/) | 账号、游客与数据选项 |
| W15 | [WooCommerce Analytics and Sales Reports](https://woocommerce.com/document/woocommerce-analytics/) | 统计定义与日期口径 |
| W16 | [WooCommerce Roles and Capabilities](https://woocommerce.com/document/roles-capabilities/) | 默认角色权限 |
| W17 | [WooPayments Payout schedule](https://woocommerce.com/document/woopayments/payouts/payout-schedule/) | 待结算余额与可出款余额 |
| W18 | [WooPayments Managing money](https://woocommerce.com/document/woopayments/managing-money/) | 出款与争议状态 |
| W19 | [WooPayments Managing disputes](https://woocommerce.com/document/woopayments/fraud-and-disputes/managing-disputes/) | 争议提交与发卡行决定 |
| W20 | [WooCommerce Removing personal data from orders](https://woocommerce.com/document/managing-orders/removing-personal-data-from-orders/) | 匿名化而保留订单 |
| P1 | [PrestaShop 9 Search parameters](https://docs.prestashop-project.org/v.9-documentation/user-guide/configuring-shop/shop-parameters/search/search-parameters.md) | 别名与搜索索引 |
| P2 | [PrestaShop 8 Shopping carts](https://github.com/PrestaShop/user-documentation-v8-en/blob/main/user-guide/selling/managing-orders/shopping-carts.md) | 未转订单购物车 |
| P3 | [PrestaShop 8 Merchandise Returns](https://github.com/PrestaShop/user-documentation-v8-en/blob/main/user-guide/selling/managing-customer-service/merchandise-returns.md) | 申请条件与包裹接收 |
| P4 | [PrestaShop 8 Customer Service](https://github.com/PrestaShop/user-documentation-v8-en/blob/main/user-guide/selling/managing-customer-service/customer-service.md) | 消息留存与会话状态 |
| P5 | [PrestaShop 8 Your customers](https://github.com/PrestaShop/user-documentation-v8-en/blob/main/user-guide/selling/managing-customers/your-customers.md) | 客户详情与订阅标记 |
| P6 | [PrestaShop 8 Groups](https://github.com/PrestaShop/user-documentation-v8-en/blob/main/user-guide/configuring-shop/shop-parameters/customer-settings/groups.md) | 客户组折扣 |
| P7 | [PrestaShop 8 Permissions](https://github.com/PrestaShop/user-documentation-v8-en/blob/main/user-guide/configuring-shop/advanced-parameters/team/permissions.md) | 查看/编辑权限 |
| P8 | [PrestaShop 8 Multistore sample usages](https://github.com/PrestaShop/user-documentation-v8-en/blob/main/user-guide/managing-multiple-stores/sample-usages-and-specifics.md) | 店面关联 |
| P9 | [PrestaShop 8 Currencies](https://github.com/PrestaShop/user-documentation-v8-en/blob/main/user-guide/improving-shop/going-international/localization/currencies.md) | 币种配置与换算 |
| P10 | [PrestaShop 8 Languages](https://github.com/PrestaShop/user-documentation-v8-en/blob/main/user-guide/improving-shop/going-international/localization/languages.md) | 启用语言与前台选择 |
| M1 | [Adobe Commerce Source algorithms and reservations](https://experienceleague.adobe.com/en/docs/commerce-admin/inventory/basics/selection-reservations) | 下单预留、取消补偿与多源发运 |
| M2 | [Adobe Commerce Order status and reservations](https://experienceleague.adobe.com/en/docs/commerce-admin/inventory/basics/order-status) | 源库存扣减与部分发运 |
| M3 | [Adobe Commerce Returns](https://experienceleague.adobe.com/en/docs/commerce-admin/stores-sales/order-management/returns/returns) | RMA 部分授权及产品范围 |

## 认知覆盖门禁：单独验收

**作者检查结果：通过本轮主要领域核查，仍为待人工审阅的研究稿。** 通过指覆盖表中每个主要领域均有正文内容或明确缺口，不指所有领域均已充分研究，也不指整个类型已完成。

- 从商品发现到交付、售后，再到经营、权限与整体形态逐项对照；覆盖表的“已展开”只列正文实际表达的机制，已删去未展开的“移除商品”“叠加限制”等表述。
- 不能让商品、订单和付款几个容易描述的状态替代其他主要领域。因此补入客服留存、个人数据、组优惠、经营日期口径、多源发运与下载权限等不同对象的结果。
- 交叉使用 WooCommerce、PrestaShop 与 Adobe Commerce，保留扩展、版本与产品范围；例如 Adobe Commerce 的 RMA 没有归给所有 Magento Open Source 安装。
- [覆盖表](COVERAGE.md)逐域保留三种缺口原因。推荐、积分储值、换货、运输丢损、成本利润等属于尚未研究；并发竞态、身份冲突和外部联动属于证据不足；卖家入驻分账为中心的市场、组织采购为中心的 B2B 等属于本轮类型边界之外。前两类不能改成“不支持”。
- 为什么纳入客户组优惠而未展开 B2B：前者改变本商城顾客价格，后者增加采购组织、报价和审批对象。为什么纳入显示币种而未研究跨境责任：前者是金额表示的配置，后者不能由显示外币推出。

这些判断针对领域及遗漏的性质，不按下方状态行数、篇幅或来源数计分。运输签收、换货、利润等缺口仍足以影响某些具体商城的理解，不能用本轮已有内容抵消。

## 语言精确性门禁：逐条复核

**作者检查结果：保留条目通过本轮语言复核。** 检查对象包括全部状态及对应变化、概览、标题、覆盖表与关系段落。使用“所指—单一主张—可观察例—变化前后—近似反例—证据范围”逐项追问；下表列出每一行的实际复核点，没有以抽样代替逐条检查。

金额与库存例子是给定条件下的判别用例，未冒充店铺实测。跨资料组合、结算摘要和客户订单关系明确标为归纳。状态可以被形成、改变或终止，不强制每项都对应一个通用状态码。

### 状态与变化逐行记录

“位置”是当前正文行号，仅用于复查定位。每条同时检查相应变化和第三列反例；以下数量仅用于防止漏检。

| 位置／领域 | 当前核心状态原文 | 复核要点 |
| --- | --- | --- |
| 正文 19／领域 18 | 同一商城的可售目录中含实体书和下载电子书。 | 可售实体书目录新增可购买文件商品；免费附件与顾客个人授权分别作反例，组合明确标为归纳。 |
| 正文 20／领域 18 | 同一商家的商品 P 在店面甲的分类 C 中出现，在店面乙的分类 C 中不出现（PrestaShop 8）。 | 变化对象是 P 与店面甲分类的关联；两店都有 C 不推出两店都有 P，保留版本 8 条件。 |
| 正文 21／领域 18 | 顾客可切换到商城已启用的第二种前台语言（PrestaShop 8）。 | 从一种可选语言到第二种已启用语言；未启用与全量翻译分别作为判别边界。 |
| 正文 22／领域 18 | 商品金额可按店铺配置汇率显示为另一已启用币种（PrestaShop 8）。 | 基础币种金额 100 经配置率 2 换为 200；明确是显示金额，非符号替换或银行汇率。 |
| 正文 32／领域 1 | 已配置的搜索别名按目标词查找已索引商品（PrestaShop 9 文档情形）。 | 别名保存前后可比较，目标词及商品已索引是明确条件；不保证无匹配时仍产生结果。 |
| 正文 33／领域 1 | 只选蓝色属性条件时，结果集合仅列出匹配该条件的商品（WooCommerce Product Search 扩展）。 | 筛选改变商品集合；蓝色属性匹配不证明蓝色变体有现货，并署名扩展。 |
| 正文 39／领域 2 | 一个商品变体有自己的售价（WooCommerce）。 | 同一变体实际售价从 100 到 120；描述文本改价不能满足。 |
| 正文 40／领域 2 | 已发布且有价格的变体，允许缺货预订时可在零库存下接受订购（WooCommerce）。 | 已发布、有价格、启用变体库存管理和缺货预订共同限定零库存可订情形；未声称其他结算条件解除。 |
| 正文 41／领域 2 | 一条商品评论的审核状态为已批准（WooCommerce）。 | 人工审核条件下从待审核到 Approve；五星评价不代替审核结果。 |
| 正文 49／领域 3 | 满足优惠券配置条件的购物车获得该券的折扣（WooCommerce）。 | 有效且未耗尽、仅最低小计限制、无运税和其他优惠的例子，90 到 110 使券条件成立。 |
| 正文 50／领域 3 | 客户的商品报价采用其客户组折扣（PrestaShop 8）。 | 仅一组、无其他优惠、未税基数使 100 到 90 可判别；不推演多组叠加。 |
| 正文 56／领域 4 | 购物车中商品甲的购买数量已更新（WooCommerce Cart block）。 | 购物车接受修改后数量 1 到 2；页面文字和正式订单不混同。 |
| 正文 57／领域 4 | 商家可查看尚未转换为正式订单的购物车（PrestaShop 8）。 | 新增未转订单购物车记录可观察；没有把这一记录说成顾客主观放弃。 |
| 正文 63／领域 5 | 结算页的订单摘要列出本次购买的商品（WooCommerce Checkout block 的文档归纳）。 | 进入结算后摘要列出本次商品；静态广告与已付款均不能替代此状态。 |
| 正文 64／领域 5 | 开启 Require Checkbox 时，未勾选条款确认的顾客不能继续提交结算（WooCommerce）。 | 开启 Require Checkbox 后，勾选只改变该项满足情况；不扩大为全部提交条件通过。 |
| 正文 70／领域 6 | 顾客可见的配送方式来自其地址首个匹配的配送区域（WooCommerce）。 | 地址由区域甲改为只匹配乙，按首个匹配区域改变可选方式；非所有方式并集。 |
| 正文 76／领域 7 | 商品税额由店铺选定的计税地址及匹配规则计算（WooCommerce）。 | 收货地址、未税基数、无优惠运费及示例税率均明确；不输出任何地区的税务义务。 |
| 正文 82／领域 8 | 商家能够查询顾客已提交的正式订单（WooCommerce）。 | 提交结算形成正式订单才进入可查询情形；临时 Draft 与支付结果各自区分。 |
| 正文 83／领域 8 | 订单已记录为取消（WooCommerce）。 | 管理员取消改变订单状态；拒付、取消与退款没有合并。 |
| 正文 89／领域 9 | 待发实物订单的收款已被商城确认（WooCommerce 文档情形）。 | 将原来的“转入已收款的处理”收窄到待发实物订单的 Processing；确认与授权的区别标为语义归纳。 |
| 正文 90／领域 9 | 交易款项进入可出款余额，但尚未因此成为银行到账款（WooPayments）。 | Pending funds 到 Available funds 是款项可出款状态变化；不承诺银行到账或统一天数。 |
| 正文 91／领域 9 | 一笔出款可被记录为仍在转账途中（WooPayments）。 | 同一笔出款从 Pending 到 In Transit；订单 Paid 不充当银行出款状态。 |
| 正文 92／领域 9 | 支付争议可记录为发卡行审查中的 Under Review（WooPayments）。 | 回应挑战后记录 Under Review；最终 Won/Lost 与提交材料明确分开。 |
| 正文 98／领域 10 | 已提交订单的预留减少该库存范围内的可售数量（Adobe Commerce）。 | 零阈值、无其他预留条件下 10 到 8 为可售量变化；仓库实际数量不是该例的变化对象。 |
| 正文 99／领域 10 | 取消尚未发货的预留数量会释放相应可售量（Adobe Commerce）。 | 只取消未发的预留数量，说明对应补偿释放；不推算其他变动后的库存总值。 |
| 正文 100／领域 10 | 实物发货减少实际发货库存源的商品数量（Adobe Commerce）。 | 单库存源且无其他变化时，实际发 2 件使 10 到 8；下单不充当实际出库。 |
| 正文 106／领域 11 | 订单可以只有部分商品数量被记录为已发货（Adobe Commerce）。 | 四件订单先发两件仍有两件未发；发货记录不证明承运签收。 |
| 正文 107／领域 11 | 同一订单含不同库存源的发运记录（Adobe Commerce）。 | 已开票四件、甲乙可发数量和原无发运记录均已说明；两个源的发运记录区别于备注。 |
| 正文 113／领域 12 | 开启付款后授权时，顾客可在订单 Processing 阶段获得所购文件资格（WooCommerce）。 | 开启付款后授权限定 Processing 授权；关闭时等待 Completed，不把所有付款当成下载授权。 |
| 正文 114／领域 12 | 某订单中的文件下载资格可被商家单独撤销（WooCommerce）。 | 变化对象是订单甲的文件资格；未声称删除订单、收回本机文件或禁用所有直链。 |
| 正文 120／领域 13 | 顾客的退货请求已成为待确认的申请（PrestaShop 8）。 | 补全原无申请；启用退货、期限、付款和发货历史标记、登录及提交选择共同限定申请形成。 |
| 正文 121／领域 13 | 一份退货授权中只有部分申请商品获准退回（Adobe Commerce）。 | 甲允许乙拒绝才是 Partially Authorized；全批授权反驳该状态，且保留 Adobe RMA 商品范围。 |
| 正文 122／领域 13 | 商家将退货包裹记录为已收到（PrestaShop 8）。 | 实际收到后记录 Package received；没有推出质检、可再售或退款完成。 |
| 正文 123／领域 13 | 订单中存在一笔退款金额记录（WooCommerce）。 | 手动新增 20 元退款记录可观察；退款申请与支付渠道返款都不等于此记录。 |
| 正文 124／领域 13 | 兼容支付网关已确认一笔退款成功（WooCommerce）。 | 网关兼容且处理成功才给出成功说明；状态改为 Refunded 本身不足。 |
| 正文 125／领域 13 | 顾客消息已保存为商家可查询的客服会话（PrestaShop 8）。 | 补全原无本次消息；Save messages 开启时进入客服工具，关闭时邮箱收信是近似反例。 |
| 正文 126／领域 13 | 客服会话可由 Open 改为 Closed（PrestaShop 8）。 | Open 到 Closed 的变化对象仅是会话；顾客满意或订单退款没有由此推出。 |
| 正文 132／领域 14 | 顾客账号可以在没有订单时存在（WooCommerce）。 | 允许注册且完成注册后有无订单账号；浏览访客与成交记录分别区分。 |
| 正文 133／领域 14 | 普通购买可以形成未绑定注册用户账号的游客订单（WooCommerce）。 | 补全原未提交本次订单；非订阅、游客结算开启时形成未绑定注册账号的订单。 |
| 正文 134／领域 14 | 商家可在某客户详情中查看关联的历史订单（PrestaShop 8）。 | 购买使订单甲归属 U 后进入客户详情；关系归纳不扩大为按相同邮箱合并。 |
| 正文 140／领域 15 | 订单个人信息可被匿名化而订单仍保留（WooCommerce）。 | 批量移除条件与字段占位结果明确；订单保留，备份和外部副本不在断言内。 |
| 正文 141／领域 15 | 客户的新闻订阅标记可改为未订阅（PrestaShop 8）。 | 商家取消 Newsletter 改变订阅标记；拥有邮箱不算订阅，外部系统联动未知。 |
| 正文 147／领域 16 | 净销售额按商品销售额扣除商品退货金额和优惠券折扣计算（WooCommerce Analytics）。 | 同一范围、数据已更新时 100−10−20=70；定义限于商品净销售额，排除运税及利润结论。 |
| 正文 148／领域 16 | 同一订单是否计入某日报表可随日期口径改变（WooCommerce Analytics）。 | 同一订单创建日和付款日明确；改变日期口径改变日范围归属，非删除订单。 |
| 正文 154／领域 17 | 非 SuperAdmin 员工的菜单编辑权限可以未被授予（PrestaShop 8）。 | 非 SuperAdmin 配置档由未授予到授予 Edit；View 和既有会话生效时点分别作边界。 |
| 正文 155／领域 17 | 默认权限配置中的 Shop Manager 具有处理订单退款的能力（WooCommerce）。 | 默认角色由 Customer 到 Shop Manager 改变退款能力；没有套用到第三方自定义角色或完整管理员。 |

### 标题、关系和其他核心陈述

| 检查范围 | 复核结果 |
| --- | --- |
| 正文标题、范围及概览标题 | 明示 B2C 单商家与研究稿；概览各行自身给出对象、条件和可观察结果，没有依靠后文补救模糊标题。 |
| 领域 1—17 标题 | 指向具体对象或机制；领域 2 标题已补入缺货预订，领域 9 不把不同的钱款结果合并，领域 10 不把预留与源数量扣减合并。 |
| 覆盖表标题、18 个领域及结论 | “已展开”与“尚未研究／证据不足／超出范围”分别定义；未用字段数量推断认知质量或全类型完成。 |
| 多店面与兼售实物、文件的组合 | 明确是跨材料归纳；店面商品关联与订单下载授权不互相推出。 |
| 部分发货与同一订单的付款、预留关系 | 说明观察对象与尺度；没有用一个“完成”标签覆盖其他结果。 |
| 退货、退款与客服关闭 | 各有判别结果，未编造跨产品统一执行顺序。 |
| 客户组优惠与企业采购边界 | 报价折扣与采购组织、报价审批是不同对象；没有仅凭“会员”一词划分类型。 |
| 语言币种与跨境责任边界 | 可选择语言、换算显示金额有文档依据；未声称法律责任因此被处理。 |
| 多店面与多卖家边界 | 店面数量不决定独立卖家身份，跨入 Marketplace 的条件是经营者与平台关系改变。 |
| 未覆盖部分与研究状态 | 未知没有被写成否定事实；没有宣称参考产品运行验收、人工读者验收或认知效果实验通过。 |

## 两项结论不能相互替代

覆盖表使读者知道本轮触及了哪些领域和还缺什么；逐条语言复核使保留的状态与变化有明确含义。语言清楚不证明无遗漏，领域多也不能替代单条定义准确。两项均是本轮作者复核，制品保持“待人工审阅的研究稿”。没有新增 SOP、开发计划或第三个核心概念。

静态检查只核对引用、文件链接、领域与逐行复核记录的对应关系，以及旧样本字节是否保持；具体结果见 [INPUTS.json](INPUTS.json)。脚本不能代替上述语义判断。
