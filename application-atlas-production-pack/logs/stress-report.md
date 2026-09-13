# 合成压力测试报告 (U3b)

- 样本: 1804 (每叶 1 个合成场景, mimo-v2.5 生成 → qwen3.8-flash 回分类)
- 整体往返准确率: **85.6%** (闸门时盲测为 94.2%, 差距=全谱系难度 vs 简单盲测)
- 错误 260: 边界混淆 168 | 完全偏移 92 | 调用异常 0

## 边界混淆 TOP 25 (真类型 → 被误判为邻居类型, 语料需强化分界)
| 真类型 | 误判为 | 次数 | 已有区分文本? |
|---|---|---|---|
| email-collaboration-application | shared-mailbox-application | 1 | 有 |
| instant-messaging-application | team-messaging-application | 1 | 有 |
| customer-to-business-messaging-application | customer-service-platform | 1 | 有 |
| business-messaging-application | customer-service-platform | 1 | 有 |
| social-profile-network | creator-storefront | 1 | **缺** |
| softphone-application | internet-calling-application | 1 | 有 |
| video-conferencing-application | virtual-meeting-platform | 1 | 有 |
| private-community-platform | employee-onboarding-platform | 1 | **缺** |
| web-browser | academic-paper-reader | 1 | **缺** |
| discussion-board | online-forum | 1 | 有 |
| knowledge-question-answering-application | self-service-support-portal | 1 | **缺** |
| vertical-search-engine | job-board | 1 | 有 |
| answer-engine | academic-search-engine | 1 | 有 |
| help-center | self-service-support-portal | 1 | 有 |
| blogging-platform | note-taking-application | 1 | **缺** |
| product-documentation-portal | help-center | 1 | 有 |
| listings-platform | property-listing-platform | 1 | 有 |
| personal-knowledge-management-application | ai-research-assistant | 1 | **缺** |
| note-taking-application | care-plan-management | 1 | **缺** |
| outliner | product-roadmap-application | 1 | **缺** |
| content-aggregator | personalized-news-feed | 1 | **缺** |
| structured-table-lightweight-database-application | personal-organizer | 1 | **缺** |
| collaborative-spreadsheet | budgeting-forecasting-platform | 1 | **缺** |
| online-form-builder | questionnaire-application | 1 | 有 |
| work-management-platform | content-planning-platform | 1 | **缺** |

## 完全偏移 TOP 20 (误判为非邻居, 检索池召回问题或定义误导)
| 真类型 | 误判为 | 次数 |
|---|---|---|
| social-profile-network | creator-storefront | 1 |
| private-community-platform | employee-onboarding-platform | 1 |
| web-browser | academic-paper-reader | 1 |
| knowledge-question-answering-application | self-service-support-portal | 1 |
| blogging-platform | note-taking-application | 1 |
| personal-knowledge-management-application | ai-research-assistant | 1 |
| note-taking-application | care-plan-management | 1 |
| outliner | product-roadmap-application | 1 |
| structured-table-lightweight-database-application | personal-organizer | 1 |
| collaborative-spreadsheet | budgeting-forecasting-platform | 1 |
| work-management-platform | content-planning-platform | 1 |
| life-planning-application | endurance-training-platform | 1 |
| team-workspace-platform | collaborative-design-platform | 1 |
| mobile-commerce-application | on-demand-delivery-platform | 1 |
| retail-merchandising-platform | supplier-commerce-network | 1 |
| digital-goods-store | e-book-library-application | 1 |
| b2b-e-commerce-platform | purchase-order-management | 1 |
| seller-portal | online-marketplace | 1 |
| contract-to-order-platform | procure-to-pay-platform | 1 |

## 各域准确率 (低于 55% 的域)

## 高频失败叶子 TOP 20 (语料质量改进优先级)
- **email-collaboration-application** (邮件协作应用) 失败 1 次 → 常被吸到 `shared-mailbox-application`
- **instant-messaging-application** (即时通讯应用) 失败 1 次 → 常被吸到 `team-messaging-application`
- **customer-to-business-messaging-application** (客户对企业消息应用) 失败 1 次 → 常被吸到 `customer-service-platform`
- **business-messaging-application** (商业消息应用) 失败 1 次 → 常被吸到 `customer-service-platform`
- **social-profile-network** (社交档案网络) 失败 1 次 → 常被吸到 `creator-storefront`
- **softphone-application** (软电话应用) 失败 1 次 → 常被吸到 `internet-calling-application`
- **video-conferencing-application** (视频会议应用) 失败 1 次 → 常被吸到 `virtual-meeting-platform`
- **private-community-platform** (私有社区平台) 失败 1 次 → 常被吸到 `employee-onboarding-platform`
- **web-browser** (浏览器) 失败 1 次 → 常被吸到 `academic-paper-reader`
- **discussion-board** (论坛) 失败 1 次 → 常被吸到 `online-forum`
- **knowledge-question-answering-application** (知识问答系统（KQA）) 失败 1 次 → 常被吸到 `self-service-support-portal`
- **vertical-search-engine** (垂直搜索引擎) 失败 1 次 → 常被吸到 `job-board`
- **answer-engine** (问答引擎) 失败 1 次 → 常被吸到 `academic-search-engine`
- **help-center** (帮助中心) 失败 1 次 → 常被吸到 `self-service-support-portal`
- **blogging-platform** (博客平台) 失败 1 次 → 常被吸到 `note-taking-application`
- **product-documentation-portal** (产品文档门户) 失败 1 次 → 常被吸到 `help-center`
- **listings-platform** (列表平台) 失败 1 次 → 常被吸到 `property-listing-platform`
- **personal-knowledge-management-application** (个人知识管理应用) 失败 1 次 → 常被吸到 `ai-research-assistant`
- **note-taking-application** (笔记应用) 失败 1 次 → 常被吸到 `care-plan-management`
- **outliner** (大纲工具) 失败 1 次 → 常被吸到 `product-roadmap-application`