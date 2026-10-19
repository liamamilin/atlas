# 固定 v0.1.4 规范，只修 A30 的脚本基线

不改变产品、架构、阶段、决策、33 个用例 ID/目标、README 或其他程序。本次 reuse_spec=true，Atlas 直接复制固定规范，不调用模型重写规划。只允许 acceptance/ui-p1.cjs；其余 19 个作者文件逐字复用。只返回必要的精确 replacements，避免重写大文件。不要联网、安装、执行任何程序或发布。

人工沿 run.cjs / support.cjs 交叉检查确认：整套 suite 只有一个 ctx.runId；defineCase 不另建 case runId，cleanup 在 executeSuite 的 finally 才执行。A20 会留下一条本 run 的回收记录。因此 A30 的 `assert(baselineCounts.trashed === 0, ...)` 是错误的内部前提：即使正确应用也可能在标准 --with-ui suite 失败。不能清库来让该错误前提成立。

仅作以下改动：

1. 将此精确旧行替换为记录原有本 run 回收条目 ID（`listRunTrash` 已存在）：

```js
  assert(baselineCounts.trashed === 0, 'A30：基线回收站记录数应为 0，实际 ' + preview(baselineCounts));
```

替换后用 `const preexistingTrashIds = (await listRunTrash(ctx)).map(function idOf(item) { return String(item.id); });`。保留 baselineCounts 对取消、move、purge 与后续计数守恒的所有比较，不改变 runCounts 的含义或 scope，不删除其他行为断言。

2. 单条永久删除后已经取得 trashAfterDelete，并检查本次目标消失、另一个特意创建的回收记录仍在。再逐个断言 preexistingTrashIds 中原有条目仍在 trashAfterDelete，以真实地覆盖不误删前面用例记录。不要执行确认清空，不触碰其他 run 或真实个人数据。

3. 删除以下无效自比较，以真正的操作前快照比较替换，不只是让结果为真：

```js
    assertEqual(staleSourceEntry.bookmarkCount, staleBefore ? staleSourceEntry.bookmarkCount : staleSourceEntry.bookmarkCount, 'A30：失效目标 move 失败后源归类记录数应可读');
```

替换为从 `staleSnapshotBefore` 中 findById(..., staleSourceId) 取得源归类，明确断言存在，再比较操作前后 bookmarkCount 相等。原有整体归类快照、runCounts、书签 id/归属/title/note/updatedAt 的零写入断言均保留。

这不是弱化产品要求：零初始回收记录不属于产品契约，且与统一 runner 的真实执行顺序冲突。修复保留所有真正行为检查，并加强此前遗留记录保护。模型只修这一文件；完成后使用新的冻结摘要另开独立静态审阅，仍不运行目标应用。
