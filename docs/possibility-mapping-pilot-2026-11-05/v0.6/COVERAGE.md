# 商家卖给个人顾客的网上商城 · 领域覆盖与遗漏（v0.6）

本页先说明研究涉及什么，再由[图谱正文](e-commerce-platform.md)说明状态与变化。范围是一家商家面向个人顾客销售；只改写 v0.5 的表达，不用减少领域来换取易读。

“已保留”指正文给出具体结果及其形成或改变的条件，不表示整个领域已经研究完。领域 1—17 对应正文的编号段落，领域 18 在开头的店铺形态概览中呈现。领域划分只为发现遗漏，不增加核心概念。

| 领域 | 正文已保留的内容 | 仍未回答的问题及原因 | 依据 |
| --- | --- | --- | --- |
| 1. 顾客找商品 | 错拼仍按指定词搜索；只看匹配蓝色条件的商品 | 尚未研究：推荐是否适合顾客、搜索改动是否真的让人更容易找到想买的东西。 | [P1][W1] |
| 2. 颜色尺码、价格和评论 | 具体颜色尺码的价格；没货时是否先接单；人工审核评论 | 尚未研究：组合套装、商品资料改版历史、图片等材料的使用权。 | [W3][W4] |
| 3. 价格优惠 | 达到金额门槛用券；一类顾客统一打折 | 证据不足：多个优惠同时满足时的一般优先规则。尚未研究：积分如何获得、使用；预存的钱如何消费、退回。 | [W5][P6] |
| 4. 顾客还没提交的待买商品 | 改变购物车数量；商家查看未变成订单的记录 | 尚未研究：手机和电脑的待买清单如何合并、多久失效、何时提醒未完成购买的顾客。 | [W6][P2] |
| 5. 提交购买前的核对和条件 | 列出本次商品；要求顾客确认条款 | 证据不足：每种资料如何核验、顾客重复提交或多人同时提交时如何处理。 | [W7][W10][W11] |
| 6. 送货方式和费用 | 按地址匹配范围，改变可选送货方式 | 尚未研究：运输公司即时费用、多个包裹合发、自提身份核验、能否按承诺日期送达。 | [W8] |
| 7. 价格中的税款 | 说明价格是否含税；按配置地址和税率计算 | 尚未研究：多层税如何计算、小数金额怎样取整。现实中应纳多少税、如何申报，超出本次软件配置研究范围。 | [W9] |
| 8. 正式订单和取消 | 提交前的临时记录与正式购买区分；取消记录 | 尚未研究：付款后修改购买、拆开或合并订单、销售单据更正。证据不足：汇集不同销售渠道订单的完整规则。 | [W10][W11] |
| 9. 顾客付款、商家收钱和扣款异议 | 收款确认；可安排转给商家的余额；转账在途；银行审查异议 | 尚未研究：与银行每条入账核对、分期付款。证据不足：如何判断和拦截可疑付款的内部规则。 | [W11][W17][W18][W19] |
| 10. 留货数量和仓库数量 | 下单后留出数量；取消后恢复可接单数量；发货后扣仓库数量 | 证据不足：多个订单同时抢最后一件货、服务故障后如何修复不一致的数量。 | [M1][M2] |
| 11. 发出实物 | 一笔订单分批发；从不同存货地点发 | 尚未研究：顾客签收、包裹丢失、补寄、仓库内怎样拣选和包装。 | [M1][M2][M4] |
| 12. 交付下载文件 | 付款后或订单标为完成后给予文件资格；单独撤销 | 证据不足：每种退款是否自动取消文件资格、存放在别处的文件网址能否阻止继续访问。 | [W13] |
| 13. 退货、退款和客服联系 | 申请退哪些商品；部分批准；接收包裹；登记退款与服务确认退款；保存和结束消息处理 | 尚未研究：换货补差价、维修保修、拒绝退货后的申诉。 | [P3][M3][W12][P4] |
| 14. 账号和过去的购买 | 没有购买的账号；免注册购买；商家查某位顾客的订单 | 证据不足：重复账号如何合并、历史免注册购买应归给哪个账号。相同邮箱不能单独证明归属。 | [W14][P5] |
| 15. 个人资料和营销消息 | 订单保留而个人内容移除；取消客户记录的订阅标记 | 尚未研究：备份和外部服务如何一起删除个人资料、取消标记后各个发信工具如何停止发送。 | [W20][P5] |
| 16. 销售金额报表 | 商品销售额扣退款与优惠；按创建日或付款日分组 | 尚未研究：进货等成本、利润、顾客从哪里被吸引来、如何汇总一段时期的财务账目。不能用销售额代替它们。 | [W15] |
| 17. 员工可做哪些操作 | 查看和修改许可分开；默认店铺经理的退款权限 | 尚未研究：改权限后已登录员工何时受影响、谁何时改过什么的记录、员工能看哪些顾客的数据。 | [P7][W16] |
| 18. 同一商家的店铺形态 | 兼售纸书与文件；不同网站的商品展示；可选语言和货币 | 尚未研究：两网站价格如何同步、缺少翻译时显示什么、小数换算取整。证据不足：汇集多个销售渠道。以独立卖家、企业采购或周期购买为中心的完整产品超出本轮范围。 | [W2][W13][P8][P9][P10] |

## 三种遗漏原因不能互相代替

- **尚未研究**：还没调查对应机制；例如换货和利润仍可能属于商城，不能说它们不存在。
- **证据不足**：读过相关材料，但条件或结果仍不够明确；例如同时下单、外部文件访问，不能补出一个通用保证。
- **超出本次范围**：主要研究对象换了；例如从一家商家卖货转为许多独立卖家入驻，需要另研究商品属于谁、平台向谁收钱、款项如何分给各卖家。[A1]

因此，给一类个人顾客打折可以放在本稿，企业如何分派采购人、提交报价和审批则未展开。显示不同货币可以放在本稿，商品过境时谁承担关税不能由换算显示金额推出。

## 覆盖检查结果

本轮没有删除上一版的主要领域或把未研究内容改称“不支持”。保留不同产品和版本的资料，不用某一个产品的默认功能定义全部商城。覆盖与语言、可理解性分别检查，记录见[三项门禁审查](READABILITY_REVIEW.md)；不以条目数量判定认知质量，也不宣称整个类型已经梳理完成。

[A1]: ../../../application-atlas-production-pack/applications/e-commerce-platform.md
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
[M4]: https://experienceleague.adobe.com/en/docs/commerce-admin/stores-sales/order-management/invoices
