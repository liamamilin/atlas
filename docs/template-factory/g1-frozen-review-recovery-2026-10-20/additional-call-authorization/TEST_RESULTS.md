# 最终源码检查结果

源码树摘要：`a6f749d0f3785cd982e432362d735c6574ef414aef6688995169aa994ad9e472`。13组规定检查全部通过，检查前后源码摘要一致。

| 检查 | 结果 | 项数 / 跳过 |
| --- | --- | --- |
| python_audit | passed | — / 0 |
| ruff | passed | — / 0 |
| backend_tests | passed | 729 / 8 |
| atlas_export | passed | — / 0 |
| web_gen | passed | — / 0 |
| web_verify_data | passed | — / 0 |
| npm_audit | passed | — / 0 |
| web_typecheck | passed | — / 0 |
| web_unit | passed | 9 / 0 |
| web_build | passed | — / 0 |
| default_e2e | passed | 17 / 0 |
| factory_e2e | passed | 27 / 0 |
| docker_integration | passed | 20 / 0 |

独立执行器协议fixture：27项通过；其中有效预算合同11项。独立书签行为fixture及真实Chromium负向fixture通过；这是隔离机制测试，不是真实P0应用通过。相关原始日志位于verification/。

本轮新增恢复链5项、旧schema列顺序及迁移3项、CLI绝对截止2项均包含在后端729项中。8项skip是既有默认集成测试跳过，单独Docker门禁20项为0skip。

历史检查记录保留：verification/full-final/各组检查曾通过，但检查中预算输出合同改动导致source_changed=true，不能作为最终门禁；verification/final/因两处旧补证fixture读取真实时钟而在原截止后失败，已仅修复fixture时钟。最终使用verification/verified/，没有修改生产门禁来使旧测试通过。

独立Chromium第一次在沙箱内无法启动，原日志保留为independent-ui-sandbox-denied.txt；正常本地权限下同一fixture通过，见independent-ui.txt。

精确提交远端CI仍需读取真实结果；本文件不声明真实冻结独审、发布、P0、G1或T08已经通过。
