#!/bin/bash
# Application Atlas parallel worker
#
# Usage: ./worker.sh <listfile>     e.g. ./worker.sh batch-B.txt
#
# 并发安全设计：
#   - 跳过判断基于文件系统（research/<slug>.md + applications/<slug>.md 都存在 = 已处理），
#     不依赖 STATUS.md，多 worker 之间无共享写状态
#   - mkdir 原子锁防止两个 worker 处理同一叶子（跨域重复叶子场景）
#   - 失败记录在每个 worker 自己的 logs/fail-<tag>.log（重试 = 删对应行）
#   - batch-A（batch.sh）运行中不受影响；它仍以 STATUS.md 判断，agent 的
#     read-edit-retry 模式使并发 STATUS 追加可自愈

set -u
PACK_DIR="/Users/milin/2026/软件开发/application-atlas/application-atlas-production-pack"

# 防 macOS 系统睡眠
if command -v caffeinate >/dev/null 2>&1 && [ "${ATLAS_CAFFEINATED:-0}" != "1" ]; then
  export ATLAS_CAFFEINATED=1
  exec caffeinate -is "$0" "$@"
fi

cd "$PACK_DIR" || exit 1
mkdir -p logs logs/locks

LIST="${1:?usage: ./worker.sh <listfile>}"
TAG=$(basename "$LIST" .txt)
FAILLOG="logs/fail-${TAG}.log"
MAX_RUN_SECS="${MAX_RUN_SECS:-2700}"   # 单叶看门狗上限（默认 45 分钟）
BREAKER_SLEEP="${BREAKER_SLEEP:-900}"  # 连续 3 次失败后的休眠时长（默认 15 分钟）
CONSEC_FAIL=0
touch "$FAILLOG"

echo "[$(date '+%F %T')] worker ${TAG} started (${LIST})" | tee -a batch.log

while IFS='|' read -r slug name; do
  [ -z "$slug" ] && continue

  # skip 1：产物文件已存在 = 已处理（跨 worker / 跨批次通用）
  if [ -f "research/${slug}.md" ] && [ -f "applications/${slug}.md" ]; then
    continue
  fi
  # skip 2：本 worker 之前失败过（重试 = 从 fail log 删行）
  if grep -qF -- "FAIL ${slug} " "$FAILLOG" 2>/dev/null; then
    continue
  fi
  # skip 3：原子锁——别的 worker 正在处理这个叶子
  if ! mkdir "logs/locks/${slug}" 2>/dev/null; then
    echo "[$(date '+%F %T')] [${TAG}] SKIP  ${slug} (locked by another worker)" | tee -a batch.log
    continue
  fi

  echo "[$(date '+%F %T')] [${TAG}] START ${slug} :: ${name}" | tee -a batch.log

  # 后台运行 + 看门狗：LLM API 限额时 opencode 会静默挂起（不报错不退出），
  # 单叶超过 MAX_RUN_SECS 强制终止并标记失败
  opencode run \
    --dir "$PACK_DIR" \
    -m "${MODEL:-opencode-go/omen-alpha}" \
    --agent atlas-writer \
    --title "atlas: ${slug}" \
    --auto \
    "处理目录叶子：${name}（slug: ${slug}）。按 atlas-writer 工作指令完成全部流程并退出。" \
    < /dev/null > "logs/${slug}.log" 2>&1 &
  RUN_PID=$!
  ELAPSED=0
  while kill -0 "$RUN_PID" 2>/dev/null && [ "$ELAPSED" -lt "$MAX_RUN_SECS" ]; do
    sleep 30
    ELAPSED=$((ELAPSED + 30))
  done
  if kill -0 "$RUN_PID" 2>/dev/null; then
    echo "[$(date '+%F %T')] [${TAG}] TIMEOUT ${slug} (>${MAX_RUN_SECS}s) — killing hung run" | tee -a batch.log
    pkill -P "$RUN_PID" 2>/dev/null
    kill "$RUN_PID" 2>/dev/null
    sleep 3
    kill -9 "$RUN_PID" 2>/dev/null
  fi
  wait "$RUN_PID" 2>/dev/null
  RC=$?

  # 成功判定基于文件系统，与 STATUS.md 解耦
  if [ -f "research/${slug}.md" ] && [ -f "applications/${slug}.md" ]; then
    echo "[$(date '+%F %T')] [${TAG}] DONE  ${slug} (rc=${RC})" | tee -a batch.log
    CONSEC_FAIL=0
  else
    echo "[$(date '+%F %T')] [${TAG}] FAIL ${slug} rc=${RC} — see logs/${slug}.log" | tee -a batch.log
    echo "FAIL ${slug} rc=${RC} $(date '+%F %T')" >> "$FAILLOG"
    CONSEC_FAIL=$((CONSEC_FAIL + 1))
    # 熔断器：连续失败（如 API 限额耗尽）→ 休眠后再试，避免快速空转烧配额
    if [ "$CONSEC_FAIL" -ge 3 ]; then
      echo "[$(date '+%F %T')] [${TAG}] BREAKER ${CONSEC_FAIL} consecutive fails — sleeping ${BREAKER_SLEEP}s (possible API quota exhaustion)" | tee -a batch.log
      sleep "$BREAKER_SLEEP"
      CONSEC_FAIL=0
    fi
  fi
done < "$LIST"

echo "[$(date '+%F %T')] worker ${TAG} finished" | tee -a batch.log
