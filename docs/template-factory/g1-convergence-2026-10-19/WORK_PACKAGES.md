# G1 收敛续作工作包

实际起点9eb88db，初始工作区干净，原停止样例不覆盖。授权只对原书签产品增加2轮（累计4），一次G1补充窗口在全部前置修复和同一新SHA远端CI通过后激活；全局500和其他产品2轮不变。

| 包 | 范围 | 证据/状态 |
|---|---|---|
| C01 | 现场与远端CI浅历史修复 | 96fb75b同SHA实际远端两job全通过；ci-history-fix-*.log。checkout完整历史，不删断言；这仅是起点CI修复，不能代替最终新代码CI |
| C02 | 统一规则、CONTRACT_COVERAGE、REPAIR_SCOPE、目标适配/URL政策 | 源码和聚合请求已冻结；83项聚焦检查通过。固定旧案例29观察与casebasis；scope fd3746…，仅A02单标签例负转正，其他断言意图保留 |
| C03 | 真UI操作与负控、独立执行器边界 | 真Chromium两负控、23执行器合同fixture及helper通过；原machineplan/网络none/receipt机制保留。仅准备证据，不是实际应用运行 |
| C04 | append-only授权、有效限额/窗口、原子取代和正式恢复 | 32项预算/真实临时库恢复测试通过；scope、旧job/candidate和checkpoint固定，过期/失败回滚；实际授权已登记并于1792408423.754534激活，详见amendment-response/resume-response |
| C05 | 独立代码审查、本地完整检查、同新SHA远端完整CI | 已通过：verification/final-2完整13项全过且source无漂移；566后端/8可选skip、9web单元、17默认E2E、27工厂E2E、20严格Docker/0skip。fc7e50b4656d4f07e5af65551b9d9e3ea542ef93远端39242394654两job全部step success，含独立Chromium负控；日志见ci-convergence-* |
| C06 | 聚合修订、冻结、独立审阅、发布、标准包真实消费、P0/phase proof/宿主G1 | 已通过正式register/resume启动；amendment-response/resume-response及budget-after-resume保留。第3轮修复，job_a53c47f3694047489c4f82cfc2e346be；窗口截止2026-10-20 03:13:43+08:00。实际case-adaptation完成；blueprint-generate-0交付成功但返回外层coverage触发宿主格式错误。44次CLI/3次修复，已正式暂停plan，保留raw/summary/input与budget；正在修复窄型无损兼容和同job已交付结果恢复。尚无新模板/P0/G1通过 |
| C07 | 原三场景T08实际生产/开发/抽验 | G1通过后直接执行，固定分母3不替换 |
| C08 | 代码阶段推送、证据/失败/恢复/下一批建议 | 随步骤记录；不自动扩大范围或额度 |

合成/fixture/真实Docker基础路径与真实模型应用分开记录。任何累计上限/有效窗口/外部阻塞留正式停止状态，禁止伪造通过。

协议恢复与旧任务重试fence的最终本地检查：`verification/recovery-fenced-final/checks.json`，13项全部通过，源码摘要c5084b5b37c04b32ff0b218c5b08d4484ad8dc00675b918ccbe4883683ad1ae2，执行期间无漂移；571后端/8可选skip、9web单元、17默认E2E、27工厂E2E、20严格Docker/0skip。此前protocol-recovery的2项夹具失败及protocol-recovery-final的旧源码通过均保留。当前准备提交并核对新SHA远端结果，生产仍暂停。
