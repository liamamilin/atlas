# B2C 电商商城 · 主要领域覆盖情况（v0.5）

依据技能提交 `59c4fc4`，先完成本页领域核查，再形成[期望状态与期望变化](e-commerce-platform.md)。研究范围是 ATLAS 的 **E-commerce Platform**（`e-commerce-platform`，05.01），聚焦同一商家面向消费者销售其经营商品；不限定为某个产品的默认功能集。

本轮重新阅读了 WooCommerce 操作文档、PrestaShop 官方文档仓库及 Adobe Commerce 文档。PrestaShop 是本地目录已关联的真实开源项目；其引用明确区分版本 8 文档与版本 9 搜索文档。不同产品的机制分别署名，不合并为一套所有商城必有的规则。领域分组只是查找线索，不是第三个核心概念。

## 主要领域逐项核查

“已展开”表示正文有具名状态、对应变化、判别例及反例，不表示该领域全部机制已经研究完。章节号对应正文同名章节。

| 领域 | 本轮已展开的结果或机制 | 主要依据 | 仍未覆盖的部分及原因 |
| --- | --- | --- | --- |
| 1. 商品发现 | 搜索别名、属性筛选后的结果集合 | PrestaShop 搜索；WooCommerce Product Search 扩展 [P1][W1] | **尚未研究**：个性化推荐排序、搜索实验与效果评估。不能从“能筛选”推出“能找到最合适商品”。 |
| 2. 商品与规格 | 变体售价、缺货预订、评论审核 | WooCommerce 商品、变体、评论文档 [W2][W3][W4] | **尚未研究**：复杂组合商品、商品资料版本、多媒体权利处理。免费附件不等于可售数字商品。 |
| 3. 价格与促销 | 有条件用券、客户组折扣 | WooCommerce 优惠券；PrestaShop 客户组 [W5][P6] | **证据不足**：已读资料不足以给出跨产品统一的多重优惠优先级。会员积分和储值生命周期**尚未研究**。 |
| 4. 购物车 | 改量、识别尚未形成订单的购物车 | WooCommerce Cart block；PrestaShop Shopping carts [W6][P2] | **尚未研究**：跨设备合并、购物车过期和自动挽回投递。未转订单不证明顾客已决定放弃。 |
| 5. 结算提交 | 当前购买摘要、强制条款确认条件；与订单、运税、付款分别关联 | WooCommerce Checkout block [W7][W10][W11] | **证据不足**：所有字段校验、重复提交与并发提交的完整规则。没有仅凭“结算页存在”就判为覆盖完成。 |
| 6. 配送选择与费用 | 地址匹配配送区域后可选方式改变 | WooCommerce Shipping zones [W8] | **尚未研究**：承运商实时报价、多包裹合箱、自提核验和时效承诺。 |
| 7. 税费计算 | 按配置地址和税率计算税额，区分含税与未税价格 | WooCommerce Taxes [W9] | **尚未研究**：复合税与精确舍入边界。各地应税义务与申报判断**超出本次软件状态研究范围**，没有据示例税率作法律结论。 |
| 8. 订单记录 | 购物车或临时草稿与正式订单、取消记录 | WooCommerce Orders 与 Order statuses [W10][W11] | **尚未研究**：修改已支付订单、拆合订单、发票更正。外部全渠道订单汇集的完整规则**证据不足**。 |
| 9. 付款、出款与支付争议 | 收款确认、可出款余额、银行出款状态、争议回应与结果的区别 | WooCommerce 状态；WooPayments 余额、出款、争议文档 [W11][W17][W18][W19] | **尚未研究**：银行账单逐笔对账和分期/先买后付。风险评分、拦截算法细节**证据不足**；不以“属于支付商”将此缺口排除。 |
| 10. 库存占用与实际库存 | 下单预留、取消释放、出库扣减分别改变什么数量 | Adobe Commerce 库存预留与订单文档；WooCommerce 变体文档 [M1][M2][W3] | **证据不足**：故障恢复、并发竞争和所有预留不一致情形；没有把全部加入购物车都写成锁库存。 |
| 11. 实物履约 | 部分发货后仍有未发数量、多库存源发货 | Adobe Commerce Shipments 与 Sources [M1][M2] | **尚未研究**：运输签收、丢件、补寄及仓内拣包作业。系统记为发货不证明顾客已收到。 |
| 12. 数字交付 | 按配置在 Processing 或 Completed 授权、手工撤销资格 | WooCommerce Digital/Downloadable guide [W13] | **证据不足**：退款与授权撤销的全部自动联动、外部文件服务访问控制。数字下载能力不等于服务已经履行。 |
| 13. 售后与客户服务 | 退货申请、部分授权、包裹接收、退款记账与退款确认、客服会话记录 | PrestaShop Returns 与 Customer Service；Adobe RMA；WooCommerce Refunds [P3][P4][M3][W12] | **尚未研究**：换货补差价、维修保修、复杂拒退申诉。将包裹记为收到，不代表已质检、可再售或钱已退回。 |
| 14. 客户身份与关系 | 无订单账号、游客订单、商家侧客户历史订单查询 | WooCommerce Accounts；PrestaShop Customers [W14][P5] | **证据不足**：重复身份合并、旧游客订单归属冲突；不假定邮箱相同即可无条件合并。 |
| 15. 个人数据与营销订阅 | 订单个人信息匿名化、客户订阅标记的改变 | WooCommerce Personal data removal；PrestaShop Customers [W20][P5] | **尚未研究**：备份、日志与第三方服务的数据删除联动、同意撤回后的全部发送渠道。没有将本机字段移除说成全系统删除。 |
| 16. 经营统计 | 净销售额定义、统计日期口径改变样本范围 | WooCommerce Analytics [W15] | **尚未研究**：成本、利润、获客归因和会计结账。销售额不等于利润，也不等于银行到账额。 |
| 17. 员工权限 | 查看与编辑权限分离、商品和退款操作权限的角色边界 | PrestaShop Permissions；WooCommerce Roles [P7][W16] | **尚未研究**：权限变更对已有会话的生效时点、完整审计记录与细粒度数据范围。 |
| 18. 整体经营形态与本地化 | 同商家多店面的商品归属、实物与文件兼售、前台语言、配置币种换算 | PrestaShop Multistore、Languages、Currencies；WooCommerce 产品类型 [P8][P9][P10][W2][W13] | **尚未研究**：跨店价格同步、字段级翻译回退顺序及币种舍入；多渠道订单汇集的完整机制**证据不足**。以多卖家分账、企业采购审批、订阅承诺为主对象的模型**超出本次范围**。 |

## 为什么这些遗漏不能混为“不支持”

- **尚未研究**：该能力仍可能属于商城，例如换货、利润分析；本轮没有继续阅读其机制资料，不能当作不存在。
- **证据不足**：已经看到了相关入口或现象，但没有足够条件支持完整断言，例如支付重复通知和外部订单汇集；正文收窄主张或保留未知。
- **超出本次范围**：研究对象的中心换了，例如独立卖家入驻与平台分账。它可与商城组合，但不拿它填补单商家商城的覆盖成绩。

客户组优惠仍属于本轮价格关系；企业采购的组织账号、报价和审批不因此被一并纳入。币种显示仍属于本轮商城；跨境责任认定不因能显示外币就自动成立。两组区别解释了为什么相关能力一部分被纳入、一部分被明确留白。[ATLAS 类型正文](../../../application-atlas-production-pack/applications/e-commerce-platform.md)

## 覆盖检查结论

本轮已为上述主要领域形成实质内容或明确缺口；跨来源比较没有把 WooCommerce 的默认实现当作类型上限。**不作“整个软件类型已经梳理完成”的结论**，也不以状态数量或来源数量作为覆盖得分。制品仍为待人工审阅的研究稿。

证据页、版本与分开的语言复核结果见[研究与双门禁记录](RESEARCH_AND_REVIEW.md)及[输入记录](INPUTS.json)。语言复核不能代替本页的领域覆盖判断。

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
