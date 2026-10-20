# R8 工作包与验收对照

本轮依据 authorization/ 下原始附件及用户授权，不重置工作区或生产记录。原 G1 的固定身份及 83/500、7/7 基线见 BASELINE.json；完整只读快照及生产前备份保存在正式根目录 host-evidence/g1-r8-convergence/。

| 工作包 | 交付与验收 | 状态/证据 |
| --- | --- | --- |
| W01 基线与授权 | 附件原字节/SHA、现有 blocked 独审、固定计划/案例/场景、调用与修复、备份 | 已核：factory82 + external1，active0；授权 RECORD.json；T08 无执行记录 |
| W02 精确内容 | 两个 authored 字段允许项、四replace/五reuse、九文件清单、八建议/六关系、精确既有断言映射 | 已准备并只读校验；prepared-programs/、patch.json、program-manifest.json、PROGRAM_CONSISTENCY.md；最终14项程序/加载隔离负控通过，非真实P0 |
| W03 正式修订 | 复用 prepare-revision/预算修订/resume-product；精确版本与有效独审基线、唯一后继、幂等/冲突/回滚；author0 | 已实现；CONTRACTS.md；6项真实 prepare/register/resume 联合fixture通过（CI边界替身），含回滚/并发重放；未激活生产 |
| W04 时间与计账 | 明确替代旧时间来源，正式激活后24小时，不提前/重复计时；external1独立计数；T08首次8小时隔离 | 已实现；预算与执行器11项回归通过；83账目/8轮上限只在正式事务生效 |
| W05 检查与源码CI | 针对性负控、原完整13组与严格Docker；实际生产源码提交/远端CI成功 | 本地13组全部通过，source_changed=false；backend760/skip8、default17、factory27、strictDocker20/skip0；verification/verified/。精确源码67d7da5及CI39438435175均通过；CI原始响应ci-source.json |
| W06 正式生产 | 原子修复8/8+唯一后继+24小时；六项新输入预审、聚合、冻结新版本及1800秒独审；GoFlash | 已激活并实际4次Go审阅；前三项有效passed，phase_acceptance非法JSON失败，追加资格耗尽后正式pause；STOP_RECORD.json，累计87/500，repair8/8 |
| W07 G1真实链路 | 发布→标准包实际消费→真实P0→冻结套件→独立浏览器/phase proof→宿主assessment | 未运行；宿主真实assessment blocked，未冻结新版本/发布/交接/P0，不用fixture替代 |
| W08 T08三场景 | G1正式通过后原固定书签/月度预算/多项目会议笔记；首次8小时；其他产品各2轮 | 未启动0/3；因G1 blocked保留原三样本及首次8小时，未扩展或替换 |

宿主实现按 Sol 规划与审查、Luna 实现与测试协作。准备字节/测试、预算时间服务与修订生产集成划分所有权，互不覆盖；生产调用仅使用用户指定 OpenCode Go。所有模型调用与生产状态变更走正式服务，不直接改库。现有旧截止、旧8维 blocked、grant和追加重试保留；本轮 author0，不自动增加第九轮或协议重试资格。每个工作包继续记录实际证据，遇到附件规定的真实停止条件才正式暂停。
