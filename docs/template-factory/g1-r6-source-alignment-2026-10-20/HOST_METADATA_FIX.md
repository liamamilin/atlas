# 聚合程序清单与生成元数据的宿主修复

本轮真实 R6 在源码 `2b40dff20bc2761be649bc3ce43b825094bf075c` 上完成六新预审、九程序继承和渲染后，聚合审阅记录 `scope_fidelity=uncertain`：输入的程序哈希清单包含生成的 `acceptance/plan.json`，但该文件不在提供给审阅者的程序目录及 exact program diff 中。

修复后的 prepared 路径使用正式 effective_plan.file_plan 定义交付程序集合；R6 同时要求与已验证九项 manifest 完全一致。程序哈希和程序差分不再混入生成 plan 元数据。`acceptance/plan.json` 另列为 host-generated-acceptance-plan-metadata，提供 before/after 字节哈希、是否变化、真实 unified diff 及审阅材料路径；实际文件复制到 baseline/candidate 的 generated-metadata/ 下。元数据记录摘要进入聚合 diff 身份，审阅提示明确要求单独审阅其内容，不隐藏变化。

正向 V1 回归确认程序清单恰好九项，元数据不是程序，且提供的元数据文件与记录的哈希一致。94 项定向测试、编译和 diff check 通过；新源码完整13组及远端CI另外记录。

独立 Sol 复核确认无新增兼容问题：unprepared fallback 新增的文件同时存在检查符合既有 contract_scope.validate_repair_diff 的 add/delete 禁止合同；未放宽语义门禁。

**本修复没有修改本轮真实任务、候选、九程序、审阅输入、报告或检查点，也没有重新调用模型。** 原聚合审阅仍然 blocked：A02 JSON 单标签正向及 A07 搜索排除两项程序覆盖缺口独立存在。本修复不能解除这两个业务阻断，不能据此重跑同一输入换取通过，也不提供第七轮修复或新窗口。
