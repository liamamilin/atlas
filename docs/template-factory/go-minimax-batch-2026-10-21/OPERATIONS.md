# 固定三个叶子的Go辅助批次

在仓库根目录执行：

```sh
python3 examples/assisted-trials/produce_go_batch.py --request docs/template-factory/go-minimax-batch-2026-10-21/BATCH_REQUEST.json
```

流程复用produce_with_opencode.py与produce_batch.py：完整叶子/场景→新会话联网选源→宿主固定真实commit和源码摘要→新会话读固定源码生成认知及验收→格式2完整材料独立复审→七维及每条观察通过→CaseLibrary提交同份研究→export_trial冻结→正式辅助导入→标准开发包实际下载→辅助目录登记。无目标应用执行、无严格发布。

本批只用opencode-go/minimax-m3.1-flash-free，最多9个CLI会话，全部沿原campaign/500台账。register_auxiliary_batch在首次调用前固定请求，reserve事务检查共享9次、模型、身份、并发和单次原8h窗口。稳定phase/identity及每项job标识不会因重启重置。注册不启动时钟，首次真实预留启动8h。

三个叶子/场景/来源线索及正文SHA在BATCH_REQUEST.json，生产顺序固定为个人看板、日常支出、个人日历。每项一个研究/生成/独审会话；失败后不替换样本、不自动补调或修订，其他项继续。--item key仅用于核对/复用该项，不提供新的调用资格。未知/失败启动默认停止该项；完整交付可从原返回恢复，绝不删除LAUNCH_INTENT、FAILURE或旧审阅。

每项的SOURCE_PIN、source-snapshot、calls及audit保留固定来源、实际session和原始返回；audit为普通文件，嵌套私有.git不提交。成功项的MODEL_PRODUCTION/IMPORT_RECEIPT绑定独立审阅、冻结摘要、案例引用和标准包SHA；失败候选不进入可用目录。

所有模型编写和静态审阅状态与应用运行区分。未运行生成probe、未安装/运行上游；程序只做AST解析及独立静态审阅。本批不开发应用。
