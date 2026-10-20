# R7 工作包与验收对照

授权：authorization/ATLAS_G1_R7_ACCEPTANCE_ALIGNMENT_CODEX_INSTRUCTIONS.txt（原字节）；SHA256 5fb0792b769739f070f68af6ea196473671c791cd895989026ebf9520e282562。
基线：2807362d804ba95dc7671b4ab250b8b6fa420456；正式现场见 BASELINE.json / baseline-state.json。

| 工作包 | 完成条件 | 证据入口 | 状态 |
|---|---|---|---|
| W1 基线与授权 | 原job/71调用/6修复/grant1/截止一致，保护历史 | BASELINE.json、authorization/ | 已核对 |
| W2 确定补丁 | A02/A07/A11、四replace五reuse、限定spec/choices与双基线 | build_patch.py、patch.json、prepared-programs/、*.diff | 已制作，等待宿主完整验证 |
| W3 宿主准备与恢复 | v3准备、V4继承deadline、原子唯一后继、幂等/回滚 | 正式源码及定向测试、准备/登记/入队回执 | 开发中 |
| W4 验证门禁 | 正负fixture、独立审查、完整13组及精确SHA远端CI | verification/、独立报告 | 进行中 |
| W5 真实候选与目录 | 六项新预审、author0、聚合、冻结后审阅、正式发布 | 原任务后继/真实检查点与报告 | 未运行 |
| W6 真实P0与G1 | 标准交接消费、首次P0、冻结套件、独立浏览器、phase proof、宿主评估 | 正式开发/运行任务与G1_ASSESSMENT | 未运行 |
| W7 T08 | 仅G1正式通过后原固定三场景 | 原T08固定清单与报告 | 未运行 |

预算不变项：campaign CLI 500；旧grant1/1；旧普通追加2+grant1历史行全部保留。仅本产品业务修复6→7，绝对截止1792495312.855422，不能延期。模板author调用为0；第七轮之后不能修P0业务问题。fixture不计真实产品，不替代实际运行证据。
